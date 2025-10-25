pacientes = {}
medicos = {}

def CadastrarMedico():
  nomeMedico = input("Nome do medico: ")
  especialidade = input("Especialidade: ")
  crm = input("CRM: ")

  medicos[crm] = {"nomeMedico": nomeMedico, "especialidade:" : especialidade}

def CadastrarPaciente():
  nome = input("Nome: ")
  cpf = input("CPF: ")
  dataNasc = input("Data de nascimento: ")
  acompanhante = input("Nome do acompanhante: ")
  quarto = int(input("Número do quarto: "))
  crmMedico = input("CRM do medico: ")
  print(f"Paciente: {nome} cadastrado!")

  pacientes[nome] = {"cpf": cpf, "acompanhante": acompanhante, "quarto": quarto, "crmMedico": crmMedico}


def ListarPaciente(nome):
  return pacientes.get(nome, "Paciente não encontrado")

#def ListarMedico(crm):
  #return medicos.get(crm, "CRM não encontrado")

def ListarMedico(crm):
  try:
    crmEncontrado = medicos[crm]
  except:
    print("CRM não encontrado")
  else:
    return crmEncontrado
  finally:
    print("Operação concluída")


while True:
  print("1. Cadastrar Médico")
  print("2. Cadastrar paciente")
  print("3. Buscar paciente")
  print("4. Buscar médico")
  print("0. Sair")
  print("teste do git")

  op = int(input())

  if(op == 1):
    CadastrarMedico()
  elif(op == 2):
    CadastrarPaciente()
  elif(op == 3):
    nome = input("Nome do paciente: ")
    resultado = ListarPaciente(nome)
    print(resultado)
  elif (op == 4):
    crm = input("CRM do médico: ")
    resultado = ListarMedico(crm)
    print(resultado)

  elif(op == 0):
    break
  else: print(pacientes)

