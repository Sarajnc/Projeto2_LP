# Mini Projeto LGPD

## Sobre o projeto

Este projeto foi desenvolvido como atividade acadêmica da FATEC e tem como objetivo trabalhar com dados de usuários utilizando Python, PostgreSQL e SQLAlchemy.
O projeto utiliza funções para anonimizar informações pessoais e exportar os dados para arquivos CSV. Também foi utilizado um decorator para medir o tempo de execução das exportações.

## Tecnologias utilizadas

- Python
- PostgreSQL
- SQLAlchemy
- CSV
- Logging

## Atividades desenvolvidas

### Anonimização de dados

Foi criada a função `LGPD()` para anonimizar os dados pessoais dos usuários
Os campos tratados são:

- **Nome:** mantém a primeira letra do primeiro nome e substitui as demais por asteriscos.
- **CPF:** mantém parte dos números e mascara o restante.
- **E-mail:** mantém a primeira letra do usuário e o domínio.
- **Telefone:** mantém apenas os quatro últimos dígitos.

Os demais campos, como identificador e datas, são mantidos.

### Exportação por ano de nascimento

Os usuários são separados de acordo com o ano de nascimento. Para cada ano encontrado, é criado um arquivo CSV com os dados anonimizados.
Exemplos de arquivos gerados:

- `1990.csv`
- `2000.csv`
- `2006.csv`

Os arquivos dependem dos anos de nascimento existentes no banco de dados.

### Exportação de todos os usuários

É gerado o arquivo `todos.csv`, contendo somente os campos `nome` e `cpf`, conforme solicitado no enunciado da atividade.

**Atenção:** esse arquivo contém dados pessoais sem anonimização e não deve ser publicado em repositórios públicos.

### Medição de tempo

Foi utilizado um decorator chamado `decorator_tempo()` para medir o tempo de execução das funções responsáveis pelas exportações.
O tempo é exibido no terminal e registrado no arquivo `tempo.log`.

## Como executar o projeto

### 1. Instalar as dependências

No terminal, execute:

python -m pip install sqlalchemy psycopg2-binary

### 2. Configurar a conexão

Configure a conexão com o PostgreSQL utilizando as credenciais fornecidas para a atividade.

Por segurança, não compartilhe senhas nem as coloque diretamente em um repositório público.

### 3. Executar os arquivos

Execute os arquivos Python correspondentes às atividades pelo terminal ou pelo VS Code.
Exemplo:

python atividade01.py

O nome do arquivo pode variar conforme a organização do projeto.

## Arquivos gerados

Durante a execução, o programa pode gerar:

- Arquivos CSV separados por ano de nascimento, com dados anonimizados.
- `todos.csv`, com nome e CPF.
- `tempo.log`, com os registros de tempo das exportações.

## Observações

Este projeto foi desenvolvido para fins de aprendizagem, com foco em manipulação de dados, consultas SQL, anonimização e exportação de arquivos utilizando Python.
Os arquivos exportados podem conter dados pessoais e devem ser tratados com cuidado, evitando compartilhamento indevido.
