class Investimento:
    def __init__(self, valor_inicial: float, taxa_juros: float, anos: int):
        self.valor_inicial = valor_inicial
        self.taxa_juros = taxa_juros
        self.anos = anos

    def calcular_valor_futuro(self) -> float:
        """Calcula o valor futuro do investimento com juros compostos."""
        return self.valor_inicial * ((1 + self.taxa_juros) ** self.anos)