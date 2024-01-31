# ### Part 2 - Star Wars Light (Local API)
# - Create a new FAST APP **starapi_app.py** 
# - Create an endpoint **/starapi/people** that return a list of all people from your **silver** folder (or somewhere else that is representative of the people)
# - Create an endpoint **/starapi/people/<people/{id}>** that accepts a parameter **person_id** 
# and returns the person if they exist. Consider the length of your people-file /list and throw an appropriate HTTP code
# if the people does not exist in your file or the index is out of range.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Star Wars"}

@app.get("/")
async def root():
    return {"message": "Star Wars"}