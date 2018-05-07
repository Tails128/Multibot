# Hoi there, pirates!

Here's a guide about how to set multibot's settings:

#### Step 1: The array of objects

In order to provide multiple commands to the bot, the easier way (and the way which is implemented) is to provide an array which in case you don't know it's as simple as this:

```
[
  //your objects here
]
```

containing an object for each bot command... like this!

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

- **answer**: the text answer that the bot will give once the command's recognized. Can be either a string or an array of strings: both will work! By default the answer will be chosen randomly, see step 3 to change this behaviour! The answer can contain tags to add dynamic data, see step 4

### Step 3: Extra properties

Todo! Be patient!

### Step 4: Variables in your strings

Todo! Be patient!
