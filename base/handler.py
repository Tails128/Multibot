"""This document contains the class which handles telegram's interactions."""
from base import helpCommand, matcher, tagHelper
import random
import math
import sys


class Handler():
    """Handle the telegram chat interactions with this class."""

    messages = []
    botname = ''
    handlerHelpCommand = ''
    __logger = None

    def setLogger(self, logger):
        """Set the default logger."""
        self.__logger = logger

    def setBotname(self, newName):
        """Set the internal variable which stores the bot's name."""
        self.botname = newName

    def setMessages(self, newMessages):
        """Set the internal variable which stores the interactions."""
        for priority in newMessages:
            for message in priority:
                if 'strictMatch' not in message:
                    message['strictMatch'] = False

        self.messages = newMessages
        self.handlerHelpCommand = helpCommand.HelpCommand()
        # TODO : fill extra fields not set in messages
        self.handlerHelpCommand.registerCommands(self.messages)

    def answer(self, answer):
        """Answer to a matching command."""
        answers = answer.get('answer')
        number = math.floor(random.random() * (len(answer['answer']) - 1))
        return answers[number]

    def checkMessage(self, message, sender):
        """Check if the message just sent is a command."""
        for messageList in self.messages:
            for candidateMessage in messageList:
                if matcher.Matcher.matches(candidateMessage, message,
                                           self.botname):
                    answer = self.answer(candidateMessage)
                    return self.parse(answer, candidateMessage, message,
                                      sender)
        return None

    def parse(self, answer, messageTemplate, message, sender):
        """Parse the message, finding the {} tags.

        Currently only {user} is supported.
        """
        tagContent = tagHelper.getTagsContent(message, messageTemplate)
        answer = tagHelper.replaceTags(answer, tagContent)
        answer = answer.replace("{user}", sender)
        return answer

    def handle(self, message, bot):
        """Handle the chat and check if any command is sent."""
        chat_id = message['chat']['id']
        fullMessage = message['text']
        sender = message['from']['username']

        # notify the user that the message is received
        logString = "Got message: " + fullMessage + "\nFrom: " + sender

        if self.__logger is None:
            # if no default logger is set, print
            print(logString)
            sys.stdout.flush()
        else:
            # else use the default logger
            self.__logger.log(logString)

        # sendHour = message['date']
        answer = self.checkMessage(fullMessage, sender)
        if answer is not None:
            bot.sendMessage(chat_id, answer)
