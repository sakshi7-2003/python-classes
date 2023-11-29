# a=50
# b=20
# if a>b:
#     print("my name is sakshi.....")
# else:
#     print("who are you....")



# a=20
# for i in range(1,10):
#     print(i)


# a="name","age","number"
# b="sakshi",20,7876765938
# ab={a[i]:b[i] for i in range(3)}
# print(ab)



# inheritence.....
# class abc:
#     def run(self):
#         print("i belong to himachal")
#     def code(self):
#         print("i belong to chandigarh")
# class xyz(abc):
#     def out(self):
#         print("i belong to goa")
#     def ink(self):
#         print("i belong to jammu")
# class num(xyz):
#     def int(self):
#         print("my name is sakshi...")
# obj=num()
# obj.code()



# class abc:
#     def __init__(self,a,b):
#         self.name=a
#         self.age=b
#     def game(self):
#         print(f"my name is {self.name} and my age is {self.age}")
# obj=abc("sakshi",20)
# obj.game()




# encapsulation.....
# class cls1:
#     def __init__(self):
#         self._a=2
# class cls2(cls1):
#     def run(self):
#         print(self._a)
# obj=cls2()
# obj.run()
        



# file handling.....
# file=open('oops.py','r')
# for each in file:
#     print(file.read()) 


# file=open('loops.py','w')
# file.write("my name is sakshi.....")
# file.close()





# class xyz:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.x<self.y:
#             ab=self.x
#             self.x=self.x+1
#             return ab
#         else:
#             raise StopIteration
# obj=xyz(1,7)
# for i in obj:
#     print(i)


