import unittest

from mermaid.configuration import Config, Themes
from mermaid.erdiagram import Entity, ERDiagram, Link  # noqa: I101


class TestEnity(unittest.TestCase):
    def test_str_entity_without_addition_info(self):
        attributes = {"id": "int", "salary": "float", "name": "string"}
        entity = Entity("Employee", attributes)
        expect_str = """Employee{
\tint id
\tfloat salary
\tstring name
}"""
        self.assertEqual(expect_str, str(entity))

    def test_str_entity_with_addition_info(self):
        attributes = {
            "id": ["int", "PK"],
            "salary": "float",
            "id_cos": ["int", "FK", "comment"],
            "name": ["string", "comment"],
        }
        entity = Entity("Employee", attributes)
        expect_str = """Employee{
\tint id PK
\tfloat salary
\tint id_cos FK "comment"
\tstring name "comment"
}"""
        self.assertEqual(expect_str, str(entity))

    def test_update_attributes(self):
        attributes = {"id": "int", "name": "string"}
        entity = Entity("Employee", attributes)
        entity.update_attributes({"age": "float", "id": ["int", "PK"]})
        expect_attributes = {"id": ["int", "PK"], "name": "string", "age": "float"}

        self.assertEqual(expect_attributes, entity.attributes)

    def test_add_attribute(self):
        attributes = {"id": "int"}
        entity = Entity("Employee", attributes)
        entity.add_attribute("age", "float")
        entity.add_attribute("id_cos", "int", constraint="FK")
        entity.add_attribute("phone", "string", constraint="UK", comment="phone number")
        expect_attributes = {
            "id": "int",
            "age": ["float"],
            "id_cos": ["int", "FK"],
            "phone": ["string", "UK", "phone number"],
        }

        self.assertEqual(expect_attributes, entity.attributes)


class TestLink(unittest.TestCase):
    def setUp(self) -> None:
        self.enity_1 = Entity("User")
        self.enity_2 = Entity("Tag")

    def test_link_without_label(self):
        link = Link(self.enity_1, self.enity_2, "exactly-one", "zero-or-more")
        expect_string = 'User||--o{Tag : ""'
        self.assertEqual(expect_string, str(link))

    def test_link_with_label(self):
        link = Link(
            self.enity_1, self.enity_2, "exactly-one", "zero-or-more", label="has"
        )
        expect_string = 'User||--o{Tag : "has"'
        self.assertEqual(expect_string, str(link))

    def test_dotted_link(self):
        link = Link(
            self.enity_1, self.enity_2, "exactly-one", "zero-or-more", dotted=True
        )
        expect_string = 'User||..o{Tag : ""'
        self.assertEqual(expect_string, str(link))


class TestERDiagram(unittest.TestCase):
    def test_script_erdiagram(self):
        entity_1 = Entity("User", {"id": ["int", "PK"], "name": ["string", "the name"]})
        entity_2 = Entity("Tag", {"id": ["int", "PK"], "name": "string"})
        entities = [entity_1, entity_2]
        links = [Link(entity_1, entity_2, "exactly-one", "zero-or-more", dotted=True)]
        diagram = ERDiagram("e-commerce website", entities, links)
        expect_str = f"""---
title: e-commerce website
---
erDiagram
\t{entities[0]}
\t{entities[1]}
\t{links[0]}
"""
        self.assertEqual(expect_str, diagram.script)

    def test_script_erdiagram_with_config(self):
        entity_1 = Entity("User", {"id": ["int", "PK"], "name": ["string", "the name"]})
        entity_2 = Entity("Tag", {"id": ["int", "PK"], "name": "string"})
        entities = [entity_1, entity_2]
        links = [Link(entity_1, entity_2, "exactly-one", "zero-or-more", dotted=True)]
        config = Config(theme=Themes.DARK, primary_color="red")
        diagram = ERDiagram("e-commerce website", entities, links, config)
        sub_string = """---
title: e-commerce website
---
%%{
\tinit: {
\t\t"theme": "dark",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red"
\t\t}
\t}
}%%
"""
        expect_string = f"""{sub_string}
erDiagram
\t{entities[0]}
\t{entities[1]}
\t{links[0]}
"""
        self.assertEqual(expect_string, diagram.script)
