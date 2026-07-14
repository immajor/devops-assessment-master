from fastapi import FastAPI, status

app = FastAPI(title="DevOps Homework App", version="1.0.0")

# GET /health
@app.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    return {"status": "ok"}