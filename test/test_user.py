import unittest

from app.models import User


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.new_user = User(email="email", username="username", password="password", profile_pic_path="no_path",
                             timestamp="now", last_login="")

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password()

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

if __name__ == '__main__':
    unittest.main()
