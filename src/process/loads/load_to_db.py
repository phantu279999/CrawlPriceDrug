import json
from config import db_redis, config_mysql
from src.db_connection.base_redis import BaseRedis
from src.db_connection.base_mysql import BaseMySQL


def load_to_db_redis(datas: list) -> None:
    rd = BaseRedis(db_redis)
    for data in datas:
        key = data.get('name', f"record_{hash(json.dumps(data))}")
        res = rd.set_string(key, json.dumps(data, ensure_ascii=False))
        print(res)


def load_to_db_mysql(datas: list) -> None:
    mysql = BaseMySQL(config_mysql)

    for data in datas:
        fields = ','.join([key for key in data.keys()])
        values = ','.join([f"'{value}'" for value in data.values()])

        query = """INSERT INTO Drug({}) VALUES ({})""".format(fields, values)
        # print(query)
        print(mysql.execute(query))
