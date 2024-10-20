#language: pt

Funcionalidade: Selenium

  Cenario: Acessar site do selenium
    Dado que acesso o site do selenium
    Entao devo validar que estou na pagina inicial


  Cenario: Acessar Getting Started
    Dado que estou na pagina inicial da doc do webdriver
    Quando navego ate Getting Started pela barra lateral
    Entao devo ser encaminhado para o Getting Started

