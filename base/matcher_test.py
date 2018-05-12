"""Test matcher class."""
from base import matcher


def test_simple_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger without pre or post
    filters, the message sent is expected to match.
    """
    botName = "test"
    candidate = {'trigger': 'botname'}

    message = botName + " noise"
    assert matcher.Matcher.matches(candidate, message, botName)

    message = botName + "sss"
    assert not matcher.Matcher.matches(candidate, message, botName)


def test_pre_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger with pre filter and no
    post filter, the message sent is expected to match.
    """
    botName = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': 'botname', 'trigger_pre': tokens}

    for token in tokens:
        message = token + " noise " + botName
        assert matcher.Matcher.matches(candidate, message, botName)

    assert not matcher.Matcher.matches(candidate, botName, botName)


def test_post_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger with no pre filter and
    a post filter, the message sent is expected to match.
    """
    botName = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': 'botname', 'trigger_extra': tokens}

    for token in tokens:
        message = botName + " noise " + token
        assert matcher.Matcher.matches(candidate, message, botName)

    assert not matcher.Matcher.matches(candidate, botName, botName)


def test_full_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger with no pre filter and
    a post filter, the message sent is expected to match.
    """
    botName = "test"
    tokens = ['hi', 'hello']
    candidate = {'trigger': 'botname', 'trigger_extra': tokens,
                 'trigger_pre': tokens}

    for pre in tokens:
        for post in tokens:
            message = pre + " noise " + botName + " noise " + post
            assert matcher.Matcher.matches(candidate, message, botName)

    message = botName
    assert not matcher.Matcher.matches(candidate, message, botName)


def test_bad_command_ignore():
    """Test if the matcher ignores a wrongly written /command trigger.

    The matches function is expected to ignore triggers like: "/comm and.
    """
    botName = "test"
    trigger = "/comm and"
    candidate = {'trigger': trigger}
    message = trigger
    assert not matcher.Matcher.matches(candidate, message, botName)


def test_simple_command_match():
    """Test the matches function on a /command trigger, with the right message.

    The matches function is tested on a /command trigger, without pre or post
    filters, the message sent is expected to match.
    """
    botName = "test"
    trigger = "/command"
    candidate = {'trigger': trigger}

    message = trigger + " do_stuff right_now"
    assert matcher.Matcher.matches(candidate, message, botName)

    message = trigger + "sss"
    assert not matcher.Matcher.matches(candidate, message, botName)


def test_pre_command_ignored():
    """Test the matches function on a /command trigger, with the right message.

    The matches function is tested on a /command trigger, with a pre filter and
    no post filters, the message sent is expected to be ignored since a command
    is supposed to be the start of the message and not be contained in a
    sentence.
    """
    botName = "test"
    trigger = "/command"
    tokens = ['hi', 'hello']
    candidate = {'trigger': trigger, 'trigger_pre': tokens}
    for token in tokens:
        message = token + " noise " + trigger
        assert not matcher.Matcher.matches(candidate, message, botName)


def test_post_command_matches():
    """Test the matches function on a /command trigger, with the right message.

    The matches function is tested on a /command trigger, with no pre filters
    and a post filter, the message sent is expected to match.
    """
    botName = "test"
    trigger = "/command"
    tokens = ['hi', 'hello']
    candidate = {'trigger': trigger, 'trigger_extra': tokens}
    for token in tokens:
        message = trigger + " noise " + token
        assert matcher.Matcher.matches(candidate, message, botName)

        message = trigger + token
        assert not matcher.Matcher.matches(candidate, message, botName)


def test_full_command_ignored():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a /command trigger, with a pre filter and
    a post filter, the message sent is expected to be ignored since a command
    is supposed to be the start of the message and not be contained in a
    sentence.
    """
    botName = "test"
    trigger = "/command"
    tokens = ['hi', 'hello']
    candidate = {'trigger': trigger, 'trigger_extra': tokens,
                 'trigger_pre': tokens}

    for pre in tokens:
        for post in tokens:
            message = pre + " noise " + trigger + " noise " + post
            assert not matcher.Matcher.matches(candidate, message, botName)


def test_simple_empty_match():
    """Test the matches function on a '' trigger, without filters.

    The matches function is tested on a '' trigger, without pre or post
    filters, the message sent is expected to match.
    """
    botName = "test"
    candidate = {'trigger': ''}
    message = "any input should trigger this."
    assert (matcher.Matcher.matches(candidate, message, botName))


def test_pre_empty_matches():
    """Test the matches function on a '' trigger, with the right message.

    The matches function is tested on a botname trigger with pre filter and no
    post filter, the message sent is expected to match.
    """
    botName = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': '', 'trigger_pre': tokens}

    for token in tokens:
        message = token + " noise "
        assert matcher.Matcher.matches(candidate, message, botName)

    assert not matcher.Matcher.matches(candidate, botName, botName)


def test_post_empty_matches():
    """Test the matches function on a '' trigger, with the right message.

    The matches function is tested on a botname trigger with no pre filters
    and a post filter, the message sent is expected to match.
    """
    botName = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': '', 'trigger_extra': tokens}

    for token in tokens:
        message = token + " noise "
        assert matcher.Matcher.matches(candidate, message, botName)

    assert not matcher.Matcher.matches(candidate, botName, botName)


def test_full_empty_matches():
    """Test the matches function on a '' trigger, with the right message.

    The matches function is tested on a '' trigger with pre filter and
    post filter, the message sent is expected to match.
    """
    botName = "test"
    tokens = ['hi', 'hello']
    candidate = {'trigger': '', 'trigger_extra': tokens,
                 'trigger_pre': tokens}

    for pre in tokens:
        for post in tokens:
            message = pre + " noise " + " noise " + post
            assert matcher.Matcher.matches(candidate, message, botName)

    message = botName
    assert not matcher.Matcher.matches(candidate, message, botName)


def test_bad_trigger_ignored():
    """Test the matches function on a not supported trigger.

    The matches function is tested on a not supported trigger (not in: ['',
    'botname','/command']), the message sent is expected NOT to match.
    """
    botName = "test"
    candidate = {'trigger': 'test'}
    message = "test"
    assert not (matcher.Matcher.matches(candidate, message, botName))
