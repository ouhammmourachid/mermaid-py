import unittest

from mermaid.piechart import PieChart


class TestPieChart(unittest.TestCase):
    def test_piechart_without_showdata(self):
        data = {
            'Calcium': 42.96,
            'Potassium': 50.05,
            'Magnesium': 10.01,
            'Iron': 5,
        }
        pie = PieChart('simple pie chart', data)
        expect_str = """---
title: simple pie chart
---
pie
\t"Calcium" : 42.96
\t"Potassium" : 50.05
\t"Magnesium" : 10.01
\t"Iron" : 5
"""
        print(expect_str)
        print('----')
        print(pie.script)
        self.assertEqual(expect_str, pie.script)

    def test_piechart_with_showdata(self):
        data = {
            'Calcium': 42.96,
            'Potassium': 50.05,
            'Magnesium': 10.01,
            'Iron': 5,
        }
        pie = PieChart('simple pie chart', data, show_data=True)
        expect_str = """---
title: simple pie chart
---
pie showData
\t"Calcium" : 42.96
\t"Potassium" : 50.05
\t"Magnesium" : 10.01
\t"Iron" : 5
"""
        print(expect_str)
        print('----')
        print(pie.script)
        self.assertEqual(expect_str, pie.script)
