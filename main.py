from fastapi import FastAPI
from inference.inference import run_inference_pipeline
from inference.pydantic_models import Request, Response

app = FastAPI()


@app.post("/predict/")
async def read_root(request: Request) -> Response:
    result: Response = await run_inference_pipeline(request)
    return result
