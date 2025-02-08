url = input("Digite a URL para validação: ")
if url.startswith("https://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida")