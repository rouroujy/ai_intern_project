# app/services/bailian_client.py
import logging
import dashscope
from dashscope import Generation
from app.config import settings
import asyncio

logger = logging.getLogger(__name__)

# 设置 API Key
dashscope.api_key = settings.BAILIAN_API_KEY


class BailianClient:
    def __init__(self):
        if not settings.BAILIAN_API_KEY:
            raise ValueError("没有配置百炼API的KEY")

    def analyze_text(self, text: str) -> str:
        """
        调用阿里云百炼大模型进行文本分析
        """
        try:
            logger.info("发送请求到百炼API...")

            response = Generation.call(
                model="qwen-turbo",  # 可改为 qwen-plus / qwen-max
                prompt=text,
                max_tokens=200
            )

            if response.status_code != 200:
                logger.error(f"百炼 API error: {response}")
                raise RuntimeError("百炼API请求失败")

            result = response.output.text
            logger.info("百炼请求接收成功！")

            return result

        except Exception as e:
            logger.exception("请求百炼API时出错")
            raise

    async def analyze_text_async(self, text:str) -> str:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,                   #使用默认线程池
            self.analyze_text,      #调用同步方法
            text
        )