from cassandra.cluster import Cluster

cluster = Cluster()
connection = cluster.connect('lab1')

batch = """
BEGIN BATCH
INSERT INTO lab1.symptom_disease (symptom_id, description, disease_id, disease_name, severity)
VALUES ('007', 'throat pain', 'J00-06', {'URTI':'infection'}, 3);

 
INSERT INTO lab1.symptom_recommend (symptom_id,description,disease_id,disease_name,severity,recommend_id,doctor)
VALUES ('007', 'throat pain', 'J00-06', {'URTI':'infection'}, 3, 'rec_01', 'therapist');
 
APPLY BATCH;
"""
connection.execute(batch)