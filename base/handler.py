"""This document contains the class which handles telegram's interactions."""
from base import helpCommand, matcher
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
                if matcher.Matcher.matches(candidateMessage, message,
                                           self.botname):
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
