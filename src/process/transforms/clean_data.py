

def clean_data_table(datas):
    result = [{k: v.replace("Xem chi tiết", "").strip() for k, v in data.items()} for data in datas]
    return result
