"""An helper for tag management."""


class TagHelper():
    """This class helps with tags recognizement and elaboration."""

    @staticmethod
    def is_valid(string):
        """Check if the tag is valid.

        A tag is considered not valid if it contains unescaped
        '{' or unescaped '}'
        """
        if "}" not in string or "{" not in string:
            return False

        total_open = string.count('{')
        total_close = string.count('}')
        answer = total_open - total_close
        if answer != 0:
            return False
        return True

    @staticmethod
    def get_tags(string):
        """Get the tags in a string."""
        answer = []

        if not TagHelper.is_valid(string):
            return answer

        temp_answer = string.split("}")
        for candidate in temp_answer:
            candidate = candidate.strip(" ")
            if "{" not in candidate:
                continue
            candidate = candidate.split("{")[1]
            answer.append(candidate)
        return answer

    @staticmethod
    def remove_tags(string):
        """Return the given string, but without the tags."""
        answer = string
        tags = TagHelper.get_tags(answer)
        for tag in tags:
            remove = " {" + tag + "}"
            answer = answer.replace(remove, "")
        return answer

    @staticmethod
    def get_tags_content(message, template_message):
        """Extract tags from a string, using stringWithTags for the syntax."""
        partial_tags = TagHelper.get_tags(template_message)
        if len(partial_tags) == 0:
            return {}
        tags = []
        for tag in partial_tags:
            tags.append("{" + tag + "}")
        extracted = message
        guide = template_message
        syntax = TagHelper.get_syntax(template_message, tags)
        for element in syntax:
            if element != '':
                extracted = extracted.replace(element, "{{}}")
                guide = guide.replace(element, "{{}}")
        extracted = extracted.split("{{}}")
        guide = guide.split("{{}}")

        answer = {}
        for index, value in enumerate(extracted):
            if guide[index] != '':
                obj_name = guide[index].replace("{", "").replace("}", "")
                answer[obj_name] = value
        return answer

    @staticmethod
    def get_syntax(string, tags):
        """Get the syntax of a string once the tags are removed."""
        if len(tags) == 0:
            return string

        answer = string
        for tag in tags:
            answer = answer.replace(tag, "{{}}")
        answer = answer.split("{{}}")
        return answer

    @staticmethod
    def replace_tags(string, tag_content):
        """Replace the content of a string with the tagContent."""
        answer = string
        for key in tag_content:
            tag = "{" + key + "}"
            answer = answer.replace(tag, tag_content[key])
        return answer
