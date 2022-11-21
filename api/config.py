from pydantic import BaseSettings


class ConfigFastapi(BaseSettings):
    openapi_prefix: str = '/'
