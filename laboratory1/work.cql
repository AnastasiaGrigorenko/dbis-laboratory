//----------ƒÀﬂ œ≈–ÿŒØ “¿¡À»÷≤----------//

//INSERT
INSERT INTO patient_symptom (patient_id, info, age, temperature, pulse, pressure, symptom_id, description)
VALUES ('Nastya',{height:160,weight:49,sex:'fem'}, 20, {38,37.5}, {100,95}, {{120:70},{120:80}},'007', 'throat pain');

INSERT INTO patient_symptom (patient_id, info, age, temperature, pulse, pressure, symptom_id, description)
VALUES ('Max', {height:180,weight:80,sex:'male'}, 21, {36.6}, {70}, {{120:80}},'008','body weak');

INSERT INTO patient_symptom (patient_id, symptom_id, description)
VALUES ('Max', '009','head pain');

SELECT * FROM patient_symptom;

//UPDATE
UPDATE patient_symptom 
SET pulse = pulse + {90} 
WHERE patient_id = 'Nastya';
SELECT * FROM patient_symptom;

UPDATE patient_symptom 
SET age = 22
WHERE patient_id = 'Max';
SELECT * FROM patient_symptom;

UPDATE patient_symptom 
SET info={height:158, weight: 50, sex:'fem'}
WHERE patient_id = 'Nastya';
SELECT * FROM patient_symptom;

//«¿œ»“
SELECT symptom_id, description
FROM patient_symptom
WHERE patient_id = 'Max';

//DELETE
DELETE pulse
FROM patient_symptom
WHERE patient_id = 'Nastya';
SELECT * FROM patient_symptom;

DELETE 
FROM patient_symptom
WHERE patient_id = 'Nastya';
SELECT * FROM patient_symptom;

DELETE age
FROM patient_symptom
WHERE patient_id = 'Max';
SELECT * FROM patient_symptom;

//----------ƒÀﬂ ƒ–”√ŒØ “¿¡À»÷≤----------//

//INSERT
INSERT INTO symptom_disease (symptom_id, description, disease_id, disease_name, severity)
VALUES ('007', 'throat pain', 'J00-06', {'URTI':'infection'}, 3);

INSERT INTO symptom_disease (symptom_id, description, disease_id, disease_name, severity)
VALUES ('007', 'throat pain', 'J11', {'flu': 'virus infection'}, 4);

INSERT INTO symptom_disease (symptom_id, description, disease_id, disease_name, severity)
VALUES ('008', 'head pain', 'G43.9', {'migraine':'disorder'}, 3);

SELECT * FROM symptom_disease;

//UPDATE
UPDATE symptom_disease 
SET disease_name['URTI'] = 'virus infection' 
WHERE symptom_id = '007' AND disease_id = 'J00-06';
SELECT * FROM symptom_disease;

UPDATE symptom_disease 
SET description = 'hard throat pain'
WHERE symptom_id = '007';
SELECT * FROM symptom_disease;

UPDATE symptom_disease 
SET severity=4
WHERE symptom_id = '008' AND disease_id = 'G43.9';
SELECT * FROM symptom_disease;

//«¿œ»“
SELECT disease_id, disease_name
FROM symptom_disease 
WHERE symptom_id = '007';

//DELETE
DELETE severity
FROM symptom_disease
WHERE symptom_id = '008' AND disease_id = 'G43.9';
SELECT * FROM symptom_disease;

DELETE 
FROM symptom_disease
WHERE symptom_id = '008' AND disease_id = 'G43.9';
SELECT * FROM symptom_disease;

DELETE description
FROM symptom_disease
WHERE symptom_id = '007';
SELECT * FROM symptom_disease;

//----------ƒÀﬂ “–≈“‹ŒØ “¿¡À»÷≤----------//

//INSERT
INSERT INTO symptom_recommend (symptom_id,description,disease_id,disease_name,severity,recommend_id,doctor)
VALUES ('007', 'throat pain', 'J00-06', {'URTI':'infection'}, 3, 'rec_01', 'therapist');

INSERT INTO symptom_recommend (symptom_id,description,disease_id,disease_name,severity,recommend_id,doctor)
VALUES ('007', 'throat pain', 'J11', {'flu': 'virus infection'}, 4, 'rec_02', 'otolaryngologist');

INSERT INTO symptom_recommend (symptom_id,description,disease_id,disease_name,severity,recommend_id,doctor)
VALUES ('008', 'head pain', 'G43.9', {'migraine':'disorder'}, 3, 'rec_03', 'neurologist');

SELECT * FROM symptom_recommend;

//UPDATE
UPDATE symptom_recommend 
SET disease_name['URTI'] = 'virus infection' 
WHERE symptom_id = '007' AND disease_id = 'J00-06' AND recommend_id = 'rec_01';
SELECT * FROM symptom_recommend;

UPDATE symptom_recommend 
SET description = 'hard throat pain'
WHERE symptom_id = '007';
SELECT * FROM symptom_recommend;

UPDATE symptom_recommend 
SET severity=4
WHERE symptom_id = '008' AND disease_id = 'G43.9' AND recommend_id = 'rec_03';

SELECT * FROM symptom_recommend;

//«¿œ»“
SELECT doctor
FROM symptom_recommend
WHERE symptom_id = '007';

//DELETE
DELETE severity
FROM symptom_recommend
WHERE symptom_id = '008' AND disease_id = 'G43.9' AND recommend_id = 'rec_03';
SELECT * FROM symptom_recommend;

DELETE 
FROM symptom_recommend
WHERE symptom_id = '008' AND disease_id = 'G43.9' AND recommend_id = 'rec_03';
SELECT * FROM symptom_recommend;

DELETE description
FROM symptom_recommend
WHERE symptom_id = '007';
SELECT * FROM symptom_recommend;

//----------ƒÀﬂ “–≈“‹ŒØ “¿¡À»÷≤----------//

//UPDATE
UPDATE count_of_disease
SET  disease_count = disease_count + 1
WHERE patient_id ='Nastya' AND disease_id = 'J11';

UPDATE count_of_disease
SET  disease_count = disease_count + 1
WHERE patient_id ='Nastya' AND disease_id = 'J00-06';

UPDATE count_of_disease
SET  disease_count = disease_count + 1
WHERE patient_id ='Max' AND disease_id = 'G43.9';

SELECT * FROM count_of_disease;

//«¿œ»“
SELECT disease_count 
FROM count_of_disease 
WHERE patient_id ='Nastya';

//DELETE
DELETE 
FROM count_of_disease
WHERE patient_id ='Max';

DELETE 
FROM count_of_disease
WHERE patient_id ='Nastya' AND disease_id = 'J11';

DELETE 
FROM count_of_disease
WHERE patient_id ='Nastya' AND disease_id = 'J00-06';

SELECT * FROM count_of_disease;





