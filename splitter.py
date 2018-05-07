"""This document contains the class which splits the custom settings."""


class Splitter():
    """The splitter class splits and classifies the custom JSON settings."""

    def sortPriorities(self, values):
        """Sort the [values] and places them in an array."""
        result = []

        sortedPriorities = sorted(values)
        for key in sortedPriorities:
            result.append(values[key])

        return result

    def splitByPriority(self, array):
        """Split and order the custom settings by priority."""
        holder = {}

        # each item gets saved in 'holder' at position 'priority'
        # priorities get saved in the set 'priorities' in order to get an
        # ordered and compact array from holder, which is a dictionary
        for arrItem in array:
            priority = arrItem['priority']
            if priority not in holder:
                holder[priority] = []
            holder[priority].append(arrItem)

        return self.sortPriorities(holder)

# def describeCommands(values):
# TODO:
