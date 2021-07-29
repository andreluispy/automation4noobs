# Skip
 Se você quiser não considerar um teste, você pode usar:
 
 *Nota: Leia os comentarios*
 ```py
class MyTestCase(unittest.TestCase):
    @unittest.skip() # Usando skip em uma função
    def test_nothing(self):
        self.fail("shouldn't happen") # self.fail é uma função da classe para criar uma falha

    @unittest.skipIf(mylib.__version__ < (1, 3), "not supported in this library version") # Pular um teste com uma condição
    def test_format(self):
        pass

    def test_maybe_skipped(self):
        if 1<3:
            self.skipTest() # Pulando um teste com self.skipTest
        pass
 ```

# Fim do Curso
 Aqui termina o curso sobre **UNITTEST** que aborda os conceitos basicos e nescessarios sobre a lib **UNITTEST**, se quiser ver mais sobre a lib, como por exemplo testes de regex, vá em: [https://docs.python.org/pt-br/3.7/library/unittest.html](https://docs.python.org/pt-br/3.7/library/unittest.html#command-line-interface)

[Retornar](../../README.md)
