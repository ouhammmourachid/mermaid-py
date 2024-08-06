import unittest

from mermaid.configuration import Config, Themes


class TestThemes(unittest.TestCase):
    def test_themes(self):
        self.assertEqual("default", Themes.DEFAULT.value)
        self.assertEqual("forest", Themes.FOREST.value)
        self.assertEqual("dark", Themes.DARK.value)
        self.assertEqual("neutral", Themes.NEUTRAL.value)
        self.assertEqual("base", Themes.BASE.value)


class TestConfig(unittest.TestCase):
    def test_default_config(self):
        config = Config()
        expect_str = """%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t}
\t}
}%%
"""
        self.assertEqual(expect_str, str(config))

    def test_config_with_primary_color(self):
        config = Config(primary_color="red")
        expect_str = """%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red"
\t\t}
\t}
}%%
"""
        self.assertEqual(expect_str, str(config))

    def test_config_with_primary_text_color(self):
        config = Config(primary_text_color="red")
        expect_str = """%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryTextColor": "red"
\t\t}
\t}
}%%
"""
        self.assertEqual(expect_str, str(config))

    def test_config_with_all_colors(self):
        config = Config(
            primary_color="red",
            primary_text_color="red",
            primary_border_color="red",
            line_color="red",
            secondary_color="red",
            tertiary_color="red",
        )
        expect_str = """%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red",
\t\t\t"primaryTextColor": "red",
\t\t\t"primaryBorderColor": "red",
\t\t\t"lineColor": "red",
\t\t\t"secondaryColor": "red",
\t\t\t"tertiaryColor": "red"
\t\t}
\t}
}%%
"""
        self.assertEqual(expect_str, str(config))

    def test_config_with_non_default_theme(self):
        config = Config(theme=Themes.FOREST)
        expect_str = """%%{
\tinit: {
\t\t"theme": "forest",
\t\t"themeVariables": {
\t\t}
\t}
}%%
"""
        self.assertEqual(expect_str, str(config))
