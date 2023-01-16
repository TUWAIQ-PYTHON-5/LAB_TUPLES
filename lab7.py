numbers_tuple =(1,2,3)
letters = ("a","b","c")
print("first number: ",numbers_tuple[0])
print("first letter: ",letters[-1])
result=(numbers_tuple+letters)
print("length for both tuples: ",len(result))
x=input("search for a number:  ")
if x in result:
    print("the number is exist")
else:
    print("the number not exist")

def convert (the_list :list)-> tuple:

    return tuple(the_list)



number_list=[4,5,6]
print(convert(number_list))
var,var1,var3=numbers_tuple
print(var,var1,var3)
print("find the index of the string b: ",letters.index("b"))
print("find the number of occurrences of the integer 2: ",result.count(2))
for index,value in enumerate(result):
    print(index,value)
