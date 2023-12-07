from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def main_route():
    return {"status": "ok"}
