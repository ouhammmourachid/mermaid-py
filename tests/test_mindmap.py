import unittest

from mermaid import Config
from mermaid.icon import Icon
from mermaid.mindmap import Level, LevelShape, Mindmap


class TestLevelShape(unittest.TestCase):
    def test_level_shape(self):
        self.assertEqual(LevelShape.SQUARE.end, "]")
        self.assertEqual(LevelShape.SQUARE.start, "[")
        self.assertEqual(LevelShape.ROUNDED_SQUARE.end, ")")
        self.assertEqual(LevelShape.ROUNDED_SQUARE.start, "(")
        self.assertEqual(LevelShape.CIRCLE.end, "))")
        self.assertEqual(LevelShape.CIRCLE.start, "((")
        self.assertEqual(LevelShape.BANG.end, "((")
        self.assertEqual(LevelShape.BANG.start, "))")
        self.assertEqual(LevelShape.CLOUD.end, "(")
        self.assertEqual(LevelShape.CLOUD.start, ")")
        self.assertEqual(LevelShape.HEXAGON.end, "}}")
        self.assertEqual(LevelShape.HEXAGON.start, "{{")
        self.assertEqual(LevelShape.DEFAULT.end, "")
        self.assertEqual(LevelShape.DEFAULT.start, "")


class TestLevel(unittest.TestCase):
    def test_level(self):
        level = Level("name")
        self.assertEqual(level.id_, "name")
        self.assertEqual(level.name, "name")
        self.assertEqual(level.children, [])
        self.assertEqual(level.shape, LevelShape.DEFAULT)

    def test_add_child(self):
        level = Level("name")
        level.add_child(Level("child"))
        self.assertEqual(level.children[0].name, "child")

    def test_str(self):
        level = Level("name")
        self.assertEqual(str(level), "\t\tname\n")

    def test_list_str(self):
        level = Level("name")
        level.add_child(Level("child"))
        self.assertEqual(level.list_str(), ["name", ["child"]])

    def test_list_str_with_level_deapth_2(self):
        level = Level("name")
        level.add_child(Level("child"))
        level.children[0].add_child(Level("grandchild", shape=LevelShape.CIRCLE))
        level.children[0].add_child(Level("grandchild2", shape=LevelShape.SQUARE))
        self.assertEqual(
            level.list_str(), ["name", ["child", ["((grandchild))", "[grandchild2]"]]]
        )

    def test_list_str_with_level_deapth_3(self):
        level = Level("name")
        level.add_child(Level("child"))
        level.children[0].add_child(Level("grandchild"))
        level.children[0].children[0].add_child(Level("greatgrandchild"))
        level.children[0].add_child(Level("grandchild2"))
        self.assertEqual(
            level.list_str(),
            ["name", ["child", ["grandchild", ["greatgrandchild"], "grandchild2"]]],
        )

    def test_str_with_deapth_2(self):
        level = Level("name")
        level.add_child(Level("child"))
        level.children[0].add_child(Level("grandchild", shape=LevelShape.CIRCLE))
        level.children[0].add_child(Level("grandchild2", shape=LevelShape.SQUARE))
        expected = (
            "\t\tname\n\t\t\tchild\n\t\t\t\t((grandchild))\n\t\t\t\t[grandchild2]\n"
        )
        self.assertEqual(str(level), expected)

    def test_str_with_deapth_3(self):
        level = Level("name")
        level.add_child(Level("child"))
        level.children[0].add_child(Level("grandchild"))
        level.children[0].children[0].add_child(Level("greatgrandchild"))
        level.children[0].add_child(Level("grandchild2"))
        expected = "\t\tname\n\t\t\tchild\n\t\t\t\tgrandchild\n\t\t\t\t\tgreatgrandchild\n\t\t\t\tgrandchild2\n"
        self.assertEqual(str(level), expected)

    def test_str_with_icon(self):
        level = Level("name", icon=Icon("icon", "fa"))
        expected = "\t\tname\n\t\t::icon(fa icon)\n"
        self.assertEqual(str(level), expected)

    def test_str_with_icon_and_deapth_2(self):
        level = Level("name")
        level.add_child(Level("child"))
        level.children[0].add_child(
            Level("grandchild", shape=LevelShape.CIRCLE, icon=Icon("icon", "fa"))
        )
        level.children[0].add_child(Level("grandchild2", shape=LevelShape.SQUARE))
        expected = """\t\tname
\t\t\tchild
\t\t\t\t((grandchild))
\t\t\t\t::icon(fa icon)
\t\t\t\t[grandchild2]
"""
        self.assertEqual(str(level), expected)


class TestMindmap(unittest.TestCase):
    def setUp(self):
        self.level_depth_1 = Level("name")
        self.level_depth_2 = Level("name 2", [Level("child")])
        self.level_depth_3 = Level("name 3", [Level("child", [Level("grandchild")])])

    def test_mindmap(self):
        mindmap = Mindmap("title")
        self.assertEqual(mindmap.title, "title")
        self.assertEqual(mindmap.levels, [])
        self.assertEqual(mindmap.shape, LevelShape.DEFAULT)

    def test_mindmap_with_levels(self):
        mindmap = Mindmap("title", levels=[self.level_depth_1])

        expecte_script = """---
title: title
---
mindmap
\ttitle
\t\tname
"""
        self.assertEqual(mindmap.script, expecte_script)

    def test_mindmap_with_levels_and_shape(self):
        mindmap = Mindmap("title", levels=[self.level_depth_1], shape=LevelShape.CIRCLE)

        expecte_script = """---
title: title
---
mindmap
\t((title))
\t\tname
"""
        self.assertEqual(mindmap.script, expecte_script)

    def test_mindmap_with_levels_depth_2(self):
        mindmap = Mindmap("title", levels=[self.level_depth_2])

        expecte_script = """---
title: title
---
mindmap
\ttitle
\t\tname 2
\t\t\tchild
"""
        self.assertEqual(mindmap.script, expecte_script)

    def test_mindmap_with_levels_depth_3(self):
        mindmap = Mindmap("title", levels=[self.level_depth_3])

        expecte_script = """---
title: title
---
mindmap
\ttitle
\t\tname 3
\t\t\tchild
\t\t\t\tgrandchild
"""
        self.assertEqual(mindmap.script, expecte_script)

    def test_mindmap_with_config(self):
        config = Config(primary_color="red")
        mindmap = Mindmap("title", config=config)

        expecte_script = """---
title: title
---
%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red"
\t\t}
\t}
}%%

mindmap
\ttitle
"""
        self.assertEqual(mindmap.script, expecte_script)
