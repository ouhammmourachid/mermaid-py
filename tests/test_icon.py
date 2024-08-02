import unittest

from mermaid.icon import Icon


class TestIcon(unittest.TestCase):
    def setUp(self) -> None:
        self.icon_v1 = Icon("icon", "fa")
        self.icon_v2 = Icon("icon", "fa", version="v2")
        self.icon_v3 = Icon("icon", "fa", version="v3")

    def test_str(self):
        self.assertEqual(str(self.icon_v1), "fa icon")
        self.assertEqual(str(self.icon_v2), "fa:icon")
        self.assertEqual(str(self.icon_v3), " fa:icon ")
