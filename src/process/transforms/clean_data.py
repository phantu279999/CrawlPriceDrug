from datetime import datetime


def clean_data_table(link: str, datas: list, config: dict) -> list:
    # result = [{k: v.replace("Xem chi tiết", "").strip() for k, v in data.items()} for data in datas]
    for data in datas:
        if "Xem chi tiết" in data['name']:
            data['name'] = data['name'].replace("Xem chi tiết", "").strip()
        if ',' in data['price']:
            data['price'] = data['price'].replace(",", "")
        data['declaration_date'] = datetime.strptime(data['declaration_date'], config['format_date']).isoformat()
        data['url'] = link
    return datas
