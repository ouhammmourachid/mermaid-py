import unittest

from mermaid.erdiagram import Entity, Link


class TestEnity(unittest.TestCase):
    def test_str_entity_without_addition_info(self):
        attributes = {'id': 'int', 'salary': 'float', 'name': 'string'}
        entity = Entity('Employee', attributes)
        expect_str = """Employee{
\tint id
\tfloat salary
\tstring name
}"""
        self.assertEqual(expect_str, str(entity))

    def test_str_entity_with_addition_info(self):
        attributes = {
            'id': ['int', 'PK'],
            'salary': 'float',
            'id_cos': ['int', 'FK', 'comment'],
            'name': ['string', 'comment']
        }
        entity = Entity('Employee', attributes)
        expect_str = """Employee{
\tint id PK
\tfloat salary
\tint id_cos FK "comment"
\tstring name "comment"
}"""
        self.assertEqual(expect_str, str(entity))

    def test_update_attributes(self):
        attributes = {'id': 'int', 'name': 'string'}
        entity = Entity('Employee', attributes)
        entity.update_attributes({'age': 'float', 'id': ['int', 'PK']})
        expect_attributes = {
            'id': ['int', 'PK'],
            'name': 'string',
            'age': 'float'
        }

        self.assertEqual(expect_attributes, entity.attributes)

    def test_add_attribute(self):
        attributes = {'id': 'int'}
        entity = Entity('Employee', attributes)
        entity.add_attribute('age', 'float')
        entity.add_attribute('id_cos', 'int', constrint='FK')
        entity.add_attribute('phone',
                             'string',
                             constrint='UK',
                             comment='phone number')
        expect_attributes = {
            'id': 'int',
            'age': ['float'],
            'id_cos': ['int', 'FK'],
            'phone': ['string', 'UK', 'phone number']
        }

        self.assertEqual(expect_attributes, entity.attributes)


class TestLink(unittest.TestCase):
    def setUp(self) -> None:
        self.enity_1 = Entity('User')
        self.enity_2 = Entity('Tag')

    def test_link_without_label(self):
        link = Link(self.enity_1, self.enity_2, 'exactly-one', 'zero-or-more')
        expect_string = 'User||--o{Tag : ""'
        self.assertEqual(expect_string, str(link))

    def test_link_with_label(self):
        link = Link(self.enity_1,
                    self.enity_2,
                    'exactly-one',
                    'zero-or-more',
                    label='has')
        expect_string = 'User||--o{Tag : "has"'
        self.assertEqual(expect_string, str(link))
