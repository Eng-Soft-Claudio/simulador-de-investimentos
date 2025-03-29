from PyQt6.QtWidgets import QApplication
from simulador.controllers.simulador_controller import SimuladorController
from simulador.views.simulador_gui import SimuladorGUI

if __name__ == "__main__":
    app = QApplication([])
    controller = SimuladorController()
    gui = SimuladorGUI(controller)
    gui.show()
    app.exec()