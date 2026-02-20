import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pydantic import field_validator
from functools import lru_cache


# 读取 .env 文件
# 把 .env 中的变量加载到 os.environ
load_dotenv()

class Settings(BaseSettings):
    ENV: str = "dev"
    APP_NAME:str = "AI Itern Project"

    # OPENAI_API_KEY:str | None = None
    BAILIAN_API_KEY:str | None = None
    LOG_LEVEL:str = "INFO"


    # 当这个字段被赋值时，自动运行下面这个函数进行校验。
    @field_validator("ENV")
    @classmethod
    def validate_env(cls,v):
        if v not in {"dev","prod"}:
            raise ValueError("环境必须是dev或prod")
        return v
    
    @field_validator("BAILIAN_API_KEY")
    @classmethod
    def validate_api_key(cls, v, values):
        if values.data.get("ENV") == "prod" and not v:
            raise ValueError("生产环境需要配置百炼API KEY")
        return v
    
    def safe_dict(self):
        """返回环境变量时隐藏敏感字段."""
        data = self.model_dump()
        if "BAILIAN_API_KEY" in data and data["BAILIAN_API_KEY"]:
            data["BAILIAN_API_KEY"] = "***"
        return data


    class config:
        env_file = ".env"


# 缓存装饰器 Least Recently Used Cache
@lru_cache
def get_settings():
    return Settings()
    

# 创建全局配置实例
settings = get_settings()




# 初版配置示例
# 读取.env文件
# load_dotenv()

# class Settings(BaseSettings):
#     openai_api_key:str
#     app_env:str = "dev"

#     model_config={
#         "env_file":".env"
#     } 

# # 创建全局配置实例
# settings = Settings()