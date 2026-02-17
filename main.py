from fastapi import FastAPI
from app.api import router  as api_router
# from app.api import app as test_api
from app.testapi import router as test_router

app = FastAPI()

app.include_router(api_router)
app.include_router(test_router)
# app.include_router(test_api)   这个test_api是一个FastAPI实例，一个项目只能有一个FastAPI实例，在其他的文件中只定义路由
