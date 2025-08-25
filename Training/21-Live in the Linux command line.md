# 21-Live in the Linux command line

### Wildcards & Globbing:

> `?` **is used to match any single character.** We can use `?` for multiple times for matching multiple characters.
```bash
# Example:
ls ???.txt # Any files that has 3 characters.

aaa.txt
```

> `*` **is used to match zero or more characters.** If we have less information to search any file or information then we can use `\*` in globbing pattern.
```bash
# Example:
ls *.txt # Any file with ".txt" format.

aaa.txt  ababa.txt  bbbb.txt
```

> `[ ]` **is used to match the character from the range.** Some of the mostly used range declarations are mentioned below:

- `[A-Z]` => All uppercase alphabets
- `[a-z]` => All lowercase alphabets
- `[a-zA-Z0-9]` => All uppercase alphabets, lowercase alphabet and digits

> The `-` character between two others represents a range that includes the two other characters and all characters between them in the collating sequence.
```bash
# Example:
ls [e-z]* # Any files including characters from 'e' to 'z' and any other characters after them.

file1  file2
```

> **The `!` character means NOT, so it matches any character except the remaining characters.**
```bash
# Example:
ls [!e-z]* # Any files NOT including characters from 'e' to 'z' and any other characters after them.

aaa.txt  ababa.txt  bbbb.txt
```

> `{ }` **can be used to match filenames with more than one globbing patterns. Each pattern is separated by comma `,` in curly bracket without any space.**
```bash
# Example:
ls {???.txt,????.txt} # Any files which have 3 or 4 characters with ".txt" format.

aaa.txt  bbbb.txt
```
```bash
# Example:
`rm {*.doc,*.docx}` # Delete all files whose extensions are ‘doc’ or ‘docx’.
```
### find:
> The `find` command searches for files or directories using all or part of the name, or by other search criteria, such as size, type, file owner, creation date, or last access date.

```sh
find Starting/Path Options Expression
```
```sh
# Example:
find /etc/ -iname "[y-z]*" # Find all files under /etc/ directory, beginning with 'y' & 'z'.

/etc/xdg/autostart/zeitgeist-datahub.desktop
/etc/zsh_command_not_found
/etc/vmware-tools/messages/zh_TW
/etc/vmware-tools/messages/zh_CN
/etc/dhcp/dhclient-exit-hooks.d/zzz_avahi-autoipd
/etc/kernel/postrm.d/zz-update-grub
/etc/kernel/postinst.d/zz-update-grub
/etc/brltty/Contraction/zu.ctb
/etc/brltty/Contraction/zh-tw-ucb.ctb
/etc/brltty/Contraction/zh-tw.ctb
```
* `-name` => Searching for files.
* `-i` => Case insensitive.

#### Finding files by type:
* `-type f` : Find file
* `-type d` : Find directory
* `-type l` : Find symbolic link

```bash
find /etc -name wgetrc
find /etc -iname WgetRC # No matter case sensitivity
find / -type f -name file
find / -type d -name dir
find / -type f -user root
find / -type f -empty
find / -type f -perm 777
find / -type f -perm /u=s
find / -type f -user user1 -exec rm -rf {} \;
find / -type f -user user1 -exec cp {} /tmp/user1/ \;
find / -type f -size +50M
find / -type f -size +50M -size -100M
find . -lname l1
```
```bash
find / -name milad
find / -iname Milad
find / -name "file*"
find / -name "*.conf" -type f -atime -ctime -mtime -user -group -maxdepth (-o|-a --> and or)
find . -name "*.conf" -exec cp {} /tmp/config/ \;
find . -name "*.conf" -exec rm -rf {} \;
find / -name "*.conf" -type f -mtime +5 -user root -group root -size +10K -exec cp {} /tmp/config/ \;
find / -name "*.conf" -type f -mtime +5 -user root -group root -size +10K -delete
```
```bash
# Example:
find / -iname *.pdf -exec cp {} /opt/pdf/ \; # Find all ".pdf" files and copy all to /opt directory. 
find / -iname *.pdf -exec rm -rf {} \; # Find all ".pdf" files and delete all of them.
find /etc/ -type f -size +10m # Find all files with size more than 10MB.
find /etc/ -type f -size +1m -size -10m # Find all files with size more than 1Mb & less than 10Mb. Between 1Mb to 10Mb.
find / -empty # Find all empty files.
find / -cmin 120 # Find all files which has been changed in less than 120 minutes ago.
```

### file:
```bash
file FileName # Show the type of data in files.
```









