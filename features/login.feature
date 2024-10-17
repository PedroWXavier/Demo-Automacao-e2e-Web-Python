#language: pt

Funcionalidade: Login

  @fixture.tag1
  @fixture.tag2
  Cenario: Realizar login
    Dado que carrego as informacoes do usuario
    Quando realizo o login
    Entao devo validar o login realizado


  Cenario: Realizar login
    Dado que carrego as informacoes do usuario "Pessoa_Fisica"
    Quando realizo o login
    Entao devo validar o login realizado


  Esquema do Cenario: Realizar login com <tipo_usuario>
    Dado que carrego as informacoes do usuario "<tipo_usuario>"
    Quando realizo o login
    Entao devo validar o login realizado do usuario "<tipo_usuario>" com o cpf "<cpf>"

    Exemplos:
      | tipo_usuario    | cpf      |
      | Pessoa_Fisica   | 00000000 |
      | Pessoa_Juridica | 12312312 |
