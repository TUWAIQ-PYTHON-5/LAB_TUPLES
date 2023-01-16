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



