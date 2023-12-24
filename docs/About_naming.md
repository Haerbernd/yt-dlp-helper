# About naming

In this file, I will explain to you the way I name my scripts, functions, classes, variables, etc. so that you can
understand their function, form and or anything else that you should know about them.

## About files/scripts

### Their location

Usually you can only find the most important files of a project directly in the "root directory" of it. I try to store
as many as possible in subdirectories but still in a way that makes sense.

### Their names

The name of a file or script is meant to be as obvious to its content or function as possible.
Generally, I adhere to the snake_case naming convention of files (replacing whitespaces with underscores), or
sometimes I replace whitespaces with dashes.

I only seldom use the camelCase naming convention (no spaces between words, and every word starts with a capital letter
except the first -> e.g.: thatIsAnExampleForCamelCase) for files or scripts,
but it is my standard for keys in json files.

## About names inside scripts

### General Rules

I name everything except comments, classes and the exception talked below about after the snake_case naming convention
(replacing whitespaces with underscores).
Classes are named in PascalCase (like camelCase, but the first word is capitalized) and comments are more or less whole
sentences.

Another interesting aspect is that variable names that appear inside and outside a function but hold different values
are named different. Most of the time I try to use synonyms but when I don't find any or don't like them, I do the
following: the variable outside the function keeps its name while the variable inside the function gets and `_f` added
to its name at the end.

I adhere to the above-mentioned method even when renaming the variable would technically not be needed as to 1. prevent
confusion and 2. stop PyCharm from annoying me with the "variable out of scope" warning.

#### The Exception of (Py)QT in naming

Functions and classes as well as some imports that are tied to (Py)QT are named not after my normal (and for python
standard) snake_case naming convention but after the for C-based programming languages common naming convention of 
camelCase (no spaces between words and every word starts with a capital letter except the first -> e.g. 
thatIsAnExampleForCamelCase).