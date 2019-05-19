
from unittest import TestCase, mock, main
from calc import exp


class TestExp(TestCase):
    def test_exp_add(self):
        with mock.patch('calc.add', return_value=3) as mocked:
            resultado = exp(1, 2, 3)

        mocked.assert_called()
        mocked.assert_called_with(1, 2)
        self.assertEqual(resultado, 0)

    def test_exp_sub(self):
        with mock.patch('calc.sub', return_value=0) as mocked:
            resultado = exp(1, 2, 3)

        mocked.assert_called()
        mocked.assert_called_with(3, 3)
        self.assertEqual(resultado, 0)

    @mock.patch('calc.sub', return_value=0)
    def test_exp_com_decorador(self, mocked):
        resultado = exp(1, 2, 3)

        mocked.assert_called()
        mocked.assert_called_with(3, 3)
        self.assertEqual(resultado, 0)

    @mock.patch('calc.sub', return_value=0)
    @mock.patch('calc.add', return_value=3)
    def test_exp_com_tudo_mockado(self, soma_mock, sub_mock):
        resultado = exp(1, 2, 3)

        sub_mock.assert_called()
        sub_mock.assert_called_with(3, 3)
        self.assertEqual(resultado, 0)

        soma_mock.assert_called()
        soma_mock.assert_called_with(1, 2)


main()
