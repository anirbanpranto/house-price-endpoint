from utils import pre_process, predict, post_process


async def run_pipeline():
    data = await pre_process()
    result = await predict(data)
    # await post_process()
    return result
