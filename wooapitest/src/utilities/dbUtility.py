import pymysql

import logging as logger
from wooapitest.src.utilities.credentialsUtility import CredentialsUtility
from wooapitest.src.configs.hosts_config import DB_HOST


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()

    def create_connection(self):

        connection = pymysql.connect(host='127.0.0.1',
                                     db='wordpress',
                                     port=3838,
                                     user=self.creds['db_user'],
                                     password=self.creds['db_password'])

        return connection

    def execute_select(self, sql):

        conn = self.create_connection()

        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n  Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass
