"""Test handler class."""
from handler import Handler


def test_setBotname():
    """Test the setBotname function."""
    testHandler = Handler()
    bName = "Test"
    testHandler.setBotname(bName)
    assert(testHandler.botname == bName)


def test_setMessages():
    """Test the setMessages function."""
    testHandler = Handler()
    messages = [[{'trigger': '/botname'}]]
    testHandler.setMessages(messages)
    assert testHandler.messages == messages
    assert testHandler.helpCommand.getHelpCommand() == "*botname*\n\n"


def test_botname_right_message():
    """Test the reaction of the bot once a matching message is sent."""
    testHandler = Handler()
    bName = "Test"
    messages = [[{'trigger': 'botname'}]]
    testHandler.setBotname(bName)
    testHandler.setMessages(messages)
    message = "Test"

    for messageList in testHandler.messages:
        for candidateMessage in messageList:
            assert testHandler.matches(candidateMessage, message)


def test_botname_right_message_get_answer():
    """Test the answer to a right message."""
    testHandler = Handler()
    bName = "Test"
    messages = [[{'trigger': 'botname', 'answer': ['success!']}]]
    testHandler.setBotname(bName)
    testHandler.setMessages(messages)

    assert testHandler.checkMessage(bName, '') is 'success!'


def test_botname_wrong_message():
    """Test the reaction of the bot once a NOT matching message is sent."""
    testHandler = Handler()
    bName = "Test"
    messages = [[{'trigger': 'botname'}]]
    testHandler.setBotname(bName)
    testHandler.setMessages(messages)
    message = 'Testsssssss'

    for messageList in testHandler.messages:
        for candidateMessage in messageList:
            assert testHandler.matches(candidateMessage, message) is False


def test_botname_wrong_message_get_answer():
    """Test the answer to a wrong message."""
    testHandler = Handler()
    bName = "Test"
    messages = [[{'trigger': 'botname', 'answer': ['success!']}]]
    testHandler.setBotname(bName)
    testHandler.setMessages(messages)

    assert testHandler.checkMessage(bName + 'sssss', '') is None
