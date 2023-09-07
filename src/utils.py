import joblib
import pandas as pd
from models import Request, Response, Data
from typing import Dict


class InferenceModel:
    model = joblib.load("data/model.joblib")

    @staticmethod
    def get_model():
        return InferenceModel.model


def get_column_map():
    return {
        "avg_area_income": "feat_Avg. Area Income",
        "avg_area_house_age": "feat_Avg. Area House Age",
        "avg_area_number_of_rooms": "feat_Avg. Area Number of Rooms",
        "avg_area_number_of_bedrooms": "feat_Avg. Area Number of Bedrooms",
        "area_population": "feat_Area Population",
        "address": "feat_Address",
    }


async def pre_process(request: Request):
    input_data: Dict = dict(request.features)
    # map the items to appropriate values
    column_map = get_column_map()
    data = dict({column_map[key]: values for key, values in input_data.items()})
    data = pd.DataFrame(data, index=[0])
    return data


async def predict(data):
    model = InferenceModel.get_model()
    predictions = model.predict(data)
    return predictions


async def post_process(input_data: Data, provider: str, output: list):
    return Response(features=input_data, provider=provider, output=output[0])
