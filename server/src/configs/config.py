class Settings():
    # Project config
    DATABASE_URL: str = "sqlite:///db.sqlite"
    DATABASE_ECHO: bool = True
    API_VERSION: str = "v0"



settings = Settings()