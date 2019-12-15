"""This document contains the class which handles telegram's interactions."""
import random
import math
import sys
from base.tag_helper import TagHelper
from base.help_command import HelpCommand
from base.matcher import Matcher

class Handler():
    """Handle the telegram chat interactions with this class."""

    messages = []
    botname = ''
    handler_help_command = ''
    __logger = None

    def set_logger(self, logger):
        """Set the default logger."""
        self.__logger = logger

    def set_botname(self, new_name):
        """Set the internal variable which stores the bot's name."""
        self.botname = new_name

    def set_messages(self, new_messages):
        """Set the internal variable which stores the interactions."""
        for priority in new_messages:
            for message in priority:
                if 'strictMatch' not in message:
                    message['strictMatch'] = False

        self.messages = new_messages
        self.handler_help_command = HelpCommand()
        # TODO : fill extra fields not set in messages
        self.handler_help_command.register_commands(self.messages)

    @staticmethod
    def answer(answer):
        """Answer to a matching command."""
        answers = answer.get('answer')
        number = math.floor(random.random() * (len(answer['answer']) - 1))
        return answers[int(number)]

    def check_message(self, message, sender):
        """Check if the message just sent is a command."""
        for message_list in self.messages:
            for candidate_message in message_list:
                if Matcher.matches(candidate_message, message,
                                   self.botname):
                    answer = self.answer(candidate_message)
                    return self.parse(answer, candidate_message, message,
                                      sender)
        return None

    @staticmethod
    def parse(answer, message_template, message, sender):
        """Parse the message, finding the {} tags.

        Currently only {user} is supported.
        """
        tag_content = TagHelper.get_tags_content(message, message_template)
        answer = TagHelper.replace_tags(answer, tag_content)
        answer = answer.replace("{user}", sender)
        return answer

    def handle(self, message, bot):
        """Handle the chat and check if any command is sent."""
        chat_id = message['chat']['id']
        full_message = message['text']
        sender = message['from']['username']

        # notify the user that the message is received
        log_string = "Got message: " + full_message + "\nFrom: " + sender

        if self.__logger is None:
            # if no default logger is set, print
            print(log_string)
            sys.stdout.flush()
        else:
            # else use the default logger
            self.__logger.log(log_string)

        # sendHour = message['date']
        answer = self.check_message(full_message, sender)
        if answer is not None:
            bot.sendMessage(chat_id, answer)
