from fastapi import FastAPI

app = FastAPI()

def return_stuff():
    return "BALLE!"

@app.get("/")
async def root():
    return {"message":return_stuff()}

