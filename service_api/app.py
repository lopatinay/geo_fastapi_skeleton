from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service_api.constants import APP_NAME
from service_api.resources import api


fast_app = FastAPI(
    title=APP_NAME,
    version="0.0.1",
    swagger_ui_parameters={"tryItOutEnabled": True},
)
fast_app.include_router(api)

fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
