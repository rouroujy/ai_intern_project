import logging
import os
import sys
from app.analyzer import analyze_text
import argparse

def setup_logging():
        os.makedirs("log",exist_ok=True)
        logging.basicConfig(
                level=logging.INFO,
                filename="log/app.log",
                filemode="a",
                format="%(asctime)s - %(levelname)s - %(message)s"
        )

def parse_args():
    parser = argparse.ArgumentParser(description="Text Analyzer Tool")
    parser.add_argument("file_path", help="Path to the text file")
    parser.add_argument("--ignore-case", action="store_true", help="Ignore case sensitivity")
    parser.add_argument("--remove-punctuation", action="store_true", help="Remove punctuation")
    return parser.parse_args()


def main():
    print("HOT RELOAD TEST")

    args = parse_args()
    file_path = args.file_path
    try:
        result = analyze_text(
             file_path,
             ignore_case = args.ignore_case,
             remove_punctuation = args.remove_punctuation
        )
        print("Text Analysis Result:")
        for key,value in result.items():
             print(f"{key}:{value}")
        logging.info(f"Successfully analyzed file: {file_path}")
    except Exception as e:
        logging.error(f"Error analyzing file: {e}")
        print(f"Error:{e}")
    
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
        main()    