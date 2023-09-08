import pandas as pd
from inference.pydantic_models import Request, Response, Features
from inference.utils import InferenceModel, get_column_map
from typing import Dict
import numpy as np


async def pre_process(request: Request) -> pd.DataFrame:
    input_data: Dict = dict(request.features)
    # map the items to appropriate values
    column_map = get_column_map()
    data = dict({column_map[key]: values for key, values in input_data.items()})
    # create dataframe
    data = pd.DataFrame(data, index=[0])
    return data


async def predict(data: pd.DataFrame) -> np.ndarray:
    model = InferenceModel.get_model()
    predictions: np.ndarray = model.predict(data)
    return predictions


async def post_process(input_data: Features, provider: str, output: np.ndarray):
    return Response(features=input_data, provider=provider, output=output[0])
