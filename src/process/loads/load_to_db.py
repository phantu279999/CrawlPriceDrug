import json
from config import db_redis
from src.db_connection.base_redis import BaseRedis


def load_to_db_redis(datas):
    rd = BaseRedis(db_redis)
    for data in datas:
        key = data.get('name', f"record_{hash(json.dumps(data))}")
        res = rd.set_string(key, json.dumps(data, ensure_ascii=False))
        print(res)