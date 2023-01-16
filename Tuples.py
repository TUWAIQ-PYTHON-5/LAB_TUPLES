
#1
numbers : tuple = 1, 2, 3
print(type(numbers))

#2
letters : tuple = "a", "b", "c"
print(type(letters))

#3
print(numbers[0])

#4
print(letters[-1])

#5
result : tuple = numbers + letters
print(result) 

#6
print(len(result))

#7
answer: str ="No"
for item in result:
    if (item==4):
        answer: str ="Yes"
        break
    else:
        answer="No"
print(answer)

#8
aList: list = [4,5,6]
newTuple : tuple =tuple(aList)
print(newTuple)

#9
var1 , var2 , var3 = newTuple
print(var3,var2,var1)