def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

def main():
    print("Suma: ",suma(5,5))
    print("Resta: ",resta(5,5))
    print("Multiplicacion: ",multiplicacion(5,5))
    print("Division: ",division(5,5))

main()
assert suma(5,5) == 10
assert resta(5,5) == 0
assert multiplicacion(5,5) == 25
assert division(5,5) == 5