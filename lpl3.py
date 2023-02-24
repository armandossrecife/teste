# Cadastro de Disciplinas
disciplinas = []
# Cadastro de Professores
professores = []
# Cadastro de Alunos
alunos = []
# Notas
disciplina_notas = {}


# função para cadastrar disciplina
def cadastrar_disciplina(disciplinas):
    codigo = int(input("Código da disciplina: "))
    # verifica se o código já existe
    for disciplina in disciplinas:
        if codigo == disciplina[0][0]:
            print("Código já cadastrado. Tente novamente.")
            return
    nome = input("Nome da disciplina: ")
    semestre = input("Semestre da disciplina (no formato AAAA.P): ")
    professores = []
    while True:
        opcao = input("Deseja cadastrar um professor para a disciplina? (S/N): ")
        if opcao.upper() == "S":
            codigo_professor = int(input("Código do professor: "))
            nome_professor = input("Nome do professor: ")
            professores.append((codigo_professor, nome_professor))
        elif opcao.upper() == "N":
            break
        else:
            print("Opção inválida. Tente novamente.")
    carga_horaria = int(input("Carga horária da disciplina: "))
    dias_semana = []
    while True:
        dia = input("Digite o dia da semana em que a disciplina ocorre (1 a 6, ou 0 para sair): ")
        if dia == "0":
            break
        horario = int(input("Digite o horário da disciplina (1 a 7): "))
        dias_semana.append((int(dia), horario))
    disciplina = ((codigo, nome, semestre, professores, carga_horaria), dias_semana)
    disciplinas.append(disciplina)
    print("Disciplina cadastrada com sucesso.")

# função para cadastrar professor
def cadastrar_professor(professores):
    codigo = int(input("Código do professor: "))
    # verifica se o código já existe
    for professor in professores:
        if codigo == professor[0]:
            print("Código já cadastrado. Tente novamente.")
            return
    nome = input("Nome do professor: ")
    professor = (codigo, nome)
    professores.append(professor)
    print("Professor cadastrado com sucesso.")

# função para cadastrar aluno
def cadastrar_aluno(alunos):
    matricula = input("Matrícula do aluno: ")
    nome = input("Nome do aluno: ")
    curso = input("Curso do aluno: ")
    aluno = (matricula, nome, curso)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso.")

def cadastrar_nota(disciplinas, alunos, disciplina_notas):
    codigo = int(input('Digite o código da disciplina: '))
    disciplina = None
    for d in disciplinas:
        if d[0][0] == codigo:
            disciplina = d
            break
    if disciplina is None:
        print('Disciplina não encontrada')
        return
    
    matricula = input('Digite a matrícula do aluno: ')
    aluno = None
    for a in alunos:
        if a[0] == matricula:
            aluno = a
            break
    if aluno is None:
        print('Aluno não encontrado')
        return
    
    nota = float(input('Digite a nota do aluno: '))
    if 0 <= nota <= 10:
        disciplina_notas = disciplina[1].setdefault(matricula, {})
        disciplina_notas['nota'] = nota
        print('Nota cadastrada com sucesso')
    else:
        print('Nota inválida')

def listar_disciplinas(disciplinas):
    if not disciplinas:
        print("Não há disciplinas cadastradas.")
        return
    for disciplina in disciplinas:
        codigo, nome, semestre, professores, carga_horaria = disciplina[0]
        dias_e_horarios = disciplina[1]
        print("Código:", codigo)
        print("Nome:", nome)
        print("Semestre:", semestre)
        print("Professores:", professores)
        print("Carga horária:", carga_horaria)
        print("Dias e horários:")
        for dia, horario in dias_e_horarios:
            print(f"  Dia {dia}: horário {horario}")

def listar_professores(professores):
    if not professores:
        print("Não há professores cadastrados.")
        return
    for codigo, nome in professores.items():
        print("Código:", codigo)
        print("Nome:", nome)

def listar_alunos(alunos):
    if not alunos:
        print("Não há alunos cadastrados.")
        return
    for matricula, dados_aluno in alunos.items():
        print("Matrícula:", matricula)
        print("Nome:", dados_aluno[0])
        print("Curso:", dados_aluno[1])

def listar_notas(notas):
    if not notas:
        print("Não há notas cadastradas.")
        return
    for codigo_disciplina, notas_disciplina in notas.items():
        print(f"Notas da disciplina {codigo_disciplina}:")
        for matricula, nota in notas_disciplina.items():
            print(f"  Aluno de matrícula {matricula}: {nota}")

def salvar_dados(disciplinas, professores, alunos, disciplina_notas):
    with open("dados.txt", "w") as arquivo:
        # salvando as disciplinas
        arquivo.write("Disciplinas:\n")
        for disciplina in disciplinas:
            arquivo.write(f"{disciplina}\n")
        
        # salvando os professores
        arquivo.write("\nProfessores:\n")
        for professor in professores:
            arquivo.write(f"{professor}\n")
        
        # salvando os alunos
        arquivo.write("\nAlunos:\n")
        for aluno in alunos:
            arquivo.write(f"{aluno}\n")
        
        # salvando as notas
        arquivo.write("\nNotas:\n")
        for nota in disciplina_notas:
            arquivo.write(f"{nota}\n")

def ler_arquivo():
    # inicializa as listas
    t_disciplinas = []
    t_professores = []
    t_alunos = []
    t_notas = []

    try:
        # abre o arquivo para leitura
        with open("dados.txt", "r") as arquivo:
            # percorre as linhas do arquivo
            for linha in arquivo:
                # separa os valores da linha e remove os espaços em branco
                valores = linha.strip().split(",")
                tipo_registro = valores[0]

                if tipo_registro == "DISCIPLINA":
                    # cria a tupla que representa a disciplina
                    codigo = int(valores[1])
                    nome = valores[2]
                    semestre = valores[3]
                    professores = valores[4].split(";") if valores[4] != "" else []
                    carga_horaria = int(valores[5])
                    dias_horarios = eval(valores[6])

                    disciplina = ((codigo, nome, semestre, professores, carga_horaria), dias_horarios)

                    # adiciona a disciplina na lista de disciplinas
                    t_disciplinas.append(disciplina)

                elif tipo_registro == "PROFESSOR":
                    # cria a tupla que representa o professor
                    codigo = int(valores[1])
                    nome = valores[2]

                    professor = (codigo, nome)

                    # adiciona o professor na lista de professores
                    t_professores.append(professor)

                elif tipo_registro == "ALUNO":
                    # cria a tupla que representa o aluno
                    matricula = valores[1]
                    nome = valores[2]
                    curso = valores[3]

                    aluno = (matricula, nome, curso)

                    # adiciona o aluno na lista de alunos
                    t_alunos.append(aluno)

                elif tipo_registro == "NOTA":
                    # cria a tupla que representa a nota
                    codigo_disciplina = int(valores[1])
                    matricula_aluno = valores[2]
                    nota = float(valores[3])

                    nota = (codigo_disciplina, matricula_aluno, nota)

                    # adiciona a nota na lista de notas
                    t_notas.append(nota)

    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")

    # retorna as listas atualizadas
    return t_disciplinas, t_professores, t_alunos, t_notas

def menu_principal(disciplinas, professores, alunos, disciplina_notas):
  while True:
    print("--- Mini controle acadêmico ---")
    print("1 - Cadastrar disciplina")
    print("2 - Cadastrar professor")
    print("3 - Cadastrar aluno")
    print("4 - Cadastrar nota")
    print("5 - Listar disciplinas")
    print("6 - Listar professores")
    print("7 - Listar alunos")
    print("8 - Listar notas")
    print("9 - Salvar dados em arquivo")
    print("10 - Recuperar dados do arquivo")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_disciplina(disciplinas)
    elif opcao == "2":
        cadastrar_professor(professores)
    elif opcao == "3":
        cadastrar_aluno(alunos)
    elif opcao == "4":
        cadastrar_nota(disciplinas, alunos, disciplina_notas)
    elif opcao == "5":
        listar_disciplinas(disciplinas)
    elif opcao == "6":
        listar_professores(professores)
    elif opcao == "7":
        listar_alunos(alunos)
    elif opcao == "8":
        listar_notas(disciplina_notas)
    elif opcao == "9":
        salvar_dados(disciplinas, professores, alunos, disciplina_notas)
    elif opcao == "10":
        disciplinas, professores, alunos, notas = ler_arquivo()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
