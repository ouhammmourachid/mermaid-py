import os
import unittest
from typing import List, Tuple

import mermaid as md
from mermaid.graph import Graph


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.file_test: str = "./test-graph.mmd"
        with open(self.file_test, "w") as file:
            file.write("""graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;""")
        return super().setUp()

    def test_read_file_should_raise_error(self):
        with self.assertRaises(FileNotFoundError):
            md.load("./file.mmd")

    def test_read_file(self):
        graph: Graph = md.load(self.file_test)
        expect_title: str = "test-graph"
        expect_script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.assertEqual(graph.title, expect_title)
        self.assertEqual(graph.script, expect_script)

    def test_convert_text_to_snake_case(self):
        test_cases: List[Tuple[str, str]] = [
            ("This is my Input", "this_is_my_input"),
            ("Some_Underscores_in_Input_", "some_underscores_in_input_"),
            (".Some.dots in Input.", ".some.dots_in_input."),
            ("Some-dashes-in Input", "some-dashes-in_input"),
            ("dots.and-dashes input", "dots.and-dashes_input"),
            ("other |chars*in input#", "other__chars_in_input_"),
        ]

        for input_id, expected_out in test_cases:
            out = md.text_to_snake_case(input_id)
            self.assertEqual(expected_out, out)

    def tearDown(self) -> None:
        if os.path.exists(self.file_test):
            os.remove(self.file_test)
        return super().tearDown()
