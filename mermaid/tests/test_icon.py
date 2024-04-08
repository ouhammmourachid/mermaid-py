import unittest

from mermaid.icon import Icon


class TestIcon(unittest.TestCase):
    def test_str_icon_v1(self):
        icon = Icon(name='database', type_='fa')
        self.assertEqual('fa database', str(icon))

    def test_str_icon_v2(self):
        icon = Icon(name='database', type_='fa', str_='v2')
        self.assertEqual(' fa:database ', str(icon))
