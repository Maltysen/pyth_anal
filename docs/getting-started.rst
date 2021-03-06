1. Getting Started
******************

Pyth is a language created by `PPCG <http://codegolf.stackexchange.com>`_ (Programming Puzzles and Code Golf) user `Isaacg <http://codegolf.stackexchange.com/users/20080/isaacg>`_. It is meant to be a golfing language based on python (notice the name), and unlike most golfing languages is fully procedural. Notable for its unreadability, it can be very effective for golfing purposes if used properly. Since Pyth is quite young, its features are constantly changing, and this document might be out of date for a few functions (Just check the source). Pyth is licensed under the `MIT license <http://opensource.org/licenses/MIT>`_.

1.1. How to Start Programming in Pyth
=====================================
Now that you know a little about Pyth, you must be wondering how on earth to start programming in it. Well there are a few options. You could install it on you machine by cloning `the repository <https://github.com/isaacg1/pyth>` then adding this alias to your .bashrc::

	alias pyth="python3 <path to pyth>/pyth.py"

(Windows users, you'll have to use the PATH and call ``pyth.py``)

But the method we will be using in the tutorial, and the suggested one, is to use the online interpreter at http://pyth.herokuapp.com. This provides a programming environment (with a handy function cheat-sheet) with places in which to put code and input. The code is executed on the server and sent back to the webpage. The examples won't be much different if you decide to install the interpreter yourself, and in fact this will become necessary later down the road, when we start conducting "unsafe" operations which allow for arbitrary execution of code. More detailed explanations will be provided then.

Now let's start programming.

1.2. Hello World!
=================

A customary start to programming tutorials is the "Hello World Program" which consists of printing out the text "Hello World!". We will be doing this task as our first example. Now, since Pyth *is* a golfing language, let's golf it, and in the process demonstrate some key features of Pyth. So without further ado, here is our first program::

	"Hello World!

Type this into the code textbox, leave the input box empty, click the run button and see what happens. The results (in the output box) should look something like this::

	Hello World!

Well that went pretty much as expected, but if you have any experience with other programming languages, you'll notice a few interesting things about the program.

#. Printing is implicit (Just name a value or identifier and it will be printed).
#. Quotes are automatically closed at the end of the program.

These features are obviously beneficially for reducing the length of your programs. Another thing you should know early on if you decide to go experimenting on your own is that programs in Pyth are typically only one line long. Statement separation is typically achieved through semicolons: ``;``.

Next up is learning more about the language.
