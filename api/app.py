from fastapi import FastAPI

from api.config import ConfigFastapi
from api.endpoints import router 
from api.endpoints.endpointsnetwork import router as router_utilisateur

def make_app() -> FastAPI:
    _app = FastAPI(
        title="social network",
        root_path=ConfigFastapi().openapi_prefix
    )
    _app.include_router(router)
    _app.include_router(router_utilisateur) 
    return _app