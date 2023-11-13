#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
import sys
import io


# ---__init__ method.--- #
class InitTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of the __init__ method of the
    Rectangle class.
    """

    def test_rectangle_creation_with_one_arg_raises_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_rectangle_is_instance_of_base(self):
        self.assertIsInstance(Rectangle(8, 3), Base)

    def test_rectangle_creation_with_two_args_increments_ids_properly(self):
        rect1 = Rectangle(8, 3)
        rect2 = Rectangle(3, 8)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_create_rectangle_with_five_args_assigns_unique_id_properly(self):
        self.assertEqual(9, Rectangle(8, 3, 0, 0, 9).id)

    def test_create_rectangle_with_more_than_five_args_raises_typeerror(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_rectangle_width_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 7, 0, 0, 1).__width)

    def test_rectangle_height_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 9, 0, 0, 1).__height)

    def test_rectangle_x_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 0, 0, 1).__x)

    def test_rectangle_y_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 4, 0, 0, 1).__y)

    def test_rectangle_width_getter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        self.assertEqual(6, rect.width)

    def test_rectangle_width_setter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        rect.width = 9
        self.assertEqual(9, rect.width)

    def test_rectangle_height_getter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        self.assertEqual(8, rect.height)

    def test_rectangle_height_setter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        rect.height = 9
        self.assertEqual(9, rect.height)

    def test_rectangle_x_getter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        self.assertEqual(8, rect.x)

    def test_rectangle_x_setter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        rect.x = 9
        self.assertEqual(9, rect.x)

    def test_rectangle_y_getter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        self.assertEqual(6, rect.y)

    def test_rectangle_y_setter_method(self):
        rect = Rectangle(6, 8, 8, 6, 1)
        rect.y = 9
        self.assertEqual(9, rect.y)

    def test_rectangle_creation_with_no_args_raises_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle()


# ---width attribute.--- #
class WidthTestCase(unittest.TestCase):
    """
    Unittests to evaluate functionality of Rectangle width attribute.
    """

    def test_string_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("StringNotAllowed", 5)

    def test_float_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(13.2, 3)

    def test_negative_width_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)

    def test_zero_width_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_none_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_dict_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"Daniel": 6, "German": 8}, 10)

    def test_bool_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 3)

    def test_list_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3, 4, 5], 6)

    def test_set_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3, 4, 5}, 6)

    def test_tuple_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3, 4, 5), 6)

    def test_range_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(1, 7), 6)

    def test_bytes_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Daniel', 6)

    def test_complex_as_width_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 3)


# ---height attribute--- #
class HeightTestCase(unittest.TestCase):
    """
    Unittests to evaluate functionality of Rectangle height attribute.
    """

    def test_string_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "StringNotAllowed")

    def test_float_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, 3.8)

    def test_negative_height_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -3)

    def test_zero_height_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)

    def test_none_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

    def test_dict_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {"Daniel": 6, "German": 8})

    def test_list_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, [1, 2, 3, 4, 5])

    def test_set_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, {1, 2, 3, 4, 5})

    def test_tuple_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3, 4, 5))

    def test_range_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, range(1, 7))

    def test_bytes_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, b'Daniel')

    def test_complex_as_height_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(2))


# ---x attribute--- #
class XTestCase(unittest.TestCase):
    """
    Unittests to evaluate functionality of Rectangle x attribute.
    """

    def test_string_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, "StringNotAllowed")

    def test_negative_x_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 8, -5)

    def test_float_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, 7.7)

    def test_none_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, None)

    def test_bool_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, True)

    def test_dict_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, {"a": 1, "b": 2})

    def test_list_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, [1, 2, 3, 4, 5])

    def test_set_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, {1, 2, 3, 4, 5})

    def test_tuple_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, (1, 2, 3, 4, 5))

    def test_range_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, range(1, 7))

    def test_bytes_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, b'Daniel')

    def test_complex_as_x_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, complex(2))


# ---y attribute--- #
class YTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of the Rectangle y attribute.
    """

    def test_string_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 4, "StringNotAllowed")

    def test_negative_y_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 8, 3, -5)

    def test_float_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 2, 7.7)

    def test_none_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 1, None)

    def test_bool_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 0, True)

    def test_dict_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 2, {"a": 1, "b": 2})

    def test_list_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 3, [1, 2, 3, 4, 5])

    def test_set_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 4, {1, 2, 3, 4, 5})

    def test_tuple_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 5, (1, 2, 3, 4, 5))

    def test_range_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 2, range(1, 7))

    def test_bytes_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 3, b'Daniel')

    def test_complex_as_y_raises_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 1, complex(2))


# ---area method.--- #
class AreaTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of area method of the
    Rectangle class.
    """

    def test_small_rectangle_area_calculation(self):
        rect = Rectangle(2, 3, 0, 0, 0)
        self.assertEqual(6, rect.area())

    def test_large_rectangle_area_calculation(self):
        rect = Rectangle(987698769876, 987698769876)
        self.assertEqual(975548860014563605055376, rect.area())

    def test_area_after_attributes_changed(self):
        rect = Rectangle(3, 4, 2, 3)
        rect.width = 5
        rect.height = 10
        self.assertEqual(50, rect.area())

    def test_area_calculation_with_arg_raises_type_error(self):
        rect = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.area("ArgNotRequired")


# ---__str__ and display methods.--- #
class StrAndDisplayTestCase(unittest.TestCase):
    """
    Unittests to evaluate functionality of __str__ and display methods of the
    Rectangle class.
    """

    @staticmethod
    def get_output_method(rect, method):
        """
        Returns text printed to stdout.
        """
        output = io.StringIO()
        sys.stdout = output
        if method == "display":
            rect.display()
        else:
            print(rect)
        sys.stdout = sys.__stdout__
        return (output)

    # __str__ test

    def test_str_method_with_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.__str__("ArgNotRequired")

    def test_str_method_with_all_attributes(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", rect.__str__())

    def test_str_method_print_with_dimensions_only(self):
        rect = Rectangle(2, 4)
        output = StrAndDisplayTestCase.get_output_method(rect, "print")
        expected_output = "[Rectangle] ({}) 0/0 - 2/4\n".format(rect.id)
        self.assertEqual(expected_output, output.getvalue())

    def test_str_method_with_dimensions_and_offset_x(self):
        rect = Rectangle(2, 4, 6)
        expected_str = "[Rectangle] ({}) 6/0 - 2/4".format(rect.id)
        self.assertEqual(expected_str, rect.__str__())

    def test_str_method_with_dimensions_offset_x_and_position_y(self):
        rect = Rectangle(2, 4, 6, 8)
        expected_str = "[Rectangle] ({}) 6/8 - 2/4".format(rect.id)
        self.assertEqual(expected_str, rect.__str__())

    def test_str_method_with_attributes_modified(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.width = 2
        rect.height = 4
        rect.x = 6
        rect.y = 8
        self.assertEqual("[Rectangle] (5) 6/8 - 2/4", rect.__str__())

    # display test
    def test_display_with_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.display("ArgNotRequired")

    def test_display_with_all_attributes(self):
        rect = Rectangle(3, 2, 4, 1, 1)
        expected_display = "\n    ###\n    ###\n"
        output = StrAndDisplayTestCase.get_output_method(rect, "display")
        self.assertEqual(expected_display, output.getvalue())

    def test_display_with_dimensions_only(self):
        rect = Rectangle(4, 2)
        output = StrAndDisplayTestCase.get_output_method(rect, "display")
        self.assertEqual("####\n####\n", output.getvalue())

    def test_display_with_dimensions_and_offset_x(self):
        rect = Rectangle(2, 3, 1)
        output = StrAndDisplayTestCase.get_output_method(rect, "display")
        self.assertEqual(" ##\n ##\n ##\n", output.getvalue())

    def test_display_with_dimensions_and_position_y(self):
        rect = Rectangle(2, 3, 0, 1)
        output = StrAndDisplayTestCase.get_output_method(rect, "display")
        self.assertEqual("\n##\n##\n##\n", output.getvalue())

    def test_display_with_dimensions_offset_x_and_position_y(self):
        rect = Rectangle(2, 3, 2, 1)
        output = StrAndDisplayTestCase.get_output_method(rect, "display")
        self.assertEqual("\n  ##\n  ##\n  ##\n", output.getvalue())


# ---update method.--- #
class UpdateArgsAndKwargsTestCase(unittest.TestCase):
    """
    Unittests to evaluate functionality of update args and kwargs method of
    the Rectangle class.
    """

    # args test
    def test_update_with_all_args(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(12, 14, 16, 18, 20)
        self.assertEqual("[Rectangle] (12) 18/20 - 14/16", str(rect))

    def test_update_with_zero_args(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update()
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", str(rect))

    def test_update_with_one_arg(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(12)
        self.assertEqual("[Rectangle] (12) 6/8 - 2/4", str(rect))

    def test_update_with_two_args(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(12, 14)
        self.assertEqual("[Rectangle] (12) 6/8 - 14/4", str(rect))

    def test_update_with_three_args(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(12, 14, 16)
        self.assertEqual("[Rectangle] (12) 6/8 - 14/16", str(rect))

    def test_update_with_four_args(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(12, 14, 16, 18)
        self.assertEqual("[Rectangle] (12) 18/6 - 14/16", str(rect))

    def test_update_with_more_than_five_args(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaises(ValueError):
            rect.update(12, 14, 16, 18, 20, 22)

    def test_update_twice(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(12, 14, 16, 18, 20)
        rect.update(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(rect))

    def test_update_with_id_equal_to_none(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(None)
        expected_output = "[Rectangle] ({}) 6/8 - 2/4".format(rect.id)
        self.assertEqual(expected_output, str(rect))

    def test_update_with_all_attributes_and_id_equal_to_none(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(None, 12, 14, 16, 18)
        expected_output = "[Rectangle] ({}) 16/18 - 12/14".format(rect.id)
        self.assertEqual(expected_output, str(rect))

    def test_update_with_width_zero(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(12, 0)

    def test_update_with_invalid_width_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(12, "StringNotAllowed")

    def test_update_with_negative_width(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(12, -14)

    def test_update_with_float_width(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            rect.update(12, 14.5)

    def test_update_with_height_zero(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(12, 14, 0)

    def test_update_with_invalid_height_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(12, 14, "StringNotALlowed")

    def test_update_with_negative_height(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(12, 14, -16)

    def test_update_with_float_height(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be an integer"):
            rect.update(12, 14, 16.5)

    def test_update_with_invalid_x_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(12, 14, 16, "StringNotAllowed")

    def test_update_with_negative_x(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(12, 14, 16, -18)

    def test_update_with_float_x(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be an integer"):
            rect.update(12, 14, 16, 18.5)

    def test_update_with_invalid_y_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(12, 14, 16, 18, "StringNotAllowed")

    def test_update_args_negative_y(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(12, 14, 16, 18, -20)

    def test_update_with_float_y(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be an integer"):
            rect.update(12, 14, 16, 18, 20.5)

    # kwargs test
    def test_update_kwargs_with_id_only(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(id=12)
        self.assertEqual("[Rectangle] (12) 6/8 - 2/4", str(rect))

    def test_update_kwargs_with_width_and_id(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(width=14, id=12)
        self.assertEqual("[Rectangle] (12) 6/8 - 14/4", str(rect))

    def test_update_kwargs_with_width_height_id(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(width=14, height=16, id=12)
        self.assertEqual("[Rectangle] (12) 6/8 - 14/16", str(rect))

    def test_update_kwargs_with_id_x_height_y_width(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(id=12, x=18, height=16, y=20, width=14)
        self.assertEqual("[Rectangle] (12) 18/20 - 14/16", str(rect))

    def test_update_kwargs_with_id_equal_to_None(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(id=None)
        correct = "[Rectangle] ({}) 6/8 - 2/4".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_kwargs_with_id_equal_to_None_and_other_attributes(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(id=None, y=20, width=14)
        correct = "[Rectangle] ({}) 6/20 - 14/4".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_kwargs_twice(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(id=12, width=14, x=18, height=16)
        rect.update(y=3, x=2, height=13, width=11)
        self.assertEqual("[Rectangle] (12) 2/3 - 11/13", str(rect))

    def test_update_kwargs_with_width_zero(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(height=12, width=0)

    def test_update_kwargs_with_invalid_width_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(width="StringNotAllowed")

    def test_update_kwargs_with_negative_width(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(id=12, width=-14)

    def test_update_kwargs_with_float_width(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            rect.update(x=12, width=14.5)

    def test_update_kwargs_with_height_zero(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(y=12, width=14, height=0)

    def test_update_kwargs_with_invalid_height_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(id=12, x=14, height="StringNotALlowed")

    def test_update_kwargs_with_negative_height(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(height=-16)

    def test_update_kwargs_with_float_height(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "height must be an integer"):
            rect.update(x=12, id=14, height=16.5)

    def test_update_kwargs_with_invalid_x_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(height=12, x="StringNotAllowed")

    def test_update_kwargs_with_negative_x(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(id=16, x=-18)

    def test_update_kwargs_with_float_x(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "x must be an integer"):
            rect.update(width=12, y=14, height=16, x=18.5)

    def test_update_kwargs_with_invalid_y_type(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(x=18, y="StringNotAllowed")

    def test_update_kwargs_with_negative_y(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(x=12, id=14, height=16, y=-20)

    def test_update_kwargs_with_float_y(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaisesRegex(ValueError, "y must be an integer"):
            rect.update(x=12, height=14, id=16, width=18, y=20.5)

    def test_update_kwargs_with_incorrect_keys(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(i=10, j=20, k=30)
        self.assertEqual("[Rectangle] (10) 6/8 - 2/4", str(rect))

    def test_update_kwargs_with_few_wrong_keys(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(id=12, width=14, x=16, y=18, i=1, j=2)
        self.assertEqual("[Rectangle] (12) 16/18 - 14/4", str(rect))

    # args and kwargs test
    def test_update_with_args_and_kwargs_combined(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        rect.update(12, 14, height=16, y=20)
        self.assertEqual("[Rectangle] (12) 6/8 - 14/4", str(rect))


# ---to_dictionary method.--- #
class ToDictionaryTestCase(unittest.TestCase):
    """
    Unittests to evaluate functionality of to_dictionary method of the
    Rectangle class.
    """

    def test_serialize_with_to_dictionary_with_argument(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaises(TypeError):
            rect.to_dictionary("ArgNotRequired")

    def test_serialize_with_to_dictionary(self):
        rect = Rectangle(2, 4, 6, 8, 10)
        expected_result = {'x': 6, 'y': 8, 'id': 10, 'height': 4, 'width': 2}
        self.assertDictEqual(expected_result, rect.to_dictionary())

    def test_update_with_to_dictionary(self):
        rect1 = Rectangle(2, 4, 6, 8, 10)
        rect2 = Rectangle(1, 2, 3, 4, 5)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)


if __name__ == "__main__":
    unittest.main()
