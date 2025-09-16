# Simple Bash Scripts:

**ٍExample 1:**
```sh
#!/bin/bash

echo "Hello! This is our first Bash Script :)"
```
```sh
# Result:
Hello! This is our first Bash Script :)
```

**Example 2:**
```sh
#!/bin/bash

echo "What is your name?"
read name
echo "Hello, $name! Welcome to Bash scripting."
```
```sh
# Result:
What is your name?
Ali
Hello, Ali! Welcome to Bash scripting.
```

**Example 3:**
```sh
#!/bin/bash

echo "What is your name?"
read name

echo "How old are you?"
read age

echo "Hello, $name! You are $age years old."
```
```sh
# Result:
What is your name?
Sara
How old are you?
25
Hello, Sara! You are 25 years old.
```

**Example 4:**
```sh
#!/bin/bash

echo "What is your name?"
read name

echo "How old are you?"
read age

if [ $age -ge 18 ]; then # If age is greater than or equal 18
    echo "Hello, $name! You are an adult."
else
    echo "Hello, $name! You are not an adult yet."
fi
```
```sh
# Result:
# Greater than 18:
What is your name?
John
How old are you?
20
Hello, John! You are an adult.
# Lower than 18:
What is your name?
Anna
How old are you?
15
Hello, Anna! You are not an adult yet.
```

**Example 5:**
```sh
#!/bin/bash

echo "Counting from 1 to 5:"

for i in 1 2 3 4 5
do
    echo "Number: $i"
done
```
```sh
# Result:
Counting from 1 to 5:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```
**Example 6:**
```sh
#!/bin/bash

colors=("Red" "Green" "Blue" "Yellow")

echo "Printing colors:"

for color in "${colors[@]}"
do
    echo "Color: $color"
done
```
```sh
# Result:
Printing colors:
Color: Red
Color: Green
Color: Blue
Color: Yellow
```
**Example 7:**
```sh
#!/bin/bash

colors=("Red" "Green" "Blue" "Yellow")

echo "Printing only colors starting with B:"

for color in "${colors[@]}"
do
    if [[ $color == B* ]]; then
        echo "Color: $color"
    fi
done
```
```sh
# Result:
Printing only colors starting with B:
Color: Blue
```











