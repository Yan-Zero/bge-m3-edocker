import os
from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel("/mnt/auto/embedding/bge-m3", use_fp16=True)

def encode(sentences: str | list[str]):
    if isinstance(sentences, str):
        sentences = [sentences]
    return model.encode(sentences)
