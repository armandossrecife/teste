import json

class Disciplina:
    def __init__(self, codigo, nome, semestre, carga_horaria, dias_horarios, professores=None, alunos=None):
        self.codigo = codigo
        self.nome = nome
        self.semestre = semestre
        self.carga_horaria = carga_horaria
        self.dias_horarios = dias_horarios
        self.professores = professores if professores is not None else []
        self.alunos = alunos if alunos is not None else []

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Professor:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

    def __str__(self):
        return f"{self.matricula} - {self.nome}"

class Nota:
    def __init__(self, codigo_disciplina, matricula_aluno, valor):
        self.codigo_disciplina = codigo_disciplina
        self.matricula_aluno = matricula_aluno
        self.valor = valor
        
def adicionar_disciplina(disciplinas):
    codigo = input("Código da disciplina: ")
    nome = input("Nome da disciplina: ")
    semestre = input("Semestre da disciplina: ")
    carga_horaria = int(input("Carga horária da disciplina: "))
    dias_horarios = []
    for i in range(2):
        dia = int(input(f"Dia da semana {i+1}: "))
        horario = int(input(f"Horário {i+1}: "))
        dias_horarios.append((dia, horario))
    disciplina = Disciplina(codigo, nome, semestre, carga_horaria, dias_horarios)
    disciplinas.append(disciplina)
    salvar_disciplinas(disciplinas)
    print(f"Disciplina '{disciplina.nome}' cadastrada com sucesso!")

def adicionar_professor(professores):
    codigo = int(input("Código do professor: "))
    nome = input("Nome do professor: ")
    professor = Professor(codigo, nome)
    professores.append(professor)
    print(f"Professor '{professor.nome}' cadastrado com sucesso!")

def adicionar_aluno(alunos):
    """
    Adiciona um aluno na lista de alunos
    :param alunos: lista de alunos
    """
    matricula = input("Digite a matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    aluno = Aluno(matricula, nome, curso)
    alunos.append(aluno)
    print("Aluno adicionado com sucesso!")     

def salvar_disciplinas(disciplinas):
    with open("disciplinas.json", "w") as file:
        json.dump([vars(d) for d in disciplinas], file, indent=4)
  
def salvar_professores(professores):
    with open('professores.json', 'w') as arquivo:
        lista_professores = []
        for professor in professores:
            dados_professor = {
                'codigo': professor.codigo,
                'nome': professor.nome
            }
            lista_professores.append(dados_professor)
        json.dump(lista_professores, arquivo, indent=4)

def salvar_alunos(alunos, arquivo="alunos.json"):
    with open(arquivo, "w") as f:
        json.dump([a.__dict__ for a in alunos], f, indent=4)
  
def carregar_disciplinas():
    try:
        with open("disciplinas.json", "r") as file:
            disciplinas_json = json.load(file)
        disciplinas = []
        for d_json in disciplinas_json:
            professores = [Professor(p["codigo"], p["nome"]) for p in d_json["professores"]]
            alunos = [Aluno(a["matricula"], a["nome"], a["curso"]) for a in d_json["alunos"]]
            disciplina = Disciplina(d_json["codigo"], d_json["nome"], d_json["semestre"], d_json["carga_horaria"], d_json["dias_horarios"], professores, alunos)
            disciplinas.append(disciplina)
        return disciplinas
    except FileNotFoundError:
        return []
