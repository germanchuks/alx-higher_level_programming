#!/usr/bin/python3
"""Unittests for Base Class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


# ---__init__ method.--- #
class InitTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of the __init__ method
    of the Base class.
    """

    def test_public_id_can_be_updated(self):
        base = Base(11)
        base.id = 12
        self.assertEqual(12, base.id)

    def test_no_argument_creates_unique_instance_ids(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_multiple_instances_have_incrementing_ids(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_private_nb_instances_attribute_raises_error(self):
        with self.assertRaises(AttributeError):
            print(Base(14).__nb_instances)

    def test_str_id_creates_instance_with_str_id(self):
        self.assertEqual("Daniel", Base("Daniel").id)

    def test_None_id_creates_incrementing_instance_ids(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_float_id_creates_instance_with_float_id(self):
        self.assertEqual(2.85, Base(2.85).id)

    def test_unique_id_assigned_properly(self):
        self.assertEqual(8, Base(8).id)

    def test_nb_instances_count_after_unique_id_creation(self):
        base1 = Base()
        base2 = Base(10)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_bytes_id_creates_instance_with_bytes_id(self):
        self.assertEqual(b'Daniel', Base(b'Daniel').id)

    def test_two_args_raises_type_error(self):
        with self.assertRaises(TypeError):
            Base(5, 8)

    def test_complex_id_creates_instance_with_complex_id(self):
        self.assertEqual(complex(2), Base(complex(2)).id)

    def test_dict_id_creates_instance_with_dict_id(self):
        self.assertEqual({"i": 5, "j": 10}, Base({"i": 5, "j": 10}).id)

    def test_set_id_creates_instance_with_set_id(self):
        self.assertEqual({2, 6, 10}, Base({2, 6, 10}).id)

    def test_bool_id_creates_instance_with_bool_id(self):
        self.assertEqual(False, Base(False).id)

    def test_list_id_creates_instance_with_list_id(self):
        self.assertEqual([2, 6, 10], Base([2, 6, 10]).id)

    def test_tuple_id_creates_instance_with_tuple_id(self):
        self.assertEqual((5, 7, 8), Base((5, 7, 8)).id)

    def test_range_id_creates_instance_with_range_id(self):
        self.assertEqual(range(3, 10), Base(range(3, 10)).id)


# ---to_json_string static method.--- #
class ToJSONStringTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of to_json_string method of
    Base class.
    """

    def test_to_json_string_for_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_for_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_for_rectangle_type(self):
        rt = Rectangle(5, 8, 2, 4, 6)
        self.assertEqual(str, type(Base.to_json_string([rt.to_dictionary()])))

    def test_to_json_string_for_rectangle_length_one_dict(self):
        rct = Rectangle(5, 8, 2, 4, 6)
        self.assertTrue(len(Base.to_json_string([rct.to_dictionary()])) == 52)

    def test_to_json_string_for_rectangle_length_multiple_dicts(self):
        rect1 = Rectangle(3, 1, 9, 7, 4)
        rect2 = Rectangle(6, 2, 1, 5, 9)
        list_dicts = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 104)

    def test_to_json_string_for_square_type(self):
        sq = Square(6, 1, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_for_square_length_one_dict(self):
        sq = Square(6, 1, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 38)

    def test_to_json_string_for_square_length_multiple_dicts(self):
        square1 = Square(6, 1, 3, 4)
        square2 = Square(2, 5, 7, 8)
        list_dicts = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 76)

    def test_to_json_string_with_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], "Daniel")


# ---save_to_file class method.--- #
class SaveToFileTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of save_to_file method
    of the Base class.
    """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_None_square(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as myFile:
            self.assertEqual("[]", myFile.read())

    def test_save_to_file_no_args_rectangle(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_empty_list_square(self):
        Square.save_to_file([])
        with open("Square.json", "r") as myFile:
            self.assertEqual("[]", myFile.read())

    def test_save_to_file_one_custom_rectangle(self):
        rect = Rectangle(5, 3, 9, 4, 7)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as myFile:
            self.assertTrue(len(myFile.read()) == 52)

    def test_save_to_file_multiple_custom_rectangles(self):
        rect1 = Rectangle(6, 2, 3, 8, 6)
        rect2 = Rectangle(4, 9, 1, 7, 2)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as myFile:
            self.assertTrue(len(myFile.read()) == 104)

    def test_save_to_file_one_custom_square(self):
        square = Square(6, 2, 5, 3)
        Square.save_to_file([square])
        with open("Square.json", "r") as myFile:
            self.assertTrue(len(myFile.read()) == 38)

    def test_save_to_file_multiple_squares(self):
        square1 = Square(3, 7, 2, 4)
        square2 = Square(5, 1, 3, 2)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as myFile:
            self.assertTrue(len(myFile.read()) == 76)

    def test_save_to_file_overwrite_square(self):
        square = Square(3, 2, 8, 7)
        Square.save_to_file([square])
        square = Square(1, 6, 4, 9)
        Square.save_to_file([square])
        with open("Square.json", "r") as myFile:
            self.assertTrue(len(myFile.read()) == 38)

    def test_save_to_file_more_than_one_arg_square(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


# ---from_json_string static method.--- #
class FromJsonStringTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of from_json_string
    method of Base class.
    """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_json_conversion_for_None_input(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_json_conversion_for_empty_list_input(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_json_conversion_for_single_rectangle(self):
        rect_dict = {"id": 57, "width": 8, "height": 5, "x": 2}
        json_input = Rectangle.to_json_string([rect_dict])
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual([rect_dict], output_list)

    def test_json_conversion_for_two_rectangles(self):
        rect_list = [
            {"id": 64, "width": 9, "height": 3, "x": 4, "y": 5},
            {"id": 73, "width": 7, "height": 2, "x": 1, "y": 6},
        ]
        json_input = Rectangle.to_json_string(rect_list)
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual(rect_list, output_list)

    def test_json_conversion_for_single_square(self):
        square_dict = {"id": 31, "size": 7, "height": 4}
        json_input = Square.to_json_string([square_dict])
        output_list = Square.from_json_string(json_input)
        self.assertEqual([square_dict], output_list)

    def test_json_conversion_for_two_squares(self):
        square_list = [
            {"id": 54, "size": 5, "height": 3},
            {"id": 29, "size": 9, "height": 2}
        ]
        json_input = Square.to_json_string(square_list)
        output_list = Square.from_json_string(json_input)
        self.assertEqual(square_list, output_list)

    def test_json_type_conversion_for_rectangle(self):
        rect_dict = {"id": 50, "width": 7, "height": 10}
        json_input = Rectangle.to_json_string([rect_dict])
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(output_list))

    def test_json_conversion_raises_type_error_for_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 'Daniel')

    def test_json_conversion_raises_type_error_for_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()


# ---create class method.--- #
class CreateTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of create method of
    the Base class.
    """

    def test_create_rectangle_original_instance(self):
        rect1 = Rectangle(4, 6, 2, 1, 10)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (10) 2/1 - 4/6", str(rect1))

    def test_create_square_original_instance(self):
        square1 = Square(5, 2, 2, 4)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual("[Square] (4) 2/2 - 5", str(square1))

    def test_create_rectangle_new_instance(self):
        rect1 = Rectangle(4, 8, 2, 6, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (7) 2/6 - 4/8", str(rect2))

    def test_create_square_new_instance(self):
        square1 = Square(4, 6, 2, 8)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual("[Square] (8) 6/2 - 4", str(square2))

    def test_create_rectangle_instances_not_equal(self):
        rect1 = Rectangle(4, 6, 2, 8, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertIsNot(rect1, rect2)

    def test_create_square_instances_not_equal(self):
        square1 = Square(4, 2, 3, 8)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertIsNot(square1, square2)

    def test_create_rectangle_instances_not_equal_after_modification(self):
        rect1 = Rectangle(4, 2, 3, 8, 5)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        rect2.width = 10
        self.assertNotEqual(rect1, rect2)

    def test_create_square_instances_not_equal_after_modification(self):
        square1 = Square(4, 2, 3, 8)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        square2.size = 10
        self.assertNotEqual(square1, square2)


# ---load_from_file class method.--- #
class LoadFromFileTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of load_from_file_method
    of Base class.
    """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_no_file(self):
        output_list = Square.load_from_file()
        self.assertEqual([], output_list)

    def test_load_from_file_custom_rectangle_types(self):
        rect1 = Rectangle(8, 5, 3, 2, 5)
        rect2 = Rectangle(4, 6, 1, 7, 4)
        Rectangle.save_to_file([rect1, rect2])
        output_list = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output_list))

    def test_load_from_file_first_custom_rectangle(self):
        rect1 = Rectangle(8, 5, 3, 2, 5)
        rect2 = Rectangle(4, 6, 1, 7, 4)
        Rectangle.save_to_file([rect1, rect2])
        output_list = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(output_list[0]))

    def test_load_from_file_second_custom_rectangle(self):
        rect1 = Rectangle(8, 5, 3, 2, 5)
        rect2 = Rectangle(4, 6, 1, 7, 4)
        Rectangle.save_to_file([rect1, rect2])
        output_list = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(output_list[1]))

    def test_load_from_file_custom_square_types(self):
        square1 = Square(6, 3, 2, 4)
        square2 = Square(7, 1, 5, 3)
        Square.save_to_file([square1, square2])
        output_list = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output_list))

    def test_load_from_file_first_custom_square(self):
        square1 = Square(6, 3, 2, 4)
        square2 = Square(7, 1, 5, 3)
        Square.save_to_file([square1, square2])
        output_list = Square.load_from_file()
        self.assertEqual(str(square1), str(output_list[0]))

    def test_load_from_file_second_custom_square(self):
        square1 = Square(6, 3, 2, 4)
        square2 = Square(7, 1, 5, 3)
        Square.save_to_file([square1, square2])
        output_list = Square.load_from_file()
        self.assertEqual(str(square2), str(output_list[1]))

    def test_load_from_file_more_than_one_arg_raises_type_error(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


# ---save_to_file_csv class method.--- #
class SaveToFileCSVTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of save_to_file_csv method
    of Base class.
    """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_None_square(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as myFile:
            self.assertEqual("[]", myFile.read())

    def test_save_to_file_csv_no_args_square(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

    def test_save_to_file_csv_empty_list_square(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as myFile:
            self.assertEqual("[]", myFile.read())

    def test_save_to_file_csv_custom_rectangle(self):
        rect = Rectangle(6, 4, 1, 2, 7)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as myFile:
            self.assertTrue("7,6,4,1,2", myFile.read())

    def test_save_to_file_csv_multiple_custom_rectangles(self):
        rect1 = Rectangle(8, 5, 2, 3, 9)
        rect2 = Rectangle(3, 7, 1, 4, 6)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as myFile:
            self.assertTrue("9,8,5,2,3\n6,3,7,1,4", myFile.read())

    def test_save_to_file_csv_custom_square(self):
        square = Square(5, 1, 3, 3)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as myFile:
            self.assertTrue("3,5,1,3", myFile.read())

    def test_save_to_file_csv_multiple_custom_squares(self):
        square1 = Square(6, 3, 2, 4)
        square2 = Square(7, 1, 5, 3)
        Square.save_to_file_csv([square1, square2])
        with open("Square.csv", "r") as myFile:
            self.assertTrue("4,6,3,2\n3,7,1,5", myFile.read())

    def test_save_to_file_csv_overwrite_square(self):
        square1 = Square(7, 4, 12, 5)
        Square.save_to_file_csv([square1])
        square2 = Square(6, 8, 2, 10)
        Square.save_to_file_csv([square2])
        with open("Square.csv", "r") as myFile:
            self.assertTrue("10,6,8,2", myFile.read())

    def test_save_to_file_csv_more_than_one_arg_square(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 5)


# ---load_from_file_csv class method.--- #
class LoadFromFileCSVTestCase(unittest.TestCase):
    """
    Unittests to evaluate the functionality of load_from_file_csv method
    of Base class.
    """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_csv_with_no_file_returns_empty_list(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_loaded_rectangles_have_correct_types(self):
        rect1 = Rectangle(8, 5, 3, 2, 1)
        rect2 = Rectangle(4, 6, 1, 7, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_loaded_squares_have_correct_types(self):
        square1 = Square(6, 3, 2, 4)
        square2 = Square(7, 1, 5, 3)
        Square.save_to_file_csv([square1, square2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_first_rectangle_from_csv(self):
        rect1 = Rectangle(8, 5, 3, 2, 1)
        rect2 = Rectangle(4, 6, 1, 7, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        rect_output_list = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(rect_output_list[0]))

    def test_load_second_rectangle_from_csv(self):
        rect1 = Rectangle(8, 5, 3, 2, 1)
        rect2 = Rectangle(4, 6, 1, 7, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        rect_output_list = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect2), str(rect_output_list[1]))

    def test_load_first_square_from_csv(self):
        square1 = Square(6, 3, 2, 4)
        square2 = Square(7, 1, 5, 3)
        Square.save_to_file_csv([square1, square2])
        square_output_list = Square.load_from_file_csv()
        self.assertEqual(str(square1), str(square_output_list[0]))

    def test_load_second_square_from_csv(self):
        square1 = Square(6, 3, 2, 4)
        square2 = Square(7, 1, 5, 3)
        Square.save_to_file_csv([square1, square2])
        square_output_list = Square.load_from_file_csv()
        self.assertEqual(str(square2), str(square_output_list[1]))

    def test_load_from_csv_with_more_than_one_arg_raises_type_error(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
