# 💲 Simulador de Investimentos

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-%3E=6.0-green.svg)](https://pypi.org/project/PyQt6/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Um simulador de investimentos simples com interface gráfica desenvolvida em **Python** utilizando **PyQt6**. O objetivo é calcular o valor futuro de um investimento com base no valor inicial, taxa de juros anual e número de anos.

---

## 📋 Funcionalidades

- Interface gráfica amigável para entrada de dados.
- Cálculo de valor futuro com juros compostos.
- Tratamento de erros para entradas inválidas.
- Estrutura modular seguindo boas práticas de programação orientada a objetos (POO).

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **PyQt6** para a interface gráfica.
- **unittest** para testes automatizados.

---

## 📂 Estrutura do Projeto

```plaintext
simulador-de-investimentos/
├── main.py                                      # Arquivo principal para executar o programa
├── simulador/                                   # Pacote principal do simulador
│   ├── __init__.py                              # Torna a pasta um pacote Python
│   ├── models/                                  # Contém as classes e lógica de negócios
│   │   ├── __init__.py
│   │   ├── investimento.py
    │   ├── views/                               # Contém a interface gráfica (GUI)
│   │   ├── __init__.py
│   │   ├── simulador_gui.py
│   ├── controllers/                             # Contém a lógica de controle entre a GUI e os modelos
│       ├── __init__.py
│       ├── simulador_controller.py
├── tests/                                       # Contém os testes unitários
│   ├── __init__.py
│   ├── test_investimento.py
├── run_tests.sh                                 # Script para rodar os testes
├── requirements.txt                             # Dependências do projeto
└── README.md                                    # Documentação do projeto
```
---

## 🛠️ Instalação e Execução
Pré-requisitos
Python 3.12 ou superior  
Gerenciador de pacotes pip

Passos

1 - Clone o repositório:
git clone https://github.com/seu-usuario/simulador-de-investimentos.git

2 - Instale as dependências:
pip install -r requirements.txt

3 - Execute o simulador:
python main.py

---

## 🧪 Testes
Para rodar os testes automatizados, utilize o script run_tests.sh:
./run_tests.sh

Ou execute diretamente com o Python:  
export PYTHONPATH=$(pwd)/simulador-de-investimentos
python -m unittest discover simulador-de-investimentos/tests

---

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**. 💡

---

## 📝 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

---

## 📧 Contato
Autor: Cláudio de Lima Tosta

Email: eng-soft-claudio@gmail.com

GitHub: Eng-Soft-Claudio

LinkedIn: claudiodelimatosta

---

## 🌟 Agradecimentos
Python Official Documentation

PyQt6 Documentation

---
