import os
import unittest
from pathlib import Path

from mermaid import Mermaid, Position
from mermaid.graph import Graph


class TestMermaid(unittest.TestCase):
    def setUp(self) -> None:
        script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.name: str = "simple-graph"
        graph: Graph = Graph(self.name, script)
        self.mermaid_object = Mermaid(graph)

    def test_make_request_to_mermaid_api_for_svg(self):
        self.assertTrue(self.mermaid_object.svg_response.status_code == 200)

    def test_make_request_to_mermaid_api_for_png(self):
        self.assertTrue(self.mermaid_object.img_response.status_code == 200)

    def test_to_svg_on_mermaid(self):
        output_path: str = f"./{self.name}.svg"
        self.mermaid_object.to_svg(output_path)

        self.assertTrue(os.path.exists(output_path))

    def test_to_svg_on_mermaid_with_path(self):
        output_path: Path = Path(f"./{self.name}.svg")
        self.mermaid_object.to_svg(output_path)

        self.assertTrue(Path.exists(output_path))

    def test_to_png_on_mermaid(self):
        output_path: str = f"./{self.name}.png"
        self.mermaid_object.to_png(output_path)

        self.assertTrue(os.path.exists(output_path))

    def test_to_png_on_mermaid_with_path(self):
        output_path: Path = Path(f"./{self.name}.png")
        self.mermaid_object.to_png(output_path)

        self.assertTrue(Path.exists(output_path))

    def test_repr_html_on_mermaid_with_default_position(self):
        self.assertEqual(
            self.mermaid_object._repr_html_(), self.mermaid_object.svg_response.text
        )

    def test_repr_html_on_mermaid_with_str_position(self):
        position = "center"
        self.mermaid_object.set_position(position)
        self.assertTrue(
            self.mermaid_object._repr_html_().startswith(
                f'<div style="text-align:{position}">'
            )
        )
        self.assertTrue(self.mermaid_object._repr_html_().endswith("</div>"))

    def test_repr_html_on_mermaid_with_enum_position(self):
        position = Position.RIGHT
        self.mermaid_object.set_position(position)
        self.assertTrue(
            self.mermaid_object._repr_html_().startswith(
                f'<div style="text-align:{position.value}">'
            )
        )
        self.assertTrue(self.mermaid_object._repr_html_().endswith("</div>"))

    def tearDown(self) -> None:
        output_svg: str = f"./{self.name}.svg"
        output_png: str = f"./{self.name}.png"
        output_svg_path: Path = Path(f"./{self.name}.svg")
        output_png_path: Path = Path(f"./{self.name}.png")

        if os.path.exists(output_svg):
            os.remove(output_svg)
        if os.path.exists(output_png):
            os.remove(output_png)
        if os.path.exists(output_svg_path):
            os.remove(output_svg_path)
        if os.path.exists(output_png_path):
            os.remove(output_png_path)

        return super().tearDown()
