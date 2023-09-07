import numpy as np
from pydantic import BaseModel, validator


class Data(BaseModel):
    avg_area_income: float
    avg_area_house_age: float
    avg_area_number_of_rooms: float
    avg_area_number_of_bedrooms: float
    area_population: float
    address: str


class Request(BaseModel):
    features: Data
    provider: str


class Response(BaseModel):
    features: Data
    provider: str
    output: float

    @validator("output")
    def result_check(cls, v):
        return round(v, 1)
