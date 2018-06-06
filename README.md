# Multibot for Telegram
##### version: 0.5 (alpha)

### What is Multibot?

This is a simple bot which aims to be easy to configure for simple tasks like [trigger]->[answer].
As the versions get released new functions may be implemented.

### Why would I use Multibot?

Multibot is meant to use for non-programmer people: all you have to do is to configure the ```triggers.json``` file containing the bot's interactions and the api key inside ```config.json```.
Once you've done this you simply have to launch the ```app.py``` python 3 script and the bot will think about the rest!

### How does it work?

Multibot works by matching a string which matches the gramar defined in ```triggers.json``` and giving back the appropriate answer.
At the moment there's no support for complex interactions (function triggering on match), but there will be in the future.

### How do I configure it?

1) install the dependencies (I suggest you using a venv):

via pip:

```
$ pip install telepot
$ pip install telepot --upgrade  # UPGRADE
```

via easy_install:
```
$ easy_install telepot
$ easy_install --upgrade telepot  # UPGRADE
```

2) Use this [guide][guide] to edit this [example file][ef1]. Easy enough!
Also remember to put your api key [here][api]

### Can I use it as a library?

The files are not encrypted and should be easy to use as a library, but unfortunately it's not yet available via pip and it's not structured as a library... I'm planning to full convert it to a library (without removing the easy-to-use repo) right after I implement the complex interactions support.

### Next steps:

1) Full match support
2) Complex interactions support (on sentence match -> call function)
3) Structure the bot as a library and make it available via pip install
4) Custom tags delimiters


[ef1]: <https://github.com/Tails128/Multibot/blob/master/triggers.json>
[guide]: <https://github.com/Tails128/Multibot/blob/master/SETTINGS.md>
[api]: <https://github.com/Tails128/Multibot/blob/master/config.json>
