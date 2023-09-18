#!/usr/bin/python3

"""unittests for square.py"""
from models.square import Square
from models.base import Base
import unittest
import sys
import io

class TestSquare_size(unittest.TestCase):
    """tests the width attribute"""
    
    def test_size_none(self):
        with self.assertRaisesRgex(TypeError, "width must be an integer"):
            Square(none, 8)

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(3), 3)

    def test_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string", 3)

    def test_size_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 3)

    def test_size_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"i": 4, "j": 5}, 5)

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((3, 8, 9), 3)

    def test_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({3, 8, 9}, 3)

    def test_size_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({3, 8, 9}), 3)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([3, 8, 9], 3)

    def test_size_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(3), 4)

    def test_size_infinity(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 3)

    def test_size_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'bytes', 5)

    def test_size_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'array'), 5)

    def test_size_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 3)

    def test_size_memview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'memview'), 4)

    def test_size_negative(self):
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            Square(-3, 5)

    def test_size_zero(self):
        with self.assertRaisesRegex(TyepError, "width must be > 0"):
            Square(0, 5)

class TestSquare_instance(unittest.TestCase):
    """Tests for instantantation"""

    def test_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_base(self):
        self.assertInstance(Square(3, 6), Base)

    def test_rectangle(self):
        self.assertInstance(Square(5), Square)

    def test_single(self):
        s1 = Square(3)
        s2= Square(5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_twoargs(self):
        s1 = Square(5, 8)
        s2 = Square(4, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_threeargs(self):
        s1 = Square(3, 4, 5)
        s2 = Square(4, 5, 6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(3, 4, 5, 6, 7).id)

    def test_more(self):
        with self.assertRaises(TypeError):
            Square(2, 4, 1, 6, 5)

    def test_size_setter(self):
        s = Square(9, 8, 7, 6)
        s.size = 5
        self.assertEqual(5, s.size)

    def test_size_getter(self):
        self.assertEqual(6, Square(9, 8, 7, 6).size)

    def test_size_pvt(self):
        with self.assertRaises(AttributeError):
            print(Square(9, 8, 7, 6).__size)

    def test_width(self):
        with self.assertRaiaes(AttributeError):
            print(Square(8, 4, 7, 9).__width)

    def test_x(self):
        with self.assertRaises(AttributeError):
            print(Square(8, 4, 7, 9).__x)

    def test_height(self):
        with self.assertRaises(AttributeError):
            print(Square(8, 4, 7, 9).__height)

    def test_y(self):
        with self.assertRaises(AttributeError):
            print(Square(3, 8, 4, 7, 9).__y)

    def test_widthgetter(self):
        r = Square(8, 4, 7, 9)
        self.assertEqual(5, r.width)

    def test_xgetter(self):
        r = Square(8, 4, 7, 9)
        self.assertEqual(5, r.x)

    def test_heightgetter(self):
        r = Square(8, 4, 7, 9)
        self.assertEqual(5, r.height)

    def test_ygetter(self):
        r = Square(8, 4, 7, 9)
        self.assertEqual(5, r.y)

    def test_ysetter(self):
        r = Square(8, 4, 7, 9)
        r.y = 5
        self.assertEqual(5, r.y)

    def test_xsetter(self):
        r = Square(8, 4, 7, 9)
        r.x = 5
        self.assertEqual(5, r.x)

    def test_widthsetter(self):
        r = Square(8, 4, 7, 9)
        r.width = 5
        self.assertEqual(5, r.width)

    def test_heightsetter(self):
        r = Square(8, 4, 7, 9)
        r.height = 5
        self.assertEqual(5, r.height)

class TestSquare_x(unittest.TestCase):
    """test for the x attribute"""
    
    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 5, None)

    def test_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, complex(4))

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, "string")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, 5.5)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, [3, 4])

    def test_x_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, {'c': 2, 'd': 5})

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, {3, 4, 5})

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, (3, 4, 5))

    def test_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, frozenset({3, 4, 5}))


    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, 4, -3)

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, b'bytes')

    def test_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, bytearray(b'bytearray'))

    def test_x_memview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, memoryview(b'memview'))

    def test_x_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, True)

    def test_x_infinity(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Recatngle(3, 4, float('inf'))

    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 4, float('nan'))

class TestSquare_y(unittest.TestCase):
    """test for the y attribute"""

    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, float('nan'))

    def test_y_infinity(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, float('inf'))

    def test_y_boolean(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, True)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, "string")

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, [3, 4])

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, (3, 4))

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, {3, 4})

    def test_y_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, {'a': 2, 'b': 3})

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, frozenset({3, 4}))

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, 4.3)

    def test_y_None(self):
        with seslf.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, None)

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, range(3))

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 4, 5, -4)

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, b'bytes')

    def test_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, bytearray(b'bytearray'))


    def test_y_memview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5, memoryview(b'memview'))

class TestSquare_area(self):
    """tests for the area of square"""

    def test_area_update_attr(self):
        r = Square(5, 4, 6, 2)
        r.size = 9
        self.assertEqual(72, r.area())

    def test_area_small(self):
        r = Square(3, 5, 4, 6, 2)
        self.assertEqual(15, r.area())

    def test_area_large(self):
        r = square(999999, 999999, 1, 2, 1)
        self.assertEqual(999998000001, r.area())

    def test_area_single_arg(self):
        r = Square(3, 5, 4, 6, 2)
        with self.assertRaises(TypeError):
            r.area(1)

class TestSquare_initialization_order(unittest.TestCase):
    """test for order of initialization"""


    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid width", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 3, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "invalid x", "invalid y")


class TestSquare_to_stdout(unittest.TestCase):
    """testing how square is displayed to stdout"""

    @staticmethod
    def capture_stdout(sq, method):
        """returns printed text to stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        r = Square(4)
        capture = TestSquare_to_stdout.capture_stdout(r, "display")
        correct = "[Square] ({}) 0/0 - 4\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        r = Square(4, 4)
        correct = "[Square] ({}) 4/0 - 4".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x_y_id(self):
        r = Square(4, 3, 5, 1)
        self.assertEqual("[Square] (1) 3/5 - 4", str(r))

    def test_str_method_size_x_y(self):
        r = Square(3, 5, 2)
        correct = "[Square] ({}) 5/2 - 3".format(r.id)
        self.assertEqual(correct, str(r))

    def test_display_single_arg(self):
        r = Square(4, 3, 5, 2)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestSquare_Update_args(unittest.TestCase):
    """test the update method"""

    def test_update_zero_args(self):
        r = Square(4, 4, 4, 4)
        r.update()
        self.assertEqual("[Square] (4) 4/4 - 4", str(r))

    def test_update_one_arg(self):
        r = Square(4, 4, 4, 4)
        r.update(6)
        self.assertEqual("[Square] (6) 4/4 - 4", str(r))

    def test_update_two_args(self):
        r = Square(4, 4, 4, 4)
        r.update(6, 8)
        self.assertEqual("[Square] (6) 4/4 - 8", str(r))

    def test_update_args_three(self):
        r = Square(4, 4, 4,, 4)
        r.update(6, 8, 7)
        self.assertEqual("[Square] (6) 7/4 - 8", str(r))

    def test_update_args_four(self):
        r =  Square(4, 4, 4, 4)
        r.update(6, 8, 7, 9)
        self.assertEqual("[Square] (6) 7/9 - 8", str(r))

    def test_update_args_more(self):
        r = Square(4, 4, 4, 4)
        r.update(6, 8, 7, 9, 3)
        self.assertEqual("[Square] (6) 7/9 - 8", str(r))

    def test_update_args_None(self):
        r = Square(4, 4, 4, 4)
        r.update(None)
        correct = "[Square] ({}) 4/4 - 4".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_and_other(self):
        r =  Square(4, 4, 4, 4)
        r.update(None, 7, 9)
        correct = "[Square] ({}) 9/4 - 7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Square(4, 4, 4, 4)
        r.update(7, 9, 3, 5)
        r.update(9, 7, 8, 6)
        self.assertEqual("[Square] (5) 7/8 - 9", str(r))

    def test_update_args_zero_size(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(6, 0)

    def test_update_args_negatve_size(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0")
        r.update(6, -8)

    def test_update_args_invalid_size(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width")

    def test_update_args_invalidx(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(6, 8, 7, "invalid x")

    def test_update_args_negative_x(self):
        r = Rectagle(4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(6, 8, 7, -9)

    def test_update_args_invalid_y(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(8, 7, 9, "invalid y")

    def test_update_args_negative_y(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "y must be >=0")
        r.update(8, 7, 9, -3)

    def test_update_args_width_before_height(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaissRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width", "invalid height")

    def test_update_args_width_before_x(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width", 7, "invalid x")

    def test_update_args_width_before_y(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(6, "invalid width", 7, 9, "invalid y")

    def test_update_args_x_before_y(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = r.update(8, 7, "invalid x", "invalid y")

    def test_update_args_height_before_x(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(6, 8, "invalid height", "invalid x")

    def test_update_args_height_before_y(self):
        r = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(TypeError, "heigh must be an integer"):
            r.update(6, 8, "invalid height", 9, "invalid y")

class TestSquare_to_dictionary(unittest.TestCase):
    """testing for the to_dictionary method"""

    def test_to_dictionary_arg(self):
        r = Square(4, 4, 4, 4)
        with self.assetRaises(TypeError)
        r.to_dictionary(1)

    def test_to_dictionary_no_obj_changes(self):
        s1 = Square(9, 8, 7, 6)
        s2 = Square(5, 6, 7, 8)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_output(self):
        r = Square(9, 8, 7, 6)
        correct = {'x': 7, 'y': 6, 'id': 5, 'width': 9}
        self.assertDictEqual(correct, r.to_dictionary())

class TestSquare_update_kwargs(unittest.TestCase):
    """testing the update method on kwargs"""

    def test_update_kwargs_one(self):
        r = Square(5, 5, 5, 5)
        r.update(id=4)
        self.assertEqual("[Square] (4) 5/5 - 5/5", str(r))

    def test_update_kwargs_two(self):
        r = Square(5, 5, 5, 5)
        r.update(size=6, id=4)
        self.assertEqual("[Square] (4) 5/5 - 6", str(r))

    def test_update_kwargs_three(self):
        r = Square(5, 5, 5, 5)
        r.update(size=6, x=3, id=4)
        self.assertEqual("[Square] (4) 3/5 - 6", str(r))

    def test_update_kwargs_four(self):
        r = Square(5, 5, 5, 5)
        r.update(id=4, x=2,  y=7, size=6)
        self.assertEqual("[Square] (4) 2/7 - 6", str(r))

    def test_update_kwargs_id_none(self):
        r = Square(5, 5, 5, 5)
        r.update(id=None)
        correct = "[Square] ({}) 5/5 - 5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_other(self):
        r = Square(5, 5, 5, 5)
        r.update(id=None, size=6)
        correct = "[Square] ({}) 5/5 - 6".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Square(5, 5, 5, 5)
        r.update(y=7, id=4, size=6)
        r.update(x=2, size=9)
        self.assertEqual("[Square] (4) 2/7 - 6", str(r))

    def test_update_kwargs_size_negative(self):
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(size=-3)

    def test_update_kwargs_size_zero(self):
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(sie=0)

    def test_update_kwargs_size_invlid(self):
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(size="invalid")

    def test_update_kwargs_y_negative(self):
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            r.update(y=-2)

    def test_update_kwargs_x_negative(self):
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            r.update(x=-2)

    def test_update_kwargs_x_invalid(self):
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_y_invalid(self):
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_with_some_wrong_keys(self):
        r = Square(5, 5, 5, 5)
        r.update(height=7, id=4, c=12, f=8)
        self.assertEqual("[Square] (4) 5/5 - 5", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Square(5, 5, 5, 5)
        r.update(d=6, j=8)
        self.assertEqual("[Square] (5) 5/5 - 5)", str(r))

    def test_update_args_and_kwargs(self):
        r = Square(5, 5, 5, 5)
        r.update(4, 7, y=4)
        self.assertEqual("[Square] (4) 5/5b - 7", str(r))

if __name__ == "__main__":
    unittest.main()
