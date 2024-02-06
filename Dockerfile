FROM pytorch/pytorch as builder

RUN pip3 install FlagEmbedding --no-cache-dir
    && mkdir /mnt/auto/
    && cd /mnt/auto
    && git clone https://huggingface.co/BAAI/bge-m3/
COPY *.py /code/

ENTRYPOINT ["python3", "-u", "/code/index.py"]
