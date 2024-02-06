from sanic import Sanic
import sanic.response
from sanic.request import Request
import service
import os
import traceback

app = Sanic("EMBEDDING")

@app.route("/embedding", methods=["post"])
async def start(request: Request):
    if 'authorization' not in request.headers:
        return sanic.response.json({"message": "Unauthorized"}, status=401)
    if request.headers['authorization'] != os.environ.get("api-key", os.environ.get("apikey", "2weu9qo2e9")):
        return sanic.response.json({"message": "Key Not Found"}, status=403)

    try:
        text = request.json["text"]
        return sanic.json({"object": "embedding-bge-m3", "data": service.encode(text)})
    except Exception as ex:
        traceback.print_exc()
        return sanic.response.json(
            {
                "message": str(ex),
                "traceback": traceback.format_exc()
            },
            status=400
        )
    

@app.route("/")
async def index():
    return sanic.json({"message":"It works."})
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
