CREATE KEYSPACE IF NOT EXISTS lab1 WITH replication = {
	'class': 'SimpleStrategy',
	'replication_factor': '1'
};
USE lab1;

CREATE TYPE IF NOT EXISTS info_type (
	height float,
	weight float,
	sex text
);

//–≈¿À≤«Œ¬¿Õ≤  Œ–»—“”¬¿÷‹ ≤ “¿ ¬ À¿ƒ≈Õ≤ “»œ» ƒ¿Õ»’
CREATE TABLE IF NOT EXISTS patient_symptom (
	patient_id varchar,
	info FROZEN<info_type> static,
	age int static,
	temperature set<float> static,
	pulse set<int> static,
	pressure set<FROZEN<map<int,int>>> static,
	symptom_id varchar,
	description text,
	PRIMARY KEY ((patient_id), symptom_id)
);

CREATE TABLE IF NOT EXISTS symptom_disease (
	symptom_id varchar,
	description text static,
	disease_id varchar,
	disease_name map<text,text>,
	severity int,
	PRIMARY KEY ((symptom_id), disease_id)
);

CREATE TABLE IF NOT EXISTS symptom_recommend (
	symptom_id varchar,
	description text static,
	disease_id varchar,
	disease_name map<text,text>,
	severity int,
	recommend_id varchar,
	doctor text,
	PRIMARY KEY ((symptom_id), disease_id, recommend_id)
);

//–≈¿À≤«Œ¬¿Õ»… À≤◊»À‹Õ» 
CREATE TABLE IF NOT EXISTS count_of_disease (
	patient_id varchar,
	disease_id varchar,
	disease_count counter,
	PRIMARY KEY ((patient_id), disease_id)
);








