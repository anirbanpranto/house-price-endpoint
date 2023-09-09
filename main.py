from fastapi import FastAPI
from inference.inference import run_inference_pipeline
from inference.pydantic_models import Request, Response
from inference.utils import InferenceModel

app = FastAPI()


@app.on_event("startup")
def initialize_model():
    InferenceModel.init_model()


@app.post("/predict")
async def predict(request: Request) -> Response:
    result: Response = await run_inference_pipeline(request)
    return result
