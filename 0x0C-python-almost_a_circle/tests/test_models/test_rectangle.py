#!/usr/bin/python3

"""unittests for rectangle.py"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
import io

class TestRectangle_width(unittest.TestCase):
    """tests the width attribute"""
    
    def test_width_none(self):
        with self.assertRaisesRgex(TypeError, "width must be an integer"):
            Rectangle(none, 8)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 3)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 3)

    def test_width_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 3)

    def test_width_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"i": 4, "j": 5}, 5)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3, 8, 9), 3)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({3, 8, 9}, 3)

    def test_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({3, 8, 9}), 3)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([3, 8, 9], 3)

    def test_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(3), 4)

    def test_width_infinity(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 3)

    def test_width_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'bytes', 5)

    def test_width_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'array'), 5)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 3)

    def test_width_memview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'memview'), 4)

    def test_width_negative(self):
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            Rectangle(-3, 5)

    def test_width_zero(self):
        with self.assertRaisesRegex(TyepError, "width must be > 0"):
            Rectangle(0, 5)

class TestRectangle_instance(unittest.TestCase):
    """Tests for instantation"""

    def test_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_base(self):
        with self.assertInstance(Rectangle(3, 6), Base)

    def test_single(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_twoargs(self):
        r1 = Rectangle(5, 8)
        r2 = Rectangle(4, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_threeargs(self):
        r1 = Rectangle(3, 4, 5)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_fourargs(self):
        r1 = Rectangle(3, 4, 5, 6)
        r2 = Rectangle(6, 7, 8, 9)
        self.assertEqual(r1.id, r2.id -1)

    def test_fiveargs(self):
        self.assertEqual(7, Rectangle(3, 4, 5, 6, 7).id)

    def test_more(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 4, 1, 6, 5)

    def test_width(self):
        with self.assertRaiaes(AttributeError):
            print(Rectangle(3, 8, 4, 7, 9).__width)

    def test_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 8, 4, 7, 9).__x)

    def test_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 8, 4, 7, 9).__height)

    def test_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 8, 4, 7, 9).__y)

    def test_widthgetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        self.assertEqual(5, r.width)

    def test_xgetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        self.assertEqual(5, r.x)

    def test_heightgetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        self.assertEqual(5, r.height)

    def test_ygetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        self.assertEqual(5, r.y)

    def test_ysetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        r.y = 5
        self.assertEqual(5, r.y)

    def test_xsetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        r.x = 5
        self.assertEqual(5, r.x)

    def test_widthsetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        r.width = 5
        self.assertEqual(5, r.width)

    def test_heightsetter(self):
        r = Rectangle(3, 8, 4, 7, 9)
        r.height = 5
        self.assertEqual(5, r.height)

class TestRectangle_height(unitest.TestCase):
    """tests the height attribute"""

    def test_height_zero(self):
        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            Rectangle(5, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -5)

    def test_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('nan'))

    def test_height_bytes(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, b'bytes')

    def test_height_infinity(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def test_height_memview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, memoryview(b'memview'))

    def test_height_bytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, bytearray(b'bytesarr'))

    def test_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, range(5))

    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {3, 4, 1})

    def test_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, frozenset({3, 4, 1}))

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, (3, 4, 1))

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {'a': 3, 'b': 4})

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [3, 4, 1])

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 5.3)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "string")

    def test_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, complex(5))

    def test_height_None(string):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

class TestRectangle_x(unittest.TestCase):
    """test for the x attribute"""
    
    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, None)

    def test_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, complex(4))

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, "string")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, 5.5)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, [3, 4])

    def test_x_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, {'c': 2, 'd': 5})

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, {3, 4, 5})

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, (3, 4, 5))

    def test_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, frozenset({3, 4, 5}))


    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 4, -3)

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, b'bytes')

    def test_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, bytearray(b'bytearray'))

    def test_x_memview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, memoryview(b'memview'))

    def test_x_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, True)

    def test_x_infinity(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Recatngle(3, 4, float('inf'))

    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('nan'))

class TestRectangle_y(unittest.TestCase):
    """test for the y attribute"""

    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, float('nan'))

    def test_y_infinity(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, float('inf'))

    def test_y_boolean(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, True)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, "string")

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, [3, 4])

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, (3, 4))

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, {3, 4})

    def test_y_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, {'a': 2, 'b': 3})

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, frozenset({3, 4}))

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, 4.3)

    def test_y_None(self):
        with seslf.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, None)

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, range(3))

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 4, 5, -4)

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, b'bytes')

    def test_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, bytearray(b'bytearray'))


    def test_y_memview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, memoryview(b'memview'))

class TestRectangle_area(self):
    """tests for the area of rectangle"""

    def test_area_update_attr(self):
        r = Rectangle(3, 5, 4, 6, 2)
        r.width = 9
        r.height = 8
        self.assertEqual(72, r.area())

    def test_area_small(self):
        r = Rectangle(3, 5, 4, 6, 2)
        self.assertEqual(15, r.area())

    def test_area_large(self):
        r = rectangle(999999, 999999, 1, 2, 1)
        self.assertEqual(999998000001, r.area())

    def test_area_single_arg(self):
        r = Rectangle(3, 5, 4, 6, 2)
        with self.assertRaises(TypeError):
            r.area(1)

class TestRectangle_initialization_order(unittest.TestCase):
    """test for order of initialization"""


    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "invalid height", 4, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 5, "invalid x", "invalid y")


class TestRectangle_to_stdout(unittest.TestCase):
    """testing how rectangle is displayed to stdout"""

    @staticmethod
    def capture_stdout(rect, method):
        """returns printed text to stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height(self):
        r = Rectangle(4, 3, 5, 1, 2)
        capture = TestRectangle_to_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(4, 3, 5, 1, 2)
        capture = TestRectangle_to_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(4, 3, 5, 1, 2)
        capture = TestRectangle_to_stdout.capture_stdout(r, "display")
        display = "\n\n  ##\n  ##\n  ##\n  ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_y(self):
        r = Rectangle(4, 3, 5, 1, 2)
        capture = TestRectangle_to_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_single_arg(self):
        r = Rectangle(4, 3, 5, 1, 2)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_Update_args(unittest.TestCase):
    """test the update method"""

    def test_update_zero_args(self):
        r = Rectangle(4, 4, 4, 4, 4)
        r.update()
        self.assertEqual("[Rectangle] (4) 4/4 - 10/10", str(r))

    def test_update_one_arg(self):
        r = Rectangle(4, 4, 4, 4, 4)
        r.update(6)
        self.assertEqual("[Rectangle] (6) 4/4 - 4/4", str(r))

    def test_update_two_args(self):
        r = Rectangle(4, 4, 4, 4, 4)
        r.update(6, 8)
        self.assertEqual("[Rectangle] (6) 4/4 - 8/4", str(r))

    def test_update_args_three(self):
        r = Rectangle(4, 4, 4, 4,, 4)
        r.update(6, 8, 7)
        self.assertEqual("[Rectangle] (6) 4/4 - 8/7", str(r))

    def test_update_args_four(self):
        r =  Rectangle(4, 4, 4, 4, 4)
        r.update(6, 8, 7, 9)
        self.assertEqual("[Rectangle] (6) 9/4 - 8/7", str(r))

    def test_update_args_five(self):
        r = Rectangle(4, 4, 4, 4, 4)
        r.update(6, 8, 7, 9, 3)
        self.assertEqual("[Rectangle] (6) 9/3 - 8/7", str(r))

    def test_update_args_more(self):
        r = Rectangle(4, 4, 4, 4, 4)
        r.update(6, 8, 7, 9, 3, 5)
        self.assertEqual("[Rectangle] (6) 9/3 - 8/7", str(r))

    def test_update_args_None(self):
        r = Rectangle(4, 4, 4, 4, 4)
        r.update(None)
        correct = "[Rectangle] ({}) 4/4 - 4/4".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_and_other(self):
        r =  Rectangle(4, 4, 4, 4, 4)
        r.update(None, 8, 7, 9)
        correct = "[Rectangle] ({}) 9/4 - 8/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(4, 4, 4, 4, 4)
        r.update(6, 8, 7, 9, 3, 5)
        r.update(5, 3, 9, 7, 8, 6)
        self.assertEqual("[Rectangle] (5) 7/8 - 3/9", str(r))

    def test_update_args_zero_width(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(6, 0)

    def test_update_args_negatve_width(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0")
        r.update(6, -8)

    def test_update_args_invalidwidth(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width")

    def test_update_args_invalidheight(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(6, 8, "invalid height")

    def test_update_args_negative_height(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegext(ValueError, "height must be > 0"):
            r.update(6, 8, -7)

    def test_update_args_zero_height(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(6, 8, 0)

    def test_update_args_invalidx(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(6, 8, 7, "invalid x")

    def test_update_args_negative_x(self):
        r = Rectagle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(6, 8, 7, -9)

    def test_update_args_invalid_y(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(6, 8, 7, 9, "invalid y")

    def test_update_args_negative_y(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "y must be >=0")
        r.update(6, 8, 7, 9, -3)

    def test_update_args_width_before_height(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaissRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width", "invalid height")

    def test_update_args_width_before_x(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width", 7, "invalid x")

    def test_update_args_width_before_y(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width", 7, 9, "invalid y")

    def test_update_args_x_before_y(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = r.update(6, 8, 7, "invalid x", "invalid y")

    def test_update_args_height_before_x(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(6, 8, "invalid height", "invalid x")

    def test_update_args_height_before_y(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "heigh must be an integer"):
            r.update(6, 8, "invalid height", 9, "invalid y")

class TestRectangle_to_dictionary(unittest.TestCase):
    """testing for the to_dictionary method"""

    def test_to_dictionary_arg(self):
        r = Rectangle(4, 4, 4, 4, 4)
        with self.assetRaises(TypeError)
        r.to_dictionary(1)

    def test_to_dictionary_no_obj_changes(self):
        r1 = Rectangle(9, 8, 7, 6, 5)
        r2 = Rectangle(5, 6, 7, 8, 9)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_output(self):
        r = Rectangle(9, 8, 7, 6, 5)
        correct = {'x': 7, 'y': 6, 'id': 5, 'height': 2, 'width': 9}
        self.assertDictEqual(correct, r.to_dictionary())

class TestRectangle_update_kwargs(unittest.TestCase):
    """testing the update method on kwargs"""

    def test_update_kwargs_one(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=4)
        self.assertEqual("[Rectangle] (4) 5/5 - 5/5", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(width=6, id=4)
        self.assertEqual("[Rectangle] (4) 5/5 - 6/5", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(width=6, height=3, id=4)
        self.assertEqual("[Rectangle] (4) 5/5 - 6/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=4, x=2, height=3, y=7, width=6)
        self.assertEqual("[Rectangle] (4) 2/7 - 6/3", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=4, x=2, height=3, y=7, width=6)
        self.assertEqual("[Rectangle] (4) 2/7 - 6/3", str(r))

    def test_update_kwargs_id_none(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=None)
        correct = "[Rectangle] ({}) 5/5 - 5/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_other(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=None, width=6, height=7)
        correct = "[Rectangle] ({}) 5/5 - 6/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(y=7, id=4, width=6)
        r.update(x=2, width=9, height=4)
        self.assertEqual("[Rectangle] (4) 2/7 - 5/4", str(r))

    def test_update_kwargs_width_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-3)

    def test_update_kwargs_width_zero(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_invlid(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_height_invalid(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-7)

    def test_update_kwargs_height_zero(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_y_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            r.update(y=-2)

    def test_update_kwargs_x_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            r.update(x=-2)

    def test_update_kwargs_x_invalid(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_y_invalid(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_with_some_wrong_keys(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(height=7, id=4, c=12, f=8)
        self.assertEqual("[Rectangle] (4) 5/5 - 5/7", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(d=6, j=8)
        self.assertEqual("[Rectangle] (5) 5/5 - 5/5)", str(r))

    def test_update_args_and_kwargs(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(4, 7, y=4, width=9)
        self.assertEqual("[Rectangle] (4) 5/5b - 5/4", str(r))

if __name__ == "__main__":
    unittest.main()
