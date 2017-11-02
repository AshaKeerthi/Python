import unittest
from mock import patch
import __builtin__
from BubbleSort import BubbleSort


class TestBubbleSort(unittest.TestCase):
    @patch.object(BubbleSort, "get_number_to_sort")
    @patch.object(__builtin__, "raw_input")
    def test_get_number_tosort(self, mock_raw_input, mock_get_number_tosort):
        mock_raw_input.return_value = 5
        sort = BubbleSort()
        sort.get_number_of_input()
        self.assertEqual(sort.number_of_element, 5)
        mock_get_number_tosort.assert_called_once_with(5)

    @patch.object(BubbleSort, "get_number_to_sort")
    @patch.object(__builtin__, "raw_input")
    def test_get_number_tosort_exception(self, mock_raw_input, mock_get_number_tosort):
        mock_raw_input.return_value = "A"
        sort = BubbleSort()
        sort.get_number_of_input()

    @patch.object(BubbleSort, "to_proceed_sorting")
    @patch.object(__builtin__, "raw_input")
    def test_to_get_element(self, mock_raw_input, mock_to_proceed_sorting):
        mock_raw_input.return_value = 67
        sort = BubbleSort()
        sort.number_of_element = 7
        sort.get_number_to_sort(sort.number_of_element)

    @patch.object(BubbleSort, "to_proceed_sorting")
    @patch.object(__builtin__, "raw_input")
    def test_to_get_element_with_string(self, mock_raw_input, mock_to_proceed_sorting):
        mock_raw_input.return_value = 'A'
        sort = BubbleSort()
        sort.number_of_element = 7
        sort.get_number_to_sort(sort.number_of_element)

    @patch.object(BubbleSort, "bubble_sort")
    @patch.object(__builtin__, "raw_input")
    def test_elements_with_string_and_number(self, mock_raw_input, mock_bubble_sort):
        mock_raw_input.return_value = 'y'
        sort = BubbleSort()
        sort.to_remove_element = ['A']
        sort. to_sort_element = [7, 6, 5, 4, 3, 2, 1]
        sort.to_proceed_sorting(sort.to_remove_element, sort. to_sort_element)

    @patch.object(BubbleSort, "bubble_sort")
    @patch.object(__builtin__, "raw_input")
    def test_elements_with_number(self, mock_raw_input, mock_bubble_sort):
        mock_raw_input.return_value = 'y'
        sort = BubbleSort()
        sort.to_remove_element = []
        sort. to_sort_element = [7, 6, 5, 4, 3, 2, 1]
        sort.to_proceed_sorting(sort.to_remove_element, sort. to_sort_element)

    @patch.object(BubbleSort, "bubble_sort")
    @patch.object(__builtin__, "raw_input")
    def test_to_cancel_sorting(self, mock_raw_input, mock_bubble_sort):
        mock_raw_input.return_value = 'n'
        sort = BubbleSort()
        sort.to_remove_element = ['K']
        sort. to_sort_element = [7, 6, 5, 4, 3, 2, 1]
        sort.to_proceed_sorting(sort.to_remove_element, sort. to_sort_element)

    @patch.object(BubbleSort, "bubble_sort")
    @patch.object(__builtin__, "raw_input")
    def test_elements_without_string_And_number(self, mock_raw_input, mock_bubble_sort):
        sort = BubbleSort()
        sort.to_remove_element = []
        sort. to_sort_element = []
        sort.to_proceed_sorting(sort.to_remove_element, sort. to_sort_element)

    def test_bubble_sort(self):
        sort = BubbleSort()
        sort.to_sort_element = [7, 6, 5, 4, 3, 2, 1]
        sort.bubble_sort(sort.to_sort_element)
        self.assertEqual(sort.to_sort_element, [1, 2, 3, 4, 5, 6, 7])
