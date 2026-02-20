import logging
import os
import sys
from app.analyzer import analyze_text , TextAnalysisError
import argparse
import asyncio
import time
from app.config import settings
from app.core.logging import setup_logging
from app.services.bailian_client import BailianClient

logger = logging.getLogger(__name__)

def setup_logging():
        os.makedirs("log",exist_ok=True)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
             "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        #file handler
        file_handler = logging.FileHandler("log/app.log")
        file_handler.setFormatter(formatter)

        #console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)


        # logging.basicConfig(
        #         level=logging.INFO,
        #         filename="log/app.log",
        #         filemode="a",
        #         format="%(asctime)s - %(levelname)s - %(message)s"
        # )

def parse_args():
    parser = argparse.ArgumentParser(description="Text Analyzer Tool")
    parser.add_argument("file_path", help="Path to the text file")
    parser.add_argument("--ignore-case", action="store_true", help="Ignore case sensitivity")
    parser.add_argument("--remove-punctuation", action="store_true", help="Remove punctuation")
    return parser.parse_args()


async def main():
    logger.info(f"现在的环境为:{settings.ENV}")
    args = parse_args()

    # 并发测试
    # start = time.perf_counter()

    # tasks = [
    #     analyze_text("data/big.txt"),
    #     analyze_text("data/big.txt"),
    #     analyze_text("data/big.txt"),
    # ]
    # print("测试async")
    # await asyncio.gather(*tasks)

    # print("Time:",time.perf_counter() - start)

    try:
        # 测试百炼API
        client = BailianClient()
        result_bailian_test = client.analyze_text("请帮我总结这段文字的主题。人工智能正在改变世界。")
        print(f"测试阿里云百炼API结果输出：{result_bailian_test}")

        result = await analyze_text(
             args.file_path,
             ignore_case = args.ignore_case,
             remove_punctuation = args.remove_punctuation
        )
        print("\n文本分析结果:")
        for key,value in result.items():
             print(f"{key}:{value}")

        
    #main捕获业务异常
    except TextAnalysisError as e:
         logger.error(f"业务异常: {e}")
         print(f"错误: {e}")
        
    #系统异常
    except Exception:
         logger.exception("系统级异常")


    # 01 未引入异常分层结构

    # file_path = args.file_path
    # try:
    #     result = analyze_text(
    #          file_path,
    #          ignore_case = args.ignore_case,
    #          remove_punctuation = args.remove_punctuation
    #     )
    #     print("Text Analysis Result:")
    #     for key,value in result.items():
    #          print(f"{key}:{value}")
    #     logging.info(f"Successfully analyzed file: {file_path}")
    # except Exception as e:
    #     logging.error(f"Error analyzing file: {e}")
    #     print(f"Error:{e}")
    

    # 00 未引入argparse机制

    # print("sys.argv 列表:", sys.argv)
    # if len(sys.argv) < 2 :
    #     print("Usage: python -m app.main <fhile_path>")
    #     sys.exit(1)
    
    # file_path = sys.argv[1]
    
    # try:
    #     result = analyze_text(file_path)
    #     print("Text Analysis Result:")
    #     for key, value in result.items():
    #           print(f"{key}:{value}")

if __name__=="__main__":
     setup_logging()
     logger.info(f"安全加载环境变量: {settings.safe_dict()}")
     asyncio.run(main())
     # main()    