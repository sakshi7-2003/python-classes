# # # # a=['name','age','number']
# # # # b=['moris',20,97672180]
# # # # y={a[i]:b[i] for i in range(3)}
# # # # print(y)



# a="i am a python developer, who are you"
# b=["a","e","i","o","u"]
# y=[i for i in a if a in b]
# print(y)



# # # generator....
# # def abc(n):
# #     for i in range(n):
# #         yield i

# # rs=abc(5)
# # print(next(rs))
# # print(next(rs))
# # print(next(rs))





# class abc:
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
# obj=abc(1,7)
# for i in obj:
#     print(i)