# 14-Live in the Linux command line

### Echo Examples:
```bash
root@server:~# echo -n devops linux
devops linuxroot@server:~# echo -e devops linux
devops linux
root@server:~# echo -e "devops \n linux"
devops
 linux
root@server:~# echo -e "devops \nlinux"
devops
linux
root@server:~# echo -e "devops \tlinux \tubuntu"
devops  linux   ubuntu
root@server:~# echo -e "devops \vlinux \vubuntu"
devops
       linux
             ubuntu
```

* **`-n` -> No Enter**
* **`-e` -> With Enter**
* **`\n` -> Enter one line**
* **`\t` -> Enter Tab Horizontal**
* **`\v` -> Enter Tab Vertical**
* **`;`  Semi-Colon** => Go to next command regardless of the result
* **`&&`  Logical AND** => If the first command done correctly execute the next command
* **`||`  Logical OR** => If the first command done correctly don't execute the next command;
If the first command failed then execute the next command
* `echo $$` -> Show the process ID of current bash  





