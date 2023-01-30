import _mysql_connector
import mysql.connector

def createTables():

    criarTabelas = """
    drop table if exists lesaojogador;
    drop table if exists jogador;
    drop table if exists clube;
    drop table if exists estadio;
    drop table if exists tecnico;
    drop table if exists lesao;
    drop table if exists jogo;
    drop table if exists competicao;
    drop table if exists cartaojogador;
    drop table if exists cartaotecnico;
    drop table if exists titulo;
    drop table if exists arbitro;
    
    create table arbitro (
        idArbitro int unsigned auto_increment,
        nome varchar(80) not null,
        dataNasc date not null,
        qtdJogos int not null,
        dataEstreia date not null,
        primary key (idArbitro));
    
    create table estadio (
        idEstadio int unsigned auto_increment,
        nome varchar(80) not null,
        dataInaug date not null,
        valor float not null,
        capacidade int not null,
        primary key(idEstadio));
    
    create table lesao (
        idLesao int unsigned auto_increment,
        descricao varchar(150) not null,
        primary key (idLesao));
    
    create table competicao (
        idComp int unsigned auto_increment,
        descricao varchar(150) not null,
        primary key (idComp));
    
    create table tecnico (
        idTecnico int unsigned auto_increment,
        nome varchar(80) not null,
        dataNasc date not null,
        qtdJogos int not null,
        dataEstreia date not null,
        primary key (idTecnico));
    
    create table clube (
        idClube int unsigned auto_increment,
        nome varchar(80) not null,
        dataFund date not null,
        idEstadio int unsigned,
        idTecnico int unsigned not null,
        primary key (idClube),
        foreign key (idEstadio) references estadio (idEstadio),
        foreign key (idTecnico) references tecnico (idTecnico));
    
    create table jogador (
        idJogador int unsigned auto_increment,
        nome varchar(80) not null,
        dataNasc date not null,
        posicao varchar(20) not null,
        qtdJogos int not null,
        qtdGols int not null,
        qtdAssist int not null,
        idClube int unsigned,
        primary key (idJogador),
        foreign key (idClube) references clube (idClube));
    
    create table LesaoJogador (
        idLesao int unsigned not null,
        idJogador int unsigned not null,
        dataLesao date not null,
        gravidade varchar(20) not null,
        regiao varchar(20) not null,
        dataRecu date,
        primary key (idLesao, idJogador),
        foreign key (idLesao) references lesao (idLesao),
        foreign key (idJogador) references jogador (idJogador));
    
    create table jogo (
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
        foreign key (idComp) references competicao (idComp));
    
    create table CartaoJogador (
        idCartao int unsigned auto_increment,
        idJogador int unsigned not null,
        idJogo int unsigned not null,
        idArbitro int unsigned not null,
        cor varchar(20) not null,
        primary key (idCartao),
        foreign key (idJogador) references jogador (idJogador),
        foreign key (idJogo) references jogo (idJogo),
        foreign key (idArbitro) references arbitro (idArbitro));
    
    create table CartaoTecnico (
        idCartao int unsigned auto_increment,
        idTecnico int unsigned not null,
        idJogo int unsigned not null,
        idArbitro int unsigned not null,
        cor varchar(20) not null,
        primary key (idCartao),
        foreign key (idTecnico) references Tecnico (idTecnico),
        foreign key (idJogo) references jogo (idJogo),
        foreign key (idArbitro) references arbitro (idArbitro));
    
    create table titulo (
        idTitulo int unsigned auto_increment,
        idComp int unsigned not null,
        idClube int unsigned not null,
        ano int not null,
        idArtilheiro int unsigned not null,
        primary key (idTitulo),
        foreign key (idComp) references competicao (idComp),
        foreign key (idClube) references clube (idClube),
        foreign key (idArtilheiro) references jogador (idJogador));
    """

    try:
        cursor.execute(criarTabelas)
        connection.commit()
    except _mysql_connector.MySQLInterfaceError:
        pass

    # end code


def mainMenu():
    while True:
        print("----------------Menu Principal-----------------")
        print("1.- Create")
        print("2.- Read")
        print("3.- Update")
        print("4.- Delete")
        print("5.- Exit")
        print("-----------------------------------------------")

        print("Select one option: ")
        option = int(input())
        if not (1 <= option <= 5):
            print("Incorrect option, insert again ...")
        elif option == 5:
            print("Thank you for using me!")
            break
        else:
            if option == 1:
                createHandler()
            elif option == 2:
                readHandler()
            elif option == 3:
                updateHandler()
            else:
                deleteHandler()


def createHandler():
    pass


def readHandler():
    pass


def updateHandler():
    pass


def deleteHandler():
    pass


if __name__ == '__main__':

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='projetobdcrud',
    )
    cursor = connection.cursor()

    createTables()
    mainMenu()

    cursor.close()
    connection.close()
