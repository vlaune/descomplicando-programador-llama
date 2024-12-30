from methods_classes.error import MeuErroPersonalizado

def error_handler_method(error):
    if isinstance(error, MeuErroPersonalizado):
        print('tratar meu erro personalizado')
        return

    if isinstance(error, ZeroDivisionError):
        print('tratar divisao por zero')
        return
    
    if isinstance(error, Exception):
        print('Tratar caso geral')
        return