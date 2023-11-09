import unittest
from unittest import mock

from mermaid.reqdiagram import Element, Link, Requirement, Risk, Type, VerifyMethod


class TestRequirement(unittest.TestCase):
    def test_create_requirement_with_str(self):
        requirement = Requirement('1', 'test_req', 'the test text.',
                                  'requirement', 'high', 'Test')
        expect_str = """requirement test_req {
\tid: 1
\ttext: the test text.
\trisk: high
\tverifymethod: Test
}
"""
        self.assertEqual(expect_str, str(requirement))

    def test_create_requirement_with_enum(self):
        requirement = Requirement('1', 'test_req', 'the test text.',
                                  Type.INTERFACE, Risk.LOW,
                                  VerifyMethod.ANALYSIS)
        expect_str = """interfaceRequirement test_req {
\tid: 1
\ttext: the test text.
\trisk: Low
\tverifymethod: Analysis
}
"""
        self.assertEqual(expect_str, str(requirement))


class TestElement(unittest.TestCase):
    def test_element_with_docref(self):
        element = Element('test_entity', 'simulation', '/test/test_....py')
        expect_str = """element test_entity {
\ttype: "simulation"
\tdocRef: /test/test_....py
}
"""
        self.assertEqual(expect_str, str(element))

    def test_element_without_docref(self):
        element = Element('test_entity', 'simulation')
        expect_str = """element test_entity {
\ttype: "simulation"
}
"""
        self.assertEqual(expect_str, str(element))


class TestLink(unittest.TestCase):
    def test_string_link_with_element_requirement(self):
        element = mock.Mock()
        element.name = 'test_entity'
        requirement = mock.Mock()
        requirement.name = 'test_req'
        link = Link(element, requirement, 'traces')
        expect_str = 'test_entity - traces -> test_req'

        self.assertEqual(expect_str, str(link))

    def test_string_link_with_requirements(self):
        requirement_1 = mock.Mock()
        requirement_1.name = 'test_req'
        requirement_2 = mock.Mock()
        requirement_2.name = 'test_req2'
        link = Link(requirement_1, requirement_2, 'contains')
        expect_str = 'test_req - contains -> test_req2'

        self.assertEqual(expect_str, str(link))
