import os
import unittest

import mermaid as md
from mermaid.graph import Graph


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.file_test: str = './test-graph.txt'
        with open(self.file_test, 'w') as file:
            file.write("""graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;""")
        return super().setUp()

    def test_read_file_should_raise_error(self):
        with self.assertRaises(FileNotFoundError):
            md.load('./file.txt')

    def test_read_file(self):
        graph: Graph = md.load(self.file_test)
        expect_title: str = 'test-graph'
        expect_script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.assertEqual(graph.title, expect_title)
        self.assertEqual(graph.script, expect_script)

    def test_convert_text_to_snake_case(self):
        input_text: str = 'This is my Input'
        out: str = md.text_to_snake_case(input_text)
        expect_out: str = 'this_is_my_input'
        self.assertEqual(expect_out, out)

    def tearDown(self) -> None:
        if os.path.exists(self.file_test):
            os.remove(self.file_test)
        return super().tearDown()
