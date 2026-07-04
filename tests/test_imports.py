import unittest

import pandas
import numpy
import yfinance


class TestImports(unittest.TestCase):

    def test_imports(self):
        self.assertIsNotNone(pandas)
        self.assertIsNotNone(numpy)
        self.assertIsNotNone(yfinance)


if __name__ == "__main__":
    unittest.main()