# # # multithreading......
# # import threading
# # class abc:
# #     def task1(self):
# #         for i in range(20):
# #             print("i am human....")

# #     def task2(self):
# #         for i in range(10):
# #             print("i am robot....")
# # obj=abc()
# # thread1=threading.Thread(target=obj.task1)
# # thread2=threading.Thread(target=obj.task2)

# # thread1.start()
# # thread2.start()

# # thread1.join()
# # thread2.join()
# # print("i am machine.....")

# # print("code processing.....")

# # print("done.....")




# class hlo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# class code(hlo):
#     def __init__(self,name,age,email):
#         super().__init__(name,age)
#         self.email=email
# obj=code("sakshi",20,"sakshi@gmail.com")
# print("the name is:",obj.name)
# print("the age is :",20)
# print("the email is:","sakshi@gmail.com"


from collections import deque
import numbers as np
import argparse
import csv
import time
ap=argparse.ArgumentParser()
ap.add_argument("-v","--video",help="path to the (optional) video file")
ap.add_argument("-b","--buffer",type=int,default=64,help="max buffer size")
args=vars(ap.parse_args())
greenlower=(29,86,6)
greenupper=(64,255,255)
pts=deque(maxlen=args["buffer"])
if not args.get("video",False):
    vs=str(src=0).start()
else:
    vs=csv.videocapture(args["video"])
    time.sleep(2.0)