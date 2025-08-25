# 14-Live in the Linux command line

### History:
```bash
/home/.bash_history # All history of commands save in this file.
```
* `!!` **BangBang** -> Execute Previous Command 
* `!cat`  -> Execute previous command begins with cat
* `Ctrl + r` -> Search in previous commands

```bash
history -c # Clear the history
or
> .bash_history # Clear the history file
```
### uname: 
```sh
uname # Show Kernel Type (Linux/Unix)
uname -r # Show Kernel release
uname -i # Show Hardware Platform
uname -a # Show all information
```

* `>` **Redirect/Rewrite** -> Write the result to a file 
```sh
> File1  # Empty the File1
> .bash_history # Empty .bash_history file.
```

* `>>` **Append** -> Append result to the file

* `|` **Pipline** -> Give the output of the first command to another command
```bash
dmesg | less # Read dmesg file with less.
cat bash.bashrc | wc -l # Count the line numbers of the bash.bashrc file.
```
* **Input (STDIN)** => `0` , `<`
* **Output (STDOUT)** => `1` , `>`
* **Error (STDERR)** => `2` , `2>`










