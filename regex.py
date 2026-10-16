# O módulo re(Operações com expressões regulares) é a biblioteca padrão 
# do Python usada para buscar, validar e substituir padrões de texto
import re

# Texto de exemplo a ser buscado o email
texto = "Entre em contato pelo email support@example.com"

# Definição do padrão do email que será a regex a ser buscada no texto
#  Para especificar um regex em Python, é necessário começar com a letra r, 
#  de modo que o Python entenda que se trata de uma expressão regular.

# [a-zA-Z0-9._%+-] corresponde a qualquer caractere de a-z minúsculas,
# A-Z maiúsculas, dígitos de 0-9 e qualquer dos caracteres especiais
# '\.' representa um ponto literal 
# Depois do ponto é aceito letras de a-z minúsculas e maiúsculas com
# extensão de duas ou mais letras(com, br, org, etc.)
padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

resultado = re.search(padrao_email, texto)

if resultado:
    print("Email encontrado:", resultado.group())
else:
    print("Nenhum email encontrado.")