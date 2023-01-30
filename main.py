import _mysql_connector
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='projetobdcrud',
)

cursor = connection.cursor()

# code here

criarTabelas = """create table arbitro (
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

cursor.close()
connection.close()
