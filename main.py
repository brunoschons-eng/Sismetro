alunos = [
    {'nome' : 'Yasmin', 'notas' : [8, 7], 'idade' : 16, 'faltas': 367},
    {'nome' : 'Bruno', 'notas' : [8, 7], 'idade' : 16, 'faltas': 32},
    {'nome' : 'Arthur', 'notas' : [7, 9], 'idade' : 16, 'faltas': 40},
    {'nome' : 'Guilherme', 'notas' : [9, 10], 'idade' : 16, 'faltas': 2},
    {'nome' : 'Jessica', 'notas' : [8, 8], 'idade' : 16, 'faltas': 120},
    {'nome' : 'Menina', 'notas' : [8, 6], 'idade' : 16, 'faltas': 290},
    {'nome' : 'Ezequiel', 'notas' : [6, 7], 'idade' : 16, 'faltas': 54},
    {'nome' : 'Rafael', 'notas' : [4, 10], 'idade' : 16, 'faltas': 444},
    {'nome' : 'Eduardo', 'notas' : [2, 7], 'idade' : 16, 'faltas': 54},
    
    ]

def calcular_media(soma, qtde):
    return soma / qtde

def status_presenca(num_faltas):
    if num_faltas < 300:
        return('Dentro do limite')
    else:
        return('Fora do limite de faltas')

def status_aprovacao(nota, num_faltas):
    if nota >= 7 and num_faltas < 300:
        return('Aprovado')
    else:
        return('Reprovado')

aprovados = []
reprovados = []

for aluno in alunos:
    qtde_notas = len(aluno['notas'])
    soma = sum(aluno['notas'])

    nota = calcular_media(soma, qtde_notas)
    status = status_aprovacao(nota, aluno['faltas'])
    dados_aluno = aluno['nome']

    nota = calcular_media(soma, qtde_notas)
    print(f"Aluno: {aluno['nome']}, Nota: {nota}, Status: {status_aprovacao(nota, aluno['faltas'])}, Faltas: {status_presenca(aluno['faltas'])}")

    if status == 'Aprovado':
        aprovados.append(dados_aluno)
    else:
        reprovados.append(dados_aluno)


print("Aprovados")
for aluno in aprovados:
    print(f"  {aluno}")

print("Reprovadod")
for aluno in reprovados:
    print(f"  {aluno}")
