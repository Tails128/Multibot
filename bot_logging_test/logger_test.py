"""Test the custom logger."""
import sys
import os
import random
sys.path.append(os.getcwd() + "/logging")
from logger import Logger


def test_makeLogLine():
    """Test the linemaker function."""
    data = "Test result"
    string = "Success!"
    line = Logger.makeLogLine(data, string)
    expected = data + ": " + string
    assert line == expected


def test_stdout(capsys):
    """Test the logging on the standard output."""
    testString = "This is a test"
    Logger.disableFileLog()
    Logger.enableConsoleLog()
    Logger.log(testString)
    captured = capsys.readouterr()
    expected = Logger.makeLogLine(Logger._lastLogData,
                                         testString) + "\n"
    assert expected == captured.out


def test_fileout():
    """Test the logging on the log file."""
    testString = "This is a test"
    dir = os.getcwd()
    fileName = dir + "\\testLog"
    while(os.path.exists(fileName)):
        fileName = dir + random.random() + "\\testLog"
    Logger.setFileName(fileName)
    Logger.disableConsoleLog()
    Logger.enableFileLog()
    Logger.log(testString)
    expected = Logger.makeLogLine(Logger._lastLogData,
                                         testString) + "\n"

    assert os.path.exists(fileName)
    with open(fileName, "r") as file:
        assert sum(1 for line in file) == 1
    with open(fileName, "r") as file:
        assert file.readline() == expected
    os.remove(fileName)
