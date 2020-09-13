from flask import Flask

from korean_patient.korean_patient_model import KoreanPatientModel
from status_of_overseas_occurrence.status_of_overseas_occurrence_model import StatusOfOverseasOccurrenceModel

app = Flask(__name__)


@app.route('/korean_patient')
def korean_patient():
    kp = KoreanPatientModel()
    return kp.data_parsing(kp.api())


@app.route('/foreign_patient')
def foreign_patient():
    soo = StatusOfOverseasOccurrenceModel()
    return soo.data_parsing(soo.api())


if __name__ == '__main__':
    app.run()
