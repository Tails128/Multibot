"""Test HelpCommand class."""
from base.help_command import HelpCommand


def test_register_commands():
    """Test the registerCommands function."""
    commands = [[{"trigger": "/test",
                  "command_description": "the test works!"}]]
    test_help_command = HelpCommand()
    test_help_command.register_commands(commands)
    assert test_help_command.commands == ["*test*\nthe test works!\n\n"]

def test_add_valid_command_valid():
    """It should add valid commands."""
    command_item = {"trigger": "/test", "command_description": "the test works!"}
    test_help_command = HelpCommand()
    test_help_command.add_valid_command(command_item)
    assert test_help_command.commands == ["*test*\nthe test works!\n\n"]

def test_add_valid_command_invalid_slash():
    """It should not add commands which have a trigger not starting with '/'."""
    command_item = {"trigger": "test", "command_description": "the test works!"}
    test_help_command = HelpCommand()
    test_help_command.commands = []
    test_help_command.add_valid_command(command_item)
    assert test_help_command.commands == []

def test_addValidCommand_invalid_empty():
    """It should not add commands which have no trigger."""
    command_item = {"/help": "test", "command_description": "the test works!"}
    test_help_command = HelpCommand()
    test_help_command.commands = []
    test_help_command.add_valid_command(command_item)
    assert test_help_command.commands == []

def test_parse_command_item():
    """It should parse correctly a command item."""
    command_item = {"trigger": "/test", "command_description": "the test works!"}
    test_help_command = HelpCommand()
    test_help_command.commands = []
    test_help_command.add_valid_command(command_item)
    result = test_help_command.commands[0]
    assert result == "*test*\nthe test works!\n\n"


def test_clean_commands():
    """Test the cleanCommands function."""
    commands = [[{"trigger": "/test",
                  "command_description": "the test works!"}]]
    test_help_command = HelpCommand()
    test_help_command.register_commands(commands)
    test_help_command.clean_commands()
    assert test_help_command.commands == []


def test_get_help_command():
    """Test the test_getHelpCommand function."""
    commands = [[{"trigger": "/test",
                  "command_description": "the test works!"}]]
    test_help_command = HelpCommand()
    test_help_command.register_commands(commands)
    help_command_string = test_help_command.get_help_command()
    assert help_command_string == "*test*\nthe test works!\n\n"
