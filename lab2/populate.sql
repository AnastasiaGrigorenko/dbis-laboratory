INSERT INTO public.patient(
	patient_id, age, height, weight, temperature)
	VALUES ('Nastya', 20, 160, 48, 38.5);
INSERT INTO public.patient(
	patient_id, age, height, weight, temperature)
	VALUES ('Max', 21, 181, 80, 36.6);
INSERT INTO public.patient(
	patient_id, age, height, weight, temperature)
	VALUES ('Igor', 21, 175, 70, 37);
	
INSERT INTO public.symptom(
	symptom_id, description)
	VALUES ('007', 'throat pain');
INSERT INTO public.symptom(
	symptom_id, description)
	VALUES ('008', 'head pain');
INSERT INTO public.symptom(
	symptom_id, description)
	VALUES ('009', 'cough');
	
INSERT INTO public.patient_symptom(
	patient_id, symptom_id)
	VALUES ('Nastya', '007');
INSERT INTO public.patient_symptom(
	patient_id, symptom_id)
	VALUES ('Nastya', '009');
INSERT INTO public.patient_symptom(
	patient_id, symptom_id)
	VALUES ('Max', '008');

INSERT INTO public.disease(
	disease_id, disease_name, severity)
	VALUES ('01', 'URTI', 3);
INSERT INTO public.disease(
	disease_id, disease_name, severity)
	VALUES ('02', 'flu', 4);
INSERT INTO public.disease(
	disease_id, disease_name, severity)
	VALUES ('03', 'migraine', 4);
	
INSERT INTO public.symptom_disease(
	symptom_id, disease_id)
	VALUES ('007', '02');
INSERT INTO public.symptom_disease(
	symptom_id, disease_id)
	VALUES ('008', '03');
INSERT INTO public.symptom_disease(
	symptom_id, disease_id)
	VALUES ('009', '01');
	
INSERT INTO public.recommendation(
	disease_id, recommend_id, doctor)
	VALUES ('01', '001', 'otolaringologist');
INSERT INTO public.recommendation(
	disease_id, recommend_id, doctor)
	VALUES ('02', '002', 'therapist');
INSERT INTO public.recommendation(
	disease_id, recommend_id, doctor)
	VALUES ('03', '003', 'neurologist');

	
