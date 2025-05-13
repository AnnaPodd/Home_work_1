import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.finance_reader import load_csv, load_xlsx


class TestFinanceReader(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_load_csv(self, mock_read_csv):
        # Настраиваем mock-объект для pd.read_csv
        mock_read_csv.return_value = pd.DataFrame({"column1": ["value1"], "column2": ["value2"]})

        expected_output = [{"column1": "value1", "column2": "value2"}]

        result = load_csv("mocked_path.csv")

        self.assertEqual(result, expected_output)

        mock_read_csv.assert_called_once_with("mocked_path.csv", delimiter=";")

    @patch("pandas.read_excel")
    def test_load_xlsx(self, mock_read_excel):
        mock_data = pd.DataFrame({"column1": ["value1"], "column2": ["value2"]})
        mock_read_excel.return_value = mock_data

        expected_output = [{"column1": "value1", "column2": "value2"}]
        result = load_xlsx("mocked_path.xlsx")

        self.assertEqual(result, expected_output)
        mock_read_excel.assert_called_once_with("mocked_path.xlsx")

    @patch("builtins.open", new_callable=mock_open)
    def test_load_csv_file_not_found(self, mock_file):
        mock_file.side_effect = FileNotFoundError("Файл 'mocked_path.csv' не найден.")

        with self.assertRaises(FileNotFoundError):
            load_csv("mocked_path.csv")

    @patch("pandas.read_excel")
    def test_load_xlsx_file_not_found(self, mock_read_excel):
        mock_read_excel.side_effect = FileNotFoundError("Файл 'mocked_path.xlsx' не найден.")

        with self.assertRaises(FileNotFoundError):
            load_xlsx("mocked_path.xlsx")


if __name__ == "__main__":
    unittest.main()
