import unittest

from compare_versions import is_version_greater_simple


class TestCompareVersionsSimple(unittest.TestCase):

    def test_patch_is_smaller(self):
        self.assertEqual(is_version_greater_simple('1.2.2', '1.2.3'), 0)

    def test_patch_is_equal(self):
        self.assertEqual(is_version_greater_simple('1.2.3', '1.2.3'), 1)

    def test_patch_is_larger(self):
        self.assertEqual(is_version_greater_simple('1.2.4', '1.2.3'), 1)

    def test_minor_and_minor_with_patch(self):
        self.assertEqual(is_version_greater_simple('1.2', '1.2.3'), 0)

    def test_patch_and_minor_with_patch(self):
        self.assertEqual(is_version_greater_simple('1.2.2', '1.2'), 1)

    def test_no_version_raises_value_error(self):
        with self.assertRaises(ValueError):
            is_version_greater_simple('', '')

    def test_cannot_accept_non_string_values(self):
        with self.assertRaises(TypeError):
            is_version_greater_simple(1.2, 2)


if __name__ == '__main__':
    unittest.main()
