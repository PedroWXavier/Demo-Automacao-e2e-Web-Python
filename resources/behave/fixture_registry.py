from resources.behave.fixtures import before_tag1, after_tag1, before_tag2, after_tag2

fixture_registry_before = {
    "fixture.tag1": before_tag1,
    "fixture.tag2": before_tag2
}

fixture_registry_after = {
    "fixture.tag1": after_tag1,
    "fixture.tag2": after_tag2
}
