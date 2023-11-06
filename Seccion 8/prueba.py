import unittest
import camiba_texto

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "Buen dia"
        resultado = camiba_texto.todo_minusculas(palabra)
        self.assertEqual(resultado, "Buen dia")


if __name__ == '__main__':
    unittest.main()
