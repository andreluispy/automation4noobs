# Bool Test
 Aqui veremos sobre os testes booleanos, nos quais podemos testar se uma comparação ou o valor de retorno de uma função é verdadeiro ou falso.

## Bool Test - True
 No exemplo abaixo, usaremos a função `self.assertTrue` para testar se uma afirmação é verdadeira, no primeiro exemplo comparamos se a função `isupper` retorna True, no segundo exemplo usamos uma comparação lógica para ver se `'FOO'` é igual a `'FOO'`:

 ```py
import unittest

class BoolTest(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue('FOO' == 'FOO')

if __name__ == '__main__':
    unittest.main()
 ```

 Como todas as comparações são verdadeiras, nosso script será executado sem nenhum erro e retornará:

 ```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
 ```

## Bool Test - False
 Nesse exemplo, usaremos a função `self.assertFalse` para testar se uma afirmação é falsa, no primeiro exemplo comparamos se a função `isupper` retorna False, no segundo exemplo usamos uma comparação lógica para ver se `'foo'` é igual a `'FOO'`:

 ```py
import unittest

class BoolTest(unittest.TestCase):
    def test_isupper(self):
        self.assertFalse('foo'.isupper())
        self.assertFalse('foo' == 'FOO')

if __name__ == '__main__':
    unittest.main()
 ```

 Como todas as comparações são falsas, nosso script será executado sem nenhum erro e retornará:

 ```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
 ```

# CLI
 UNITTEST fornece alguns argumentos que podemos passar no terminal ao executar o script.

## CLI - VERBOSE
 Passando a opção -v para o nosso Script permite um nível mais alto de detalhes, neste exemplo:
 
 ```py
import unittest

class BoolTest(unittest.TestCase):
    def test_isupper(self):
        self.assertFalse('foo'.isupper())

if __name__ == '__main__':
    unittest.main()
 ```

 Se passarmos o argumento -v: `python test.py -v`. O resultado será:
 
 ```
test_isupper (__main__.BoolTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
 ```

 Podemos ver `test_isupper` que é a função que criamos, podemos ver `(__main __. BoolTest)` que diz que a função faz um teste booleano e no final podemos ver `ok` que diz que o teste passou

## CLI - UNITTEST Para Terminal
 O módulo unittest pode ser usado diretamente no terminal para rodar testes de módulos, classes ou mesmo testes de métodos individuais:


 - python -m unittest test_module1 test_module2
 - python -m unittest test_module.TestClass
 - python -m unittest test_module.TestClass.test_method

 O arquivo especificado precisa ser “importável” como um módulo. Se você quer executar um arquivo de teste que não é importável como um módulo, você deve executar o arquivo diretamente.

 Veja as principais opções de linha de comando:

 - -f, --failfast

    Parar a execução do teste no primeiro erro ou falha.

 - --locals

    Mostra variáveis locais no traceback.

 A linha de comando também pode ser usada para descobrir testes, para executar todos os testes de um projeto ou apenas de um subconjunto usando Test Discovery

 Para serem compatíveis com o descobrimento de testes, todos os arquivos de teste devem ser módulos ou pacotes com nomes validos.

 O descobrimento de testes é implementado no TestLoader.discover(), mas também pode ser utilizado a partir da linha de comando. O comando básico para uso é:

 `python -m unittest discover`

 Como um atalho, python -m uniitest é o equivalente a python -m uniitest discover. Se você deseja passar argumentos para a descoberta de testes, o subcomando discover deve ser usado explicitamente.

 Veja as principais opções do discover:

 - -v, --verbose

    Saída verbosa

 - -s, --start-directory directory

    Diretório no qual se inicia o descobrimento

 - -p, --pattern pattern

    Padrão de texto para se descobrir os arquivos de teste (test*.py por padrão)

 Veja mais sobre a CLI em: [https://docs.python.org/pt-br/3.7/library/unittest.html#command-line-interface](https://docs.python.org/pt-br/3.7/library/unittest.html#command-line-interface)

[Retornar](../../README.md)
