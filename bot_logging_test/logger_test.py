"""Test the custom logger."""
import sys
import os
import random
sys.path.append(os.getcwd() + "/bot_logging")
from bot_logging.logger import Logger


def test_makeLogLine():
    """Test the linemaker function."""
    data = "Test result"
    string = "Success!"
    line = Logger.make_log_line(data, string)
    expected = data + ": " + string
    assert line == expected


def test_stdout(capsys):
    """Test the logging on the standard output."""
    testString = "This is a test"
    Logger.disable_file_log()
    Logger.enable_console_log()
    Logger.log(testString)
    captured = capsys.readouterr()
    expected = Logger.make_log_line(Logger._lastLogData, testString) + "\n"
    assert expected == captured.out


def test_fileout():
    """Test the logging on the log file."""
    testString = "This is a test"
    currentDir = os.getcwd()
    fileName = currentDir + "\\testLog"
    while(os.path.exists(fileName)):
        fileName = currentDir + random.random() + "\\testLog"
    Logger.set_file_name(fileName)
    Logger.disable_console_log()
    Logger.enable_file_log()
    Logger.log(testString)
    expected = Logger.make_log_line(Logger._lastLogData,
                                         testString) + "\n"

    assert os.path.exists(fileName)
    with open(fileName, "r") as file:
        assert sum(1 for line in file) == 1
    with open(fileName, "r") as file:
        assert file.readline() == expected
    os.remove(fileName)
