"""This document contains the class which handles telegram's interactions."""


class Handler():
    """Handle the telegram chat interactions with this class."""

    messages = []
    botname = ''

    # this function collapses the config data into the property 'trigger' to
    # save time when the bot has to check if messages match
    # def riComposeTrigger():
    #   for messageList in messages:
    #       for candidateMessage in messageList:
    # TODO

    def setBotname(self, newName):
        """Set the internal variable which stores the bot's name."""
        self.botname = newName

    def setMessages(self, newMessages):
        """Set the internal variable which stores the interactions."""
        self.messages = newMessages
        # TODO : fill extra fields not set in messages

    def fullMatch(self, candidate, message):
        """Check if the message and the candidate match more deeply."""
        return True
        # TODO

    def matches(self, candidate, message):
        """Check if the candidate and the message match (trigger only)."""
        # if trigger = /command, check only if the message contains the command
        if candidate.get('trigger')[0] == '/':
            splittedCandidate = candidate['trigger'].split(' ')
            if splittedCandidate.len() > 1:
                return
            splittedMessage = message.split(' ')
            if splittedMessage[0] == splittedCandidate[0]:
                return True
            return False

        # if trigger is botname, check if the message contains the botname,
        # then delegate to fullMatch
        elif candidate['trigger'] == 'botname':
            splittedMessage = message.split(' ')
            for splitted in splittedMessage:
                if self.botname == splitted:
                    return self.fullMatch(candidate, message)
            return False

        # if trigger's empty, delegate to fullMatch
        elif candidate['trigger'] == '':
            return self.fullMatch(candidate, message)

        # default return false
        return False

    def answer(self, answer):
        """Answer to a matching command."""
        print("MATCH!")

    def checkMessage(self, message):
        """Check if the message just sent is a command."""
        for messageList in self.messages:
            for candidateMessage in messageList:
                if self.matches(candidateMessage, message):
                    self.answer(candidateMessage)
                    return
