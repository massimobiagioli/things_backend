from fastapi import APIRouter

from things_backend.models.health import Health

router = APIRouter(
    prefix="/health",
)


@router.get("/", response_model=Health)
async def health() -> Health:
    return Health(status="ok")
