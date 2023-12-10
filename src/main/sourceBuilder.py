import mysql.connector
import os


class SourceBuilder:
    def __init__(self, host=None, port=None, user=None, password=None, schema=None) -> None:
        self.host = host
        self.port = port
        self.connector = None
        self.user = user
        self.password = password
        self.schema = schema
    
    def build_connector(self):
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.schema
        )
    
    def query(self, sql: str):
        print('execute doris sql: ', sql)
        connect = self.build_connector()
        cursor = connect.cursor()
        try:
            cursor.execute(sql)
            try:
                results = cursor.fetchall()
                return results
            except:
                return None
        finally:
            cursor.close()
            connect.close()

        