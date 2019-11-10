from flask import Flask, render_template, request, redirect
from forms.patient_form import PatientForm
from forms.symptom_form import SymptomForm
from forms.disease_form import DiseaseForm
import uuid
import json
import plotly
from sqlalchemy.sql import func
import plotly.graph_objs as go
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:fastdagger@localhost/milev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PatientHasSymptom(db.Model):
    __tablename__ = 'patient_has_symptom'

    patient_id = db.Column(db.String(8), db.ForeignKey('orm_patient.patient_id'), primary_key=True)
    symptom_id = db.Column(db.String(8), db.ForeignKey('orm_symptom.symptom_id'), primary_key=True)

    patient = db.relationship("OrmPatient", back_populates="symptoms")
    symptom = db.relationship("OrmSymptom", back_populates="patients")

class OrmPatient(db.Model):
    __tablename__ = 'orm_patient'

    patient_id = db.Column(db.String(8), primary_key=True)
    patient_age = db.Column(db.Integer, nullable=False)
    patient_height = db.Column(db.Float, nullable=False)
    patient_weight = db.Column(db.Float, nullable=False)
    patient_temperature = db.Column(db.Float, nullable=False)

    symptoms = db.relationship('PatientHasSymptom', back_populates = 'patient')


class OrmSymptom(db.Model):
    __tablename__ = 'orm_symptom'

    symptom_id = db.Column(db.String(8), primary_key=True)
    description = db.Column(db.String(50), nullable=False)

    patients = db.relationship('PatientHasSymptom', back_populates='symptom')

    diseases = db.relationship('SymptomHasDisease', back_populates='symptom')


class SymptomHasDisease(db.Model):
    __tablename__ = 'symptom_has_disease'

    disease_id = db.Column(db.String(8), db.ForeignKey('orm_disease.disease_id'), primary_key=True)
    symptom_id = db.Column(db.String(8), db.ForeignKey('orm_symptom.symptom_id'), primary_key=True)

    symptom = db.relationship("OrmSymptom", back_populates="diseases")
    disease = db.relationship("OrmDisease", back_populates="symptoms")


class OrmDisease(db.Model):
    tablename = 'orm_disease'

    disease_id = db.Column(db.String(8), primary_key=True)
    disease_name = db.Column(db.String(20), nullable=False)
    severity = db.Column(db.Integer, nullable=False)

    symptoms = db.relationship('SymptomHasDisease', back_populates='disease')


db.create_all()

db.session.query(PatientHasSymptom).delete()
db.session.query(SymptomHasDisease).delete()
db.session.query(OrmPatient).delete()
db.session.query(OrmSymptom).delete()
db.session.query(OrmDisease).delete()

db.create_all()

Nastya = OrmPatient(
    patient_id='Nastya',
    patient_age=19,
    patient_height=190,
    patient_weight=77,
    patient_temperature=37.7
)

Max = OrmPatient(
    patient_id='Max',
    patient_age=20,
    patient_height=166,
    patient_weight=56,
    patient_temperature=3
)

Serg = OrmPatient(
    patient_id='Serg',
    patient_age=29,
    patient_height=196,
    patient_weight=49,
    patient_temperature=37.1
)

Kate = OrmPatient(
    patient_id='Kate',
    patient_age=43,
    patient_height=163,
    patient_weight=77,
    patient_temperature=37.4
)


URTI = OrmDisease(
    disease_id='J00-06',
    disease_name='URTI',
    severity=3
)

Flu = OrmDisease(
    disease_id='J10',
    disease_name='Flu',
    severity=4
)

Migraine = OrmDisease(
    disease_id='G43.0',
    disease_name='Migraine',
    severity=5
)

Cold = OrmDisease(
    disease_id='J00',
    disease_name='Cold',
    severity=3
)

cough = OrmSymptom(
    symptom_id = '21122253',
    description = 'cough'
)

throat = OrmSymptom(
    symptom_id = '31122253',
    description = 'throat pain'
)

head = OrmSymptom(
    symptom_id = '11122253',
    description = 'head pain'
)

relation1 = SymptomHasDisease(
    symptom_id = '21122253',
    disease_id = 'J10'
)

relation2 = SymptomHasDisease(
    symptom_id = '21122253',
    disease_id = 'J00-06'
)


relation3 = SymptomHasDisease(
    symptom_id = '31122253',
    disease_id = 'J00-06'
)


relation4 = SymptomHasDisease(
    symptom_id = '31122253',
    disease_id = 'J00'
)


relation5 = SymptomHasDisease(
    symptom_id = '11122253',
    disease_id = 'G43.0'
)

relation7 = PatientHasSymptom(
    patient_id = 'Nastya',
    symptom_id = '31122253'
)

relation8 = PatientHasSymptom(
    patient_id = 'Nastya',
    symptom_id = '21122253'
)

relation9 = PatientHasSymptom(
    patient_id = 'Max',
    symptom_id = '11122253'
)

relation10 = PatientHasSymptom(
    patient_id = 'Serg',
    symptom_id = '21122253'
)

relation11 = PatientHasSymptom(
    patient_id = 'Serg',
    symptom_id = '31122253'
)

db.session.add_all([

    relation1,
    relation2,
    relation3,
    relation4,
    relation5,
    relation7,
    relation8,
    relation9,
    relation10,
    relation11,
    Nastya,
    Max,
    Serg,
    Kate,
    URTI,
    Flu,
    Migraine,
    Cold,
    cough,
    throat,
    head
])

db.session.commit()


    # symptom_id_fk = db.relationship('OrmSymptom', secondary='patient_has_symptom')


# class PatientHasSymptom(db.Model):
#     tablename = 'patient_has_symptom'
#     patient_id = db.Column(db.String(20), db.ForeignKey('orm_patient.patient_id'), primary_key=True)
#     symptom_id = db.Column(db.String(20), db.ForeignKey('orm_symptom.symptom_id'), primary_key=True)
#
#
# class OrmSymptom(db.Model):
#     tablename = 'orm_symptom'
#
#     symptom_id = db.Column(db.String(20), primary_key=True)
#     description = db.Column(db.String(50), nullable=False)
#
#     patient_id_fk = db.relationship('OrmPatient', secondary='patient_has_symptom')
#     disease_id_fk = db.relationship('OrmDisease', secondary='symptom_has_disease')
#
# class SymptomHasDisease(db.Model):
#     tablename = 'symptom_has_disease'
#     disease_id = db.Column(db.String(20), db.ForeignKey('orm_disease.disease_id'), primary_key=True)
#     symptom_id = db.Column(db.String(20), db.ForeignKey('orm_symptom.symptom_id'), primary_key=True)
#
# class OrmDisease(db.Model):
#     tablename = 'orm_skill'
#
#     disease_id = db.Column(db.String(20), primary_key=True)
#     disease_name = db.Column(db.String(20), nullable=False)
#     severity = db.Column(db.Integer, nullable=False)
#
#     symptom_id_fk = db.relationship('OrmSymptom', secondary='symptom_has_disease')



@app.route('/')
def root():
    return render_template('index.html')

@app.route('/patients')
def patients():
    res = db.session.query(OrmPatient).all()

    return render_template('patients_table.html', patients=res)

@app.route('/create_patient', methods=['POST', 'GET'])
def create_patient():
    form = PatientForm()

    if request.method == 'POST':
        new_patient = OrmPatient(
            patient_id=form.patient_id.data,
            patient_age=form.patient_age.data,
            patient_height=form.patient_height.data,
            patient_weight=form.patient_weight.data,
            patient_temperature=form.patient_temperature.data
        )
        db.session.add(new_patient)
        db.session.commit()
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('patient_form.html', form=form)


@app.route('/patient_edit/<string:id>', methods=['GET', 'POST'])
def edit_patient(id):
    form = PatientForm()
    result = db.session.query(OrmPatient).filter(OrmPatient.patient_id == id).one()

    if request.method == 'GET':

        form.patient_id.data = result.patient_id
        form.patient_age.data = result.patient_age
        form.patient_height.data = result.patient_height
        form.patient_weight.data = result.patient_weight
        form.patient_temperature.data = result.patient_temperature

        return render_template('edit_patient.html', form=form, form_name='edit patient')
    elif request.method == 'POST':

        result.patient_age = form.patient_age.data
        result.patient_height = form.patient_height.data
        result.patient_weight = form.patient_weight.data
        result.patient_temperature = form.patient_temperature.data

        db.session.commit()
        return redirect('/patients')

@app.route('/delete_patient/<string:id>', methods=['GET', 'POST'])
def delete_patient(id):
    result = db.session.query(OrmPatient).filter(OrmPatient.patient_id == id).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')

# SYMPTOM
@app.route('/symptoms')
def symptoms():
    res = db.session.query(OrmSymptom).all()

    return render_template('symptoms_table.html', symptoms=res)

@app.route('/new_symptom', methods=['GET', 'POST'])
def new_symptom():
    form = SymptomForm()

    if request.method == 'POST':
        new_symptom = OrmSymptom(
            symptom_id=form.symptom_id.data,
            description=form.description.data
        )
        db.session.add(new_symptom)
        db.session.commit()
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('symptom_form.html', form=form)

@app.route('/edit_symptom/<string:id>', methods=['GET', 'POST'])
def edit_symptom(id):
    form = SymptomForm()
    result = db.session.query(OrmSymptom).filter(OrmSymptom.symptom_id == id).one()

    if request.method == 'GET':

        form.symptom_id.data = result.symptom_id
        form.description.data = result.description

        return render_template('edit_symptom.html', form=form, form_name='edit symptom')
    elif request.method == 'POST':

        result.description = form.description.data

        db.session.commit()
        return redirect('/symptoms')


@app.route('/delete_symptom/<string:id>', methods=['GET', 'POST'])
def delete_symptom(id):
    result = db.session.query(OrmSymptom).filter(OrmSymptom.symptom_id == id).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


# DISEASE
@app.route('/diseases')
def diseases():
    res = db.session.query(OrmDisease).all()

    return render_template('diseases_table.html', diseases=res)


@app.route('/new_disease', methods=['GET', 'POST'])
def new_disease():
    form = DiseaseForm()

    if request.method == 'POST':
        new_disease = OrmDisease(
            disease_id=form.disease_id.data,
            disease_name=form.disease_name.data,
            severity=form.severity.data

        )
        db.session.add(new_disease)
        db.session.commit()
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('disease_form.html', form=form)


@app.route('/edit_disease/<string:id>', methods=['GET', 'POST'])
def edit_disease(id):
    form = DiseaseForm()
    result = db.session.query(OrmDisease).filter(OrmDisease.disease_id == id).one()

    if request.method == 'GET':

        form.disease_id.data = result.disease_id
        form.disease_name.data = result.disease_name
        form.severity.data = result.severity

        return render_template('edit_disease.html', form=form, form_name='edit disease')
    elif request.method == 'POST':

        result.disease_name = form.disease_name.data
        result.severity = form.severity.data

        db.session.commit()
        return redirect('/diseases')


@app.route('/delete_disease/<string:id>', methods=['GET', 'POST'])
def delete_disease(id):
    result = db.session.query(OrmDisease).filter(OrmDisease.disease_id == id).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    my_query = (
        db.session.query(
            OrmPatient.patient_id,
            func.count(OrmSymptom.symptom_id).label('symptom_count')
        ).join(PatientHasSymptom, PatientHasSymptom.patient_id == OrmPatient.patient_id).join(OrmSymptom, OrmSymptom.symptom_id == PatientHasSymptom.symptom_id).
            group_by(OrmPatient.patient_id)
    ).all()

    dy_query = (
        db.session.query(
            OrmSymptom.description,
            func.count(OrmDisease.disease_id).label('disease_count')
        ).join(SymptomHasDisease, SymptomHasDisease.symptom_id == OrmSymptom.symptom_id).join(OrmDisease, OrmDisease.disease_id == SymptomHasDisease.disease_id).
            group_by(OrmSymptom.symptom_id)
    ).all()


    patient_id, symptom_count = zip(*my_query)

    bar = go.Bar(
        x=patient_id,
        y=symptom_count
    )

    description, disease_count = zip(*dy_query)
    pie = go.Pie(
        labels=description,
        values=disease_count
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphs_json)



if __name__ == '__main__':
    app.debug = True
    app.run()




