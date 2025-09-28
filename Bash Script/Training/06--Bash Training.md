# Bash Training Session 6:

* `Case Statements` 
* `Signs` : `&&` , `||` , `;;` , ...
* `Loop`
* `Positional Arguments`

### Case:
> `case` using instead of `if & else`.

### Signs:
* `&` : Run program in background
* `|` : And , or in case statements
* `&&` : If command 1 success, then execute command 2
* `||` : If command 1 success, not execute command 2. If command 1 error, then execute command 2.
* `;` , `:` : Separate commands
* `;;` , `::` : Separate case commands

### Loop:
* `for`
* `while`
* `until`


### Sample Script:
```sh
#!/bin/bash
# This is a Bash script that prompts the user for input and performs various actions based on the input.

read -p "What's your favorite fruit? " fruit
# Prompt the user to enter their favorite fruit and store the input in a variable called "fruit".

case "$fruit" in
apple)
    echo "apple costs you 2$"
    exit 0
    ;;
orange)
    echo "orange costs you 2$"
    exit 0
    ;;
kiwi)
    echo "kiwi costs you 2$"
    exit 0
    ;;
*)  # Anything else
    echo "your fruit is not available in this store." > &2
    exit 1
    ;;
esac
# Check the value of "fruit" and print the cost of the fruit if it is available in the store.
```
```sh
read -p "Enter a file or directory path: " path
# Prompt the user to enter a file or directory path and store the input in a variable called "path".

case "$path" in
    -f*)
        if [ -f "${path:3}" ]; then
            echo "File exists"
            exit 0  
        else
            echo "File does not exist" > &2
            exit 1
        fi
        ;;
    -d*)
        if [ -d "${path:3}" ]; then
            echo "Directory exists"
            exit 0
        else
            echo "Directory does not exist" > &2
            exit 1
        fi
        ;;
    *)
        echo "Invalid input"
        exit 1
        ;;
esac
# Check the value of "path" and print whether it is a file or directory, or print an error message if the input is invalid.
```
```sh
read -p "Enter y or n: " ANSWER
# Prompt the user to enter 'y' or 'n' and store the input in a variable called "ANSWER".

case "$ANSWER" in
    [yY]|[yY][eE][sS])
        echo "You answered yes."
        exit 0
        ;;
    [nN]|[nN][oO])
        echo "You answered no."
        exit 0
        ;;
   *)
        echo "Invalid answer."
        exit 1
        ;;
esac
# Check the value of "ANSWER" and print whether the user answered yes or no, or print an error message if the input is invalid.
```
```sh
for i in 1 2 3 4 5
do
   echo $i
done
# Loop through the numbers 1 to 5 and print them.

while read line
do
   echo $line
done < file.txt
# Read lines from the file "file.txt" and print them.

while [ $number -gt 5 ]
do
   echo $line
   ((number++))
done

until [ -e "example.txt" ]; do
    sleep 1
done
# Wait until the file "example.txt" is created.

echo "File created!"
# Print a message indicating that the file has been created.
```

## Challenge six description

### Part 1: Reading user input and performing actions based on input.

- The script prompts the user to enter their favorite color.
- It then uses a `case` statement to check if the input is a primary color (red, blue, yellow) or a secondary color (green, orange, purple).
- remember (red, blue, yellow) should be accepted case-insesitive.
- The script outputs a message based on the color input.

### Part 2: Looping through a sequence of numbers and outputting them.

- The script uses a for loop to iterate through the numbers 1 to 10.
- It outputs each number to the console using the echo command.

### Hints to remember

- Always add comments to your script to explain what each section is doing. This makes it easier for others to understand your code and for you to come back to it later.
- Use descriptive variable names that are easy to understand. This makes your code easier to read and debug.
- Test your script with different input values to make sure it works as expected.
- Use exit codes to indicate success or failure of your script. An exit code of 0 means success, while any other value means failure.
- Use conditional statements like if/else and case to perform different actions based on the user's input.
- Use loops like for and while to repeat certain actions multiple times.
- Use sleep to pause the execution of your script for a certain amount of time.
- Always validate user input to prevent errors or unexpected behavior.

### Challenge Answer:
```sh
#!/bin/bash

# Prompt the user to enter their favorite color
read -p "Enter your favorite color: " color

# Check if the entered color is a primary color
case "$color" in
    [Rr][Ee][Dd]|[Bb][Ll][Uu][eE]|[Yy][Ee][Ll][Ll][Oo][wW])
        echo "Your favorite color is a primary color."
        ;;

    # Check if the entered color is a secondary color
    green|orange|purple)
        echo "Your favorite color is a secondary color."
        ;;

    # If the entered color is not a primary or secondary color, display an error message
    *)
        echo "Your favorite color is neither a primary nor a secondary color."
        ;;
esac

# Print the numbers from 1 to 10
for i in {1..10}
do
   echo $i
done
```


