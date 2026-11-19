import unittest
from unittest.mock import patch
from io import StringIO

from processing import is_valid_column, find_valid_columns
from main import main


class TestIntegration(unittest.TestCase):

    def test_column_divisible_by_five(self):
        self.assertTrue(is_valid_column([5, 10, 15]))

    def test_column_divisible_by_seven(self):
        self.assertTrue(is_valid_column([7, 14, 21]))

    def test_column_mixed_divisibility(self):
        self.assertTrue(is_valid_column([5, 7, 35]))

    def test_invalid_column(self):
        self.assertFalse(is_valid_column([5, 8, 15]))

    def test_find_valid_columns(self):
        matrix = [
            [5, 3, 7],
            [10, 8, 14],
            [15, 9, 21]
        ]
        self.assertEqual(find_valid_columns(matrix), [1, 3])

    def test_no_valid_columns(self):
        matrix = [
            [2, 4],
            [3, 6]
        ]
        self.assertEqual(find_valid_columns(matrix), [])

    def test_empty_matrix(self):
        self.assertEqual(find_valid_columns([]), [])

    @patch("main.print_result")
    @patch("main.input_matrix")
    def test_main_integration(self, mock_input, mock_output):
        mock_input.side_effect = [
            [[5, 3], [10, 8]],
            [[7, 2], [14, 3]]
        ]

        with patch("sys.stdout", new_callable=StringIO):
            main()

        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_output.call_count, 2)
        mock_output.assert_any_call(1, [1])
        mock_output.assert_any_call(2, [1])


if __name__ == "__main__":
    unittest.main()
