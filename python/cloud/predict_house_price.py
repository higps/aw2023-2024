from fastapi import FastAPI,Query
from predict_houses_function import run_prediction
from  pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/echo/{input_param}")
async def echo(input_param: str):
    """
    Endpoint to echo the provided parameter.

    Parameters:
    - input_param (str): Parameter to be echoed.

    Returns:
    - dict: A JSON object with the key "result" and the echoed parameter as its value.
    """
    return {"result": input_param}

class HouseFeatures(BaseModel):
    sqft_living: int
    bedrooms: int
    sqft_lot: int
    bathrooms: int
    waterfront: int
    grade: int

@app.post("/houses/")
async def create_item(house: HouseFeatures):

    house_features = [
        house.sqft_living,
        house.bedrooms,
        house.sqft_lot,
        house.bathrooms,
        house.waterfront,
        house.grade
    ]
    return {"predicted_price_from_list": run_prediction([house_features])}



def sum_of_lists(list_of_lists):
    """
    Calculate the sum of each list in the given list of lists.

    Parameters:
    - list_of_lists (list of list): List containing multiple lists of numerical values.

    Returns:
    - list: A list containing the sum of each individual list.
    """
    return [sum(lst) for lst in list_of_lists]

@app.post("/sum_list_of_lists")
async def post_sum_of_list(features: List[List[int]]):
    return {"sum of the lists": sum_of_lists(features)}


@app.post("/predict_houses")
async def post_sum_of_list(features: List[List[int]]):
    return {"predicted_price_from_list": run_prediction(features)}