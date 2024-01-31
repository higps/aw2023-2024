from fastapi import FastAPI
import requests


app = FastAPI()
# ### Part 1 - Joke API (Reverse Proxy)
# This API will be utilizing the https://icanhazdadjoke.com/api for fetching random dad-jokes. We can call this a *reverse proxy* API since our python API will function as a broker / intermediate connection point between the joke API and the client (consumer of our API).
# - Create a new flask APP **joke_app.py**
# - Create a new endpoint **/jokes** that returns a random joke on JSON format


def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)
    return response.json()["joke"]

# print(get_joke())

@app.get("/joke")
async def root():
    return get_joke(1)

def get_jokes(param):
    joke_list = []
    print("param",param)
    for i in range(len(param)):
        print(i)
        joke_list.append(get_joke())

    return joke_list

@app.get("/jokes")
async def root(param):
    return get_jokes(param)