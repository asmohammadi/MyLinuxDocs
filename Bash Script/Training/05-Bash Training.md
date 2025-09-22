# Bash Training Session 5:

### Logical Operators:
* `-a` , `&&` : And
* `-o` , `||` : Or
```sh
# Samples:
[ condition1 -o/-a condition2 ]
[ condition1 ] &&/|| [ condition2 ]
[[ condition1 ||/&& condition2  ]]
```

### Files & Directories Operators:
> Existence of :
* `-f` = regular file
* `-e` = any file
* `-d` = directory
* `-b` = block devices
* `-x` `-w` `-r` = file permissions

### Check Empty Streams & Variables:
* `-z` : String is empty 
* `-n` : Variable is empty


### Sample Script:
```sh
#!/bin/bash

: ' 
Using logical operators:

  [ condition1 -o/-a condition2 ], [ condition1 ] &&/|| [ condition2 ]. [[ condition1 ||/&& condition2  ]] 

'
# checks if the given number is between 0 and 10 or not
read -p "give a number between 0 and 10: " number

if [[ "$number" -ge 0 && "$number" -lt 10 ]]; then

   echo "Number is correct and the inputed number is ${number}" 
   exit 0

else 
   echo "Number is not correct becuase ${number} is not between 0 and 10" >&2
   exit 1
fi
: ' 
Heres is a list of file and directory operators you can also check a full version of them on:
https://www.tutorialspoint.com/unix/unix-basic-operators.htm
existence of :
-f = regular file
-e = any file
-d = directory
-b = block devices
-x/ -w/ -r = file permissions
'

read -p "give a path to an existing file: " path

if [[ ! -f "$path" || ! -r "$path" ]]; then
   echo "file is not either a regular file or not readable" >&2
   exit 1
 else
  echo "file exists and is readable"
  exit 0
fi


# if the variable is empty then it will be true. there was an exclaimation mark(!) in the video which 
# posed a problem because it made it flase
# -n is also used but it comes handy when the var is null
if [[ -n "$path" ]]; then

 echo "you haven't entered a path"
 exit 1

fi

#########

if [[ ! -f "$path" || ! -x "$path" ]]; then
   echo "Error : file is not either a regular file or not executable" >&2
   exit 1
else
   echo "file exists and is executable"
   exit 0
fi
```

## Challenge five description

1. ask the user for a number between 0-100
2. validate the number and check if it's entered correctly, otherwise throw an error message and a non-zero code.
3. at this stage, ask the user for a path to an optional file, verify if the file exists or is readable. If it didn't exist or wasn't readable, you should throw an error message and a non-zero code, same as the first step.
4. at last, echo the variable that holds the number for you then redirect it to the path and give the user the path to the file. Exit with zero code. That's it! Good luck!

### Hints to remember

- you can use either `[[ ]]` or `[ ]` when checking for condition but ensure that you know the diffrence.
- when statement includes ||/-o the command will be executed if one of the conditions became True whereas when it comes to &&/-a both conditions must be True.
- `-f` Unix operator, solely checks for regular files but `-e` checks for the existance of all files regardless of their type.
- always use `exit integer` in your commands to call an exit systemcall and throw the exit code.
- you can checkot this [tutorial ](https://www.tutorialspoint.com/unix/unix-basic-operators.htm#)to learn more about Unix operators.

### Challenge Answer:
```sh
#!/bin/bash

read -p "Enter a number between 0 and 100 : " number

# as it's mentioned in the video it's recommended to consider the negative condition but here
# we want to understand the usage of &&
if [[ "$number" -ge 0 && "$number" -lt 100 ]]; then
    echo "Good, your number is ${number}"
    read -p "Now, enter a path to a file that you want the number to be stored in : " path
else 
    echo "Error : please enter a number between 0 and 100!!">&2
    exit 1
fi

if [[ ! -f "$path" || ! -r "$path" ]]; then
    echo "Error : the file is either not existing or not regular or unreadable!!" >&2
    exit 1
else
    echo $number > $path
    echo "Awsome, here is the path to your number: ${path} "
    exit 0
fi 
```




