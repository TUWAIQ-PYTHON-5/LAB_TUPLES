# LAB_TUPLES
#- Create a tuple called numbers that contains the integers 1, 2, and 3.
#- Print out the first item in the numbers tuple.

tuple_numbers = (1, 2 , 3)
print(tuple_numbers[0])

# - Create a tuple called letters that contains the strings "a", "b", and "c".
# - Print out the last item in the letters tuple.

tuple_letters = ("a", "b", "c")
print(tuple_letters[2])

# - Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.

result = tuple_numbers + tuple_letters

# - Print out the length of the result tuple.

tuples_length = len(result)
print(tuples_length)

# - Use the in keyword to check if the integer 4 is in the result tuple.

if 4 in result :
    print(" 4 is in the tuple ! " )
else :
    print(" 4 is not in the tuple ! " )



# - Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.

convert_list_to_tuple = [4,5,6]
tuple(convert_list_to_tuple)
print (tuple)

# - Use tuple unpacking to save the values of the above tuple into variables. 

Value_1, Value_2, Value_3 = tuple_numbers

print(Value_1,Value_2 , Value_3)




Value_11, Value_22, Value_33 = tuple_letters

print(Value_11,Value_22 , Value_33)



