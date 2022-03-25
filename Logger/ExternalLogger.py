import time
from loguru import logger
from pathlib import Path

#Debuh
#Info
#Warning
#Error
#Critical


filepath = Path(__file__).parent.joinpath("log_standartLoguru.log")
logger.add(filepath, rotation= "1 Week")


@logger.catch()
def divide_integers(a: int , b: int) -> float:
        logger.debug("TEST")
        result = a / b
        return result



def main():
    for _ in range(10):
        time.sleep(1.5)
        print(divide_integers(10, 5))


if __name__ == "__main__":
    main()
