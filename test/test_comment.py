import unittest

from app.models import Comment


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self):
        self.new_comment = Comment(comment_txt="comment_txt", creator_id="current_user", blog_id=1,
                                   timestamp="now")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

if __name__ == '__main__':
    unittest.main()
