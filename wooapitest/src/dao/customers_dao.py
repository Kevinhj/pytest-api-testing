from wooapitest.src.utilities.dbUtility import DBUtility


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
