import unittest


def test_split_by_default(input_data):
    return input_data.split()


def test_split_by_comma(input_data):
    return input_data.split(',')


def test_split_by_hash(input_data):
    return input_data.split('#')


class TestAllFunctionSplits(unittest.TestCase):
    def test_to_check_split_space(self):
        actual = test_split_by_default('Python Testing')
        expected = ['Python', 'Testing']
        self.assertEqual(actual, expected)

    def test_to_check_split_comma(self):
        actual = test_split_by_comma('open,high,low,close')
        expected = ['open', 'high', 'low', 'close']
        self.assertEqual(actual, expected)

    def test_to_check_split_hash(self):
        actual = test_split_by_hash('summer#time#vibes')
        expected = ['summer', 'time', 'vibes']
        self.assertEqual(actual, expected)
