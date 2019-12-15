"""Test handler class."""
from base.handler import Handler
from base.matcher import Matcher


def test_set_botname():
    """Test the setBotname function."""
    test_handler = Handler()
    bot_name = "Test"
    test_handler.set_botname(bot_name)
    assert test_handler.botname == bot_name


def test_set_messages():
    """Test the setMessages function."""
    test_handler = Handler()
    messages = [[{'trigger': '/botname'}]]
    test_handler.set_messages(messages)
    assert test_handler.messages == messages
    assert test_handler.handler_help_command.get_help_command() == "*botname*\n\n"


def test_botname_right_message():
    """Test the reaction of the bot once a matching message is sent."""
    test_handler = Handler()
    bot_name = message = "Test"
    messages = [[{'trigger': 'botname'}]]
    test_handler.set_botname(bot_name)
    test_handler.set_messages(messages)

    for message_list in test_handler.messages:
        for candidate_message in message_list:
            assert Matcher.matches(candidate_message, message, bot_name)


def test_botname_right_message_get_answer():
    """Test the answer to a right message."""
    test_handler = Handler()
    bot_name = "Test"
    messages = [[{'trigger': 'botname', 'answer': ['success!']}]]
    test_handler.set_botname(bot_name)
    test_handler.set_messages(messages)

    assert test_handler.check_message(bot_name, '') == 'success!'


def test_botname_wrong_message():
    """Test the reaction of the bot once a NOT matching message is sent."""
    test_handler = Handler()
    bot_name = "Test"
    messages = [[{'trigger': 'botname'}]]
    test_handler.set_botname(bot_name)
    test_handler.set_messages(messages)
    message = 'Testsssssss'

    for message_list in test_handler.messages:
        for candidate_message in message_list:
            assert Matcher.matches(candidate_message,
                                   message, bot_name) is False


def test_parse():
    """Test the if the parse works as intended, replacing tags."""
    test_handler = Handler()
    sender = "Tester"
    answer = 'hello, {user}! You tagged: {tag}'
    message = "yourself"
    message_template = "{tag}"
    sender = "tester"
    result = "hello, tester! You tagged: yourself"

    answer = test_handler.parse(answer, message_template, message, sender)

    assert result == answer


def test_botname_wrong_message_get_answer():
    """Test the answer to a wrong message."""
    test_handler = Handler()
    bot_name = "Test"
    messages = [[{'trigger': 'botname', 'answer': ['success!']}]]
    test_handler.set_botname(bot_name)
    test_handler.set_messages(messages)

    assert test_handler.check_message(bot_name + 'sssss', '') is None
