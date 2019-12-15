"""Test the tag helper."""
from base.tag_helper import TagHelper


def test_GetTags():
    """Test the getTags function."""
    message = "{I am} {A tester} {And} {I} {Test} {Tags}"
    tags = ["I am", "A tester", "And", "I", "Test", "Tags"]

    answer = TagHelper.get_tags(message)

    for tag in tags:
        assert tag in answer


def test_RemoveTags():
    """Test if removeTags returns a tagless text."""
    string = "The test is {not} successfull {at} {all}"

    answer = TagHelper.remove_tags(string)
    assert (answer == "The test is successfull")


def test_getSyntax():
    """Test if the syntax is extracted correctly from a string."""
    string = "I {will} now {test} if {this} works!"
    tags = ["{will}", "{test}", "{this}"]
    result = ["I ", " now ", " if ", " works!"]
    assert TagHelper.get_syntax(string, tags) == result


def test_getTagsContent():
    """Test if the tags are extracted correctly from a string."""
    stringWithTags = "This is a {tag}"
    string = "This is a test."
    answer = {"tag": "test."}
    assert TagHelper.get_tags_content(string, stringWithTags) == answer


def test_replaceTags():
    """Test if the tags are replaced correctly."""
    string = "try {1} replace {2}"
    tags = {"1": "to", "2": "this"}
    answer = "try to replace this"
    assert answer == TagHelper.replace_tags(string, tags)
