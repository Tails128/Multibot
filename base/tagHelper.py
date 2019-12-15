"""An helper for tag management."""


class TagHelper():
    """This class helps with tags recognizement and elaboration."""

    @staticmethod
    def isValid(string):
        """Check if the tag is valid.

        A tag is considered not valid if it contains unescaped
        '{' or unescaped '}'
        """
        if "}" not in string or "{" not in string:
            return False

        totalOpen = string.count('{')
        totalClose = string.count('}')
        answer = totalOpen - totalClose
        if answer is not 0:
            return False
        return True

    @staticmethod
    def getTags(string):
        """Get the tags in a string."""
        answer = []

        if not TagHelper.isValid(string):
            return answer

        tempAnswer = string.split("}")
        for candidate in tempAnswer:
            candidate = candidate.strip(" ")
            if "{" not in candidate:
                continue
            candidate = candidate.split("{")[1]
            answer.append(candidate)
        return answer

    @staticmethod
    def removeTags(string):
        """Return the given string, but without the tags."""
        answer = string
        tags = TagHelper.getTags(answer)
        for tag in tags:
            remove = " {" + tag + "}"
            answer = answer.replace(remove, "")
        return answer

    @staticmethod
    def getTagsContent(message, templateMessage):
        """Extract tags from a string, using stringWithTags for the syntax."""
        partialTags = TagHelper.getTags(templateMessage)
        if len(partialTags) is 0:
            return {}
        tags = []
        for tag in partialTags:
            tags.append("{" + tag + "}")
        extracted = message
        guide = templateMessage
        syntax = TagHelper.getSyntax(templateMessage, tags)
        for element in syntax:
            if element is not '':
                extracted = extracted.replace(element, "{{}}")
                guide = guide.replace(element, "{{}}")
        extracted = extracted.split("{{}}")
        guide = guide.split("{{}}")

        answer = {}
        for index, value in enumerate(extracted):
            if guide[index] is not '':
                obj_name = guide[index].replace("{", "").replace("}", "")
                answer[obj_name] = value
        return answer

    @staticmethod
    def getSyntax(string, tags):
        """Get the syntax of a string once the tags are removed."""
        if len(tags) is 0:
            return string

        answer = string
        for tag in tags:
            answer = answer.replace(tag, "{{}}")
        answer = answer.split("{{}}")
        return answer

    @staticmethod
    def replaceTags(string, tagContent):
        """Replace the content of a string with the tagContent."""
        answer = string
        for key in tagContent:
            tag = "{" + key + "}"
            answer = answer.replace(tag, tagContent[key])
        return answer
