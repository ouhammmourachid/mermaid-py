import unittest

from mermaid import Direction
from mermaid.configuration import Config
from mermaid.flowchart import FlowChart, Link, LinkHead, LinkShape, Node
from mermaid.flowchart.node import NodeShape
from mermaid.style import Style


class TestNode(unittest.TestCase):
    def test_creating_node_without_content(self):
        node: Node = Node("First Node")
        expect_id: str = "first_node"
        expect_content: str = "First Node"
        expect_shape: NodeShape = NodeShape("[", "]")
        self.assertEqual(expect_id, node.id_)
        self.assertEqual(expect_content, node.content)
        self.assertEqual(expect_shape, node.shape)

    def test_creating_node_with_content(self):
        node: Node = Node("First Node", "this is my content", "hexagon")
        expect_id: str = "first_node"
        expect_content: str = "this is my content"
        expect_shape: NodeShape = NodeShape("{{", "}}")
        self.assertEqual(expect_id, node.id_)
        self.assertEqual(expect_content, node.content)
        self.assertEqual(expect_shape, node.shape)

    def test_string_repr_for_node(self):
        node: Node = Node("First Node", "this is my content", "hexagon")
        expect_string: str = "first_node{{" + '"this is my content"' + "}}"
        self.assertEqual(expect_string, str(node))

    def test_string_repr_for_node_with_sub_nodes(self):
        node_1: Node = Node("First Node")
        node_2: Node = Node("Second Node")
        node: Node = Node("Main Node", sub_nodes=[node_1, node_2])
        expect_string: str = """subgraph main_node ["Main Node"]
\tdirection LR
\tfirst_node["First Node"]
\tsecond_node["Second Node"]
end"""
        self.assertEqual(expect_string, str(node))

    def test_string_node_with_href_type_deafult(self):
        node: Node = Node("Node Name", href="www.github.com")
        expect_string: str = """node_name["Node Name"]
click node_name "www.github.com" _blank"""

        self.assertEqual(expect_string, str(node))

    def test_string_node_without_href_type_deafult(self):
        node: Node = Node("Node Name", href="www.github.com", href_type="top")
        expect_string: str = """node_name["Node Name"]
click node_name "www.github.com" _top"""

        self.assertEqual(expect_string, str(node))

    def test_string_node_with_styles(self):
        styles = [
            Style(name="firstStyle", fill="red"),
            Style(name="secondStyle", stroke="green"),
        ]
        node: Node = Node("Node Name", styles=styles)
        expect_string: str = """node_name["Node Name"]
node_name:::firstStyle
node_name:::secondStyle"""
        self.assertEqual(expect_string, str(node))

    def test_string_sub_nodes_with_styles(self):
        styles = [
            Style(name="firstStyle", fill="red"),
            Style(name="secondStyle", stroke="green"),
        ]
        node_1: Node = Node("First Node")
        node_2: Node = Node("Second Node")
        node: Node = Node("Main Node", sub_nodes=[node_1, node_2], styles=styles)
        expect_string: str = """subgraph main_node ["Main Node"]
\tdirection LR
\tfirst_node["First Node"]
\tsecond_node["Second Node"]
end
main_node:::firstStyle
main_node:::secondStyle"""
        self.assertEqual(expect_string, str(node))

    def test_string_sub_nodes_with_non_default_direction(self):
        node_1: Node = Node("First Node")
        node_2: Node = Node("Second Node")
        node: Node = Node(
            "Main Node", sub_nodes=[node_1, node_2], direction=Direction.TOP_TO_BOTTOM
        )
        expect_string: str = """subgraph main_node ["Main Node"]
\tdirection TB
\tfirst_node["First Node"]
\tsecond_node["Second Node"]
end"""
        self.assertEqual(expect_string, str(node))


class TestLink(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1: Node = Node("First Node")
        self.node_2: Node = Node("Second Node")
        return super().setUp()

    def test_str_link_without_message(self):
        link: Link = Link(self.node_1, self.node_2)
        expect_string: str = "first_node --> second_node"
        self.assertEqual(expect_string, str(link))

    def test_str_link_with_message(self):
        message: str = "this is my message"
        link: Link = Link(self.node_1, self.node_2, message=message)
        expect_string: str = f"first_node -->|{message}| second_node"
        self.assertEqual(expect_string, str(link))

    def test_str_link_with_no_default_value(self):
        message: str = "this is my message"
        link: Link = Link(
            self.node_1,
            self.node_2,
            shape="dotted",
            head_left="bullet",
            head_right="cross",
            message=message,
        )
        expect_string: str = f"first_node o-.-x|{message}| second_node"
        self.assertEqual(expect_string, str(link))

    def test_str_link_with_enum_shape(self):
        link: Link = Link(self.node_1, self.node_2, shape=LinkShape.DOTTED)
        expect_string: str = "first_node -.-> second_node"
        self.assertEqual(expect_string, str(link))

    def test_str_link_with_enum_link_head(self):
        link: Link = Link(
            self.node_1,
            self.node_2,
            head_left=LinkHead.BULLET,
            head_right=LinkHead.CROSS,
        )
        expect_string: str = "first_node o--x second_node"
        self.assertEqual(expect_string, str(link))


class TestFlowChart(unittest.TestCase):
    def test_make_flowchart_script_with_default_orientation(self):
        nodes = [Node("First Node"), Node("Second Node"), Node("Third Node")]
        links = [
            Link(nodes[0], nodes[1], head_left="cross"),
            Link(nodes[1], nodes[2], head_right="bullet"),
        ]
        flowchart: FlowChart = FlowChart("simple flowchart", nodes, links)
        expect_script: str = f"""---
title: simple flowchart
---
flowchart TB
\t{nodes[0]}
\t{nodes[1]}
\t{nodes[2]}
\t{links[0]}
\t{links[1]}
"""
        self.assertEqual(expect_script, flowchart.script)

    def test_make_flowchart_script_without_default_orientation(self):
        nodes = [Node("First Node"), Node("Second Node"), Node("Third Node")]
        links = [
            Link(nodes[0], nodes[1], head_left="cross"),
            Link(nodes[1], nodes[2], head_right="bullet"),
        ]
        flowchart: FlowChart = FlowChart(
            "simple flowchart", nodes, links, orientation="LR"
        )
        expect_script: str = f"""---
title: simple flowchart
---
flowchart LR
\t{nodes[0]}
\t{nodes[1]}
\t{nodes[2]}
\t{links[0]}
\t{links[1]}
"""
        self.assertEqual(expect_script, flowchart.script)

    def test_make_flowchart_script_with_enum_orientation(self):
        nodes = [Node("First Node"), Node("Second Node"), Node("Third Node")]

        links = [
            Link(nodes[0], nodes[1], head_left="cross"),
            Link(nodes[1], nodes[2], head_right="bullet"),
        ]
        flowchart: FlowChart = FlowChart(
            "simple flowchart", nodes, links, orientation=Direction.LEFT_TO_RIGHT
        )
        expect_script: str = f"""---
title: simple flowchart
---
flowchart LR
\t{nodes[0]}
\t{nodes[1]}
\t{nodes[2]}
\t{links[0]}
\t{links[1]}
"""
        self.assertEqual(expect_script, flowchart.script)

    def test_make_flowchart_script_with_styles(self):
        styles = [
            Style(name="firstStyle", fill="red"),
            Style(name="secondStyle", stroke="green"),
        ]
        nodes = [
            Node("First Node", styles=[styles[0]]),
            Node("Second Node", styles=[styles[1]]),
            Node("Third Node"),
        ]
        links = [
            Link(nodes[0], nodes[1], head_left="cross"),
            Link(nodes[1], nodes[2], head_right="bullet"),
        ]
        styles = list(set(styles))
        flowchart: FlowChart = FlowChart("simple flowchart", nodes, links)
        expect_script: str = f"""---
title: simple flowchart
---
flowchart TB
\t{styles[0]}
\t{styles[1]}
\t{nodes[0]}
\t{nodes[1]}
\t{nodes[2]}
\t{links[0]}
\t{links[1]}
"""
        self.assertEqual(expect_script, flowchart.script)

    def test_make_flowchart_script_with_duplicate_styles(self):
        styles = [
            Style(name="firstStyle", fill="red"),
            Style(name="secondStyle", stroke="green"),
        ]
        nodes = [
            Node("First Node", styles=styles),
            Node("Second Node", styles=styles),
            Node("Third Node"),
        ]
        links = [
            Link(nodes[0], nodes[1], head_left="cross"),
            Link(nodes[1], nodes[2], head_right="bullet"),
        ]
        styles = list(set(styles))
        flowchart: FlowChart = FlowChart("simple flowchart", nodes, links)
        expect_script: str = f"""---
title: simple flowchart
---
flowchart TB
\t{styles[0]}
\t{styles[1]}
\t{nodes[0]}
\t{nodes[1]}
\t{nodes[2]}
\t{links[0]}
\t{links[1]}
"""
        self.assertEqual(expect_script, flowchart.script)

    def test_str_flowchart_with_config(self):
        nodes = [Node("First Node"), Node("Second Node"), Node("Third Node")]
        links = [
            Link(nodes[0], nodes[1], head_left="cross"),
            Link(nodes[1], nodes[2], head_right="bullet"),
        ]
        config = Config(primary_color="red")
        flowchart: FlowChart = FlowChart(
            "simple flowchart", nodes, links, config=config
        )
        sub_string = """---
title: simple flowchart
---
%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red"
\t\t}
\t}
}%%
"""
        expect_script: str = f"""{sub_string}
flowchart TB
\t{nodes[0]}
\t{nodes[1]}
\t{nodes[2]}
\t{links[0]}
\t{links[1]}
"""
        self.assertEqual(expect_script, flowchart.script)
