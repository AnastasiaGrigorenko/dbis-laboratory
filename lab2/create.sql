CREATE TABLE patient (
	patient_id varchar PRIMARY KEY,
	age int,
	height float8,
	weight float8,
	temperature float8
);

CREATE TABLE symptom(
	symptom_id varchar PRIMARY KEY,
	description text
);

CREATE TABLE patient_symptom(
	patient_id varchar REFERENCES patient(patient_id),
	symptom_id varchar REFERENCES symptom(symptom_id)
);

CREATE TABLE disease(
	disease_id varchar PRIMARY KEY,
	disease_name text,
	severity int
);

CREATE TABLE symptom_disease(
	symptom_id varchar REFERENCES symptom(symptom_id),
	disease_id varchar REFERENCES disease(disease_id)
);

CREATE TABLE recommendation(
	disease_id varchar REFERENCES disease(disease_id),
	recommend_id varchar PRIMARY KEY,
	doctor text
);