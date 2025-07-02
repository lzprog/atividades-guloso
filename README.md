# Algoritmo Guloso — Seleção de Atividades Compatíveis

Este projeto implementa uma **solução gulosa** para o clássico problema da **seleção de atividades compatíveis**. O objetivo é selecionar o maior número de atividades que **não se sobrepõem no tempo**, com base nos seus horários de início e término.

---

# Descrição do Problema

Dado um conjunto de `n` atividades, onde cada uma possui um horário de início e término, selecione o **máximo de atividades mutuamente compatíveis** — ou seja, que não tenham interseção de tempo.

# Estratégia Gulosa

A abordagem utilizada ordena as atividades pelo horário de **término crescente**. A cada passo, seleciona-se a próxima atividade cujo horário de início **não conflita com a atividade previamente selecionada**.

---

# Estrutura do Projeto

- `atividades.py`: arquivo principal que contém a implementação do algoritmo guloso.
- `atividades_100.py`: arquivo com 100 atividades para testes em larga escala.
- `atividades_1000.py`: arquivo com 1000 atividades para testes de desempenho.
