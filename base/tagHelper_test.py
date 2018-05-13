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
