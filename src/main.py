from typing import Union
import json

from fastapi import FastAPI
from pipeline import run_pipeline
from models import Request, Response

app = FastAPI()


@app.post("/predict/")
async def read_root(request: Request) -> Response:
    result = list(await run_pipeline(request))
    return result
