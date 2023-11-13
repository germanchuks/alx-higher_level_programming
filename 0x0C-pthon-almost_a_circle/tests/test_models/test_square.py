#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import io
import sys


# ---__init__ method.--- #
class InitTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of the init method of
    the Square class.
    """

    def test_square_creation_with_no_arg_raises_type_error(self):
        with self.assertRaises(TypeError):
            Square()

    def test_square_is_instance_of_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_square_is_instance_of_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_square_creation_with_one_arg_increments_ids_properly(self):
        square1 = Square(5)
        square2 = Square(3)
        self.assertEqual(square1.id, square2.id - 1)

    def test_square_creation_with_four_args_assigns_unique_id_properly(self):
        self.assertEqual(9, Square(8, 2, 2, 9).id)

    def test_square_creation_with_more_than_four_args_raises_type_error(self):
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 4, 7)

    def test_square_size_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            print(Square(6, 0, 0, 1).__width)

    def test_square_x_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 2, 0, 0, 1).__x)

    def test_square_y_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            print(Square(3, 4, 0, 0, 1).__y)

    def test_square_size_getter_method(self):
        square = Square(6, 2, 3, 1)
        self.assertEqual(6, square.size)

    def test_square_size_setter_method(self):
        square = Square(6, 2, 3, 1)
        square.size = 9
        self.assertEqual(9, square.width)

    def test_square_x_getter_method(self):
        square = Square(6, 2, 3, 1)
        self.assertEqual(2, square.x)

    def test_square_x_setter_method(self):
        square = Square(6, 2, 3, 1)
        square.x = 5
        self.assertEqual(5, square.x)

    def test_square_y_getter_method(self):
        square = Square(6, 2, 3, 1)
        self.assertEqual(3, square.y)

    def test_square_y_setter_method(self):
        square = Square(6, 2, 3, 1)
        square.y = 5
        self.assertEqual(5, square.y)


# ---size attribute.--- #
class SizeTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of the Square size attribute.
    """

    def test_string_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("StringNotAllowed")

    def test_float_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(13.2)

    def test_negative_size_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3)

    def test_zero_size_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_none_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_dict_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"Daniel": 6, "German": 8})

    def test_bool_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_list_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3, 4, 5])

    def test_set_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3, 4, 5})

    def test_tuple_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3, 4, 5))

    def test_range_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(1, 7))

    def test_bytes_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Daniel')

    def test_complex_as_size_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(2))


# ---x attribute.--- #
class TestSquare_x(unittest.TestCase):
    """
    Unittests to evaluate the functionality of the Square x attribute.
    """

    def test_string_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "StringNotAllowed")

    def test_negative_x_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -5)

    def test_float_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, 7.7)

    def test_none_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, None)

    def test_bool_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, True)

    def test_dict_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {"a": 1, "b": 2})

    def test_list_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [1, 2, 3, 4, 5])

    def test_set_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {1, 2, 3, 4, 5})

    def test_tuple_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, (1, 2, 3, 4, 5))

    def test_range_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, range(1, 7))

    def test_bytes_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, b'Daniel')

    def test_complex_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, complex(2))


# ---y attribute--- #
class YTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of the Square y attribute.
    """

    def test_string_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, "StringNotAllowed")

    def test_negative_y_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 2, -5)

    def test_float_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, 7.7)

    def test_none_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, None)

    def test_bool_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 0, True)

    def test_dict_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, {"a": 1, "b": 2})

    def test_list_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, [1, 2, 3, 4, 5])

    def test_set_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 4, {1, 2, 3, 4, 5})

    def test_tuple_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, (1, 2, 3, 4, 5))

    def test_range_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, range(1, 7))

    def test_bytes_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, b'Daniel')

    def test_complex_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, complex(2))


# ---area method--- #
class AreaTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of area method of
    the Square class.
    """

    def test_small_square_area_calculation(self):
        square = Square(5, 1, 2, 0)
        self.assertEqual(25, square.area())

    def test_large_square_area_calculation(self):
        square = Square(987698769876)
        self.assertEqual(975548860014563605055376, square.area())

    def test_area_after_attributes_changed(self):
        square = Square(3, 4, 2, 3)
        square.size = 12
        square.id = 12
        self.assertEqual(144, square.area())

    def test_area_calculation_with_arg_raises_type_error(self):
        square = Square(5, 2, 5, 1)
        with self.assertRaises(TypeError):
            square.area("ArgNotRequired")


# ---__str__ and display methods--- #
class StrAndDisplayTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of __str__ and display methods
    of the Square class.
    """

    @staticmethod
    def get_output_method(square, method):
        """
        Returns text printed to stdout.
        """
        output = io.StringIO()
        sys.stdout = output
        if method == "display":
            square.display()
        else:
            print(square)
        sys.stdout = sys.__stdout__
        return (output)

    # __str__ test
    def test_str_method_with_arg(self):
        square = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            square.__str__("ArgNotRequired")

    def test_str_method_with_all_attributes(self):
        square = Square(2, 4, 6, 8)
        self.assertEqual("[Square] (8) 4/6 - 2", square.__str__())

    def test_str_method_print_with_size_only(self):
        square = Square(2)
        output = StrAndDisplayTestCase.get_output_method(square, "print")
        expected_output = "[Square] ({}) 0/0 - 2\n".format(square.id)
        self.assertEqual(expected_output, output.getvalue())

    def test_str_method_with_size_and_offset_x(self):
        square = Square(2, 4)
        expected_str = "[Square] ({}) 4/0 - 2".format(square.id)
        self.assertEqual(expected_str, square.__str__())

    def test_str_method_with_size_offset_x_and_position_y(self):
        square = Square(2, 4, 6)
        expected_str = "[Square] ({}) 4/6 - 2".format(square.id)
        self.assertEqual(expected_str, square.__str__())

    def test_str_method_with_attributes_modified(self):
        square = Square(1, 2, 3, 4)
        square.size = 5
        square.x = 6
        square.y = 7
        self.assertEqual("[Square] (4) 6/7 - 5", square.__str__())

    # display test
    def test_display_with_arg(self):
        square = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            square.display("ArgNotRequired")

    def test_display_with_all_attributes(self):
        square = Square(3, 2, 3, 1)
        expected_display = "\n\n\n  ###\n  ###\n"
        output = StrAndDisplayTestCase.get_output_method(square, "display")
        self.assertEqual(expected_display, output.getvalue())

    def test_display_with_size_only(self):
        square = Square(4)
        output = StrAndDisplayTestCase.get_output_method(square, "display")
        self.assertEqual("####\n####\n####\n####\n", output.getvalue())

    def test_display_with_size_and_offset_x(self):
        square = Square(2, 1)
        output = StrAndDisplayTestCase.get_output_method(square, "display")
        self.assertEqual(" ##\n ##\n", output.getvalue())

    def test_display_with_size_and_position_y(self):
        square = Square(2, 0, 1)
        output = StrAndDisplayTestCase.get_output_method(square, "display")
        self.assertEqual("\n##\n##\n", output.getvalue())

    def test_display_with_size_offset_x_and_position_y(self):
        square = Square(2, 2, 1)
        output = StrAndDisplayTestCase.get_output_method(square, "display")
        self.assertEqual("\n  ##\n  ##\n", output.getvalue())


# ---update method--- #
class UpdateArgsAndKwargsTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of update args and kwargs method
    of the Square class.
    """

    # args test
    def test_update_with_all_args(self):
        square = Square(2, 4, 6, 8)
        square.update(12, 14, 16, 18)
        self.assertEqual("[Square] (12) 16/18 - 14", str(square))

    def test_update_with_zero_args(self):
        square = Square(2, 4, 6, 8)
        square.update()
        self.assertEqual("[Square] (8) 4/6 - 2", str(square))

    def test_update_with_one_arg(self):
        square = Square(2, 4, 6, 8)
        square.update(12)
        self.assertEqual("[Square] (12) 4/6 - 2", str(square))

    def test_update_with_two_args(self):
        square = Square(2, 4, 6, 8)
        square.update(12, 14)
        self.assertEqual("[Square] (12) 4/6 - 14", str(square))

    def test_update_with_three_args(self):
        square = Square(2, 4, 6, 8)
        square.update(12, 14, 16)
        self.assertEqual("[Square] (12) 16/6 - 14", str(square))

    def test_update_with_more_than_four_args(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaises(IndexError):
            square.update(12, 14, 16, 18, 20)

    def test_update_twice(self):
        square = Square(2, 4, 6, 8)
        square.update(12, 14, 16, 18)
        square.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(square))

    def test_update_with_id_equal_to_none(self):
        square = Square(2, 4, 6, 8)
        square.update(None)
        expected_output = "[Square] ({}) 4/6 - 2".format(square.id)
        self.assertEqual(expected_output, str(square))

    def test_update_with_all_attributes_and_id_equal_to_none(self):
        square = Square(2, 4, 6, 8)
        square.update(None, 12, 14, 16)
        expected_output = "[Square] ({}) 14/16 - 12".format(square.id)
        self.assertEqual(expected_output, str(square))

    def test_update_with_size_zero(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(12, 0)

    def test_update_with_invalid_size_type(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(12, "StringNotAllowed")

    def test_update_with_negative_size(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(12, -14)

    def test_update_with_float_size(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            square.update(12, 14.5)

    def test_update_with_invalid_x_type(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(12, 14, "StringNotAllowed")

    def test_update_with_negative_x(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(12, 14, -16)

    def test_update_with_float_x(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be an integer"):
            square.update(12, 14, 16.5)

    def test_update_with_invalid_y_type(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(12, 14, "StringNotAllowed")

    def test_update_args_negative_y(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(12, 14, 16, -18)

    def test_update_with_float_y(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be an integer"):
            square.update(12, 14, 16, 18.5)

    # kwargs test
    def test_update_kwargs_with_id_only(self):
        square = Square(2, 4, 6, 8)
        square.update(id=12)
        self.assertEqual("[Square] (12) 4/6 - 2", str(square))

    def test_update_kwargs_with_size_and_id(self):
        square = Square(2, 4, 6, 8)
        square.update(width=14, id=12)
        self.assertEqual("[Square] (12) 4/6 - 14", str(square))

    def test_update_kwargs_with_id_x_size_y(self):
        square = Square(2, 4, 6, 8)
        square.update(id=12, x=18, size=16, y=20)
        self.assertEqual("[Square] (12) 18/20 - 16", str(square))

    def test_update_kwargs_with_id_equal_to_None(self):
        square = Square(2, 4, 6, 8)
        square.update(id=None)
        expected_result = "[Square] ({}) 4/6 - 2".format(square.id)
        self.assertEqual(expected_result, str(square))

    def test_update_kwargs_with_id_equal_to_None_and_other_attributes(self):
        square = Square(2, 4, 6, 8)
        square.update(id=None, y=20, size=14)
        expected_result = "[Square] ({}) 4/20 - 14".format(square.id)
        self.assertEqual(expected_result, str(square))

    def test_update_kwargs_twice(self):
        square = Square(2, 4, 6, 8)
        square.update(id=12, size=14, x=18)
        square.update(y=3, x=2, size=13)
        self.assertEqual("[Square] (12) 2/3 - 13", str(square))

    def test_update_kwargs_with_size_zero(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=0)

    def test_update_kwargs_with_invalid_size_type(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="StringNotAllowed")

    def test_update_kwargs_with_negative_size(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(id=12, size=-14)

    def test_update_kwargs_with_float_size(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            square.update(x=12, size=14.5)

    def test_update_kwargs_with_invalid_x_type(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(size=12, x="StringNotAllowed")

    def test_update_kwargs_with_negative_x(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(id=16, x=-18)

    def test_update_kwargs_with_float_x(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be an integer"):
            square.update(y=14, size=16, x=18.5)

    def test_update_kwargs_with_invalid_y_type(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(x=18, y="StringNotAllowed")

    def test_update_kwargs_with_negative_y(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(x=12, id=14, size=16, y=-20)

    def test_update_kwargs_with_float_y(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be an integer"):
            square.update(x=12, size=14, id=16, y=20.5)

    def test_update_kwargs_with_incorrect_keys(self):
        square = Square(2, 4, 6, 8)
        square.update(i=10, j=20, k=30)
        self.assertEqual("[Square] (8) 4/6 - 2", str(square))

    def test_update_kwargs_with_few_wrong_keys(self):
        square = Square(2, 4, 6, 8)
        square.update(id=12, size=14, x=16, y=18, i=1, j=2)
        self.assertEqual("[Square] (12) 16/18 - 14", str(square))

    # args and kwargs test
    def test_update_with_args_and_kwargs_combined(self):
        square = Square(2, 4, 6, 8)
        square.update(12, 14, size=16, y=20)
        self.assertEqual("[Square] (12) 4/6 - 14", str(square))


# ---to_dictionary method--- #
class ToDictionaryTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of to_dictionary method of
    the Square class.
    """

    def test_serialize_with_to_dictionary_with_argument(self):
        square = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            square.to_dictionary("ArgNotRequired")

    def test_serialize_with_to_dictionary(self):
        square = Square(2, 4, 6, 8)
        expected_result = {'id': 8, 'x': 6, 'size': 2, 'y': 8}
        self.assertDictEqual(expected_result, square.to_dictionary())

    def test_update_with_to_dictionary(self):
        square1 = Square(2, 4, 6, 8)
        square2 = Square(1, 2, 3, 4)
        square2.update(**square1.to_dictionary())
        self.assertNotEqual(square1, square2)


if __name__ == "__main__":
    unittest.main()
