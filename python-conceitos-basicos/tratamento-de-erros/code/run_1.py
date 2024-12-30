try:
    num1 = 3
    num2 = 0
    response = num1/num2
    print(response)
except ZeroDivisionError:
    print('Divisao por zero')
except Exception as exception:
    print(exception)
finally:
    print('Vai ser executado independente do que acontecer')