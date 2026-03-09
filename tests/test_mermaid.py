import os
import unittest
from pathlib import Path
from unittest import mock

from mermaid import Mermaid, MermaidError, Position
from mermaid.graph import Graph


class TestMermaid(unittest.TestCase):
    def setUp(self) -> None:
        self.script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.name: str = "simple-graph"
        self.graph: Graph = Graph(self.name, self.script)
        self.mermaid_object = Mermaid(self.graph)

    def test_make_request_to_mermaid_api_for_svg(self):
        self.assertTrue(self.mermaid_object.svg_response.status_code == 200)

    def test_make_request_to_mermaid_api_for_png(self):
        self.assertTrue(self.mermaid_object.img_response.status_code == 200)

    def test_using_mermaid_with_str_script(self):
        mermaid_with_str_script = Mermaid(self.script)
        self.assertTrue(mermaid_with_str_script.svg_response.status_code == 200)
        self.assertTrue(mermaid_with_str_script.img_response.status_code == 200)

    def test_query_params_to_mermaid_api_for_svg(self):
        mermaid_with_params = Mermaid(self.graph, height=1024, scale=2)
        self.assertTrue(mermaid_with_params.img_response.status_code == 200)

    def test_should_raise_error_on_invalid_scale(self):
        with self.assertRaises(AssertionError):
            Mermaid(self.graph, scale=2)

        with self.assertRaises(AssertionError):
            Mermaid(self.graph, height=100, scale=4)

        with self.assertRaises(AssertionError):
            Mermaid(self.graph, width=100, scale=0.5)

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


class TestMermaidError(unittest.TestCase):
    """Test cases for MermaidError exception."""

    def setUp(self) -> None:
        self.script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.name: str = "error-test-graph"
        self.graph: Graph = Graph(self.name, self.script)

    def test_mermaid_error_on_400_bad_request(self):
        """Test that MermaidError is raised when API returns 400."""
        with mock.patch("requests.get") as mock_get:
            mock_response = mock.Mock()
            mock_response.ok = False
            mock_response.status_code = 400
            mock_response.text = "Invalid diagram syntax"
            mock_get.return_value = mock_response

            with self.assertRaises(MermaidError) as context:
                Mermaid(self.graph)

            error = context.exception
            self.assertEqual(error.status_code, 400)
            self.assertIn("Bad Request", str(error))
            self.assertIn("Invalid diagram syntax", str(error))

    def test_mermaid_error_on_500_internal_server_error(self):
        """Test that MermaidError is raised when API returns 500."""
        with mock.patch("requests.get") as mock_get:
            mock_response = mock.Mock()
            mock_response.ok = False
            mock_response.status_code = 500
            mock_response.text = "Internal server error"
            mock_get.return_value = mock_response

            with self.assertRaises(MermaidError) as context:
                Mermaid(self.graph)

            error = context.exception
            self.assertEqual(error.status_code, 500)
            self.assertIn("Internal Server Error", str(error))
            self.assertIn("Internal server error", str(error))

    def test_mermaid_error_on_503_service_unavailable(self):
        """Test that MermaidError is raised when API returns 503."""
        with mock.patch("requests.get") as mock_get:
            mock_response = mock.Mock()
            mock_response.ok = False
            mock_response.status_code = 503
            mock_response.text = "Service temporarily unavailable"
            mock_get.return_value = mock_response

            with self.assertRaises(MermaidError) as context:
                Mermaid(self.graph)

            error = context.exception
            self.assertEqual(error.status_code, 503)
            self.assertIn("Service Unavailable", str(error))

    def test_mermaid_error_on_404_not_found(self):
        """Test that MermaidError is raised when API returns 404."""
        with mock.patch("requests.get") as mock_get:
            mock_response = mock.Mock()
            mock_response.ok = False
            mock_response.status_code = 404
            mock_response.text = "Endpoint not found"
            mock_get.return_value = mock_response

            with self.assertRaises(MermaidError) as context:
                Mermaid(self.graph)

            error = context.exception
            self.assertEqual(error.status_code, 404)
            self.assertIn("Not Found", str(error))

    def test_mermaid_error_contains_metadata(self):
        """Test that MermaidError stores error metadata."""
        with mock.patch("requests.get") as mock_get:
            mock_response = mock.Mock()
            mock_response.ok = False
            mock_response.status_code = 400
            mock_response.text = "Test error details"
            mock_get.return_value = mock_response

            with self.assertRaises(MermaidError) as context:
                Mermaid(self.graph)

            error = context.exception
            self.assertEqual(error.status_code, 400)
            self.assertEqual(error.response_text, "Test error details")
            self.assertIsNotNone(error.url)

    def test_mermaid_error_message_formatting_long_response(self):
        """Test that MermaidError truncates long response messages."""
        long_error_text = "x" * 600  # Longer than 500 chars
        
        with mock.patch("requests.get") as mock_get:
            mock_response = mock.Mock()
            mock_response.ok = False
            mock_response.status_code = 400
            mock_response.text = long_error_text
            mock_get.return_value = mock_response

            with self.assertRaises(MermaidError) as context:
                Mermaid(self.graph)

            error_message = str(context.exception)
            # Should contain truncation indicator
            self.assertIn("...", error_message)
