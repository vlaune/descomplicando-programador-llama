Em Python erros sao excecoes, pense que uma aplicacao/script segue um processamento natural como uma linha reta:
--------->
No momento em que algo nao entre em concordancia, ele gera uma excecao, que sai do processamento natural e vai por outro caminho.
----|--> :Processamento natural
    ---> :Excecao

No `run.py` que criamos no diretorio **/code**, geramos um `ZeroDivisionError: division by zero`, e percebemos que tudo que passamos, foi gerado ate o momento do erro.
- Para tratar erros desse tipo, podemos utilizar o `try except`. Adicionando o `try except`, conseguimos direcionar o fluxo do processamento para a excecao, sem gerar um erro;
- O python trata suas excecoes como classes, e eh possivel "brincar" com isso, instanciando por exemplo o proprio erro como excecao. Como fiz na linha 8 (`run.py`)
    - `print(isinstance(exception, ZeroDivisionError))`: `True`;
- Podemos tambem chamar a classe especifica do erro, por exemplo, chamar o `ZeroDivisionError`. Como feito na linha 6;
- Temos tambem o comando `finally` (`run.py`). Que independente do que ocorrer no `try except`, o `finally` sera executado;

No `usecase.py`, temos um exemplo de uso interessante:
    - Se trata de uma conexao de banco de dados, em que vai ser realizada uma coleta;
    - Caso nao tenha resultado `NoResultFound`:
        - Ele ira retornar None.
    - Caso seja outra excecao, ele ira fazer um rollback.
    - E independente do que aconteca, ele ira fazer um `database.session.close()`

Para conhecer sobre os diferentes tipos de erros:
- https://www.tutorialsteacher.com/python/error-types-in-python

Quando utilizar o processamento de erros:
- Processamento matemático extenso;
- Transformacao de valores;
- Comunicações externas (DBs, http, Socket, RabbitMQ...)
- **Levantamento de erros personalizados**

O que eh esse **Levantamento de Erros Personalizados**?
- O python possui a capacidade de lancar erros com o `raise` (`run2.py` linha 4);
- O `raise` lanca um erro e acaba o processamento no momento em que eh chamado.
    - Um caso de uso, quando rodamos uma query em um banco de dados e nao encontramos nada.
- Posso tambem criar o meu erro, herdando da classe `Exception`:
    - Exemplo: `error.py`
    - Criamos tambem o `error_handler.py`, que serve para tratar diferentes tipos de erros com uma mesma classe.
    - `usecase_2.py` apresenta um exemplo de como utilizar o `error_handler.py` de forma utilizavel em projetos.