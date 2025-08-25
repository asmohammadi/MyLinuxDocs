# 19-Live in the Linux command line

* `sed`
* `tee`
* `grep`

### sed:
```bash
sed # (Stream Editor)Replace some text in a file without opening the file.
sed "s/yes/NO/g" sshd_config # (Preview) Search in File and replace all "yes" with "NO".
sed "s|yes/NO|g" sshd_config # (Preview) Search in File and replace all "yes" with "NO".
sed -i "s/yes/NO/g" sshd_config # (In-place Edit) Search in File and replace all "yes" with "NO".
sed -i "64s/yes/NO/g" sshd_config # Change & replace "yes" with "NO" in Line 64.
sed -i "63,64s/yes/NO/g" sshd_config # Change & replace "yes" with "NO" in Line 63 & 64.
sed -i "s/yes/NO/g" /etc/ssh/sshd_config # Change & replace "yes" with "NO" in specific file in a PATH.
sed "YES/d" sshd_config # Search & Delete all line with "YES".
```
* `s/` => Search and replace
* `/g` => Global
* `/d` => Delete
* `-i` => In-place editing
* `Number` => Line Number/Numbers
* `|` => Used as a Delimiter.

### tee:
```bash
tee # Show & Put the result of a command to a file.
ls -l | tee lsfile.txt
```
### grep:
```bash
grep # Find text in files content & show all the lines matches. (By default case sensitive)
grep "YES" sshd_config # Find & show all "YES" in the file.
grep -i "YES" sshd_config # Ignore case sensitivity.
grep -i "YES" File1 File2 # Find "YES" in Multiple Files.
grep -i -n "YES" File1 File2 # Find & show the line numbers.
grep -i -c "YES" File1 File2 # Find & Count results.
grep -i -n -v "YES" sshd_config # Find those are not match.
grep -i -n -r "YES" /etc/ssh/ # Find in all files in a directory.
grep -i -n -w "YES" sshd_config # Find the exact word.
grep -B1 "YES" sshd_config # Find & show with one line before it.
grep -A1 "YES" sshd_config # Find & show with one line after it.
grep -C1 "YES" sshd_config # Find & show with one line After & one line Before.
```
* `-i` => Ignore Case Sensitive
* `-n` => Line Number
* `-c` => Count
* `-v` => Verse mode (Find those are not match)
* `-r` => Recursive (In directory)
* `-w` => Exact Word
* `-B1` => Show with one line before.
* `-A1` => Show with one line After.
* `-C1` => Show with one line After & one line Before.





