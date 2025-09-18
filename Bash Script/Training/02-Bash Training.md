# Bash Training - Session 2

### Standard Streams:
* `STDIN` : Standard Input -> 0
* `STDOUT` : Standard Output -> 1
* `STDERR` : Standard Error -> 2

* `File Descriptor` : When we run a command it will execute an APP, then the APP will start a process, then this process will create a file which has a number that will save some where in a system. This number is `File Descriptor`.

```sh
#!/bin/bash

apt update > stdout.txt
```
* This script will save output in stdout.txt, but will display the error after running the script.
* It will not save th error output in a file.

```sh
claer 2> error.txt # It will save the error output in a error.txt file.
```
```sh
cat error.txt >> output.txt # Append output to the output.txt
```
```sh
#!/bin/bash

apt update 2> error.txt
```
* This script will save the error in error.txt file.
* But it will display the output of running script in terminal.

```sh
#!/bin/bash

apt update &> out-error.txt
```
* This script will save both output & error in out-error.txt file.

```sh
#!/bin/bash

apt update > stdout.txt 2> error.txt
```
* This script will save output to stdout.txt file & save error to error.txt file.

```sh
#!/bin/bash

apt update &> /dev/null
```
* This script will not save output or error.


### Hints to remember
- you input a command and you get an output; what you have entered using your keyboard is called stdin and what get as an output is called stdout.
- if the command generated an error then the error output is called stderr. 
- In very simple terms, file descriptor A.K.A fd is an integer number somewhere on the OS that represents every file that is opened by a process.
- `/proc/PID/fd` is the path which you can check FDs that belongs to a process where PID is the Process Identifier.
- We write shell scripts to automate our command line interface(CLI)

## Challenge two description

1. echo "this is a message to be stored in a file" then redirect its output to a file of your choice.
2. run a command that performs a task and redirect both of its error and output to the trash.
3. cat a file of your choice and get the last 3 lines of it.
- you may use tail with a suitable flag to do such a thing. 

### Challenge Answer:
```sh
#!/bin/bash

#part 1
echo "this is a message to be stored in a file" > optional_file

#part 2
# redirect both stderr and stdout to /dev/null
apt upgrade &> /dev/null

#part 3
# list upgradabe packages and redirect stdout to 'test' and sterr to /dev/null
apt list --upgradable > test 2> /dev/null

#to get the last three lines of a file where -n is the number of the lines 
tail -n 3 test >  lines
```














