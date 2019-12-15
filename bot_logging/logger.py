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
    def set_file_name(name):
        """Set the logfile path."""
        if isinstance(name, str):
            Logger._filename = name
        else:
            Logger.log("Logfile path is not a str instance!")

    @staticmethod
    def enable_file_log():
        """Enable log via file."""
        Logger._logFile = True

    @staticmethod
    def disable_file_log():
        """Disable log via file."""
        Logger._logFile = False

    @staticmethod
    def enable_console_log():
        """Enable log via console."""
        Logger._consoleLog = True

    @staticmethod
    def disable_console_log():
        """Disable log via console."""
        Logger._consoleLog = False

    @staticmethod
    def log(string):
        """Check how to log and log."""
        log_data = Logger.get_log_data()
        if Logger._logFile:
            Logger.log_file(log_data, string)
        if Logger._consoleLog:
            Logger.log_console(log_data, string)

    @staticmethod
    def get_log_data():
        """Get log data (time)."""
        time = datetime.datetime.now().time().strftime("%d-%m-%Y %H:%M:%S")
        Logger._lastLogData = time
        return time

    @staticmethod
    def log_file(log_data, string):
        """Log the given string via file."""
        if not os.path.exists(Logger._filename):
            with open(Logger._filename, "w") as file:
                file.write("")
        with open(Logger._filename, "a") as file:
            file.write(Logger.make_log_line(log_data, string) + "\n")

    @staticmethod
    def log_console(log_data, string):
        """Log the given string via console."""
        print(Logger.make_log_line(log_data, string))
        sys.stdout.flush()  # this is needed since we're in a loop

    @staticmethod
    def make_log_line(log_data, string):
        """Make a log line formatted with time and content."""
        return log_data + ": " + string
