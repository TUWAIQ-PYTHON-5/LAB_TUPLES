# LAB_TUPLES




# Create a tuple called numbers that contains the integers 1, 2, and 3.
# Create a tuple called letters that contains the strings "a", "b", and "c".
numbers = (1,2,3)
letters = ("a","b","c")

# Print out the first item in the numbers tuple.
# Print out the last item in the letters tuple.
print("The first item in numbers tuple is :",numbers[0])
print("The last item in letters tuple is :",letters[-1])

# Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.

result = (numbers + letters)
print(result)
# Print out the length of the result tuple.
print("The length of result tuple is : ", len(result))


# Use the in keyword to check if the integer 4 is in the result tuple.

if 4 in result:
  print("yes")
else :
    print ("don't find this value in result tuple ! ")

# Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.
list_num = [4,5,6]
print(tuple(list_num))

# Use tuple unpacking to save the values of the above tuple into variables. 

var1 ,var2,var3 = list_num
print(var1,var2,var3)





