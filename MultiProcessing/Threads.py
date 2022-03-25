from threading import Thread
import time


def worker(sleep_time: int) -> None:
    print("Start Worker")
    time.sleep(sleep_time)
    print("End Worker")


t1 = Thread(target=worker, name="t1", args=(2.0,))

print(f"Ident: {t1.ident}")
print(f"Alive: {t1.is_alive()}")
print(f"Name:  {t1.name}")

t1.start()

print(f"Ident: {t1.ident}")
print(f"Alive: {t1.is_alive()}")
print(f"Name:  {t1.name}")


t1.join()