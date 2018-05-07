class Handler():

    messages = []
    botname = '';



    # this function collapses the config data into the property 'trigger' to save
    # time when the bot has to check if messages match
    # def riComposeTrigger():
        # for messageList in messages:
            # for candidateMessage in messageList:
                ##TODO


    # simple setter for botname.
    def setBotname(self, newName):
        self.botname = newName


    # simple setter for messages
    def setMessages(self, newMessages):
        self.messages = newMessages
        ## TODO : fill extra fields not set in messages


    # this function checks if a message matches with the candidate analyzing the extra fields
    def fullMatch(self, candidate, message):
        return True
        ## TODO

    # this function checks if the trigger matches and in case the trigger's not a /command
    # delegates the matching to the function fullMatch(candidate, message)
    def matches(self, candidate, message):

        #if trigger = /command, check only if the message contains the /command
        if candidate.get('trigger')[0] == '/':
            splittedCandidate = candidate['trigger'].split(' ')
            if splittedCandidate.len() > 1:
                return
            splittedMessage = message.split(' ')
            if splittedMessage[0] == splittedCandidate[0] :
                return True;
            return False;

        #if trigger is botname, check if the message contains the botname, then delegate to fullMatch
        elif candidate['trigger'] == 'botname':
            splittedMessage = message.split(' ')
            for splitted in splittedMessage:
                if self.botname == splitted:
                    return self.fullMatch(candidate, message)
            return False

        #if trigger's empty, delegate to fullMatch
        elif candidate['trigger'] == '':
            return self.fullMatch(candidate, message)

        #default return false
        return False


    def answer(self, answer):
        print("MATCH!")


    def checkMessage(self, message):
        for messageList in self.messages:
            for candidateMessage in messageList:
                if self.matches(candidateMessage, message):
                    self.answer(candidateMessage)
                    return
