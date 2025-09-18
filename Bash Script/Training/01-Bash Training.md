# Bash Training - Session 1

```sh
echo $shell # Display type of Shell
-> /bin/bash
```

### Making the file executable
- The command **chmod** A.K.A change mode is used to change the access permissions of a file 
- you can check the access permissions using ```ls -l ```
```shell
chmod +x ./challenge_one.sh
```

### Running the script 
- /path/to/the/script

```shell
./challenge_one.sh
```

### Hints to remember
- A bash script consists of a series of bash commands 
- In scripting languages like bash, commands are executed line by line and in order
- Always use a shebang(#!) on top of your scripts; if excluded, the defualt shell will be used 
- We write shell scripts to automate our command line interface(CLI)

## Challenge one description

1. **Write a script to print "welcome to this application, dude :)" to the screen (output)**
2. **Make the file executable**
3. **Run the file and get the output**

### Challenge Answer:
```sh
#!/bin/bash

echo "welcome to this application, dude :)"
```







