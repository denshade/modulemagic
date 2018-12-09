import unittest
from sourcemodule.twitter.TweetRecipientSource import  get_recipients

class TestStringMethods(unittest.TestCase):

    def test_recipients(self):
        self.assertEqual(0, len(get_recipients("hello")))
        self.assertEqual(1, len(get_recipients("@hello")))
        self.assertEqual("hello", get_recipients("@hello")[0])



    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()