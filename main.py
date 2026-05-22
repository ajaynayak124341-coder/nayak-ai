from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Nayak AI Server is Running Perfectly, Ajay Bhai!"}