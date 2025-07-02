from datetime import time

def sort_lista(atividades):
    return sorted(atividades, key=lambda k: k['horario_termino'])

def obter_maior_atividades_compativeis(atividades, n):
    # Ordena as atividades pelo horário de término
    atividades_ordenadas = sort_lista(atividades);

    # Lista para armazenar as atividades compatíveis
    atividades_compativeis = []
    # Variável para armazenar o horário de término da última atividade adicionada
    ultimo_horario_termino = time.min

    for i in range(n):
        atividade = atividades_ordenadas[i]
        if atividade['horario_inicio'] >= ultimo_horario_termino:
            atividades_compativeis.append(atividade)
            ultimo_horario_termino = atividade['horario_termino']

    return atividades_compativeis

def printar_array(atividades):
    for atividade in atividades:
        print(f"{atividade['nome']} - Início: {atividade['horario_inicio']}, Término: {atividade['horario_termino']}")

# Inserindo um conjunto de atividades padrão:
atividades = [
    {"nome": "Leitura", "horario_inicio": time(19, 30), "horario_termino": time(20, 30)},
    {"nome": "Almoço", "horario_inicio": time(13, 0), "horario_termino": time(14, 0)},
    {"nome": "Lanche", "horario_inicio": time(11, 0), "horario_termino": time(11, 15)},
    {"nome": "Aula de Matemática", "horario_inicio": time(8, 0), "horario_termino": time(9, 30)},
    {"nome": "Exercício Físico", "horario_inicio": time(18, 0), "horario_termino": time(19, 0)},
    {"nome": "Pausa para Café", "horario_inicio": time(16, 0), "horario_termino": time(16, 15)},
    {"nome": "Revisão de Conteúdo", "horario_inicio": time(16, 30), "horario_termino": time(17, 30)},
    {"nome": "Estudo de Programação", "horario_inicio": time(11, 30), "horario_termino": time(13, 0)},
    {"nome": "Reunião com equipe", "horario_inicio": time(10, 0), "horario_termino": time(11, 0)},
    {"nome": "Projeto de Pesquisa", "horario_inicio": time(14, 0), "horario_termino": time(16, 0)},
]

printar_array(obter_maior_atividades_compativeis(atividades, len(atividades)))



# Análise da complexidade:
# Temos o incremento da complexidade de O(n log n) devido à ordenação das atividades pelo horário de término.
# A complexidade do loop que percorre as atividades é O(n), onde n é o número de atividades.
# Portanto, a complexidade total é O(n log n) + O(n) = O(n log n).
# A complexidade espacial é O(n) para armazenar as atividades compatíveis.