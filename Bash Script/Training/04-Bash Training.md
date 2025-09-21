# Bash Training Session 4:

### Variables:
* `Local Variables`
* `Shell Variables`
* `Environment Variables`

### Local Variables:
```sh
variable_name="value"
name="Amir"
age=25
NAME="Ali" # Capital used when we want to export the variable as an Environment Variable
echo "Your name is $name, and you are $age years old." # Calling the variable
```
```sh
# Put anything beside the variable:
echo "Your family name is ${name}i ."
Your family name is Amiri.
```
```sh
# Get variable from a message:
read -p "Message" Variable
# Example:
read -p "what is your name?" name

what is your name? Ali
Ali

# With echo:
echo "Message"
read Variable
# Example:
echo "how old are you?"
read age

what is your name? Ali
how old are you?
25
Ali 25
```

### Shell & Environment Variables:
> Available only on the same session and its child processes.
```sh
# Make a Shell Variable into an Environment Variable:
export NAME=Asghar
echo $NAME
Asghar
```

### IF:
```sh
# Structure:
if [ condition ]; then
echo "what you want to do"
else
echo "something else"
fi
```
```sh
# Example:
read -p "what is your name?" name
echo "how old are you?"
read age
echo $name $age
age=25
if [ $age -gt 18 ]; then
echo "You are adult."
else
echo "You are not eligible."
fi
```
#### Arithmetic Operators:
* `-lt` : Less than
* `-gt` : Grater than
* `-eq` : Equal
* `-ne` : Not equal
* `-ge` : Grater or Equal
* `-le` : Less or Equal

#### String Operators:
* `=` : Equal
* `!=` : Not Equal


### Sample Script:
```sh
#!/bin/bash

variable_name="value"

name="Amir"
age=25
# NAME="Amir"

# echo "your family name is ${name}i, and you are ${age} years old"

# This is how you can do basic math and operation and store it on a variable
val=`expr 2 + 2`
echo "Total value : $val"

# as said in the video you can store output of commands, too. use $()
number_of_files=$(ls -l | wc -l)
echo "there are ${number_of_files} in this directory"

# read -p "what's your name? " name
# echo "how old are you? "
# read age
# echo $name $age     

# ----------------------------------------------------------------

# if [ condition ]; then
#  echo "this what you would like to do"

# fi
age=18
name="SHAYAN"
if [ $age -lt 18 ]; then
echo "you are not eligible, since you are ${age} years old"
elif [ $name != "Ehsan" ]; then
echo "you are not eligible, since you are ${name} not Ehsan"
else
 echo "welcome to the club"
fi

# ----------------------------------------------------------------

#arithmetic opretors
# -lt -gt -eq -ne -ge -le

#string opretors
# =, != 
```

## Challenge four description
1. ask the user about their age and major then store them in variables, AGE and MAJOR.
2. check if they are 18 or above and echo "you are not old enough!" if they are not.
3. if they were older than 18 (passed the first test)
check if their major is "Engineering" (elif) then tell them "You have to study Engineering to be part of us, it doesn't seem so :))"
4. otherwise, echo "You can take part for sure!"

### Hints to remember
- when defining variables you must not have any space around = (equall sign).
- if you use variable with extra data such as String(concatenation) you should enclose the variable like `"some data ${variable_name}, some other data"`
- variables are case sensitive and you should define them with UPPERCASE when declaring a shell or environment varaiable. 
- arithmetic operators including ` -ne, -eq, -gt, -lt,etc` are solely used for checking numbers.
- leave some space in condition part when using if and elif is neccessary.

### Challenge Answer:
```sh
#!/bin/bash

#part 1
read -p "What's your Major? (e.g Engineering) " major

read -p "How old are you? " age 

#part 2 & 3
# always check the negative case, since it reduces the number of conditions 
if [ "$age" -lt 18 ]; then
    echo "Sorry, you are not old enough!" >&2
    exit 1
elif [ "$major" != "Engineering" ]; then
    echo "You have to study Engineering to be part of us, it doesn't seem so :))" >&2
    exit 1
else
    echo "You can take part for sure!"
    exit 0
fi
```


