"""Test the tag helper."""
from base import tagHelper


def test_GetTags():
    """Test the getTags function."""
    message = "{I am} {A tester} {And} {I} {Test} {Tags}"
    tags = ["I am", "A tester", "And", "I", "Test", "Tags"]

    answer = tagHelper.getTags(message)

    for tag in tags:
        assert tag in answer


def test_RemoveTags():
    """Test if removeTags returns a tagless text."""
    string = "The test is {not} successfull {at} {all}"

    answer = tagHelper.removeTags(string)
    assert (answer == "The test is successfull")


def test_extractSyntax():
    """Test if the syntax is extracted correctly from a string."""
    string = "I {will} now {test} if {this} works!"
    tags = ["{will}", "{test}", "{this}"]
    result = ["I ", " now ", " if ", " works!"]
    assert tagHelper.extractSyntax(string, tags) == result


def test_extractTags():
    """Test if the tags are extracted correctly from a string."""
    stringWithTags = "This is a {tag}"
    string = "This is a test."
    answer = {"tag": "test."}
    assert tagHelper.extractTags(string, stringWithTags) == answer
