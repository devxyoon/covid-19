from flask import Flask

from korean_patient.korean_patient_model import KoreanPatientModel

app = Flask(__name__)


@app.route('/korean_patient')
def hello_world():
    kp = KoreanPatientModel()
    return kp.data_parsing(kp.api())


if __name__ == '__main__':
    app.run()
