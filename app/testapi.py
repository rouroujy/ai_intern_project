from fastapi import APIRouter

router = APIRouter()

@router.get("/testapi")
def testapi():
    return {'mes':"hello testpai successful!"}

