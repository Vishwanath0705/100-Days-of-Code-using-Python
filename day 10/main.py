def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operation = {'+':add,'-':sub,'*':mul,'/':div}
def calculator():
    num1 = float(input("Enter the first number:"))
    end_of_calculation = False
    while not end_of_calculation:
        for opr in operation:
            print(opr)
        opr = input("Enter any operation from the above : ")
        num2 = float(input("Enter the second number : "))
        operation_symbol = operation[opr]
        answer = operation_symbol(num1,num2)
        print("Answer : ",answer)
        choice = input("Enter y if you want to proceed with further calculation else type n :")
        if choice == 'y':
            num1 = answer
        else:
            print("Final answer:" ,answer)
            end_of_calculation = True
calculator()
