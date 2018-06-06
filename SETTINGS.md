# Hoi there, pirates!

Here's a guide about how to set multibot's triggers:

#### Step 1: The array of objects

In order to provide multiple commands to the bot, the easier way (and the way which is implemented) is to provide an array which in case you don't know it's as simple as this:

```
[
  //your objects here
]
```

the array must contain an object for each bot command... like this!

```
[
  {    
    //your properties for the current command here
  },
  {    
    //your properties for the current command here
  }
]
```

#### Step 2: Mandatory properties (hello world)

So, you want to make your first command? Nothing easier, just add the mandatory properties and the hello world is ready to go!

The mandatory properties are:

- **trigger** , which can be one of the following:
  - botname : The bot will trigger if its name is called
  - /{command} : The bot will trigger every time you call the command you have inserted (e.g. /say)
  - '': The bot will trigger with every command (unless you add extra properties, see step 3)

- **answer**: the text answer that the bot will give once the command's recognized. Can be either a string or an array of strings: both will work! By default the answer will be chosen randomly, see step 3b to change this behaviour! The answer can contain tags to add dynamic data, see step 4

-**priority**: in order to decide the correct answer to give, you must give a priority.
Available priorities are positive integers and zero.
If for instance you create a trigger any ("") and you wish to also have a botname trigger,
the any trigger needs to have priority 0 and the botname trigger needs to have the
priority 1.

Here's an example for the minimum configuration!

```
{
  "trigger" : "botname",
  "answer": "hi!"
  "priority": 0
}
```

And here's an example for the priority:

```
{
  "trigger" : "",
  "answer": "I am listening you!",
  "priority": 0
}
{
  "trigger" : "botname",
  "answer": "hi!",
  priority: 1
}
```

### Step 3a: Extra properties: syntax

You can now set simple triggers, but what about if you want your bot to answer to:
"hi " followed by the bot's name? Or what if you want it to answer to something like
its name followed by " answer me!"?
Well, you can use the two extra properties to enhance the "botname" and the ''
triggers!
The two properties are:

- "trigger_pre": a string containing the string before the botname or the custom strings
passed in trigger.
-"trigger_extra": a string containing the string after the botname or the custom strings
passed in trigger.

You can also use both properties to create a trigger as: "hi, botName! How are you?".

Little sidenote: Right now the matching of the extra properties is loose: the
trigger will trigger if the part before the botname or custom string CONTAINS the
"trigger_pre/extra".

### Step 3b: Extra properties: randomness

Let's assume you want to give your bot multiple answers to a sentence like:
"hi botName!"... how do you manage them?
All you have to do is to make and set a ```"random"``` property to either ```True```
or ```False```.
If random is true the answer will be chosen randomly.
If random is false the answers will be consequential.

### Step 4: Variables in your strings

Great! You now have a bot able to answer to complex sentences, but what if you
were an evil overlord and you wanted to tell your bot to slap someone via "/slap name"?
All you need to do is to set some tags inside your "trigger_pre" or "trigger_extra"!
In this case, since you're using a "/" command you cannot use the "trigger_pre", but
in case you were using either botName or "" as triggers, you could put the tags in your
"trigger_pre".

To set a tag simply write the tag name between "{" and "}"!
To use the tag simply write it (still between "{" and "}") in your answer!
You don't need to use every tag you set (this is useful if you have multiple answers).
