# Fontes
 O curso é baseado nas documentações oficiais do python para o framework: [https://docs.python.org/pt-br/dev/library/unittest.html](https://docs.python.org/pt-br/dev/library/unittest.html)

# O que é UNITTEST?
 O framework unittest foi originalmente inspirado no JUnit e tem um código semelhante contendo as principais estruturas de teste de unidades existentes em outras linguagens. Ele suporta a automação de testes, compartilhamento de configuração e código de desligamento para testes, agregação de testes em coleções e independência dos testes do framework de relatórios.

# O que preciso saber?
 O módulo unittest suporta alguns conceitos importantes de forma orientada a objetos:

 - definição de contexto de teste

    Uma definição de contexto de teste representa a preparação necessária pra performar um ou mais testes, além de quaisquer ações de limpeza relacionadas. Isso pode envolver, por exemplo, criar bancos de dados proxy ou temporários, diretórios ou iniciar um processo de servidor.

 - caso de teste

    Um test case é uma unidade de teste individual. O mesmo verifica uma resposta específica a um determinado conjunto de entradas. O unittest fornece uma classe base, TestCase, que pode ser usada para criar novos casos de teste.

 - Suíte de Testes

    Uma test suite é uma coleção de casos de teste, conjuntos de teste ou ambos. O mesmo é usado para agregar testes que devem ser executados juntos.

 - test runner

    Um test runner é um componente que orquestra a execução de testes e fornece o resultado para o usuário. O runner pode usar uma interface gráfica, uma interface textual ou retornar um valor especial para indicar os resultados da execução dos testes.

 Se você não entendeu, não se preocupe, pois lidaremos melhor com isso nas próximas partes.

[Retornar](../../README.md)
