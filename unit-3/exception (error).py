'''#exception error
a=10
b=0
print(a/b)
print("hello")'''

'''#python program to handle simple runtime error
a=10
b=0
try:
    
    print(a/b)
except Exception as e:
    print(e)
print("hello")'''


#finally =
a=10
b=0
try:
    
    print(a/b)
except Exception as e:
    print("ohh its error",e)

finally:
    print("hello")

