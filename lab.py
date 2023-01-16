numbers = (1,2,3)
letters = ("a","b","c")
print(numbers[0])
print(letters[2])

result=numbers+letters
print(result)

if 4 in result:
    print("Number 4 is available")
else:
    print("Number 4 is not available")


num = [4,5,6]
print(tuple(num))


x , y , z = num

print(x,y,z)

# Bonus :

# 1
Inndex = letters.index("b")
print(Inndex)

# 2
count = result.count(2)
print(count)

# 3

enumerated_list = enumerate(result)
for index , value in enumerated_list:
    print(index,value)
