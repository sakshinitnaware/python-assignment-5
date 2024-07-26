data = [10,501,22,37,100,999,87,351]
# the lambda funtion used to check the element greater than 4 in the list 
result = filter(lambda data: data > 4,data)
print(list(result))

#output all the elements in the list are greater than 4
#[10, 501, 22, 37, 100, 999, 87, 351]
