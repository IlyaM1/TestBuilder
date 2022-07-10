import unittest
from db.sqlite import SQLInteract


class TestSql(unittest.TestCase):
    def setUp(self):
        self.sql = SQLInteract(table_name="test")

    def test_sql_add_new_user(self):
        self.sql.sql_add_new_user(user_obj=[0, "Ilya", "QwertyI", "Junior", "[]"])
        self.assertEqual(self.sql.sql_add_new_user(user_obj=[0, "Ilya", "QwertyI", "Junior", "[]"]), None)

    def test_return_full_table(self):
        self.assertEqual(self.sql.return_full_table(),
                         [(1, 'Vlad', 'aboba', 'Junior', '[]'), (2, 'Ilya', 'QwertyI', 'Junior', '[]')])

    def test_generating_values(self):
        self.assertEqual(self.sql.generating_values(), "(?, ?, ?, ?, ?)")

    def test_sql_delete_one(self):
        self.assertEqual(self.sql.sql_delete_one(), None)

    def test_return_full_table_2(self):
        self.assertEqual(self.sql.return_full_table(), [(1, 'Vlad', 'aboba', 'Junior', '[]')])


if __name__ == "__main__":
    s = SQLInteract(table_name="test")
    s.sql_add_new_user(user_obj=[0, "Ilya", "QwertyI", "Junior", "[]"])
    print(s.return_full_table())
    s.sql_delete_one()
    print(s.return_full_table())
    unittest.main()
