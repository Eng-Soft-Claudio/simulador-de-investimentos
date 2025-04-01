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

**MIT** License

Copyright (c) 2025 Cláudio de Lima Tosta

Permissão é concedida, gratuitamente, a qualquer pessoa que obter uma cópia deste software e dos arquivos de documentação associados (o "Software"), para usar o Software sem restrições, incluindo, sem limitação, os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e para permitir que as pessoas a quem o Software é fornecido faça o mesmo, sujeito às seguintes condições:

O aviso de copyright acima e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O Software é fornecido "no estado em que se encontra", sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando às garantias de comercialização, adequação a um fim específico e não infração. Em nenhum caso os autores ou detentores dos direitos autorais serão responsáveis por qualquer reclamação, dano ou outra responsabilidade, seja em uma ação de contrato, ato ilícito ou outra, decorrente de, fora de ou em conexão com o Software ou o uso ou outros negócios no Software.

---

## 📧 Contato

Email: eng-soft-claudio@gmail.com

LinkedIn: claudiodelimatosta

---

## 🌟 Agradecimentos
Python Official Documentation

PyQt6 Documentation

---
