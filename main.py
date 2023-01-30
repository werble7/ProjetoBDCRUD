import mysql.connector


def createTables():

    arbitro = """create table if not exists arbitro (
	idArbitro int unsigned auto_increment,
	nome varchar(80) not null,
	dataNasc date not null,
	qtdJogos int not null,
	dataEstreia date not null,
	primary key (idArbitro)); """

    cursor.execute(arbitro)
    connection.commit()

    estadio = """create table if not exists estadio (
	idEstadio int unsigned auto_increment,
	nome varchar(80) not null,
	dataInaug date not null,
	valor float not null,
	capacidade int not null,
	primary key(idEstadio));"""

    cursor.execute(estadio)
    connection.commit()

    lesao = """create table if not exists lesao (
	idLesao int unsigned auto_increment,
	descricao varchar(150) not null,
	primary key (idLesao));"""

    cursor.execute(lesao)
    connection.commit()

    comp = """create table if not exists competicao (
	idComp int unsigned auto_increment,
	descricao varchar(150) not null,
	primary key (idComp));"""

    cursor.execute(comp)
    connection.commit()

    tecnico = """create table if not exists tecnico (
	idTecnico int unsigned auto_increment,
	nome varchar(80) not null,
	dataNasc date not null,
	qtdJogos int not null,
	dataEstreia date not null,
	primary key (idTecnico));"""

    cursor.execute(tecnico)
    connection.commit()

    clube = """create table if not exists clube (
	idClube int unsigned auto_increment,
	nome varchar(80) not null,
	dataFund date not null,
	idEstadio int unsigned,
	idTecnico int unsigned not null,
	primary key (idClube),
	foreign key (idEstadio) references estadio (idEstadio),
	foreign key (idTecnico) references tecnico (idTecnico));"""

    cursor.execute(clube)
    connection.commit()

    jogador = """create table if not exists jogador (
	idJogador int unsigned auto_increment,
	nome varchar(80) not null,
	dataNasc date not null,
	posicao varchar(20) not null,
	qtdJogos int not null,
	qtdGols int not null,
	qtdAssist int not null,
	idClube int unsigned,
	primary key (idJogador),
	foreign key (idClube) references clube (idClube));"""

    cursor.execute(jogador)
    connection.commit()

    lesaojog = """create table if not exists LesaoJogador (
	idLesao int unsigned not null,
	idJogador int unsigned not null,
	dataLesao date not null,
	gravidade varchar(20) not null,
	regiao varchar(20) not null,
	dataRecu date,
	primary key (idLesao, idJogador),
	foreign key (idLesao) references lesao (idLesao),
	foreign key (idJogador) references jogador (idJogador));"""

    cursor.execute(lesaojog)
    connection.commit()

    jogo = """create table if not exists jogo (
	idJogo int unsigned not null,
	idClube1 int unsigned not null,
	idClube2 int unsigned not null,
	idArbitro int unsigned not null,
	resultado varchar(10),
	idComp int unsigned not null,
	primary key (idJogo),
	foreign key (idClube1) references clube (idClube),
	foreign key (idClube2) references clube (idClube),
	foreign key (idArbitro) references arbitro (idArbitro),
	foreign key (idComp) references competicao (idComp));"""

    cursor.execute(jogo)
    connection.commit()

    cartaojog = """create table if not exists CartaoJogador (
	idCartao int unsigned auto_increment,
	idJogador int unsigned not null,
	idJogo int unsigned not null,
	idArbitro int unsigned not null,
	cor varchar(20) not null,
	primary key (idCartao),
	foreign key (idJogador) references jogador (idJogador),
	foreign key (idJogo) references jogo (idJogo),
	foreign key (idArbitro) references arbitro (idArbitro));"""

    cursor.execute(cartaojog)
    connection.commit()

    cartaotec = """create table if not exists CartaoTecnico (
	idCartao int unsigned auto_increment,
	idTecnico int unsigned not null,
	idJogo int unsigned not null,
	idArbitro int unsigned not null,
	cor varchar(20) not null,
	primary key (idCartao),
	foreign key (idTecnico) references Tecnico (idTecnico),
	foreign key (idJogo) references jogo (idJogo),
	foreign key (idArbitro) references arbitro (idArbitro));"""

    cursor.execute(cartaotec)
    connection.commit()

    titulo = """create table if not exists titulo (
	idTitulo int unsigned auto_increment,
	idComp int unsigned not null,
	idClube int unsigned not null,
	ano int not null,
	idArtilheiro int unsigned not null,
	primary key (idTitulo),
	foreign key (idComp) references competicao (idComp),
	foreign key (idClube) references clube (idClube),
	foreign key (idArtilheiro) references jogador (idJogador));"""

    cursor.execute(titulo)
    connection.commit()


def menuPrincipal():

    while True:
        print('-------------------------Comandos-------------------------')
        print("1.- Create")
        print("2.- Read")
        print("3.- Update")
        print("4.- Delete")
        print("5.- Sair")
        print("----------------------------------------------------------")

        print("Digite sua opção: ")
        opcao = int(input())
        if 5 < opcao or opcao < 1:
            print("Digite um valor válido!")
        elif opcao == 5:
            print("Obrigado por me usar!")
            break
        elif opcao == 1:
            telaCreate()
        elif opcao == 2:
            telaRead()
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        input("Pressione enter para voltar!")


def telaCreate():
    while True:
        print('-------------------------Tabelas-------------------------')
        print('1.- Arbitro')
        print('2.- Estadio')
        print('3.- Lesao')
        print('4.- Competicao')
        print('5.- Tecnico')
        print('6.- Clube')
        print('7.- Jogador')
        print('8.- LesaoJogador')
        print('9.- Jogo')
        print('10.- CartaoJogador')
        print('11.- CartaoTecnico')
        print('12.- Titulo')
        print('13.- Sair')
        print('----------------------------------------------------------')

        print("Selecione uma tabela: ")
        opcao = int(input())
        if opcao == 13:
            break
        if opcao == 1:
            print('Digite o nome do arbitro: ')
            nome = input()
            print('Digite a data de nascimento do arbitro (YYYY-MM-DD)')
            datanasc = input()
            print('Digite o numero de jogos apitados pelo arbitro')
            qtdJogos = int(input())
            print('Digite a data de estreia do arbitro (YYYY-MM-DD')
            dataEstreia = input()
            comando = f"insert into arbitro(nome, dataNasc, qtdJogos, dataEstreia) values('{nome}', '{datanasc}', {str(qtdJogos)}, '{dataEstreia}')"
            cursor.execute(comando)
            connection.commit()
        if opcao == 2:
            print('Digite o nome do estádio: ')
            nome = input()
            print('Digite a data de inaugaração do estádio (YYYY-MM-DD): ')
            dataInaug = input()
            print('Digite o valor do estádio: ')
            valor = float(input())
            print('Digite a capacidade do estádio: ')
            capac = int(input())
            comando = f"insert into estadio(nome, dataInaug, valor, capacidade) values('{nome}', '{dataInaug}', {str(valor)}, '{str(capac)}')"
            cursor.execute(comando)
            connection.commit()
        if opcao == 3:
            print("Digite a descrição da lesão")
            desc = input()
            comando = f"insert into lesao(descricao) values('{desc}')"
            cursor.execute(comando)
            connection.commit()
        input("Digite enter para voltar")


def telaRead():
    while True:
        print('-------------------------Tabelas-------------------------')
        print('1.- Arbitro')
        print('2.- Estadio')
        print('3.- Lesao')
        print('4.- Competicao')
        print('5.- Tecnico')
        print('6.- Clube')
        print('7.- Jogador')
        print('8.- LesaoJogador')
        print('9.- Jogo')
        print('10.- CartaoJogador')
        print('11.- CartaoTecnico')
        print('12.- Titulo')
        print('13.- Sair')
        print('----------------------------------------------------------')

        print("Selecione uma tabela: ")
        opcao = int(input())

        if opcao == 1:
            comando = "select * from arbitro"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 2:
            comando = "select * from estadio"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 3:
            comando = "select * from lesao"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 4:
            comando = "select * from competicao"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 5:
            comando = "select * from tecnico"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 6:
            comando = "select * from clube"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 7:
            comando = "select * from jogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 8:
            comando = "select * from lesaoJogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 9:
            comando = "select * from jogo"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 10:
            comando = "select * from cartaoJogador"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 11:
            comando = "select * from cartaoTecnico"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 12:
            comando = "select * from titulo"
            cursor.execute(comando)
            result = cursor.fetchall()
            print(result)
        if opcao == 13:
            break
        input("Digite enter para voltar")


if __name__ == '__main__':

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='projetobdcrud',
    )
    cursor = connection.cursor()

    createTables()

    menuPrincipal()

    cursor.close()
    connection.close()
