create table if not exists Executors (
	Id serial primary key,
	Name_of_executors varchar(100) not null
	);
	
create table if not exists Genres (	
	Id serial primary key,
	Name_of_genre varchar(40) not null
	);
	
create table if not exists Executors_Genres (
	Id serial primary key,
	id_of_executor integer references Executors(id),
	id_of_genre integer references Genres(id)
	);
	
create table if not exists Albums (
	Id serial primary key,
	Name_of_album varchar(60) not null,
	Year_of_issue date not null,
	Description text
	);
	
create table if not exists Executors_Albums (
	Id serial primary key,
	Id_of_executor integer references Executors(id),
	Id_of_album integer references Albums(id)
	);
	
create table if not exists Tracks (
	Id serial primary key,
	Name_of_track varchar(60) not null,
	Duration numeric(4,2),
	Id_of_album integer references Albums(Id)
	);

create table if not exists Collections (
	Id serial primary key,
	Name_of_collection varchar(100) not null,
	Collect_year_of_issue date not null
	);
	
create table if not exists Tracks_Collections (
	Id serial primary key,
	Id_of_track integer references Tracks(id),
	Id_of_collection integer references Collections(id)
	);