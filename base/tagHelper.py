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
