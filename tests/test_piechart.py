import unittest

from mermaid.configuration import Config
from mermaid.piechart import PieChart


class TestPieChart(unittest.TestCase):
    def test_piechart_without_showdata(self):
        data = {
            "Calcium": 42.96,
            "Potassium": 50.05,
            "Magnesium": 10.01,
            "Iron": 5,
        }
        pie = PieChart("simple pie chart", data)
        expect_str = """---
title: simple pie chart
---
pie
\t"Calcium" : 42.96
\t"Potassium" : 50.05
\t"Magnesium" : 10.01
\t"Iron" : 5
"""
        self.assertEqual(expect_str, pie.script)

    def test_piechart_with_showdata(self):
        data = {
            "Calcium": 42.96,
            "Potassium": 50.05,
            "Magnesium": 10.01,
            "Iron": 5,
        }
        pie = PieChart("simple pie chart", data, show_data=True)
        expect_str = """---
title: simple pie chart
---
pie showData
\t"Calcium" : 42.96
\t"Potassium" : 50.05
\t"Magnesium" : 10.01
\t"Iron" : 5
"""
        self.assertEqual(expect_str, pie.script)

    def test_piechart_with_config(self):
        data = {
            "Calcium": 42.96,
            "Potassium": 50.05,
            "Magnesium": 10.01,
            "Iron": 5,
        }
        config = Config(primary_color="red")
        pie = PieChart("simple pie chart", data, show_data=True, config=config)
        expect_str = """---
title: simple pie chart
---
%%{
\tinit: {
\t\t"theme": "default",
\t\t"themeVariables": {
\t\t\t"primaryColor": "red"
\t\t}
\t}
}%%

pie showData
\t"Calcium" : 42.96
\t"Potassium" : 50.05
\t"Magnesium" : 10.01
\t"Iron" : 5
"""
        self.assertEqual(expect_str, pie.script)
