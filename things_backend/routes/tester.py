from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/tester",
)


@router.get("/publish")
async def publish(request: Request):
    request.app.mqtt.publish("/mqtt", "Hello from Fastapi")  # publishing mqtt topic

    return {"result": True, "message": "Published"}
