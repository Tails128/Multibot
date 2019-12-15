"""This class checks if the given message and the given message item match."""
import re
from base.tag_helper import TagHelper


class Matcher():
    """Matcher for message items."""

    @staticmethod
    def __full_match(candidate, pre_message, post_message):
        """Check if the message and the candidate match more deeply."""

        # If message has no pre-trigger conditions confirm the match for
        # pre-trigger conditions.
        has_pre = Matcher.__evaluate_pre_post(pre_message, candidate.get("trigger_pre"))
        has_post = Matcher.__evaluate_pre_post(post_message, candidate.get("trigger_extra"))

        return has_pre and has_post

    @staticmethod
    def __evaluate_pre_post(message, values_to_check):
        """Check if the pre and post elements matches something in the array."""
        if values_to_check is None or len(values_to_check) <= 0:
            return True
        
        if values_to_check is not None:
            return Matcher.__check_in_array(values_to_check, message)
        
        return False

    @staticmethod
    def __check_in_array(values_to_check, message):
        """Check if string matches one of the pre-post elements in the array.

        Check if the given string matches one of the ones in the array. The
        match is a loose match and must handle the {tags}.
        """
        for element in values_to_check:

            tags = TagHelper.get_tags(element)
            has_simple_match = len(tags) == 0 and element in message
            if has_simple_match:
                return True

            has_correct_structure = Matcher.__all_non_tag_components_match(element, message)
            if has_correct_structure:
                return True

        return False

    @staticmethod
    def __all_non_tag_components_match(template_message, compiled_message):
        """Check if the structure of the message match... excluding the tags, ofc!"""
        all_tags = len(TagHelper.get_tags(template_message))
        string_chunks = re.split("{.+}", template_message)

        for string_chunk in string_chunks:
            if string_chunk not in compiled_message:
                return False

            compiled_message = compiled_message.replace(string_chunk, "{{}}")

        number_of_matching_tags = len(TagHelper.get_tags_content(compiled_message, template_message))
        are_all_tags_present = number_of_matching_tags is all_tags

        return are_all_tags_present

    @staticmethod
    def matches(candidate, message, botname):
        """Check if the candidate and the message match (trigger only)."""
        candidate = Matcher.sanitize(candidate)
        trigger = candidate['trigger']

        is_trigger_empty = trigger == '' or trigger is None
        if is_trigger_empty:
            return Matcher.__full_match(candidate, message, message)

        is_trigger_slash_command = trigger[0] == '/'
        if is_trigger_slash_command:
            return Matcher.matches_slash_command(candidate, message)

        is_trigger_bot_name = trigger == 'botname'
        if is_trigger_bot_name:
            return Matcher.matches_bot_name(candidate, message, botname)

        # default return false
        return False

    @staticmethod
    def matches_slash_command(candidate, message):
        """Check if the message matches the given /command."""
        splitted_candidate = candidate['trigger'].split(' ')

        if len(splitted_candidate) > 1:
            return False
        splitted_message = message.split(' ')

        is_case_sensitive = candidate['strictMatch']
        if not is_case_sensitive:
            splitted_message[0] = splitted_message[0].lower()
            splitted_candidate[0] = splitted_candidate[0].lower()

        if splitted_message[0] == splitted_candidate[0]:
            post_message = message.lstrip(candidate.get('trigger'))
            post_message = post_message.lstrip(" ")
            return Matcher.__full_match(candidate, '', post_message)

        return False

    @staticmethod
    def matches_bot_name(candidate, message, botname):
        """Check if the message matches the given botname command."""
        is_case_sensitive = candidate['strictMatch']
        new_message = message if is_case_sensitive else message.lower()
        new_bot_name = botname if is_case_sensitive else botname.lower()

        new_message = new_message.split(' ')

        if new_bot_name in new_message:
            new_split = message.split(botname)
            if len(new_split) == 2:
                return Matcher.__full_match(candidate, new_split[0], new_split[1])

        return False

    @staticmethod
    def sanitize(candidate):
        """Fill the item with the default optional data if it's not set."""
        if 'strictMatch' not in candidate:
            candidate['strictMatch'] = False

        return candidate
