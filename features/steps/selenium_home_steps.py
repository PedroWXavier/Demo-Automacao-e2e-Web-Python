from behave import given, when, then

from features.page_objects.selenium_home import SeleniumHome


@given(u'que acesso o site do selenium')
def step_impl(context):
    context.selenium_home = SeleniumHome()
    context.selenium_home.ir_para_selenium_home_page()


@then(u'devo validar que estou na pagina inicial')
def step_impl(context):
    assert context.selenium_home.verificar_texto_na_home()

