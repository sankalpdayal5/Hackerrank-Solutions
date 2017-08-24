def recur_factorial(n):  
    if n == 2:  
        return n  
    else:  
        return n*recur_factorial(n-1)  
# take input from the user  
num = int(input()) 
if(num>=2 and num<=12):
    print(recur_factorial(num))
