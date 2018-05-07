"""This document contains the class which splits the custom settings."""


class Splitter():
    """The splitter class splits and classifies the custom JSON settings."""

    # compacts the dictionary vaules using the set priorities to define a range
    # of priorities
    def compactPriorities(self, values, priorities):
        """Order the [values] according to the [priorities]."""
        result = []

        # sort priorities, append corresponding dictionary entry to the array
        sortedPriorities = sorted(priorities)
        for key in sortedPriorities:
            result.append(values[key])

        return result

    def splitByPriority(self, array):
        """Split and order the custom settings by priority."""
        holder = {}
        priorities = set()

        # each item gets saved in 'holder' at position 'priority'
        # priorities get saved in the set 'priorities' in order to get an
        # ordered and compact array from holder, which is a dictionary
        for arrItem in array:
            priority = arrItem['priority']
            if priority not in holder:
                holder[priority] = []
            holder[priority].append(arrItem)
            priorities.add(priority)

        return self.compactPriorities(holder, priorities)

# def describeCommands(values):
# TODO:
