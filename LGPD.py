import csv
import time
import logging
import functools
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2")

logging.basicConfig(
    filename="tempo.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)
COLUNAS = ["id", "nome", "cpf", "email", "telefone",
           "data_nascimento", "created_on", "updated_on"]

def decorator_tempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        logging.info(f"{func.__name__} executou em {fim - inicio:.2f} segundos")
        print(f"{func.__name__} executou em {fim - inicio:.2f} segundos")
        return resultado
    return wrapper

def anonimizar_nome(nome):
    partes = nome.split()                                
    pos = 1 if partes[0].endswith(".") and len(partes) > 1 else 0
    palavra = partes[pos]
    partes[pos] = palavra[0] + "*" * (len(palavra) - 1)  
    return " ".join(partes)
    
def anonimizar_cpf(cpf):
    return cpf[:4] + "***.***-**"                        

def anonimizar_email(email):
    usuario, dominio = email.split("@")
    return usuario[0] + "*" * (len(usuario) - 1) + "@" + dominio

def anonimizar_telefone(telefone):
    digitos = "".join(c for c in telefone if c.isdigit())  
    return digitos[-4:]                                  

def LGPD(registro):
    id, nome, cpf, email, telefone, nascimento, criado, atualizado = registro
    return (
        id,
        anonimizar_nome(nome),
        anonimizar_cpf(cpf),
        anonimizar_email(email),
        anonimizar_telefone(telefone),
        nascimento,
        criado,
        atualizado,
    )

@decorator_tempo
def gerar_arquivos_por_ano():
    por_ano = {}                                

    with engine.connect() as conexao:
        resultado = conexao.execute(text("SELECT * FROM usuarios;"))
        for registro in resultado:
            ano = registro[5].year                       
            por_ano.setdefault(ano, []).append(LGPD(registro))

    for ano, registros in por_ano.items():
        with open(f"{ano}.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(COLUNAS)
            writer.writerows(registros)

@decorator_tempo
def gerar_arquivo_todos():
    with engine.connect() as conexao:
        resultado = conexao.execute(text("SELECT nome, cpf FROM usuarios;"))
        with open("todos.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["nome", "cpf"])
            writer.writerows(resultado)
            
if __name__ == "__main__":
    with engine.connect() as conexao:
        resultado = conexao.execute(text("SELECT * FROM usuarios LIMIT 10;"))
        for registro in resultado:
            print(LGPD(registro))
            
    gerar_arquivos_por_ano()    
    gerar_arquivo_todos()       
