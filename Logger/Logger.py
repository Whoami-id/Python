import time
import logging
from pathlib import Path

#Debuh
#Info
#Warning
#Error
#Critical


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')
filepath = Path(__file__).parent.joinpath("log_standart.log")
file_handler = logging.FileHandler(filepath)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def divide_integers(a: int , b: int) -> float:
    try:
        logger.debug("TEST")
        result = a / b
        return result
    except Exception as e:
        logger.critical(e)


def main():
    for _ in range(10):
        time.sleep(1.5)
        print(divide_integers(10, 5))


if __name__ == "__main__":
    main()
