'''

Create a tuple called numbers that contains the integers 1, 2, and 3.
Create a tuple called letters that contains the strings "a", "b", and "c".
Print out the first item in the numbers tuple.
Print out the last item in the letters tuple.
Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.
Print out the length of the result tuple.
Use the in keyword to check if the integer 4 is in the result tuple.
Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.
Use tuple unpacking to save the values of the above tuple into variables
'''

#Create a tuple

numbers = (1, 2, 3)
letters = ('a' , 'b', 'c')

print(numbers[0])
print(letters[-1])

result = numbers + letters
print(len(result))

#Use the in keyword

if 4 in result:
    print("the number is exsit")
else:
    print("the number is not exsit")

#Use the tuple() function

list_=[4,5,6]
tuple_ = tuple(list_)
print(tuple_)

#Use tuple unpacking

num1 , num2 , num3 = tuple_

print(num1 , num2 , num3)


