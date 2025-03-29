import unittest
from simulador.models.investimento import Investimento

class TestInvestimento(unittest.TestCase):
    def test_calcular_valor_futuro(self):
        investimento = Investimento(1000, 0.05, 10)
        self.assertAlmostEqual(investimento.calcular_valor_futuro(), 1628.89, places=2)

if __name__ == "__main__":
    unittest.main()