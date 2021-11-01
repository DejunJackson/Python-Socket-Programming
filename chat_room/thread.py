from threading import *
from time import sleep

# each execution is a main thread on same thread
# class Hello:
#     def run(self):
#         for i in range(5):
#             print("Hello")


# class Hi:
#     def run(self):
#         for i in range(5):
#             print("Hi")


# t1 = Hello()
# t2 = Hi()

# t1.run()
# t2.run()

# creates classes on two different threads
class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(1)  # causes program to pause for one second


class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

# .start executes two different threads
t1.start()
sleep(0.2)
t2.start()
# prints hello hi hello hi hello hi hello hi hello
