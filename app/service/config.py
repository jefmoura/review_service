from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    API_VERSION: str = "0.0.1"
    API_VERSION_PREFIX: str = "/v1"
    API_DEBUG: bool = False

    @validator("API_DEBUG", pre=True)
    def convert_api_debug(cls, v: str) -> bool:
        return False if v == "False" else True

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", "http://localhost:8080"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "Skolens - Review Service"

    class Config:
        case_sensitive = True


settings = Settings()
