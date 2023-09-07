import json
import joblib
import pandas as pd


class InferenceModel:
    model = joblib.load("data/model.joblib")

    @staticmethod
    def get_model():
        # this it to ensure we do not load the model many times
        return InferenceModel.model


async def pre_process():
    config = json.load(open("data/config.json"))
    features = config["features"]
    data = pd.read_csv("data/data.csv")
    data = data[features]
    data.columns = ["feat_" + str(col) for col in data.columns]
    return data


async def predict(data):
    model = InferenceModel.get_model()
    predictions = model.predict(data)
    return predictions


async def post_process():
    pass
