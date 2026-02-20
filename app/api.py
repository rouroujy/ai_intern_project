# from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter

# app = FastAPI()
router = APIRouter()


class TextRequest(BaseModel):
    text:str

@router.post("/apiRouter")
def api_main_test(request:TextRequest):
    length = len(request.text)
    return {"length": length,
            "message":"测试注册路由的api->router成功!"}


# @app.get("/hello")
# def say_hello():
#     return {"message":"Hello Word!"}

# @app.post("/analyze")
# def analyze_text(request:TextRequest):
#     length = len(request.text)
#     return {"length": length}
