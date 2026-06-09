## Ambiente Virtual (.venv)

### O que é?
Uma "bolha" isolada que contém o Python e todas as bibliotecas 
necessárias para esse projeto rodar corretamente.

### Para que serve?
Imagine que você tem dois projetos Python:
- Projeto A precisa da versão 1.0 de uma biblioteca
- Projeto B precisa da versão 2.0 da mesma biblioteca

Se você instalasse tudo no Python global do seu computador, 
eles iriam se conflitar. O ambiente virtual resolve isso — 
cada projeto tem suas próprias dependências, nas versões certas, 
sem interferir nos outros.

### Por que não está no repositório?
A pasta .venv pode ser muito pesada e é gerada automaticamente. 
Por isso está listada no .gitignore. Basta recriá-la localmente 
seguindo as instruções abaixo.

### Como recriar localmente

# 1. Criar o ambiente virtual
python -m venv .venv

# 2. Ativar
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Mac/Linux

# 3. Instalar as dependências do projeto
pip install -r requirements.txt

## Por que o main.py fica fora do .venv?

O `.venv` é infraestrutura — contém o Python e as bibliotecas necessárias 
para o projeto rodar. O `main.py` é o código em si — o que você criou.

São responsabilidades diferentes, por isso ficam separados.
O `.venv` existe para servir o seu código, não para guardá-lo.

# 4. Desativar quando terminar
deactivate

# Python — Conceitos Básicos

## Variáveis

Variáveis armazenam valores e não precisam de tipo declarado.

```python
nome = "Ana"
idade = 30
preco = 9.99
ativo = True
```

---

## Listas

Estrutura ordenada e mutável que armazena múltiplos valores.

```python
frutas = ["maçã", "banana", "uva"]

frutas.append("manga")   # adiciona
frutas.remove("banana")  # remove
frutas[0]                # acessa pelo índice
```

---

## Funções

Bloco de código reutilizável, definido com `def`.

```python
def somar(a, b):
    return a + b

resultado = somar(3, 5)  # 8
```

---

## Dicionários

Armazena dados em pares de **chave: valor**.

```python
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}

pessoa["nome"]           # acessa
pessoa["profissao"] = "Dev"  # adiciona
del pessoa["cidade"]     # remove
```
