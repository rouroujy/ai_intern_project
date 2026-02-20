from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.api import router  as api_router
# from app.api import app as test_api
from app.testapi import router as test_router
import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI()

class TextRequest(BaseModel):
    text: str

app.include_router(api_router)
app.include_router(test_router)
# app.include_router(test_api)   这个test_api是一个FastAPI实例，一个项目只能有一个FastAPI实例，在其他的文件中只定义路由

@app.post("/analyze")
async def analyze_text(request:TextRequest):
    logger.info("收到请求")

    try:
        text = request.text

        if not text.strip():
            logger.warning("收到空字符串")
            raise HTTPException(status_code = 400, detail = "文字不能为空")

        length = len(text)
        word_count = len(text.split())

        logger.info("处理成功！")
        return{
            "文字长度length":length,
            "文字数word_count":word_count,
            "是否为空is_empty":False
        }
    
    except Exception as e:
        logger.error(f"发生异常{e}")
        raise



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