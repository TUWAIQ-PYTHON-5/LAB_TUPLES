#Create a tuple called numbers that contains the integers 1, 2, and 3.
tuple_numbers = (1,2,3)

#Create a tuple called letters that contains the strings "a", "b", and "c".
tuple_letters = ("a","b","c")

#Print out the first item in the numbers tuple.
print(tuple_numbers[0])

#Print out the last item in the letters tuple
print(tuple_letters[2])

#Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.
result = (tuple_numbers+tuple_letters)
print(result)

#Print out the length of the result tuple.
print(len(result))

#Use the in keyword to check if the integer 4 is in the result tuple.
if 4 in tuple_numbers:
    print("number 4 in tuple_number")
else:
    print("not found")
  
#Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.
list_number = [4,5,6]
number1 = tuple(list_number)
print(number1)
print(type(number1))


#Use tuple unpacking to save the values of the above tuple into variables.
tuple_numbers1, tuple_numbers2, tuple_numbers3 = tuple_numbers
print(tuple_numbers1,tuple_numbers2,tuple_numbers3)

tuple_letters1, tuple_letters2, tuple_letters3 = tuple_letters
print(tuple_letters1,tuple_letters2,tuple_letters3)