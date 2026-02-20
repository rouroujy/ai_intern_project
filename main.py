from fastapi import FastAPI
from app.api import router  as api_router
# from app.api import app as test_api
from app.testapi import router as test_router

app = FastAPI()

app.include_router(api_router)
app.include_router(test_router)
# app.include_router(test_api)   这个test_api是一个FastAPI实例，一个项目只能有一个FastAPI实例，在其他的文件中只定义路由

# FastAPI依赖注入配置
from fastapi import Depends
from app.config import Settings,get_settings



# 路由装饰器  
# 当浏览器访问 GET /config 时，执行下面这个函数
@app.get("/config")
def read_config(settings: Settings = Depends(get_settings)):
    print("正在运行的环境是:",settings.app_env)
    return {"env":settings.ENV}

# FastAPI 依赖注入配置  不推荐这样
# from app.config import settings
# print("Running in environment:",settings.app_env)