from simulador.models.investimento import Investimento

class SimuladorController:
    def calcular(self, valor_inicial: float, taxa_juros: float, anos: int) -> float:
        investimento = Investimento(valor_inicial, taxa_juros, anos)
        return investimento.calcular_valor_futuro()