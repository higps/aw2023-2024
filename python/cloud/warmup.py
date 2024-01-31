from fastapi import FastAPI

app = FastAPI()

def return_stuff():
    return "Greetings from Marius"

@app.get("/")
async def root():
    return return_stuff()


@app.get("/boot")
async def boots():
    return {"message":"Teh boot"}


@app.get("/get_string", summary="Returns two params", description="Something here")
async def get_string(param1, param2):
    return {"message": f"{param1} Hello, {param2}!"}


def sum_nums(nums):
    sum_num = 0
    for num in nums:
        sum_num += num
    return sum_num


@app.post("/calculate", summary="Calculates numbers", description="Good for math")
async def sum(num_dict):
    # return list_of_nums
    return {"sum": sum_nums(num_dict["numbers"])}