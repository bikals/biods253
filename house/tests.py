#!/usr/bin/env python3

from PIL import Image
import matplotlib.testing.compare as mpcompare
import unittest
import housedraw
import tempfile
import os.path
import svg_turtle
import inspect

from affine import Affine


from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

CANVAS_SIZE = (500, 500)

class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename, override_tmpdir=None):
        ''' compares the current canvas to an expected file.
        Returns None if and only if the files are identical.

        If override_tmpdir is set, use that directory for temporary files
        (useful for generating known good testdata images.
        '''

        TOLERANCE = 3.0  # somewhere between 0 and 255, higher is more lax.

        with tempfile.TemporaryDirectory() as tmp_dirname:
            calling_function = inspect.stack()[1][3]
            tmp_dirname = tmp_dirname if not override_tmpdir else override_tmpdir

            actual_svg = os.path.join(tmp_dirname, '%s.svg' % calling_function)
            actual_png = os.path.join(tmp_dirname, '%s.png' % calling_function)
            self._turtle.save_as(actual_svg)

            # canvas generates a svg file, but we have to convert it to a png in
            # order to compare it using matplotlib's library
            drawing = svg2rlg(actual_svg)
            renderPM.drawToFile(drawing, actual_png, fmt="PNG")
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)

    def setUp(self):
        # this is run before every test
        self._turtle = svg_turtle.SvgTurtle(*CANVAS_SIZE)
        self._drawer = housedraw.BasicDrawing(self._turtle)
        self._turtle.speed(0)

    def test_circle(self):
        self._drawer.draw_circle(20, 20, 20, fill = False)

        # compare this 20,20,20 turtle against the well-known turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/circle-20.png'))

    def test_circle_fail(self):
        # test that a badly sized circle fails to compare as equal
        self._drawer.draw_circle(20, 20, 29, fill = False)

        # this should not match, therefore should be not none.
        self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='testdata/circle-20.png'))

    def test_line(self):
        self._drawer.draw_line(20, 20, 20, 60)

        # compare this line against a line on the turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/line-20.png'))



    def test_translated_line(self):
        self._drawer.set_affine(Affine.translation(-20, -20))
        self._drawer.draw_line(20, 20, 20, 60)
        # compare this line against a line on the turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/test_translated_line.png'))

    def test_rotated_line(self):
        self._drawer.set_affine(Affine.rotation(45))
        self._drawer.draw_line(20, 20, 20, 60)
        # compare this line against a line on the turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/test_rotated_line.png'))


    def test_rotated_scaled_translated_line(self):
        self._drawer.set_affine(Affine.rotation(45) * Affine.scale(5.0) * Affine.translation(0,-50))
        self._drawer.draw_line(20, 20, 20, 60)
        # compare this line against a line on the turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/test_rotated_scaled_translated_line.png'))

    def test_rotated_scaled_translated_circle(self):
        self._drawer.set_affine(Affine.rotation(45) * Affine.scale(5.0) * Affine.translation(-50,-50))
        self._drawer.draw_circle(20,20,20)
        # compare this line against a line on the turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/test_rotated_scaled_translated_circle.png'))


    def test_line_fail(self):
        # test that a badly sized line fails to compare as equal
        self._drawer.draw_line(20, 20, 20, 80)

        # this should not match, therefore should be not none.
        self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='testdata/line-20.png'))

if __name__ == '__main__':
    unittest.main()