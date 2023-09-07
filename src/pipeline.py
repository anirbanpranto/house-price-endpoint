from utils import pre_process, predict, post_process
from models import Data, Request, Response


async def run_pipeline(request: Request) -> Response:
    data = await pre_process(request)
    result = await predict(data)
    response = await post_process(
        input_data=request.features, provider=request.provider, output=result
    )
    return response
