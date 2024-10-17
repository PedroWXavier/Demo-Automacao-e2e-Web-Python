from behave import given, when, then


@given(u'que carrego as informacoes do usuario')
def step_impl(context):
    pass


@when(u'realizo o login')
def step_impl(context):
    pass


@then(u'devo validar o login realizado')
def step_impl(context):
    pass


@given(u'que carrego as informacoes do usuario "{tipo_usuario}"')
def step_impl(context, tipo_usuario):
    print(f'Tipo de usuario recebido no Given: {tipo_usuario}')


@then(u'devo validar o login realizado do usuario "{tipo_usuario}" com o cpf "{cpf}"')
def step_impl(context, tipo_usuario, cpf):
    print(f'Tipo de usuario recebido no Then: {tipo_usuario} e cpf {cpf}')
