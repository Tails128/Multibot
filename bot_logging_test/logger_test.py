"""Test the custom logger."""
import os
import random
from bot_logging.logger import Logger


def test_make_log_line():
    """Test the linemaker function."""
    data = "Test result"
    string = "Success!"
    line = Logger.make_log_line(data, string)
    expected = data + ": " + string
    assert line == expected


def test_stdout(capsys):
    """Test the logging on the standard output."""
    test_string = "This is a test"
    Logger.disable_file_log()
    Logger.enable_console_log()
    Logger.log(test_string)
    captured = capsys.readouterr()
    # pylint:disable=protected-access
    expected = Logger.make_log_line(Logger._lastLogData, test_string) + "\n"
    assert expected == captured.out


def test_fileout():
    """Test the logging on the log file."""
    test_string = "This is a test"
    current_dir = os.getcwd()
    file_name = current_dir + "\\testLog"
    while os.path.exists(file_name):
        file_name = current_dir + random.random() + "\\testLog"
    Logger.set_file_name(file_name)
    Logger.disable_console_log()
    Logger.enable_file_log()
    Logger.log(test_string)
    # pylint:disable=protected-access
    expected = Logger.make_log_line(Logger._lastLogData,
                                    test_string) + "\n"

    assert os.path.exists(file_name)
    with open(file_name, "r") as file:
        assert sum(1 for line in file) == 1
    with open(file_name, "r") as file:
        assert file.readline() == expected
    os.remove(file_name)
