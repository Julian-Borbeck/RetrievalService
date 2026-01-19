from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, AnyUrl

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    model_rewrite: str = Field(validation_alias="MODEL_REWRITE")
    ollama_url: AnyUrl = Field(validation_alias="OLLAMA_URL")
    chroma_dir: str = Field(validation_alias="CHROMA_DIR")
    collection_name: str = Field(validation_alias="COLLECTION_NAME")
    embedding_url: AnyUrl = Field(validation_alias="EMBEDDING_URL")
    
    

settings = Settings()