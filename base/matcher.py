"""This class checks if the given message and the given message item match."""


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

        # if not hasPre:
        #     hasPre = True
        # else:
        #     tags = Matcher.__getTags(preMessage)
        #     if len(tags) > 0:
        #         # TODO
        #         hasPre = False
        #     else:
        #         pre_messages = candidate.get("trigger_pre")
        #         hasPre = Matcher.__checkInArray(pre_messages, preMessage)

        # if not hasPost:
        #     hasPost = True
        # else:
        #     tags = Matcher.__getTags(postMessage)
        #     if len(tags) > 0:
        #         # TODO
        #         hasPost = False
        #     else:
        #         post_messages = candidate.get("trigger_extra")
        #         hasPost = Matcher.__checkInArray(post_messages, postMessage)

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
            tags = Matcher.__getTags(string)
            if len(tags) > 0:
                # TODO
                return False
            else:
                return Matcher.__checkInArray(array, string)

    @staticmethod
    def __checkInArray(array, string):
        """Check if string matches one of the pre-post elements in the array.

        Check if the given string matches one of the ones in the array. The
        match is a loose match and must handle the {tags}.
        """
        for element in array:
            # TODO: a better matching must be made: tags need to be considered.
            hasPost = element in string
            if(hasPost):
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

    @staticmethod
    def __getTags(string):
        answer = []
        tempAnswer = string.split("}")
        if len(tempAnswer) is 1:
            return []
        for candidate in tempAnswer:
            print(candidate)
            candidate = candidate[candidate.index("{") + 1:]
            # TODO also check validity
            if candidate is not "user":
                answer.append(candidate)
        return answer
