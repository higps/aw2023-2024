from fastapi import FastAPI

app = FastAPI()

def return_stuff():
    return "Whale hello there 🐳"

@app.get("/")
async def root():
    return {"message": return_stuff()}

