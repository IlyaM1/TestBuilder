import unittest
from db.sqlite import SQLInteract


class TestSql(unittest.TestCase):
    def setUp(self):
        self.sql = SQLInteract(table_name="emp")
        self.sql.sql_create_new_table()

    def test_sql(self):
        # self.assertEqual(self.sql.sql_create_new_table(), None)
        # self.assertEqual(self.sql.sql_add_new_user(user_obj=[0, "Ilya", "QwertyI", "Junior", "[]"]), None)

        self.assertEqual(self.sql.return_full_table(),
                         [(1, 'Vlad', 'QwertyI', 'Junior', '[]'), (2, 'Ilya', 'QwertyI', 'Junior', '[]')])

        self.assertEqual(self.sql.generating_values(), "(?, ?, ?, ?, ?)")

        self.assertEqual(self.assertEqual(self.sql.sql_update_one_by_id("password", "'Lol'", 1)), None)

        self.assertEqual(self.sql.sql_delete_one(), None)
        self.assertEqual(self.sql.sql_delete_one(), None)

        self.assertEqual(self.sql.return_full_table(), [(1, 'Vlad', 'Lol', 'Junior', '[]')])


if __name__ == "__main__":
    # s = SQLInteract(table_name="test")
    # s.sql_add_new_user(user_obj=[0, "Ilya", "QwertyI", "Junior", "[]"])
    # print(s.return_full_table())
    # s.sql_delete_one()
    # print(s.return_full_table())
    unittest.main()
