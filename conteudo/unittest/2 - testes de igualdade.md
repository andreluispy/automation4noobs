# Teste de Igualdade
 O módulo unittest fornece um conjunto amplo de ferramentas para a construção e execução de testes.

 Aqui, criaremos uma função para testar se uma string está em maiúsculo:

 ```py
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

unittest.main()
 ```

 Aqui criamos uma classe para nossos testes e podemos ver que ela herda a classe `unittest.TestCase`, dentro dela criamos uma função para nossos testes, a função `test_upper`, dentro dela chamamos a função `self.assertEqual`(usamos self porque é uma função da classe) que leva 2 parâmetros:

    - Entrada
    - Saída
 
   A entrada é o valor que queremos testar, neste caso eu pego a string `'foo'` e deixo ela em maiúscula usando `.upper () `, e na saída passamos o valor esperado que é `'FOO'`(a mesma string em maiúsculo).

   No final do script chamamos a função `unittest.main ()` que executa o código, no final a saída esperada no console é algo como:

 ```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
 ```

 Abaixo dos traços vemos informações sobre os testes, podemos ver que 1 teste foi executado e que demorou 0.000 segundos. Abaixo disso podemos ver OK, o que significa que passamos em todos os testes.

# Vários Testes

 Claro que este teste sempre passará, isso porque eu usei `.upper ()` que retorna a string em maiúsculas. Mas vamos testar várias strings agora:

 ```py
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper_01(self):
        self.assertEqual('foo', 'FOO')
    def test_upper_02(self):
        self.assertEqual('FOO', 'FOO')
    def test_upper_03(self):
        self.assertEqual('FoO', 'FOO')

unittest.main()
 ```

 Podemos ver que o único teste que passa é `test_upper_02`.
 
 Em test_upper_01 comparamos se `'foo'` é igual a `'FOO'`, a string que comparamos não está em maiúscula e a string correta é maiúscula e isso gera um erro.

 Em test_upper_03 comparamos se `'FoO'` é igual a `'FOO'`, a string que comparamos não está toda em maiúsculo e a string correta é maiúscula e isso gera um erro.

 A saida final é:

 ```
F.F
======================================================================
FAIL: test_upper_01 (__main__.TestStringMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/media/andre/Elements/github/unittest4noobs/test.py", line 5, in test_upper_01
    self.assertEqual('foo', 'FOO')
AssertionError: 'foo' != 'FOO'
- foo
+ FOO


======================================================================
FAIL: test_upper_03 (__main__.TestStringMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/media/andre/Elements/github/unittest4noobs/test.py", line 9, in test_upper_03
    self.assertEqual('FoO', 'FOO')
AssertionError: 'FoO' != 'FOO'
- FoO
?  ^
+ FOO
?  ^


----------------------------------------------------------------------
Ran 3 tests in 0.002s
 ```

 A primeira coisa que podemos ver é `FAIL: test_upper_01 (__main __. TestStringMethods)` que informa que test_upper_01 falhou, e podemos ver o porquê em:

 ```
AssertionError: 'foo' != 'FOO'
- foo
+ FOO
 ```

 Isso nos diz que `'foo'` é diferente(!=) de `"FOO"`, abaixo vemos as duas strings, uma que tem `-` que é a que testamos e outra tem `+` que é a certa.

 Então podemos ver `FAIL: test_upper_03 (__main __. TestStringMethods)` que informa que test_upper_03 falhou, e podemos ver o porquê em:

 ```
AssertionError: 'FoO' != 'FOO'
- FoO
?  ^
+ FOO
?  ^

 ```

 Isso nos diz que a string `'FoO'` é diferente(!=) de `"FOO"`, e desta vez podemos ver que ela indica a letra errada na string.

 No final, vemos que ele executou 3 testes em 0,002 segundos.

# Usando retorno de funções
 Nos testes de igualdade, podemos comparar os retornos de uma função. No teste a seguir, vou criar uma função que retorna um número e testar se retorna 0. E vamos testar o retorno da função:

 ```py
import unittest

def funcao_teste():
    return 0

class TestStringMethods(unittest.TestCase):
    def test_igualdade_funcao(self):
        self.assertEqual(funcao_teste(), 0)

unittest.main()
 ```

 A sáida vai ser:

 ```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
 ```

 Podemos ver que a função passou em nosso teste porque retornou o valor esperado (0).
 
 O que vimos pode parecer pouco, mas a maioria dos testes em funções e programas será desse tipo!

[Retornar](../../README.md)
