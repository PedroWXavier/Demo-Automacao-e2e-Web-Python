from behave import fixture


@fixture
def before_tag1(context):
    print('Before tag1.......')


@fixture
def after_tag1(context):
    print('After tag1.......')


@fixture
def before_tag2(context):
    print('Before tag2.......')


@fixture
def after_tag2(context):
    print('After tag2.......')
