import time
import sys
from pathlib import Path
from typing import Dict, List, Any

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common.base_logger import BaseLogger
from src.selenium_base.base_selenium import BaseSelenium
from src.process.extracts.extract_page import extract_page_by_config
from src.process.transforms.clean_data import clean_data_table
from src.process.loads.load_to_db import load_to_db_redis, load_to_db_mysql


logger = BaseLogger(name='CrawlData', log_file='log/crawl_data.log')

class Process:
    def __init__(self):
        # self.driver = BaseSelenium('chrome_headless')
        self.driver = BaseSelenium('chrome')

    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit_driver()

    def load_to_db(self, datas: List[Dict[str, Any]], link:str, config: Dict[str, Any]) -> None:
        load_functions = {
            'mysql': load_to_db_mysql,
            'redis': load_to_db_redis,
        }
        load_to = config[link]['load_to']
        if load_to in load_functions:
            load_functions[load_to](datas)
        else:
            raise ValueError(f"Unsupported 'load_to' value: {load_to}")

    def app_run(self, config):

        for link in config['links']:
            if not isinstance(config.get(link), dict):
                raise ValueError(f"Config for link '{link}' must be a dictionary.")
            if 'load_to' not in config[link]:
                raise ValueError(f"Config for link '{link}' must specify 'load_to'.")

            logger.info(f"Processing link '{link}' ...")

            self.driver.get_domain(link)
            is_next = True
            while is_next:
                try:
                    # Extract
                    data_extracted = extract_page_by_config(self.driver, link, config[link])
                    # Transform
                    data_transformed = clean_data_table(link, data_extracted, config[link])
                    # Load
                    self.load_to_db(data_transformed, link, config)

                    element = self.driver.get_element(config[link]['next_page'])
                    is_next = self.driver.is_element_enable(element)
                    if is_next:
                        print(self.driver.click_to_element(element))
                        # Check data loaded
                        while self.driver.wait_element(config[link]['check_data']):
                            # print("Waiting data")
                            pass
                except Exception as e:
                    logger.error(f"Error processing link {link}: {e}")
                    continue
