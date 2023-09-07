from typing import Union
import json

from fastapi import FastAPI
from pipeline import run_pipeline

app = FastAPI()


@app.get("/predict/")
async def read_root():
    result = list(await run_pipeline())
    return f"{result}"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
