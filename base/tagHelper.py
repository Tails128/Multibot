"""An helper for tag management."""


def getTags(string):
    """Get the tags in a string."""
    answer = []

    if not isValid(string):
        return answer

    tempAnswer = string.split("}")
    for candidate in tempAnswer:
        candidate = candidate.strip(" ")
        if "{" not in candidate:
            continue
        candidate = candidate.split("{")[1]
        answer.append(candidate)
    return answer


def isValid(string):
    """Check if the tag is valid.

    A tag is considered not valid if it contains unescaped '{' or unescaped '}'
    """
    if "}" not in string or "{" not in string:
        return False

    totalOpen = string.count('{')
    totalClose = string.count('}')
    answer = totalOpen - totalClose
    if answer is not 0:
        return False
    return True


def removeTags(string):
    """Return the given string, but without the tags."""
    answer = string
    tags = getTags(answer)
    for tag in tags:
        remove = " {" + tag + "}"
        answer = answer.replace(remove, "")
    return answer


def extractTags(string, stringWithTags):
    """Extract tags from a string, using stringWithTags for the syntax."""
    partialTags = getTags(stringWithTags)
    if len(partialTags) is 0:
        return {}

    tags = []
    for tag in partialTags:
        tags.append("{" + tag + "}")

    extracted = string
    guide = stringWithTags
    syntax = extractSyntax(stringWithTags, tags)
    for element in syntax:
        if element is not '':
            extracted = extracted.replace(element, "{{}}")
            guide = guide.replace(element, "{{}}")
    extracted = extracted.split("{{}}")
    guide = guide.split("{{}}")

    answer = {}
    for index in range(0, len(extracted)):
        if guide[index] is not '':
            obj_name = guide[index].replace("{", "").replace("}", "")
            answer[obj_name] = extracted[index]
    return answer


def extractSyntax(string, tags):
    """Get the syntax of a string once the tags are removed."""
    if len(tags) is 0:
        return string

    answer = string
    for tag in tags:
        answer = answer.replace(tag, "{{}}")
    answer = answer.split("{{}}")
    return answer
