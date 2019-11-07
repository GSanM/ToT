import sys
import re

f = open(sys.argv[1], 'r')
final = {}
for line in f:
    s_line = line.rstrip().lower()
    part = s_line.split(':')
    try:
        if part[1] is not '':
            final.update({part [0]: part [1]})
    except:
        pass
# print(final)
# print("Referência:", final['referencia '])
print("CEP:", final['c.e.p.'])
print("CNPJ:", final['c.n.p.j.'])
# print("Fornecedor:", final['fornecedor '])
# print("Gerente:", final['gerente'])
print("Emissor:", final['emissor'])
print("Data de Emissão:", final['data emissão'])
print("Tipo de Avaliação:", final['tipo de avaliação'])
print("Tipo de Inspeção:", final['tipo de inspeção'])