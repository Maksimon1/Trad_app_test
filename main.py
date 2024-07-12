from fastapi import FastAPI

app = FastAPI(
   title = "Trading app"
)


@app.get("/")
def hello():
    return "Hello world"
