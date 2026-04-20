from fastapi import FastAPI

app = FastAPI()

@app.post("/generate")
def post_generate():

    return {
        "status": "ok"
    }