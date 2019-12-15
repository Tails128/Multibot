"""Test matcher class."""
from base.matcher import Matcher


def test_simple_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger without pre or post
    filters, the message sent is expected to match.
    """
    bot_name = "test"
    candidate = {'trigger': 'botname'}

    message = bot_name + " noise"
    assert Matcher.matches(candidate, message, bot_name)

    message = bot_name + "sss"
    assert not Matcher.matches(candidate, message, bot_name)


def test_pre_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger with pre filter and no
    post filter, the message sent is expected to match.
    """
    bot_name = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': 'botname', 'trigger_pre': tokens}

    for token in tokens:
        message = token + " noise " + bot_name
        assert Matcher.matches(candidate, message, bot_name)

    assert not Matcher.matches(candidate, bot_name, bot_name)


def test_post_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger with no pre filter and
    a post filter, the message sent is expected to match.
    """
    bot_name = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': 'botname', 'trigger_extra': tokens}

    for token in tokens:
        message = bot_name + " noise " + token
        assert Matcher.matches(candidate, message, bot_name)

    assert not Matcher.matches(candidate, bot_name, bot_name)


def test_full_botname_matches():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a botname trigger with no pre filter and
    a post filter, the message sent is expected to match.
    """
    bot_name = "test"
    tokens = ['hi', 'hello']
    candidate = {'trigger': 'botname', 'trigger_extra': tokens,
                 'trigger_pre': tokens}

    for pre in tokens:
        for post in tokens:
            message = pre + " noise " + bot_name + " noise " + post
            assert Matcher.matches(candidate, message, bot_name)

    message = bot_name
    assert not Matcher.matches(candidate, message, bot_name)


def test_bad_command_ignore():
    """Test if the matcher ignores a wrongly written /command trigger.

    The matches function is expected to ignore triggers like: "/comm and.
    """
    bot_name = "test"
    trigger = "/comm and"
    candidate = {'trigger': trigger}
    message = trigger
    assert not Matcher.matches(candidate, message, bot_name)


def test_simple_command_match():
    """Test the matches function on a /command trigger, with the right message.

    The matches function is tested on a /command trigger, without pre or post
    filters, the message sent is expected to match.
    """
    bot_name = "test"
    trigger = "/command"
    candidate = {'trigger': trigger}

    message = trigger + " do_stuff right_now"
    assert Matcher.matches(candidate, message, bot_name)

    message = trigger + "sss"
    assert not Matcher.matches(candidate, message, bot_name)


def test_pre_command_ignored():
    """Test the matches function on a /command trigger, with the right message.

    The matches function is tested on a /command trigger, with a pre filter and
    no post filters, the message sent is expected to be ignored since a command
    is supposed to be the start of the message and not be contained in a
    sentence.
    """
    bot_name = "test"
    trigger = "/command"
    tokens = ['hi', 'hello']
    candidate = {'trigger': trigger, 'trigger_pre': tokens}
    for token in tokens:
        message = token + " noise " + trigger
        assert not Matcher.matches(candidate, message, bot_name)


def test_post_command_matches():
    """Test the matches function on a /command trigger, with the right message.

    The matches function is tested on a /command trigger, with no pre filters
    and a post filter, the message sent is expected to match.
    """
    bot_name = "test"
    trigger = "/command"
    tokens = ['hi', 'hello']
    candidate = {'trigger': trigger, 'trigger_extra': tokens}
    for token in tokens:
        message = trigger + " noise " + token
        assert Matcher.matches(candidate, message, bot_name)

        message = trigger + token
        assert not Matcher.matches(candidate, message, bot_name)


def test_full_command_ignored():
    """Test the matches function on a botname trigger, with the right message.

    The matches function is tested on a /command trigger, with a pre filter and
    a post filter, the message sent is expected to be ignored since a command
    is supposed to be the start of the message and not be contained in a
    sentence.
    """
    bot_name = "test"
    trigger = "/command"
    tokens = ['hi', 'hello']
    candidate = {'trigger': trigger, 'trigger_extra': tokens,
                 'trigger_pre': tokens}

    for pre in tokens:
        for post in tokens:
            message = pre + " noise " + trigger + " noise " + post
            assert not Matcher.matches(candidate, message, bot_name)


def test_simple_empty_match():
    """Test the matches function on a '' trigger, without filters.

    The matches function is tested on a '' trigger, without pre or post
    filters, the message sent is expected to match.
    """
    bot_name = "test"
    candidate = {'trigger': ''}
    message = "any input should trigger this."
    assert Matcher.matches(candidate, message, bot_name)


def test_pre_empty_matches():
    """Test the matches function on a '' trigger, with the right message.

    The matches function is tested on a botname trigger with pre filter and no
    post filter, the message sent is expected to match.
    """
    bot_name = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': '', 'trigger_pre': tokens}

    for token in tokens:
        message = token + " noise "
        assert Matcher.matches(candidate, message, bot_name)

    assert not Matcher.matches(candidate, bot_name, bot_name)


def test_post_empty_matches():
    """Test the matches function on a '' trigger, with the right message.

    The matches function is tested on a botname trigger with no pre filters
    and a post filter, the message sent is expected to match.
    """
    bot_name = "test"
    tokens = ['hello', 'hi']
    candidate = {'trigger': '', 'trigger_extra': tokens}

    for token in tokens:
        message = token + " noise "
        assert Matcher.matches(candidate, message, bot_name)

    assert not Matcher.matches(candidate, bot_name, bot_name)


def test_full_empty_matches():
    """Test the matches function on a '' trigger, with the right message.

    The matches function is tested on a '' trigger with pre filter and
    post filter, the message sent is expected to match.
    """
    bot_name = "test"
    tokens = ['hi', 'hello']
    candidate = {'trigger': '', 'trigger_extra': tokens,
                 'trigger_pre': tokens}

    for pre in tokens:
        for post in tokens:
            message = pre + " noise " + " noise " + post
            assert Matcher.matches(candidate, message, bot_name)

    message = bot_name
    assert not Matcher.matches(candidate, message, bot_name)


def test_bad_trigger_ignored():
    """Test the matches function on a not supported trigger.

    The matches function is tested on a not supported trigger (not in: ['',
    'botname','/command']), the message sent is expected NOT to match.
    """
    bot_name = "test"
    candidate = {'trigger': 'test'}
    message = "test"
    assert not Matcher.matches(candidate, message, bot_name)


def test_matching_with_tags():
    """Test the matches function on a botname trigger, with tags.

    The matches function is tested on a botname trigger with pre filter and
    post filter, plus tags. The message sent is expected to match.
    """
    pre_message = "Would {you} kindly use a {tag}, "
    bot_name = "test"
    post_message = "?"
    candidate = {'trigger': 'botname', 'trigger_extra': [post_message],
                 'trigger_pre': [pre_message]}

    not_tagged_pre = pre_message.replace("{tag}", "tag")
    not_tagged_pre = not_tagged_pre.replace("{you}", "thou")
    message = not_tagged_pre + " noise " + bot_name
    message += " noise " + post_message + " noise"

    assert Matcher.matches(candidate, message, bot_name)
