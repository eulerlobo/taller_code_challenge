from fastapi import FastAPI

app = FastAPI(
    title="Taller challenge",
    description="Taller challenge API",
)

@app.get("/")
def root():
    return {"message": "Hello World"}