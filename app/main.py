import logging
import os
import sys
from app.analyzer import analyze_text , TextAnalysisError
import argparse
import asyncio
import time


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
    print("HOT RELOAD TEST")
    args = parse_args()

    # 测试async
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
        result = await analyze_text(
             args.file_path,
             ignore_case = args.ignore_case,
             remove_punctuation = args.remove_punctuation
        )
        print("\nText Analysis Result:")
        for key,value in result.items():
             print(f"{key}:{value}")

        
    #main捕获业务异常
    except TextAnalysisError as e:
         logger.error(f"Business error: {e}")
         print(f"Error: {e}")
        
    #系统异常
    except Exception:

         logger.exception("System level error occurred")

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
        asyncio.run(main())
        # main()    