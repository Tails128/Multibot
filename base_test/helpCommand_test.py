"""Test HelpCommand class."""
import sys
import os
sys.path.append(os.getcwd() + "/base")
from base.helpCommand import HelpCommand


def test_registerCommands():
    """Test the registerCommands function."""
    commands = [[{"trigger": "/test",
                 "command_description": "the test works!"}]]
    testHelpCommand = HelpCommand()
    testHelpCommand.registerCommands(commands)
    assert testHelpCommand.commands == ["*test*\nthe test works!\n\n"]

def test_addValidCommand_valid():
    """It should add valid commands."""
    commandItem = {"trigger": "/test", "command_description": "the test works!"}
    testHelpCommand = HelpCommand()
    testHelpCommand.addValidCommand(commandItem)
    assert testHelpCommand.commands == ["*test*\nthe test works!\n\n"]

def test_addValidCommand_invalid_slash():
    """It should not add commands which have a trigger not starting with '/'."""
    commandItem = {"trigger": "test", "command_description": "the test works!"}
    testHelpCommand = HelpCommand()
    testHelpCommand.commands = []
    testHelpCommand.addValidCommand(commandItem)
    assert testHelpCommand.commands == []

def test_addValidCommand_invalid_empty():
    """It should not add commands which have no trigger."""
    commandItem = {"/help": "test", "command_description": "the test works!"}
    testHelpCommand = HelpCommand()
    testHelpCommand.commands = []
    testHelpCommand.addValidCommand(commandItem)
    assert testHelpCommand.commands == []

def test_parseCommandItem():
    """It should parse correctly a command item."""
    commandItem = {"trigger": "/test", "command_description": "the test works!"}
    testHelpCommand = HelpCommand()
    testHelpCommand.commands = []
    testHelpCommand.addValidCommand(commandItem)
    result = testHelpCommand.commands[0]
    assert result == "*test*\nthe test works!\n\n"


def test_cleanCommands():
    """Test the cleanCommands function."""
    commands = [[{"trigger": "/test",
                 "command_description": "the test works!"}]]
    testHelpCommand = HelpCommand()
    testHelpCommand.registerCommands(commands)
    testHelpCommand.cleanCommands()
    assert testHelpCommand.commands == []


def test_getHelpCommand():
    """Test the test_getHelpCommand function."""
    commands = [[{"trigger": "/test",
                 "command_description": "the test works!"}]]
    testHelpCommand = HelpCommand()
    testHelpCommand.registerCommands(commands)
    helpCommandString = testHelpCommand.getHelpCommand()
    assert helpCommandString == "*test*\nthe test works!\n\n"
