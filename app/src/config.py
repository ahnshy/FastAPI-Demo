from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.abspath(__file__)))

@dataclass
class Config:
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL:str = "mysql+pymysql://root@localhost:3306/user?serverTimezone=UTC&characterEncoding=UTF-8"

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False

print(LocalConfig())
print(asdict(LocalConfig()))
print(LocalConfig().DB_ECHO)

def conf():
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))
