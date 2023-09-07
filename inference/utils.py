import joblib


def load_model_from_artifact(artifact_name: str):
    # ideally this should be fetched from some kind of storage -> (i.e. - S3)
    return joblib.load("inference/artifacts/" + artifact_name)


class InferenceModel:
    model = load_model_from_artifact("model.joblib")

    # to make sure we don't load the model for every request
    @staticmethod
    def get_model():
        return InferenceModel.model
