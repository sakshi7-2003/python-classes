#  class ink:











# # # # # # inheritance
# # # # # class abc1:
# # # # #     def a(self):
# # # # #         print("my name is sakshi")
# # # # #     def b(self):
# # # # #         print("my name is kajal")

# # # # # class abc2(abc1):
# # # # #     def c(self):
# # # # #         print("my name is ritika")

# # # # # class abc3(abc1):
# # # # #     def d(self):
# # # # #         print("my name is shruti")
# # # # # obj=abc1()
# # # # # obj=abc2()
# # # # # obj=abc3()
# # # # # obj.d()





# # # # from abc import ABC, abstractmethod
# # # # class animal(ABC):
# # # #     @abstractmethod
# # # #     def move(self):
# # # #         pass
# # # # class human(animal):
# # # #     def run(self):
# # # #         print("i can walk and run")
# # # # class snake(animal):
# # # #     def move(self):
# # # #         print("i can crawl")
# # # # obj=human()
# # # # obj.run()




# # # class base:
# # #     def __init__(self,a,b):
# # #         self._name=a
# # #         self.surname=b
# # # class abc(base):
# # #     def xyz(self):
# # #       print(f"my name is {self._name} and my surname is {self.surname}")

# # # obj=abc()
# # # obj=base("xyz","jamwal")




# # class base:
# #     def __init__(self):
# #         self.a="welcome"
# #         self.__c="you`re welcome"
# # class derived(base):
# #     def __init__(self):
# #         print("calling private member of base class:")
# #         print(self.__c)
# # obj=base()
# # print(obj.__c)




# class cls1:
#     def __init__(self):
#         self.name=0
#     def get_age(self):
#        print("getter method")
#        return self.name
#     def set_age(self,a):
#         print("setter method")
#         self._name=a
#     def del_name(self):
#         del self._name

# obj=cls1()
# obj.name="xyz"
# print(obj.name)




class cls1:
    def __init__(self):
        self._age=0
    @property
    def age(self):
        print("getter method")
        return self._age
    @age.setter
    def age(self,a):
        if(a>18):
            print("setter method")
            self._age=a
obj=cls1()
obj.age=19
print(obj.age)










