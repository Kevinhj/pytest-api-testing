from wooapitest.src.utilities.dbUtility import DBUtility
import random

class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        """

        Args:

        Returns:

        """

        sql = f"SELECT * FROM wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        """
        Pull from the DB existing users by a limit of 100
        Args:
        qty is the quantity of users the func will return
        Returns:
        Return one or more existing users randomly
        """

        sql = "SELECT * FROM wp_users ORDER BY id DESC LIMIT 100;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))