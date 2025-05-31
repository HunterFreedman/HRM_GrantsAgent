from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "HRM_GrantsAgent is running"}
