import unittest

from app.models import Blog


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    def setUp(self):
        self.new_blog = Blog(title='hilarious', description='I saw you in my dreams and i dint wanna wake up',
                             blog_txt='Pickup Line', creator_id=1, timestamp="now", saves='', comments="")


    def test_add_blog(self):
        self.new_blog.add_blog()
        blog = self.new_blog.get_blog(1)
        self.assertEqual(blog, self.new_blog)


if __name__ == '__main__':
    unittest.main()
