from Cpf import Documento
from validate_docbr import CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "03313540201"

# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
# documentoCNPJ = CpfCnpj(exemplo_cnpj,'cnpj')
# documentoCPF = CpfCnpj(exemplo_cpf,'cpf')
# print(documentoCNPJ)
# print(documentoCPF)
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

