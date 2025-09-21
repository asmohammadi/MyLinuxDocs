# Bash Training Session 3:


### <<EOF:
```sh
cat > test # End writing with Ctrl+d
cat <<EOF # When writing EOF it will end the file.
```
```sh
#!/bin/bash

apt update &> /dev/null
# or:
apt update > /dev/null 2> /dev/null
# or:
apt update > /dev/null 2>&1
# or:
apt update 2>&1 /dev/null
```
* This script will not save output or error.

```sh
#!/bin/bash

apt update 2> error.txt > output.txt
(ls -z ; ls -l) 2> Error.txt > Output.txt
(ls -z ; ls -l) > Output.txt 2>&1 
```
* Separate errors & output. 

### Exit code:
* `exit code` : 0-255
* `0` : Done without error
```sh
echo $? # Get exit code
```

## Challenge three description
1. echo the usage of comments and try using a multi-line comment
2. inside your main script write another script named exit_code.sh to do an optional task using  <<EOF 
   - then make the file executable. Ensure that each part is specified 
3. install Nginx and get the first 3 lines of its conf using pipes.
4. initialize a git directory somewhere in your system and add READ + LICENSE then use `git add .` .
finally, commit them using `commit -m " initail commit"` . (optional)
- You can certainly play with the output (redirection) of each command if needed :)

### Hints to remember
- `cmd &> /dev/null`, `cmd > /dev/null 2>&1` and `cmd > /dev/null 2> /dev/null` are identical.
- `2>&1` is considered and read from **right to left** not left to right 
- if the return (exit) code of an operation is non-zero it has failed otherwise, it's been successful. 
- you can use `<<EOF` with pipe as well.

### Challenge Answer:
```sh
#!/bin/bash

#part 1
# This is a comment
echo "comments explains what's going on in your code
it improves readability, and specifies a block of code." > /dev/null # This is also a comment but not a good practice

: '
 this a multi-line comment
 you can comment multiple line of code or comment
 using this or <<whatever
 whatever is optional you can replace it with anything else but
 make sure you end it with the same word like the following line.
 whatever

'

#part 2
# creating a directory to store a multi-line script written using <<EOF
mkdir -p ~/test_challenge

cat <<EOF > ~/test_challenge/exit_code.sh
#/bin/bash
# making a directory in /boot and printing the exit code of this operation
mkdir -p /boot/got_denied_huh
echo $?
EOF

# making the file executable
chmod +x ~/test_challenge/exit_code.sh

#part3
# initializing a git directory
mkdir -p /tmp/git_dir
cd $_
git init > /dev/null 2> /dev/null
touch README.md
echo this is a README file > README.md
touch LICENSE
echo this an invalid LICENSE file > LICENSE
git add . > /dev/null 2>&1
git commit -m "initial commit" &> /dev/null

# part4
# install Nginx and get the first 3 lines of its conf using pipes
sudo apt update &> /dev/null
sudo apt install -y nginx &> /dev/null
cat /etc/nginx/nginx.conf | head -n 3
```

```sh
#!/bin/bash

# uses EOF to write a bash script that prints system information
cat <<EOF > /home/shayan/Desktop/system_info.sh
#!/bin/bash
uname -a
EOF

# making the file executable
cd ~/shayan/Desktop/
chmod +x ./system_info.sh

# all of these tasks uninstall docker and redirect both stderr and stdout to /dev/null
apt autoremove --purge docker &> /dev/null
apt autoremove --purge docker > /dev/null 2>&1
apt autoremove --purge docker > /dev/null 2> /dev/null

# lists all allowed ports on ufw firewall and then stores its exit code in `exit_code`
ufw status
echo $? > exit_code
```







