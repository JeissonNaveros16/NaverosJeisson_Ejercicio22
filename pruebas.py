# Referencias http://katyhuff.github.io/python-testing/
# https://docs.python.org/2/library/unittest.html

import unittest
import complejo
import math

class TestComplejo(unittest.TestCase):
    def test_conjugado(self):
        c = complejo.Complejo(2.0,5.0)
        c.conjugado()
        self.assertEqual(c.imaginario, -5.0)

        c = complejo.Complejo(2.0,-2.8)
        c.conjugado()
        self.assertEqual(c.imaginario, 2.8)

    def test_norma(self):
        c = complejo.Complejo(0,1.0)
        c.calcula_norma()
        self.assertEqual(c.norma, 1.0)
        c = complejo.Complejo(1.0,0.0)
        c.calcula_norma()
        self.assertEqual(c.norma, 1.0)

        c = complejo.Complejo(5.0,5.0)
        c.calcula_norma()
        self.assertAlmostEqual(c.norma, math.sqrt(50.0))

    def test_pow(self):
        c = complejo.Complejo(0, 1.0)
        d = c.pow(2)
        self.assertAlmostEqual(d.real,-1.0)
        self.assertAlmostEqual(d.imaginario,0.0)

        c = complejo.Complejo(1.0, 1.0)
        d = c.pow(6)
        self.assertAlmostEqual(d.real,0.0)
        self.assertAlmostEqual(d.imaginario,-8.0)
    
    def test_multiplicacion(self):
        b = complejo.Complejo(8, 6)
        a = complejo.Complejo(2, 2)
        a.multiplicacion(b)
        self.assertEqual(a.real, 4)
        self.assertEqual(a.imaginario, 28)
        
        b = complejo.Complejo(0, 1)
        a = complejo.Complejo(0, 1)
        a.multiplicacion(b)
        self.assertEqual(a.real, -1)
        self.assertEqual(a.imaginario, 0)
        
        b = complejo.Complejo(12, 3)
        a = complejo.Complejo(4, 5)
        a.multiplicacion(b)
        self.assertEqual(a.real, 33)
        self.assertEqual(a.imaginario, 72)


if __name__ == '__main__':
    unittest.main()
    
# este archivo se debe utilizar como 'python -m unittest -v pruebas'
