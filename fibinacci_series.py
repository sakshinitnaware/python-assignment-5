# lamnda funtion to calculate fibonacci series, if data is negatite or 1 then returing data and else data greater than 1 then calculating the fibonacci
result = lambda data : data if data <=1 else result(data - 1) + result(data - 2)
# for loop tto print the fibonacci from 1 to 50 
for data in range(1,51):    
    # storing the result into a variable fibo
    fibo = result(data)
    # printing the results from 1 tp 50
    print(f"list(result({data})) : {fibo}") 
