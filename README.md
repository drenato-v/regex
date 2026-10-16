# Buscador de E-mails com Regex

Projeto simples em Python que encontra um endereço de e-mail dentro de um texto usando **expressões regulares (regex)**.

---

## O que é Regex?

### Definição

Uma **expressão regular** (*regular expression*, ou **regex**) é uma sequência de caracteres que descreve um **padrão de texto**. Esse padrão é usado por um motor de busca para encontrar, validar, extrair ou substituir trechos de texto que se encaixem nele.

### Como funciona

Em vez de procurar uma palavra exata, a regex descreve a **forma** do que se procura. Por exemplo, em vez de buscar `maria@gmail.com`, descrevemos: *"letras ou números, seguidos de @, seguidos de um domínio, um ponto e uma extensão"*. Assim, qualquer e-mail que siga esse formato é encontrado.

Para isso, a regex combina caracteres comuns com **metacaracteres**, que têm significados especiais:

| Símbolo  | Significado                                      | Exemplo                                   |
| --------- | ------------------------------------------------ | ----------------------------------------- |
| `[...]` | Qualquer **um** dos caracteres listados    | `[abc]` casa com `a`, `b` ou `c`  |
| `a-z`   | Intervalo de caracteres (dentro de `[]`)       | `[0-9]` casa com qualquer dígito       |
| `+`     | **Um ou mais** do item anterior            | `a+` casa com `a`, `aa`, `aaa`... |
| `{n,}`  | **No mínimo n** repetições              | `[a-z]{2,}` casa com `com`, `br`... |
| `.`     | **Qualquer** caractere                     | `a.c` casa com `abc`, `a-c`...      |
| `\`     | **Escape**: torna literal um metacaractere | `\.` casa só com um ponto              |

### Exemplos de uso no dia a dia

- Validar se um e-mail, CPF ou telefone foi digitado no formato correto
- Extrair todas as datas ou links de um documento
- Substituir ou limpar trechos de texto em massa

---

## A ideia do projeto

O script recebe um texto e procura nele o **primeiro endereço de e-mail** que encontrar, usando o módulo `re`, a biblioteca padrão do Python para expressões regulares.

### O padrão utilizado

```python
padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```

| Trecho                | Parte do e-mail | O que aceita                                      |
| --------------------- | --------------- | ------------------------------------------------- |
| `[a-zA-Z0-9._%+-]+` | Usuário        | Uma ou mais letras, números ou `. _ % + -`     |
| `@`                 | Arroba          | A arroba, literal                                 |
| `[a-zA-Z0-9.-]+`    | Domínio        | Uma ou mais letras, números, `.` ou `-`      |
| `\.`                | Ponto           | Um ponto literal                                  |
| `[a-zA-Z]{2,}`      | Extensão       | Duas ou mais letras (`com`, `br`, `org`...) |

### Por que o `r` antes das aspas?

O `r'...'` cria uma **raw string** (string "crua"): o Python deixa de interpretar a barra invertida `\` como sequência de escape (como `\n` ou `\t`) e entrega o texto intacto ao motor de regex. Como regex usa `\` com frequência, é boa prática escrever todo padrão como raw string.

---

## Como executar

Requisitos: **Python 3** (o módulo `re` já vem instalado).

```bash
python main.py
```

> Ajuste `main.py` para o nome do seu arquivo.

### Saída esperada

```
Email encontrado: support@example.com
```

---

## 🧪 Exemplos

| Texto                                               | Resultado                                           |
| --------------------------------------------------- | --------------------------------------------------- |
| `Entre em contato pelo email support@example.com` | `support@example.com`                             |
| `Fale com joao.silva@empresa.com.br hoje`         | `joao.silva@empresa.com.br`                       |
| `Meu email é maria@gmail`                        | Nenhum email encontrado (falta a extensão)         |
| `Escreva para ana@site.c`                         | Nenhum email encontrado (extensão com só 1 letra) |

---

## Possíveis melhorias

- Usar `re.findall()` para encontrar **todos** os e-mails do texto, não só o primeiro
- Ler o texto de um arquivo em vez de deixá-lo fixo no código
- Usar `re.fullmatch()` para **validar** se uma string inteira é um e-mail
