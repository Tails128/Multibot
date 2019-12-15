"""This class checks if the given message and the given message item match."""
from base.tagHelper import TagHelper
import re


class Matcher():
    """Matcher for message items."""

    @staticmethod
    def __fullMatch(candidate, message, preMessage, postMessage):
        """Check if the message and the candidate match more deeply."""

        # If message has no pre-trigger conditions confirm the match for
        # pre-trigger conditions.
        hasPre = Matcher.__evaluatePrePost(preMessage, candidate.get("trigger_pre"))
        hasPost = Matcher.__evaluatePrePost(postMessage, candidate.get("trigger_extra"))

        return hasPre and hasPost

    @staticmethod
    def __evaluatePrePost(message, valuesToCheck):
        """Check if the pre-post element matches something in the array."""
        if valuesToCheck is None or len(valuesToCheck) <= 0:
            return True
        elif valuesToCheck is not None:
            return Matcher.__checkInArray(valuesToCheck, message)
        return False

    @staticmethod
    def __checkInArray(message, valuesToCheck):
        """Check if string matches one of the pre-post elements in the array.

        Check if the given string matches one of the ones in the array. The
        match is a loose match and must handle the {tags}.
        """
        for element in message:

            tags = TagHelper.getTags(element)
            hasSimpleMatch = len(tags) is 0 and element in valuesToCheck
            if hasSimpleMatch:
                return True

            hasCorrectStructure = Matcher.__allNonTagComponentsMatch(element, valuesToCheck)
            if hasCorrectStructure:
                return True

        return False

    @staticmethod
    def __allNonTagComponentsMatch(templateMessage, compiledMessage):
        """Check if the structure of the message match... excluding the tags, ofc!"""
        allTags = len(TagHelper.getTags(templateMessage))
        stringChunks = re.split("{.+}", templateMessage)

        for stringChunk in stringChunks:
            if stringChunk not in compiledMessage:
                return False
            else:
                compiledMessage = compiledMessage.replace(stringChunk, "{{}}")

        numberOfMatchingTags = len(TagHelper.getTagsContent(compiledMessage, templateMessage))
        areAllTagsPresent = numberOfMatchingTags is allTags

        return areAllTagsPresent

    @staticmethod
    def matches(candidate, message, botname):
        """Check if the candidate and the message match (trigger only)."""
        candidate = Matcher.sanitize(candidate)
        trigger = candidate['trigger']

        isTriggerEmpty = trigger == '' or trigger is None
        if isTriggerEmpty:
            return Matcher.__fullMatch(candidate, message, message, message)

        isTriggerSlashCommand = trigger[0] == '/'
        if isTriggerSlashCommand:
            return Matcher.matchesSlashCommand(candidate, message)

        isTriggerBotName = trigger == 'botname'
        if isTriggerBotName:
            return Matcher.matchesBotName(candidate, message, botname)

        # default return false
        return False

    @staticmethod
    def matchesSlashCommand(candidate, message):
        """Check if the message matches the given /command."""
        splittedCandidate = candidate['trigger'].split(' ')

        if len(splittedCandidate) > 1:
            return False
        splittedMessage = message.split(' ')

        isCaseSensitive = candidate['strictMatch']
        if not isCaseSensitive:
            splittedMessage[0] = splittedMessage[0].lower()
            splittedCandidate[0] = splittedCandidate[0].lower()

        if splittedMessage[0] == splittedCandidate[0]:
            postMessage = message.lstrip(candidate.get('trigger'))
            postMessage = postMessage.lstrip(" ")
            return Matcher.__fullMatch(candidate, message, '', postMessage)

        return False

    @staticmethod
    def matchesBotName(candidate, message, botname):
        """Check if the message matches the given botname command."""
        isCaseSensitive = candidate['strictMatch']
        newMessage = message if isCaseSensitive else message.lower()
        newBotName = botname if isCaseSensitive else botname.lower()

        newMessage = newMessage.split(' ')

        if newBotName in newMessage:
            newSplit = message.split(botname)
            if(len(newSplit) is 2):
                return Matcher.__fullMatch(candidate, message, newSplit[0], newSplit[1])

        return False

    @staticmethod
    def sanitize(candidate):
        """Fill the item with the default optional data if it's not set."""
        if 'strictMatch' not in candidate:
            candidate['strictMatch'] = False

        return candidate
