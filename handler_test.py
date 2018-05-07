from handler import Handler


def test_setBotname():
    testHandler = Handler()
    bName = "Test";
    testHandler.setBotname(bName)
    assert(testHandler.botname == bName)

def test_setMessages():
    testHandler = Handler()
    messages = [[{'trigger': 'botname'}]]
    testHandler.setMessages(messages)
    assert(testHandler.messages == messages)

def test_botname_right_message():
    testHandler = Handler()
    bName = "Test";
    messages = [[{'trigger': 'botname'}]]
    testHandler.setBotname(bName)
    testHandler.setMessages(messages)
    message = "Test"

    for messageList in testHandler.messages:
        for candidateMessage in messageList:
            assert testHandler.matches(candidateMessage, message)

def test_botname_wrong_message():
    testHandler = Handler()
    bName = "Test";
    messages = [[{'trigger': 'botname'}]]
    testHandler.setBotname(bName)
    testHandler.setMessages(messages)
    message = 'Testsssssss'

    for messageList in testHandler.messages:
        for candidateMessage in messageList:
            assert testHandler.matches(candidateMessage, message) == False
