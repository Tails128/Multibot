class Splitter():

    # compacts the dictionary vaules using the set priorities to define a range of
    # priorities
    def compactPriorities(self, values, priorities):

        result = []

        # sort priorities, append corresponding dictionary entry to the array
        sortedPriorities = sorted(priorities)
        for key in sortedPriorities:
            result.append(values[key])

        return result


    # splits the array of settings by the field "priority"
    def splitByPriority(self, array):

        holder = {}
        priorities = set()

        # each item gets saved in 'holder' at position 'priority'
        # priorities get saved in the set 'priorities' in order to get an
        # ordered and compact array from holder, which is a dictionary
        for arrItem in array:
            priority = arrItem['priority']
            if not priority in holder:
                holder[priority] = []
            holder[priority].append(arrItem)
            priorities.add(priority)

        return self.compactPriorities(holder, priorities)


    # def describeCommands(values):
        ## TODO:
