"""
Lista de exercícios de programação.
Este módulo contém uma série de exercícios para praticar lógica de programação e manipulação de dados.
"""

from collections import Counter

# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = 40
# preco = 20

# if quantidade >= 0 and preco >= 0:
#     print('Dados válidos')
# else:
#     print('Dados inválidos')

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# temp = 20

# if temp > 70:
#     print('Alta')
# elif temp > 30:
#     print('Normal')
# else:
#     print('Baixa')

# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log.get('level') == 'ERROR':
#     print('Erro de severidade detectado')

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = 40
# email = 'teste@teste.com'

# if 18 < idade < 65:
#     if '@' in email:
#         print('Dados de usuário válidos')
#     else:
#         print('Email inválido')
# else:
#     print('Idade inválida')

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 12000, 'hora': 20}

# if transacao.get('valor') > 10_000 or not (9 <= transacao.get('hora') <= 18):
#     print('Transação suspeita')
# else:
#     print('Transação Normal')

# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = 'dfsdfosdaofjweripofjeriofgjwoerifjwoeipnmdcioasj easdfj weofwejfop we'

# contador = texto.count('e')
# print(contador)

# def contar_palavras(texto):
#     """
#     Conta quantas vezes cada palavra única aparece em um texto.

#     :param texto: String contendo o texto a ser analisado.
#     :return: Um dicionário com palavras como chave e contagem como valor.
#     """
#     palavras = texto.lower().split()  # Converte para minúsculas e divide em palavras
#     contagem = Counter(palavras)  # Conta as ocorrências de cada palavra
#     return contagem

# # Exemplo de uso
# texto = "Python é ótimo. Python é poderoso. Python é simples!"
# resultado = contar_palavras(texto)

# # Exibe a contagem de palavras
# for palavra, quantidade in resultado.items():
#     print(f"'{palavra}': {quantidade}")

# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# def normalizar_lista(numeros):
#     """ Normaliza uma lista de números para a escala de 0 a 1 """
#     minimo = min(numeros)
#     maximo = max(numeros)

#     # Evita divisão por zero se todos os números forem iguais
#     if maximo == minimo:
#         return [0] * len(numeros)

#     return [(x - minimo) / (maximo - minimo) for x in numeros]

# # Exemplo de uso
# numeros = [10, 20, 30, 40, 50]
# numeros_normalizados = normalizar_lista(numeros)

# print(numeros_normalizados)  # Lista normalizada entre 0 e 1

# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando


# def filtrar_dados_faltantes(lista_usuarios, campo):
#     """
#     Filtra usuários que possuem um campo específico faltando.

#     :param lista_usuarios: Lista de dicionários com dados dos usuários.
#     :param campo: O nome do campo que deve estar presente.
#     :return: Lista contendo apenas os dicionários que possuem o campo.
#     """
#     return [usuario for usuario in lista_usuarios if campo in usuario and usuario[campo] is not None]


# # Exemplo de uso
# usuarios = [
#     {"nome": "Alice", "email": "alice@email.com", "idade": 25},
#     {"nome": "Bob", "email": None, "idade": 30},
#     {"nome": "Carlos", "idade": 22},  # Falta o campo 'email'
#     {"nome": "Diana", "email": "diana@email.com", "idade": None},
# ]

# # Filtra apenas usuários que possuem email válido
# usuarios_com_email = filtrar_dados_faltantes(usuarios, "email")

# print(usuarios_com_email)

# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = '1,23,4,54,45,65,2,23,4,54,65,77,8,7,34,234,45,467456'
# num = numeros.split(',')
# pares = []

# for i in num:
#     if int(i)%2 == 0:
#         pares.append(int(i))

# print(pares)

# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.



# Exercícios com WHILE

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# texto = ''

# while 'sair' not in texto:
#     texto = input("Digite o que quiser e sair para sair: ")
#     print(texto)

# print('Pediu para sair fraco')

# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# num_sorte = 45
# num = 0

# while num != num_sorte:

#     num = input('Como esta sua sorte? Digite um numero entre 0 e 50: ') 
#     if num.isdigit():
#         num = int(num)
#         print('Errouuuu, tente novamente')
#         print('')
#     else:
#         print('Digite um numero valido!')
#         print('')

# print('Acertouuu')

# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# import time
# import random

# def simular_api(pagina):
#     """
#     Simula o retorno de uma API paginada.
    
#     :param pagina: Número da página solicitada.
#     :return: Um dicionário com os dados da página e o próximo número de página.
#     """
#     dados_por_pagina = 5  # Quantidade de registros por página
#     total_paginas = 4  # Número máximo de páginas

#     if pagina > total_paginas:
#         return {"dados": [], "proxima_pagina": None}  # Indica que não há mais páginas

#     # Simula dados fictícios para cada página
#     dados = [f"Item {i + (pagina - 1) * dados_por_pagina}" for i in range(1, dados_por_pagina + 1)]

#     # Retorna os dados e a próxima página
#     return {
#         "dados": dados,
#         "proxima_pagina": pagina + 1 if pagina < total_paginas else None
#     }

# # Simulação do consumo da API paginada
# pagina_atual = 1
# while pagina_atual is not None:
#     resposta = simular_api(pagina_atual)  # Consome a API

#     # Processa os dados retornados
#     for item in resposta["dados"]:
#         print(f"Processando: {item}")
#         time.sleep(random.uniform(0.2, 0.5))  # Simula um tempo de processamento

#     # Verifica se há mais páginas
#     pagina_atual = resposta["proxima_pagina"]

# print("Todos os dados foram processados! ✅")


# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# import time
# import random

# def conectar_servico():
#     """
#     Simula uma tentativa de conexão a um serviço.
#     Retorna True se a conexão for bem-sucedida e False caso contrário.
#     """
#     return random.random() < 0.3  # 30% de chance de sucesso na conexão

# # Configuração do número máximo de tentativas
# max_tentativas = 5
# tentativa_atual = 0

# while tentativa_atual < max_tentativas:
#     tentativa_atual += 1
#     print(f"Tentativa {tentativa_atual}/{max_tentativas}...")

#     if conectar_servico():
#         print("✅ Conexão bem-sucedida!")
#         break
#     else:
#         print("❌ Falha na conexão. Tentando novamente...")
#         time.sleep(2)  # Aguarda 2 segundos antes da próxima tentativa

# if tentativa_atual == max_tentativas:
#     print("⚠️ Máximo de tentativas atingido. O serviço está indisponível.")


# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# def processar_lista(lista, valor_parada):
#     """
#     Processa itens de uma lista até encontrar um valor específico que indica a parada.

#     :param lista: Lista de elementos a serem processados.
#     :param valor_parada: O valor que indica a interrupção do processamento.
#     """
#     for item in lista:
#         if item == valor_parada:
#             print(f"🛑 Valor de parada '{valor_parada}' encontrado. Interrompendo processamento.")
#             break
#         print(f"✅ Processando: {item}")

# # Exemplo de uso
# dados = [10, 20, 30, 40, 50, 99, 60, 70]  # Lista de dados
# valor_parada = 99  # Número que indica a parada

# processar_lista(dados, valor_parada)
