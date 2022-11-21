from starlette.middleware.cors import CORSMiddleware

from api.app import make_app

app = make_app()

app = CORSMiddleware(
    app=app,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

__all__ = [app]
