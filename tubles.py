#Create a tuple called numbers that contains the integers 1, 2, and 3.
number = 1, 2, 3

#Create a tuple called letters that contains the strings "a", "b", and "c".
letters = "a", "b", "c"

#Print out the first item in the numbers tuple.
print(number[0])

#Print out the last item in the letters tuple.
print(letters[-1])

#Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.
result=number+letters
print(result)

#Print out the length of the result tuple.
print(len(result))

#Use the in keyword to check if the integer 4 is in the result tuple.
res = 4 in result
print (res)

#Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.
def convert(list):
    return tuple(list)
  
list = [4,5,6]
print(convert(list))

#Use tuple unpacking to save the values of the above tuple into variables.
n1,n2,n3 =([4,5,6])
print (n1,n2,n3)

#Use the index() method to find the index of the string "b" in the letters tuple. 
ind = (letters)  
print(ind)  
index = ind.index('b') 
print("Index of b is: ",index)

#Use the count() method to find the number of occurrences of the integer 2 in the result tuple.
count = result.count(2)
print(count) 

#Use the enumerate() function to iterate over the result tuple, along with its index, and print out each item and its index.
e_list = enumerate(result,2)
print(tuble(e_list))





