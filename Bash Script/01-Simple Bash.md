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

**Example 8:**
```sh
#!/bin/bash

echo "Enter first number:"
read num1

echo "Enter second number:"
read num2

sum=$((num1 + num2))

echo "The sum of $num1 and $num2 is: $sum"
```
```sh
# Result:
Enter first number:
5
Enter second number:
7
The sum of 5 and 7 is: 12
```

**Example 9:**
```sh
#!/bin/bash

echo "Enter a directory path:"
read dir

if [ -d "$dir" ]; then # Check the validation of directory path
    files=$(ls -1 "$dir" | wc -l) # Count files items in a directory
    echo "The directory '$dir' contains $files items."
else
    echo "Directory does not exist."
fi
```
```sh
# Result:
Enter a directory path:
/home/user/Documents
The directory '/home/user/Documents' contains 8 items.
```

**Example 10:**
```sh
#!/bin/bash

echo "Enter a file path:"
read file

if [ -f "$file" ]; then # Check file existence
    echo "The file '$file' exists."
else
    echo "The file '$file' does not exist."
fi
```
```sh
# Result:
Enter a file path:
/etc/hosts
The file '/etc/hosts' exists.
```

**Example 11:**
```sh
#!/bin/bash

cp /etc/hosts /tmp/hosts.backup

echo "Backup created at /tmp/hosts.backup"
```
```sh
# Result:
Backup created at /tmp/hosts.backup
```

**Example 12:**
* `Scenario` : Backup a directory to a tar file.
```sh
#!/bin/bash

SOURCE_DIR="/home/user/documents"
BACKUP_DIR="/home/user/backups"
DATE=$(date +%Y-%m-%d)

mkdir -p "$BACKUP_DIR"

tar -czf "$BACKUP_DIR/backup-$DATE.tar.gz" "$SOURCE_DIR"

echo "Backup of $SOURCE_DIR completed: $BACKUP_DIR/backup-$DATE.tar.gz"
```
```sh
# Result:
Backup of /home/user/documents completed: /home/user/backups/backup-2025-09-17.tar.gz
```

**Example 13:**
* `Scenario` : We want to delete log files older than 7 days in `/var/log/myapp/` which creates every day.

```sh
#!/bin/bash

LOG_DIR="/var/log/myapp"
DAYS=7

echo "Cleaning up log files older than $DAYS days in $LOG_DIR ..."

find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -exec rm -v {} \;

echo "Cleanup completed!"
```
```sh
# Result:
Cleanup completed!
```

**Example 14:**
* `Scenario` : Delete files older than 30 days from `/temp` directory.
```sh
#!/bin/bash
# Cleanup old temporary files

TEMP_DIR="/tmp"
DAYS=30

echo "Removing files older than $DAYS days from $TEMP_DIR ..."

find "$TEMP_DIR" -type f -mtime +$DAYS -exec rm -v {} \;

echo "Cleanup completed!"
```
```sh
# Result:
Removing files older than 30 days from /tmp ...
removed '/tmp/oldfile1.txt'
removed '/tmp/cache123.tmp'
Cleanup completed!
```

**Example 15:**
* `Scenario` : Count log files.
```sh
#!/bin/bash
# Count number of log files in /var/log

LOG_DIR="/var/log"

count=$(ls -1 "$LOG_DIR"/*.log 2>/dev/null | wc -l)

echo "Number of log files in $LOG_DIR: $count"
```
```sh
# Result:
Number of log files in /var/log: 42
```

**Example 16:**
* `Scenario` : Check directory size.
```sh
#!/bin/bash
# Get the size of /home/user/documents

DIR="/home/user/documents"

size=$(du -sh "$DIR" 2>/dev/null | awk '{print $1}')

echo "Size of $DIR: $size"
```
```sh
# Result:
Size of /home/user/documents: 1.5G
```

**Example 17:**
* `Scenario` : Check status of critical services.
```sh
#!/bin/bash
# Check status of nginx and ssh services

services=("nginx" "ssh")

for service in "${services[@]}"
do
    systemctl is-active --quiet $service
    if [ $? -eq 0 ]; then
        echo "$service is running"
    else
        echo "$service is NOT running"
    fi
done
```
```sh
# Result:
nginx is running
ssh is running
```

**Example 18:**
* `Scenario` : 
```sh

```
```sh
# Result:

```

**Example 19:**
* `Scenario` : 
```sh

```
```sh
# Result:

```



















