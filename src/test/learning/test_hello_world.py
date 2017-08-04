import unittest

from learning import hello_world


class HelloWorldTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world.hello_world(), "Hello world")
