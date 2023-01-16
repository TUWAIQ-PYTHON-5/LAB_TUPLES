numbers = (1, 2, 3)
letters  = ("a", "b", "c")
print(numbers[0])
print(letters[2])

print(numbers + letters)
result = numbers + letters
print(len(result))


if "4" in result:
   print("4 is in the tuple")
else:
    print("not found")



val = [4, 5, 6]
numbers = tuple(val)
print(numbers)

college, student, type_ofcollege = numbers
print(college)

index = letters.index('b')
print("index of b is:", index)

occurrences_num = result.count(2)
print("number of occurrences of the integer 2 is:", occurrences_num)


enumerate_list = enumerate(result)
for index, val in enumerate_list:
    print(index, val)