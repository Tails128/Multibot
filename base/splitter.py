"""This document contains the class which splits the custom settings."""

def sanitize(array):
    """Sanitize the entries."""
    result = []
    for item in array:
        if 'answer' not in item:
            item['answer'] = []
        elif isinstance(item.get('answer'), str):
            arr = [item.get('answer')]
            item['answer'] = arr
        result.append(item)
    return result


class Splitter():
    """The splitter class splits and classifies the custom JSON settings."""

    @staticmethod
    def sort_priorities(values):
        """Sort the [values] and places them in an array."""
        result = []

        sorted_priorities = sorted(values)
        for key in sorted_priorities:
            sanitized_values = sanitize(values[key])
            result.append(sanitized_values)

        return result

    def split_by_priority(self, array):
        """Split and order the custom settings by priority."""
        holder = {}

        # each item gets saved in 'holder' at position 'priority'
        # priorities get saved in the set 'priorities' in order to get an
        # ordered and compact array from holder, which is a dictionary
        for array_item in array:
            priority = array_item['priority']
            if priority not in holder:
                holder[priority] = []
            holder[priority].append(array_item)

        return self.sort_priorities(holder)
