import unittest
from polynomial import Polynomial


class PolynomialTestCase(unittest.TestCase):
    def setUp(self):
        self.p0 = Polynomial([0, ])
        self.p1 = Polynomial([1, 2, 3])
        self.p2 = Polynomial([1, -2, 3, -4])
        self.p3 = Polynomial([-1, 0, 2, -3])

    def test_init(self):
        self.assertEqual(self.p1.coeffs, [1, 2, 3])

    def test_init_incorrect_coeffs(self):
        self.assertRaises(TypeError, Polynomial, [1, 'errno'])

    def test_init_empty(self):
        self.assertEqual(self.p0, Polynomial([]))

    def test_init_copy(self):
        self.assertEqual(self.p1, Polynomial(self.p1))

    def test_init_incorrect_arg(self):
        self.assertRaises(TypeError, Polynomial, "errno")

    def test_repr(self):
        self.assertEqual(self.p1.__repr__(), "Polynomial([1, 2, 3])")

    def test_str(self):
        self.assertEqual(self.p3.__str__(), "-x^3+2x-3")

    def test_str2(self):
        self.assertEqual((self.p3 + 5).__str__(), "-x^3+2x+2")

    def test_sum_polynoms(self):
        self.assertEqual(self.p1 + self.p2, Polynomial([1, -1, 5, -1]))

    def test_rsum_polynoms(self):
        self.assertEqual(self.p2 + self.p1, Polynomial([1, -1, 5, -1]))

    def test_sum_error(self):
        self.assertRaises(TypeError, self.p1.__add__, "x")

    def test_sum_number(self):
        self.assertEqual(self.p1 + 10, Polynomial([1, 2, 13]))

    def test_rsum_number(self):
        self.assertEqual(10 + self.p1, Polynomial([1, 2, 13]))

    def test_rsum_error(self):
        self.assertRaises(TypeError, self.p1.__radd__, "x")

    def test_sub_polynoms(self):
        self.assertEqual(self.p1 - self.p2, Polynomial([-1, 3, -1, 7]))

    def test_rsub_polynoms(self):
        self.assertEqual(self.p2 - self.p1, Polynomial([1, -3, 1, -7]))

    def test_sub_number(self):
        self.assertEqual(self.p1 - 10, Polynomial([1, 2, -7]))

    def test_sub_error(self):
        self.assertRaises(TypeError, self.p1.__sub__, "x")

    def test_rsub_number(self):
        self.assertEqual(10 - self.p1, Polynomial([-1, -2, 7]))

    def test_rsub_error(self):
        self.assertRaises(TypeError, self.p1.__rsub__, "x")

    def test_mul_number(self):
        self.assertEqual(self.p1 * 10, Polynomial([10, 20, 30]))

    def test_mul_polynoms(self):
        self.assertEqual(self.p1 * self.p2, Polynomial([1, 0, 2, -4, 1, -12]))

    def test_mul_error(self):
        self.assertRaises(TypeError, self.p1.__mul__, "x")

    def test_rmul_number(self):
        self.assertEqual(10 * self.p1, Polynomial([10, 20, 30]))

    def test_rmul_error(self):
        self.assertRaises(TypeError, self.p1.__rmul__, "x")

    def test_eq(self):
        self.assertEqual(self.p1 == Polynomial([1, 2, 3]), True)

    def test_ne(self):
        self.assertEqual(self.p1 != Polynomial([1, 2, 0]), True)

    def test_lt(self):
        self.assertEqual(self.p1 < self.p2, True)

    def test_le(self):
        self.assertEqual(self.p1 <= self.p2 and self.p1 <= self.p1, True)

    def test_gt(self):
        self.assertEqual(self.p2 > self.p1, True)

    def test_ge(self):
        self.assertEqual(self.p2 >= self.p1 and self.p2 >= self.p2, True)

    def test_eq_false(self):
        self.assertEqual(self.p1 == "x", False)

    def test_ne_error(self):
        self.assertRaises(TypeError, self.p1.__ne__, "x")

    def test_lt_error(self):
        self.assertRaises(TypeError, self.p1.__lt__, "x")

    def test_le_error(self):
        self.assertRaises(TypeError, self.p1.__le__, "x")

    def test_gt_error(self):
        self.assertRaises(TypeError, self.p2.__gt__, "x")

    def test_ge_error(self):
        self.assertRaises(TypeError, self.p2.__ge__, "x")


if __name__ == '__main__':
    unittest.main()
