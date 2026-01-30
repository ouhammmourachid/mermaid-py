import unittest

from mermaid.style import Style


class TestStyle(unittest.TestCase):
    def test_str_style_with_just_name(self):
        style = Style(name="style1")
        self.assertEqual(str(style), "classDef style1 ")

    def test_str_style_with_some_style(self):
        style = Style(name="style1", fill="red", color="white")
        self.assertEqual(str(style), "classDef style1 fill:red,color:white")

    def test_str_style_with_other_style(self):
        style = Style(name="style1", other="fill:blue,stroke:yellow")
        self.assertEqual(str(style), "classDef style1 fill:blue,stroke:yellow")

    def test_str_style_with_defined_and_other_style(self):
        style = Style(name="style1", fill="red", other="stroke:#333,stroke-width:4px")
        self.assertEqual(
            str(style), "classDef style1 fill:red,stroke:#333,stroke-width:4px"
        )
