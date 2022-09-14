
def calc(operation,x,y):
    if operation=='add':
        return x+y
    elif operation=='sub':
        return x-y
    elif operation=='multi':
        return x*y
    elif operation=='div':
        return x/y
    elif operation=='power':
        return x**y
    elif operation=='modulus':
        return x//y

calculation = "Yes"

while calculation == "Yes":    
    operation  = input("Enter the operation like add,sub,multi,div,power,modulus here: ")
    first_num = float(input("Enter the first num "))
    second_num = float(input("Enter the second num "))
    
    print(f"The operation of {first_num} {operation} {second_num} is: ",int(calc(operation, first_num, second_num)))
    
    calculation = input("Want to continue: ")