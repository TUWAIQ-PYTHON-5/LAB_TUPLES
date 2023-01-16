# LAB_TUPLES

#- Create a tuple called numbers that contains the integers 1, 2, and 3.
number_tuple = ( 1 , 2 , 3)

#- Create a tuple called letters that contains the strings "a", "b", and "c".
letter_tuple = ("a" , "b" , "c")
#- Print out the first item in the numbers tuple.

print(number_tuple[0])
#- Print out the last item in the letters tuple.

print(letter_tuple[-1])
#- Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.

result = number_tuple + letter_tuple
#- Print out the length of the result tuple.

print(len(result))

#- Use the in keyword to check if the integer 4 is in the result tuple.

if 4 in result:
    print("4 is exist")
else:
    print("not found") 
#- Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.

list_number = [4 , 5 , 6]
convert_list_to_tuple = tuple(list_number)
print(type(convert_list_to_tuple))
print(convert_list_to_tuple)
#- Use tuple unpacking to save the values of the above tuple into variables. '''

val1 , val2 , val3 = convert_list_to_tuple