import time
from bs4 import BeautifulSoup
from src.selenium_base.base_selenium import BaseSelenium


def extract_page_by_config(driver: BaseSelenium, url: str, config: dict) -> list:
    datas = []

    driver.get_domain(url)
    if not driver.wait_element('table', 'tag name'):
        return datas
    time.sleep(1)
    soup = BeautifulSoup(driver.get_page_source(), 'html.parser')

    table_body = soup.find('tbody') or soup.find('table')  # Ensure table extraction is flexible
    if not table_body:
        return []

    if config.get('format', '') == 'table':
        for it in table_body.find_all('tr'):
            data = [ele.get_text(strip=True) for ele in it.find_all('td')]
            datas.append({field: data[idx] for field, idx in config['rows'].items() if idx < len(data)})

    return datas