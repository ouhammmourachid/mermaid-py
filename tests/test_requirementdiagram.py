import unittest
from unittest import mock

from mermaid.configuration import Config
from mermaid.reqdiagram import (
    Element,
    Link,
    Requirement,
    RequirementDiagram,
    Risk,
    Type,
    VerifyMethod,
)


class TestRequirement(unittest.TestCase):
    def test_create_requirement_with_str(self):
        requirement = Requirement(
            "1", "test_req", "the test text.", "requirement", "high", "Test"
        )
        expect_str = """requirement test_req {
\tid: 1
\ttext: the test text.
\trisk: high
\tverifymethod: Test
}
"""
        self.assertEqual(expect_str, str(requirement))

    def test_create_requirement_with_enum(self):
        requirement = Requirement(
            "1",
            "test_req",
            "the test text.",
            Type.INTERFACE,
            Risk.LOW,
            VerifyMethod.ANALYSIS,
        )
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
        element = Element("test_entity", "simulation", "/test/test_....py")
        expect_str = """element test_entity {
\ttype: "simulation"
\tdocRef: /test/test_....py
}
"""
        self.assertEqual(expect_str, str(element))

    def test_element_without_docref(self):
        element = Element("test_entity", "simulation")
        expect_str = """element test_entity {
\ttype: "simulation"
}
"""
        self.assertEqual(expect_str, str(element))


class TestLink(unittest.TestCase):
    def test_string_link_with_element_requirement(self):
        element = mock.Mock()
        element.name = "test_entity"
        requirement = mock.Mock()
        requirement.name = "test_req"
        link = Link(element, requirement, "traces")
        expect_str = "test_entity - traces -> test_req"

        self.assertEqual(expect_str, str(link))

    def test_string_link_with_requirements(self):
        requirement_1 = mock.Mock()
        requirement_1.name = "test_req"
        requirement_2 = mock.Mock()
        requirement_2.name = "test_req2"
        link = Link(requirement_1, requirement_2, "contains")
        expect_str = "test_req - contains -> test_req2"

        self.assertEqual(expect_str, str(link))


class TestRequirementDiagram(unittest.TestCase):
    def test_script_diagram(self):
        elements = [
            Element("test_entity_1", "simulation"),
            Element("test_entity_2", "simulation"),
        ]
        requirements = [
            Requirement(
                "1.1", "test_req_1", "the test text.", "requirement", "high", "Test"
            ),
            Requirement(
                "1.2", "test_req_2", "the test text.", "requirement", "high", "Test"
            ),
        ]
        links = [
            Link(elements[0], requirements[0], "traces"),
            Link(elements[1], requirements[1], "traces"),
            Link(requirements[0], requirements[1], "contains"),
        ]
        diagram = RequirementDiagram(
            "simple requirement", elements, requirements, links
        )
        expect_str = f"""---
title: simple requirement
---
requirementDiagram
{elements[0]}
{elements[1]}
{requirements[0]}
{requirements[1]}
{links[0]}
{links[1]}
{links[2]}
"""
        self.assertEqual(expect_str, diagram.script)

    def test_script_diagram_with_config(self):
        elements = [
            Element("test_entity_1", "simulation"),
            Element("test_entity_2", "simulation"),
        ]
        requirements = [
            Requirement(
                "1.1", "test_req_1", "the test text.", "requirement", "high", "Test"
            ),
            Requirement(
                "1.2", "test_req_2", "the test text.", "requirement", "high", "Test"
            ),
        ]
        links = [
            Link(elements[0], requirements[0], "traces"),
            Link(elements[1], requirements[1], "traces"),
            Link(requirements[0], requirements[1], "contains"),
        ]
        config = Config(primary_color="red")
        diagram = RequirementDiagram(
            "simple requirement", elements, requirements, links, config
        )
        sub_string = """---
title: simple requirement
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
        expect_str = f"""{sub_string}
requirementDiagram
{elements[0]}
{elements[1]}
{requirements[0]}
{requirements[1]}
{links[0]}
{links[1]}
{links[2]}
"""
        self.assertEqual(expect_str, diagram.script)
