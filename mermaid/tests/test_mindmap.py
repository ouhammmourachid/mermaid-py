import unittest

from mermaid.mindmap import *


class TestLevelShape(unittest.TestCase):
    def test_level_shape(self):
        self.assertEqual(LevelShape.SQUARE.end, ']')
        self.assertEqual(LevelShape.SQUARE.start, '[')
        self.assertEqual(LevelShape.ROUNDED_SQUARE.end, ')')
        self.assertEqual(LevelShape.ROUNDED_SQUARE.start, '(')
        self.assertEqual(LevelShape.CIRCLE.end, '))')
        self.assertEqual(LevelShape.CIRCLE.start, '((')
        self.assertEqual(LevelShape.BANG.end, '((')
        self.assertEqual(LevelShape.BANG.start, '))')
        self.assertEqual(LevelShape.CLOUD.end, '(')
        self.assertEqual(LevelShape.CLOUD.start, ')')
        self.assertEqual(LevelShape.HEXAGON.end, '}}')
        self.assertEqual(LevelShape.HEXAGON.start, '{{')
        self.assertEqual(LevelShape.DEFAULT.end, '')
        self.assertEqual(LevelShape.DEFAULT.start, '')


class TestLevel(unittest.TestCase):
    def test_level(self):
        level = Level('name')
        self.assertEqual(level.id_, 'name')
        self.assertEqual(level.name, 'name')
        self.assertEqual(level.children, [])
        self.assertEqual(level.shape, LevelShape.DEFAULT)

    def test_add_child(self):
        level = Level('name')
        level.add_child(Level('child'))
        self.assertEqual(level.children[0].name, 'child')

    def test_str(self):
        level = Level('name')
        self.assertEqual(str(level), 'name')

    def test_list_str(self):
        level = Level('name')
        level.add_child(Level('child'))
        self.assertEqual(level.list_str(), ['name', ['child']])

    def test_list_str_with_level_deapth_2(self):
        level = Level('name')
        level.add_child(Level('child'))
        level.children[0].add_child(
            Level('grandchild', shape=LevelShape.CIRCLE))
        level.children[0].add_child(
            Level('grandchild2', shape=LevelShape.SQUARE))
        print(level.list_str())
        self.assertEqual(
            level.list_str(),
            ['name', ['child', ['((grandchild))', '[grandchild2]']]])

    def test_list_str_with_level_deapth_3(self):
        level = Level('name')
        level.add_child(Level('child'))
        level.children[0].add_child(Level('grandchild'))
        level.children[0].children[0].add_child(Level('greatgrandchild'))
        level.children[0].add_child(Level('grandchild2'))
        print(level.list_str())
        self.assertEqual(level.list_str(), [
            'name',
            ['child', ['grandchild', ['greatgrandchild'], 'grandchild2']]
        ])
