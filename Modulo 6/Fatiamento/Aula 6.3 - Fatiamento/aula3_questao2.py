# Lista de URLs fornecida
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Usando fatiamento para extrair os nomes dos domínios
dominios = [url[4:-4] for url in urls]

# Exibir o resultado
print("dominios:", dominios)
