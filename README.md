## Minha API - Car Evaluation - Savio Reis


## Descrição

Esta API permite a predição do melhor carro para compra com base em diferentes parâmetros fornecidos pelo usuário do sistema, ela utiliza um modelo de Machine Learning pré-treinado para avaliar carros e retornar a melhor opção disponível.

## Descrição do Dataset
O dataset utilizado nesta API contém informações sobre diferentes características de carros e tem como objetivo auxiliar na predição de qual carro é a melhor opção para compra com base em suas especificações.

## Atributos
O dataset contém os seguintes atributos:

buying: Nível de preço de compra do carro

Valores possíveis:
1: low (baixo)
2: med (médio)
3: high (alto)
4: vhigh (muito alto)
maint: Nível de custo de manutenção do carro

Valores possíveis:
1: low (baixo)
2: med (médio)
3: high (alto)
4: vhigh (muito alto)
doors: Número de portas do carro

Valores possíveis:
2: 2 portas
3: 3 portas
4: 4 portas
5: Mais de 4 portas
persons: Capacidade de passageiros do carro

Valores possíveis:
2: 2 pessoas
4: 4 pessoas
5: Mais de 4 pessoas
lug_boot: Capacidade do porta-malas

Valores possíveis:
1: small (pequeno)
2: med (médio)
3: big (grande)
safety: Nível de segurança do carro

Valores possíveis:
1: low (baixo)
2: med (médio)
3: high (alto)
result: Classificação final do carro

Valores possíveis:
1: unacc (inaceitável)
2: acc (aceitável)
3: good (bom)
4: vgood (muito bom)

## Objetivo do Projeto

O objetivo deste projeto é fornecer um conjunto de características relevantes para a avaliação de carros, permitindo a classificação dos veículos com base em uma série de fatores que influenciam a decisão de compra. Esses fatores incluem o custo de compra, custo de manutenção, número de portas, capacidade de passageiros, espaço no porta-malas e nível de segurança.

Especificamente, o dataset foi projetado para:

Este tipo de dataset é utilizado em sistemas de recomendação de produtos e aprendizado supervisionado, onde a meta é prever a melhor opção de carro com base em múltiplas variáveis categóricas. O objetivo final é otimizar a escolha do consumidor, facilitando a decisão de compra ao sugerir carros que oferecem a melhor relação custo-benefício dentro das condições especificadas.
