class Settings():
    # Project config
    DATABASE_URL: str = "sqlite:///db.sqlite"
    DATABASE_ECHO: bool = True
    VERSION: str = "0.0.1"
    API_V0_STR: str = "/api/v0"
    PROJECT_NAME: str = "Bug Bounty Bank"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "A bank for bug bounty hunters"



settings = Settings()