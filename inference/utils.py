import joblib
from typing import Dict, Any


def load_model_from_artifact(artifact_name: str) -> Any:
    # ideally this should be fetched from some kind of storage -> (i.e. - S3)
    return joblib.load("inference/artifacts/" + artifact_name)


def get_column_map() -> Dict:
    return {
        "avg_area_income": "feat_Avg. Area Income",
        "avg_area_house_age": "feat_Avg. Area House Age",
        "avg_area_number_of_rooms": "feat_Avg. Area Number of Rooms",
        "avg_area_number_of_bedrooms": "feat_Avg. Area Number of Bedrooms",
        "area_population": "feat_Area Population",
        "address": "feat_Address",
    }


class InferenceModel:
    model = None

    # to make sure we don't load the model for every request
    @staticmethod
    def get_model() -> Any:
        if InferenceModel.model:
            return InferenceModel.model
        else:
            InferenceModel.init_model()
            return InferenceModel.model

    @staticmethod
    def init_model() -> None:
        InferenceModel.model = load_model_from_artifact("model.joblib")
