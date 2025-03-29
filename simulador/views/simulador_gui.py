from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
)

class SimuladorGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Simulador de Investimentos")

        layout = QVBoxLayout()

        self.label_valor_inicial = QLabel("Valor Inicial (R$):")
        self.input_valor_inicial = QLineEdit()
        layout.addWidget(self.label_valor_inicial)
        layout.addWidget(self.input_valor_inicial)

        self.label_taxa_juros = QLabel("Taxa de Juros Anual (%):")
        self.input_taxa_juros = QLineEdit()
        layout.addWidget(self.label_taxa_juros)
        layout.addWidget(self.input_taxa_juros)

        self.label_anos = QLabel("Número de Anos:")
        self.input_anos = QLineEdit()
        layout.addWidget(self.label_anos)
        layout.addWidget(self.input_anos)

        self.botao_calcular = QPushButton("Calcular")
        self.botao_calcular.clicked.connect(self.calcular_investimento)
        layout.addWidget(self.botao_calcular)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calcular_investimento(self):
        try:
            valor_inicial = float(self.input_valor_inicial.text())
            taxa_juros = float(self.input_taxa_juros.text()) / 100
            anos = int(self.input_anos.text())
            resultado = self.controller.calcular(valor_inicial, taxa_juros, anos)
            QMessageBox.information(self, "Resultado", f"Valor Futuro: R$ {resultado:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos.")