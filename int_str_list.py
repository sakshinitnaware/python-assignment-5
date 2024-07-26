# data is a list with mixed elements of integer and string
data = [10,'keyboard',13,'python',41,'green',2,2,2,]
# lambda funtion to check with isinstance() function to check the mixed list of int and str respectively
result = filter(lambda data: isinstance(data,int),data)
result_1 = filter(lambda data: isinstance(data,str), data)
# printing the result list for only integer in the data list 
print(list(result))
# printing the result list for only string in the data list
print(list(result_1))
