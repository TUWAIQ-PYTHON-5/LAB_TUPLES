# - Create a tuple called numbers that contains the integers 1, 2, and 3.
numbers = (1,2,3)

# - Create a tuple called letters that contains the strings "a", "b", and "c".
letters = ("a", "b", "c")

# - Print out the first item in the numbers tuple.
print(numbers[0])

# - Print out the last item in the letters tuple.
print(letters[0])

#- Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.
result = numbers + letters
print(result)

# - Print out the length of the result tuple.
print(len(result))

# - Use the in keyword to check if the integer 4 is in the result tuple.
if 4 in result :
    print("number 4 exsits in the result tuble")
else :
    print("number 4 does not exsits in the result tuble")

# - Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.
newTuble = tuple([4, 5, 6])

# - Use tuple unpacking to save the values of the above tuple into variables. 
var1, var2, var3 = newTuble
print(var1, var2, var3)

print("-----------------")

# Bonus : 
# - Use the index() method to find the index of the string "b" in the letters tuple. 
index = result.index("b")
print(index)

# without index() method
# counter = 0
# doesNotExsits = True
# for char in result :
#     if char == "b":
#         print(counter)
#         doesNotExsits = False
#     else : 
#         counter += 1
# if doesNotExsits :
#     print("b does not exsits")

# - Use the count() method to find the number of occurrences of the integer 2 in the result tuple.
counter2 = result.count(2)
print(counter2)

# - Use the enumerate() function to iterate over the result tuple, along with its index, and print out each item and its index.
enm = enumerate(result)
print(list(enm))


