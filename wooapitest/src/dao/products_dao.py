from wooapitest.src.utilities.dbUtility import DBUtility
import random

class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        """
        This function gets a random product from the db
        Args: qty is the amount of products you want to retrieve/get, default to 1

        Returns: The product(s)

        """

        sql = f"SELECT * FROM wp_posts WHERE post_type = 'product' LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):
        sql = f"SELECT * FROM wp_posts WHERE ID = {product_id};"

        return self.db_helper.execute_select(sql)