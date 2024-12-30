from methods_classes.error_handler import error_handler_method
from methods_classes.error import MeuErroPersonalizado

def calculate(num1, num2):
    result = num1/num2
    if (num1 + num2 == 2):
        raise MeuErroPersonalizado('Resultado 2')
    return result

try:
    response = calculate(1,1)
except Exception as exception:
    error_handler_method(exception)