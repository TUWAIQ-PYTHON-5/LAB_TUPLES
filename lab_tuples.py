my_tuple=(1 ,2 ,3 )
second_tuple=("a","b","c")
print(my_tuple[0])
print(second_tuple[2])
result= my_tuple + second_tuple
x=len(result)
print("the length of the result tuple",x)
if 4 in result:
    print("4 is in the result tuple")
else:
    print("4 is not in the result tuple")

lst=[4, 5, 6]
my_new_tuple=tuple(lst)
print(type(my_new_tuple))
var1:int
var2:int 
var3:int
var1,var2,var3=my_new_tuple
