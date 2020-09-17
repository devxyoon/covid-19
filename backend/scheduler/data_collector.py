import time
import multiprocessing
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from db_handler.mongodb_handler import MongoHandler
from korea_news.korea_news_model import KoreaNewsModel
from korean_patient.korean_patient_model import KoreanPatientModel
from status_of_overseas_occurrence.status_of_overseas_occurrence_model import StatusOfOverseasOccurrenceModel


class DataCollector:

    def collect_kp_list(self):
        lock = multiprocessing.Lock()
        lock.acquire()
        kp = KoreanPatientModel()
        mongodb = MongoHandler()
        result = kp.data_parsing(kp.api())
        mongodb.delete_items({}, "covid19", "korean_patients")
        mongodb.insert_items(result, "covid19", "korean_patients")
        lock.release()

    def run_process_collect_kp_list(self):
        p1 = multiprocessing.Process(target=self.collect_kp_list)
        p1.start()
        p1.join()

    def collect_soo_list(self):
        lock = multiprocessing.Lock()
        lock.acquire()
        soo = StatusOfOverseasOccurrenceModel()
        mongodb = MongoHandler()
        result = soo.data_parsing(soo.api())
        mongodb.delete_items({}, "covid19", "status_of_overseas_occurrence")
        mongodb.insert_items(result, "covid19", "status_of_overseas_occurrence")
        lock.release()

    def run_process_collect_soo_list(self):
        p2 = multiprocessing.Process(target=self.collect_soo_list)
        p2.start()
        p2.join()

    def collect_kn_list(self):
        lock = multiprocessing.Lock()
        lock.acquire()
        kn = KoreaNewsModel()
        mongodb = MongoHandler()
        result = kn.news_crawling()
        mongodb.delete_items({}, "covid19", "korea_news")
        mongodb.insert_items(result, "covid19", "korea_news")
        lock.release()

    def run_process_collect_kn_list(self):
        p2 = multiprocessing.Process(target=self.collect_kn_list)
        p2.start()
        p2.join()


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    dataCollector = DataCollector()
    scheduler.add_job(func=dataCollector.run_process_collect_kp_list, trigger="interval", seconds=30)
    scheduler.add_job(func=dataCollector.run_process_collect_soo_list, trigger="interval", seconds=30)
    scheduler.add_job(func=dataCollector.run_process_collect_kn_list, trigger="interval", seconds=30)
    scheduler.start()
    while True:
        print("running", datetime.now())
        time.sleep(1)
