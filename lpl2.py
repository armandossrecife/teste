# Cadastro de Disciplinas
disciplinas = []
# Cadastro de Professores
professores = []
# Cadastro de Alunos
alunos = []
# Cadastro de Notas
notas = {}

def cadastrar_disciplina():
    codigo = int(input("Código da disciplina: "))
    nome = input("Nome da disciplina: ")
    semestre = input("Semestre (no formato aaaa.p): ")
    professores = input("Professores (separados por vírgula): ").split(",")
    carga_horaria = int(input("Carga horária: "))
    dias_horarios = []
    while True:
        dia = input("Dia da semana (1 a 6) ou ENTER para encerrar: ")
        if not dia:
            break
        horario = int(input("Horário (1 a 7): "))
        dias_horarios.append(([int(dia)], horario))
    disciplina = ((codigo, nome, semestre, professores, carga_horaria), dias_horarios)
    if codigo in [d[0][0] for d in disciplinas]:
        print("Já existe uma disciplina com este código!")
    else:
        disciplinas.append(disciplina)
        print("Disciplina cadastrada com sucesso!")

def cadastrar_professor():
    codigo = int(input("Código do professor: "))
    nome = input("Nome do professor: ")
    professor = (codigo, nome)
    if codigo in [p[0] for p in professores]:
        print("Já existe um professor com este código!")
    else:
        professores.append(professor)
        print("Professor cadastrado com sucesso!")

def cadastrar_aluno():
    matricula = input("Matrícula do aluno: ")
    nome = input("Nome do aluno: ")
    curso = input("Curso do aluno: ")
    aluno = (matricula, nome, curso)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def cadastrar_nota():
    disciplina_codigo = int(input("Código da disciplina: "))
    matricula = input("Matrícula do aluno: ")
    nota = float(input("Nota do aluno: "))
    if disciplina_codigo not in [d[0][0] for d in disciplinas]:
        print("Disciplina não encontrada!")
    elif matricula not in [a[0] for a in alunos]:
        print("Aluno não encontrado!")
    else:
        chave = (disciplina_codigo, matricula)
        notas[chave] = nota
        print("Nota cadastrada com sucesso!")

def listar_disciplinas(disciplinas):
    for disciplina in disciplinas:
        codigo, nome, semestre, professores, carga_horaria = disciplina[0]
        dias_horarios = disciplina[1]
        print(f"Código: {codigo}")
        print(f"Nome: {nome}")
        print(f"Semestre: {semestre}")
        print(f"Professores: {professores}")
        print(f"Carga horária: {carga_horaria}")
        print(f"Dias e horários: {dias_horarios}")

def listar_professores(professores):
    print("Professores cadastrados:")
    for professor in professores:
        print(f"Código: {professor[0]}")
        print(f"Nome: {professor[1]}")
        print("-----------------------")

def listar_alunos(alunos):
    print("Lista de Alunos")
    for aluno in alunos:
        print(f"Matrícula: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}")

def listar_notas(notas):
    print("---- Notas Cadastradas ----")
    for chave, valores in notas.items():
        print(f"Disciplina: {chave[0]} | Matrícula: {chave[1]} | Notas: {valores}")
    
# Menu principal
while True:
    print("="*50)
    print("SISTEMA DE CADASTRO E NOTAS")
    print("="*50)
    print("1. Cadastrar disciplina")
    print("2. Cadastrar professor")
    print("3. Cadastrar aluno")
    print("4. Cadastrar nota")
    print("5. Listar disciplinas")
    print("6. Listar professores")
    print("7. Listar alunos")
    print("8. Listar notas")
    print("9. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_disciplina()
    elif opcao == "2":
        cadastrar_professor()
    elif opcao == "3":
        cadastrar_aluno()
    elif opcao == "4":
        cadastrar_nota()
    elif opcao == 5:
        listar_disciplinas(disciplinas)
    elif opcao == 6:
        listar_professores(professores)
    elif opcao == 7:
        listar_alunos(alunos)
    elif opcao == 8:
        listar_notas(notas)
    elif opcao == "9":
        break
    else:
        print("Opção inválida!")
