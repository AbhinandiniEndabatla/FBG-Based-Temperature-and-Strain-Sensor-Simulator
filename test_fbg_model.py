

import unittest

from fbg_model import calculate_wavelength_shift


class TestFBGModel(unittest.TestCase):

    def test_zero_temperature_and_strain(self):
        result = calculate_wavelength_shift(
            1550, 0, 0, 10.3, 1.2
        )

        self.assertEqual(
            result,
            (0.0, 0.0, 0.0, 1550.0)
        )

    def test_temperature_only(self):
        temp, strain, total, new_wl = calculate_wavelength_shift(
            1550, 10, 0, 10.0, 1.2
        )

        self.assertAlmostEqual(temp, 100.0)
        self.assertAlmostEqual(strain, 0.0)
        self.assertAlmostEqual(total, 100.0)
        
        self.assertAlmostEqual(new_wl, 1550.1)

    def test_strain_only(self):
        temp, strain, total, new_wl = calculate_wavelength_shift(
            1550, 0, 100, 10.0, 1.2
        )

        self.assertAlmostEqual(temp, 0.0)
        self.assertAlmostEqual(strain, 120.0)
        self.assertAlmostEqual(total, 120.0)
        self.assertAlmostEqual(new_wl, 1550.12)

    def test_combined_shift(self):
        temp, strain, total, new_wl = calculate_wavelength_shift(
            1550, 10, 100, 10.0, 1.2
        )

        self.assertAlmostEqual(total, temp + strain)
        self.assertAlmostEqual(new_wl, 1550.22)


if __name__ == "__main__":
    unittest.main()
