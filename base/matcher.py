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
        if not hasPre:
            hasPre = True
        else:
            tags = Matcher.__getTags(preMessage)
            if len(tags) > 0:
                # TODO
                hasPre = False
            else:
                pre_messages = candidate.get("trigger_pre")
                for pre_message in pre_messages:
                    print(pre_message + " | " + preMessage)
                    hasPre = pre_message in preMessage
                    if(hasPre):
                        break

        if not hasPost:
            hasPost = True
        else:
            tags = Matcher.__getTags(postMessage)
            if len(tags) > 0:
                # TODO
                hasPost = False
            else:
                post_messages = candidate.get("trigger_extra")
                for post_message in post_messages:
                    print(post_message + " | " + postMessage)
                    hasPost = post_message in postMessage
                    if(hasPost):
                        break

        return hasPre and hasPost

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
