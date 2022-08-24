from codigo.bytebank import Funcionario

# lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)
# print(lucas.idade())
#
# -> código ja traduzido para o pytest
# def teste_idade():
#     funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
#     print(f'Teste = {funcionario_teste.idade()}')
#
#     funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
#     print(f'Teste = {funcionario_teste1.idade()}')
#
#     funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
#     print(f'Teste = {funcionario_teste2.idade()}')
#
# teste_idade()


ana = Funcionario('Ana', '12/03/1997', 10000000)
print(ana.calcular_bonus())