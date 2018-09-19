"""A settable logger."""
import datetime
import os
import sys


class Logger():
    """This class will retain log variables as log mode."""

    _logFile = True
    _consoleLog = True
    _lastLogData = ""
    _filename = "log"

    @staticmethod
    def setFileName(name):
        """Set the logfile path."""
        if isinstance(name, str):
            Logger._filename = name
        else:
            Logger.log("Logfile path is not a str instance!")

    @staticmethod
    def enableFileLog():
        """Enable log via file."""
        Logger._logFile = True

    @staticmethod
    def disableFileLog():
        """Disable log via file."""
        Logger._logFile = False

    @staticmethod
    def enableConsoleLog():
        """Enable log via console."""
        Logger._consoleLog = True

    @staticmethod
    def disableConsoleLog():
        """Disable log via console."""
        Logger._consoleLog = False

    @staticmethod
    def log(string):
        """Check how to log and log."""
        logData = Logger.getLogData()
        if(Logger._logFile):
            Logger.logFile(logData, string)
        if(Logger._consoleLog):
            Logger.logConsole(logData, string)

    @staticmethod
    def getLogData():
        """Get log data (time)."""
        time = datetime.datetime.now().time().strftime("%d-%m-%Y %H:%M:%S")
        Logger._lastLogData = time
        return time

    @staticmethod
    def logFile(logData, string):
        """Log the given string via file."""
        if not os.path.exists(Logger._filename):
            with open(Logger._filename, "w") as file:
                file.write("")
        with open(Logger._filename, "a") as file:
            file.write(Logger.makeLogLine(logData, string) + "\n")

    @staticmethod
    def logConsole(logData, string):
        """Log the given string via console."""
        print(Logger.makeLogLine(logData, string))
        sys.stdout.flush()  # this is needed since we're in a loop

    @staticmethod
    def makeLogLine(logData, string):
        """Make a log line formatted with time and content."""
        return logData + ": " + string
