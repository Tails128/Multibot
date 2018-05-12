"""Test matcher class."""
from base import matcher


def test_simple_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger without pre or post
    filters, the message sent is expected to match.
    """
    botName = "test"
    candidate = {'trigger': 'botname'}
    message = botName
    assert(matcher.Matcher.matches(candidate, message, botName))


def test_simple_botname_does_not_match():
    """Test the matches function on a botname trigger, with the wrong message.

    The matches function is tested on a botname trigger without pre or post
    filters, the message sent is expected NOT to match.
    """
    botName = "test"
    candidate = {'trigger': 'botname'}
    message = botName + "ssss"
    assert not (matcher.Matcher.matches(candidate, message, botName))


def test_bad_command_ignore():
    """Test if the matcher ignores a wrongly written /command trigger.

    The matches function is expected to ignore triggers like: "/comm and.
    """
    botName = "test"
    trigger = "/comm and"
    candidate = {'trigger': trigger}
    message = trigger
    assert not (matcher.Matcher.matches(candidate, message, botName))


def test_simple_command_match():
    """Test the matches function on a /command trigger, with the right message.

    The matches function is tested on a /command trigger, without pre or post
    filters, the message sent is expected to match.
    """
    botName = "test"
    trigger = "/command"
    candidate = {'trigger': trigger}
    message = trigger + " do_stuff right_now"
    assert (matcher.Matcher.matches(candidate, message, botName))


def test_simple_command_not_match():
    """Test the matches function on a /command trigger, with the wrong message.

    The matches function is tested on a /command trigger, without pre or post
    filters, the message sent is expected NOT to match.
    """
    botName = "test"
    trigger = "/command"
    candidate = {'trigger': trigger}
    message = trigger + "_this_part_of_the_command"
    assert not (matcher.Matcher.matches(candidate, message, botName))


def test_simple_empty_match():
    """Test the matches function on a '' trigger, without filters.

    The matches function is tested on a '' trigger, without pre or post
    filters, the message sent is expected to match.
    """
    botName = "test"
    candidate = {'trigger': ''}
    message = "any input should trigger this."
    assert (matcher.Matcher.matches(candidate, message, botName))


def test_bad_trigger_ignored():
    """Test the matches function on a not supported trigger.

    The matches function is tested on a not supported trigger (not in: ['',
    'botname','/command']), the message sent is expected NOT to match.
    """
    botName = "test"
    candidate = {'trigger': 'test'}
    message = "test"
    assert not (matcher.Matcher.matches(candidate, message, botName))
