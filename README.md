calculadora.py - Contem funções matemáticas
test_calculadora.py - existem testes para as funções( melhorados com IA usando exemplos do github de base)
test_calculadora_IA.py - Feito com IA para atividade solicitada (código sugerido abaixo da análise)

## Uso de IA para geração de cenários de teste

### Função escolhida

def potencia(a,b):
    return a ** b

### Prompt utilizado

Atue como um professor de Teste de Software.
Tenho a seguinte função Python:

def potencia(a,b):
    return a ** b

Quero criar testes unitários usando unittest.

Liste pelo menos 6 cenários de teste para essa função.

Para cada cenário, informe:

- nome do cenário;

- entrada;

- resultado esperado;

- tipo do cenário: caso normal, caso de borda ou caso de erro.

Não gere código ainda.


# Lista de casos sugerida

Cenários de teste para a função potencia(a, b)

1 Potência com números inteiros positivos
Entrada: a=2, b=3
Resultado esperado: 8
Tipo: Caso normal

2 Potência com expoente igual a 1
Entrada: a=7, b=1
Resultado esperado: 7
Tipo: Caso de borda

3 Potência com expoente igual a 0
Entrada: a=5, b=0
Resultado esperado: 1
Tipo: Caso de borda

4 Potência com base igual a 0 e expoente positivo
Entrada: a=0, b=4
Resultado esperado: 0
Tipo: Caso de borda

5 Potência com expoente negativo
Entrada: a=2, b=-2
Resultado esperado: 0.25
Tipo: Caso normal

6 Potência com base negativa e expoente ímpar
Entrada: a=-2, b=3
Resultado esperado: -8
Tipo: Caso normal

7 Potência com base negativa e expoente par
Entrada: a=-2, b=4
Resultado esperado: 16
Tipo: Caso normal

8 Potência com números decimais
Entrada: a=2.5, b=2
Resultado esperado: 6.25
Tipo: Caso normal

9 Potência de zero elevado a zero
Entrada: a=0, b=0
Resultado esperado: 1
Tipo: Caso de borda

10 Parâmetro inválido (texto como base)
Entrada: a="2", b=3
Resultado esperado: Exceção TypeError
Tipo: Caso de erro

11 Parâmetro inválido (texto como expoente)
Entrada: a=2, b="3"
Resultado esperado: Exceção TypeError
Tipo: Caso de erro

12 Base e expoente negativos
Entrada: a=-2, b=-3
Resultado esperado: -0.125
Tipo: Caso normal

Essa lista cobre operações comuns, valores de fronteira (0 e 1) e entradas inválidas, fornecendo uma boa base para os testes unitários da função.

## Análise
Julgo os casos 10 e 11 irrelevantes para a proposta, por isso foram removidos.
Os outros testes são plausíveis.

## Código da IA
def test_potencia_inteiros_positivos(self):
    self.assertEqual(potencia(2, 3), 8)

def test_potencia_expoente_um(self):
    self.assertEqual(potencia(7, 1), 7)

def test_potencia_expoente_zero(self):
    self.assertEqual(potencia(5, 0), 1)

def test_potencia_base_zero_expoente_positivo(self):
    self.assertEqual(potencia(0, 4), 0)

def test_potencia_expoente_negativo(self):
    self.assertEqual(potencia(2, -2), 0.25)

def test_potencia_base_negativa_expoente_impar(self):
    self.assertEqual(potencia(-2, 3), -8)

def test_potencia_base_negativa_expoente_par(self):
    self.assertEqual(potencia(-2, 4), 16)

def test_potencia_numeros_decimais(self):
    self.assertEqual(potencia(2.5, 2), 6.25)

def test_potencia_zero_elevado_zero(self):
    self.assertEqual(potencia(0, 0), 1)

def test_potencia_base_expoente_negativos(self):
    self.assertEqual(potencia(-2, -3), -0.125)

## Resultado Terminal
PS C:\Users\Luis\Desktop\Coisas Luis\teste_unitario_python> python  -m  unittest  test_calculadora_IA.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK