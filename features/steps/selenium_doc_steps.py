from time import sleep

from behave import given, when, then

from features.page_objects.selenium_doc import SeleniumDoc


@given(u'que estou na pagina inicial da doc do webdriver')
def step_impl(context):
    context.execute_steps(f'Dado que acesso o site do selenium')
    context.selenium_home.clicar_em_doc()
    sleep(2)


@when(u'navego ate Getting Started pela barra lateral')
def step_impl(context):
    context.selenium_doc = SeleniumDoc()
    context.selenium_doc.clica_em_webdriver_na_barra_lateral()
    context.selenium_doc.clica_em_getting_started_na_barra_lateral()
    sleep(3)


@then(u'devo ser encaminhado para o Getting Started')
def step_impl(context):
    pass
