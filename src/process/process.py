import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
path_project = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

from src.selenium_base.base_selenium import BaseSelenium
from src.process.extracts.extract_page import extract_page_by_config
from src.process.transforms.clean_data import clean_data_table
from src.process.loads.load_to_db import load_to_db_redis


class Process:
    def __init__(self):
        self.driver = BaseSelenium('chrome_headless')

    def app_run(self, config):

        for link in config['links']:
            # Extract
            data_extracted = extract_page_by_config(self.driver, link, config[link])
            # Transform
            data_transformed = clean_data_table(data_extracted)
            # Load
            load_to_db_redis(data_transformed)

if __name__ == '__main__':
    process = Process()
    process.app_run()