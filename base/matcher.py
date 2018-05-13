"""This class checks if the given message and the given message item match."""
from base import tagHelper


class Matcher():
    """Matcher for message items."""

    @staticmethod
    def __fullMatch(candidate, message, preMessage, postMessage):
        """Check if the message and the candidate match more deeply."""
        hasPre = "trigger_pre" in candidate
        if hasPre:
            hasPre = len(candidate.get("trigger_pre")) > 0
        hasPost = "trigger_extra" in candidate
        if hasPost:
            hasPost = len(candidate.get("trigger_extra")) > 0

        # If message has no pre-trigger conditions confirm the match for
        # pre-trigger conditions.
        hasPre = Matcher.__evaluatePrePost(preMessage,
                                           candidate.get("trigger_pre"),
                                           hasPre)
        hasPost = Matcher.__evaluatePrePost(postMessage,
                                            candidate.get("trigger_extra"),
                                            hasPost)

        return hasPre and hasPost

    @staticmethod
    def __evaluatePrePost(string, array, hasIt):
        """Check if the pre-post element matches something in the array.

        If hasIt (the given condition) is positive, try to match the given
        string to one of the elements in the array.
        """
        if not hasIt:
            return True
        elif array is None:
            return False
        else:
            return Matcher.__checkInArray(array, string)
        return False

    @staticmethod
    def __checkInArray(array, string):
        """Check if string matches one of the pre-post elements in the array.

        Check if the given string matches one of the ones in the array. The
        match is a loose match and must handle the {tags}.
        """
        for element in array:
            tags = tagHelper.getTags(element)
            if len(tags) is 0:
                if element in string:
                    return True

            if Matcher.__tagMatch(tags, element, string):
                return True
        return False

    @staticmethod
    def __tagMatch(tags, textWithTags, string):
        """Check if a tagwise match is possible."""
        stringChunks = textWithTags
        cleanString = string
        for tag in tags:
            stringChunks = stringChunks.replace(" {" + tag + "}", "{{}}")
        stringChunks = stringChunks.split("{{}}")

        print(stringChunks)

        print("checking chunks")
        for stringChunk in stringChunks:
            if stringChunk not in string:
                return False
            else:
                cleanString = cleanString.replace(stringChunk, "{{}}")

        # adding 2 to the number of tags to ignore text before and after the
        # sentence
        total = len(tags) + 2
        splittedTags = len(cleanString.split("{{}}"))

        for split in cleanString.split(" "):
            print(split)

        if splittedTags == total:
            return True
        return False

    @staticmethod
    def matches(candidate, message, botname):
        """Check if the candidate and the message match (trigger only)."""
        # if trigger = /command, check only if the message contains the command

        # if trigger's empty, delegate to fullMatch
        if candidate['trigger'] == '':
            return Matcher.__fullMatch(candidate, message, message, message)

        # if trigger's a /command, try to match it
        elif candidate.get('trigger')[0] == '/':
            splittedCandidate = candidate['trigger'].split(' ')
            if len(splittedCandidate) > 1:
                return False
            splittedMessage = message.split(' ')
            if splittedMessage[0] == splittedCandidate[0]:
                postMessage = message.lstrip(candidate.get('trigger'))
                postMessage = postMessage.lstrip(" ")
                return Matcher.__fullMatch(candidate, message, '', postMessage)
            return False

        # if trigger is botname, check if the message contains the botname,
        # then delegate to fullMatch
        elif candidate['trigger'] == 'botname':
            splittedMessage = message.split(' ')
            if botname in splittedMessage:
                newSplit = message.split(botname)
                if(len(newSplit) is not 2):
                    return False
                else:
                    return Matcher.__fullMatch(candidate, message, newSplit[0],
                                               newSplit[1])
            return False

        # default return false
        return False
