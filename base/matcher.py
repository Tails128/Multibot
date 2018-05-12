"""This class checks if the given message and the given message item match."""


class Matcher():
    """Matcher for message items."""

    @staticmethod
    def __fullMatch(candidate, message):
        """Check if the message and the candidate match more deeply."""
        hasPre = "trigger_pre" in candidate
        if hasPre:
            hasPre = len(candidate.get("trigger_pre").strip(" "))
        hasPost = "trigger_extra" in candidate
        if hasPost:
            hasPost = len(candidate.get("trigger_extra").strip(" "))

        if not hasPre and not hasPost:
            return True

        return False
        # TODO

    @staticmethod
    def matches(candidate, message, botname):
        """Check if the candidate and the message match (trigger only)."""
        # if trigger = /command, check only if the message contains the command

        # if trigger's empty, delegate to fullMatch
        if candidate['trigger'] == '':
            return Matcher.__fullMatch(candidate, message)

        # if trigger's a /command, try to match it
        elif candidate.get('trigger')[0] == '/':
            splittedCandidate = candidate['trigger'].split(' ')
            if len(splittedCandidate) > 1:
                return False
            splittedMessage = message.split(' ')
            if splittedMessage[0] == splittedCandidate[0]:
                return Matcher.__fullMatch(candidate, message)
            return False

        # if trigger is botname, check if the message contains the botname,
        # then delegate to fullMatch
        elif candidate['trigger'] == 'botname':
            splittedMessage = message.split(' ')
            for splitted in splittedMessage:
                if botname == splitted:
                    return Matcher.__fullMatch(candidate, message)
            return False

        # default return false
        return False
