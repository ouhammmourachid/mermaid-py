import unittest

from mermaid.erdiagram import Entity


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
