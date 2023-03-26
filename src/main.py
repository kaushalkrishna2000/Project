from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return "hello world"


@app.get("/part_1")
def returner():
    return "Yo boys"


@app.get("/part_2")
def retrun1():
    return "hi boys"
