import unittest

from mermaid.reqdiagram import Requirement, Risk, Type, VerifyMethod


class TestRequirement(unittest.TestCase):
    def test_create_requirement_with_str(self):
        requirement = Requirement(1, 'test_req', 'the test text.',
                                  'requirement', 'high', 'Test')
        expect_str = """requirement test_req {
\tid: 1
\ttext: the test text.
\trisk: high
\tverifymethod: Test
}
"""
        self.assertEqual(expect_str, str(requirement))

    def test_create_requirement_with_enum(self):
        requirement = Requirement(1, 'test_req', 'the test text.',
                                  Type.INTERFACE, Risk.LOW,
                                  VerifyMethod.ANALYSIS)
        expect_str = """interfaceRequirement test_req {
\tid: 1
\ttext: the test text.
\trisk: Low
\tverifymethod: Analysis
}
"""
        self.assertEqual(expect_str, str(requirement))
