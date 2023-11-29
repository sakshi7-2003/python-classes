# # # a=lambda a:a+100
# # # print(a(100))



# # numbers=[1,2,3,4,5,]
# # result=map(lambda x:x+x,numbers)
# # print(list(result))





# a=(2,4,5,6,7,8,10,6)
# s=filter(lambda x:x%2!=0,a)
# print(list(s))




from functools import partial
def f(a,b,c,x):
    return 100*a+100*b+10*c+x
    g=partial(f,3,1,4)
    print(g(3))
    g()