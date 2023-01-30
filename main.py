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
        print("5.- Exit")
        print("----------------------------------------------------------")

        print("Digite sua opção: ")
        opcao = int(input())
        if 5 < opcao or opcao < 1:
            print("Digite um valor válido!")
        elif opcao == 5:
            print("Obrigado por me usar!")
            break
        elif opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        input("Pressione enter para voltar!")


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
