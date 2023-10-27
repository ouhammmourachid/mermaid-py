import os
import unittest
from pathlib import Path

from mermaid.graph import Graph
from mermaid.graph.flowchart import Link, Node
from mermaid.graph.flowchart.node import NodeShape


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        script: str = """graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;"""
        self.graph_test: Graph = Graph('test-graph', script)
        return super().setUp()

    def test_save_graph_without_path(self) -> None:
        self.graph_test.save()
        self.assertTrue(Path.exists(Path('./test-graph.txt')))

    def test_save_graph_with_path(self) -> None:
        self.graph_test.save(Path('./test-graph-file.txt'))
        self.assertTrue(Path.exists(Path('./test-graph-file.txt')))

    def test_save_graph_name_contain_space(self) -> None:
        self.graph_test.name = 'test graph file'
        self.graph_test.save(Path('./test graph file.txt'))
        self.assertTrue(Path.exists(Path('./test graph file.txt')))

    def tearDown(self) -> None:
        if os.path.exists('./test-graph.txt'):
            os.remove('./test-graph.txt')
        if os.path.exists('./test-graph-file.txt'):
            os.remove('./test-graph-file.txt')
        if os.path.exists('./test graph file.txt'):
            os.remove('./test graph file.txt')
        return super().tearDown()


class TestNode(unittest.TestCase):
    def test_creating_node_without_content(self):
        node: Node = Node('First Node')
        expect_id: str = 'first_node'
        expect_content: str = 'First Node'
        expect_shape: NodeShape = NodeShape('[', ']')
        self.assertEqual(expect_id, node.id_)
        self.assertEqual(expect_content, node.content)
        self.assertEqual(expect_shape, node.shape)

    def test_creating_node_with_content(self):
        node: Node = Node('First Node', 'this is my content', 'hexagon')
        expect_id: str = 'first_node'
        expect_content: str = 'this is my content'
        expect_shape: NodeShape = NodeShape('{{', '}}')
        self.assertEqual(expect_id, node.id_)
        self.assertEqual(expect_content, node.content)
        self.assertEqual(expect_shape, node.shape)

    def test_string_repr_for_node(self):
        node: Node = Node('First Node', 'this is my content', 'hexagon')
        expect_string: str = 'first_node{{' + '"this is my content"' + '}}'
        self.assertEqual(expect_string, str(node))

    def test_string_repr_for_node_with_sub_nodes(self):
        node_1: Node = Node('First Node')
        node_2: Node = Node('Second Node')
        node: Node = Node('Main Node', sub_nodes=[node_1, node_2])
        expect_string: str = """subgraph main_node ["Main Node"]
\tfirst_node["First Node"]
\tsecond_node["Second Node"]
end"""
        self.assertEqual(expect_string, str(node))


class TestLink(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1: Node = Node('First Node')
        self.node_2: Node = Node('Second Node')
        return super().setUp()

    def test_str_link_without_message(self):

        link: Link = Link(self.node_1, self.node_2)
        expect_string: str = 'first_node ------> second_node'
        self.assertEqual(expect_string, str(link))

    def test_str_link_with_message(self):
        message: str = 'this is my message'
        link: Link = Link(self.node_1, self.node_2, message=message)
        expect_string: str = f'first_node ---|{message}|---> second_node'
        self.assertEqual(expect_string, str(link))
        self.assertEqual(expect_string, str(link))

    def test_str_link_with_no_default_value(self):
        message: str = 'this is my message'
        link: Link = Link(self.node_1,
                          self.node_2,
                          shape='dotted',
                          head_left='bullet',
                          head_right='cross',
                          message=message)
        expect_string: str = f'first_node o-.-|{message}|-.-x second_node'
        self.assertEqual(expect_string, str(link))
        self.assertEqual(expect_string, str(link))
