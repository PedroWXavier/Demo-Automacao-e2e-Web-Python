from behave.fixture import use_fixture_by_tag

from main import debug
from resources.behave.fixture_registry import fixture_registry_before, fixture_registry_after
from resources.commons.driver import Driver


def before_all(context):
    if debug:
        print('before all')


def after_all(context):
    if debug:
        print('after all')


def before_feature(context, feature):
    if debug:
        print(f'before feature: {feature}')


def after_feature(context, feature):
    if debug:
        print(f'after feature: {feature}')


def before_tag(context, tag):
    if debug:
        print(f'before tag: {tag}')

    if tag.startswith("fixture.") and tag in fixture_registry_before:
        print(tag + ":")
        use_fixture_by_tag(tag, context, fixture_registry_before)


def after_tag(context, tag):
    if debug:
        print(f'after tag: {tag}')

    if tag.startswith("fixture.") and tag in fixture_registry_after:
        print(tag + ":")
        use_fixture_by_tag(tag, context, fixture_registry_after)


def before_scenario(context, scenario):
    print('iniciando driver')
    Driver.get_driver()
    if debug:
        print(f'before scenario: {scenario}')


def after_scenario(context, scenario):
    print('finalizando driver')
    Driver.quit()
    if debug:
        print(f'after scenario: {scenario}')


def before_step(context, step):
    if debug:
        print(f'before step: {step}')


def after_step(context, step):
    if debug:
        print(f'after step: {step}')
