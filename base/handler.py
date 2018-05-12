"""This document contains the class which handles telegram's interactions."""
from base import helpCommand
import random
import math


class Handler():
    """Handle the telegram chat interactions with this class."""

    messages = []
    botname = ''
    handlerHelpCommand = ''

    def setBotname(self, newName):
        """Set the internal variable which stores the bot's name."""
        self.botname = newName

    def setMessages(self, newMessages):
        """Set the internal variable which stores the interactions."""
        self.messages = newMessages
        self.handlerHelpCommand = helpCommand.HelpCommand()
        # TODO : fill extra fields not set in messages
        self.handlerHelpCommand.registerCommands(self.messages)

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
        answers = answer.get('answer')
        if len(answers) is 1:
            return answers[0]
        number = math.floor(random.random() * len())
        return answers[number]

    def checkMessage(self, message, sender):
        """Check if the message just sent is a command."""
        for messageList in self.messages:
            for candidateMessage in messageList:
                if self.matches(candidateMessage, message):
                    answer = self.answer(candidateMessage)
                    return self.parse(answer, sender)
        return None

    def parse(self, answer, sender):
        """Parse the message, finding the {} tags."""
        """Currently only {user} is supported."""
        answer = answer.replace("{user}", sender)
        return answer

    def handle(self, message, bot):
        """Handle the chat and check if any command is sent."""
        chat_id = message['chat']['id']
        fullMessage = message['text']
        sender = message['from']['username']
        # sendHour = message['date']
        answer = self.checkMessage(fullMessage, sender)
        if answer is not None:
            bot.sendMessage(chat_id, answer)
