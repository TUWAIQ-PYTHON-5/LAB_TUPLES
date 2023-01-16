numbers = (1, 2, 3)
letters  = ("a", "b", "c")
print(numbers[0])
print(letters[2])

print(numbers + letters)
result = numbers + letters
print(len(result))

res = False
for ele in numbers:
    if result == ele:
        res = True
        break
 
print("Does tuple contain required value ? : " + str(res))

val = [4, 5, 6]
numbers = tuple(val)
print(numbers)

college, student, type_ofcollege = numbers
print(college)