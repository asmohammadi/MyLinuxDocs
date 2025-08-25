# 17-Live in the Linux command line

* `sort`
* `uniq`
* `split`
* `wc`

### sort:
```bash
sort # Sort the content of file(By default Alphabetical)
sort -n File # Sort numeric
```
Sorting Priority:
* Empty lines
* Lowercase
* Uppercase
* Numbers

### uniq:
```bash
uniq # Remove repeated lines.
# Used just for sorted content.
sort File1 | uniq # Sort & then remove repeated lines.
sort File1 | uniq -c # Sort & count the number of repeated lines.
sort File1 | uniq -d # Sort & show duplicated lines.
sort File1 | uniq -d -c 
sort File1 | uniq -u # Sort & show just uniq lines.
```
```bash
# Example:
 sort -n /var/log/nginx/access.log | grep 192.168.64.1 | uniq -c
```
### split:
```bash
split -l # Split by Line
split -b # Split by Size(Byte)
```
```bash
# Example1:
split -l 10 File1 # Split File1 and put each 10 line in one new file.

root@server:~# ls -lh
-rw-r----- 1 root root  12K May 28 18:35 access.log
root@server:~# split -l 10 access.log access.log_output
root@server:~# ls -lh
-rw-r----- 1 root root  12K May 28 18:35 access.log
-rw-r--r-- 1 root root 2.2K May 28 18:36 access.log_outputaa
-rw-r--r-- 1 root root 2.2K May 28 18:36 access.log_outputab
-rw-r--r-- 1 root root 2.2K May 28 18:36 access.log_outputac
-rw-r--r-- 1 root root 2.2K May 28 18:36 access.log_outputad
-rw-r--r-- 1 root root 2.2K May 28 18:36 access.log_outputae
-rw-r--r-- 1 root root 1.1K May 28 18:36 access.log_outputaf
```
```bash
# Example2:
split -b 2K File1 # Split File1 to 2K size files.

root@server:~# ls -lh
-rw-r----- 1 root root  12K May 28 18:35 access.log
root@server:~# split -b 2k  access.log access.log_output
root@server:~# ls -lh
-rw-r----- 1 root root  12K May 28 18:35 access.log
-rw-r--r-- 1 root root 2.0K May 28 18:52 access.log_outputaa
-rw-r--r-- 1 root root 2.0K May 28 18:52 access.log_outputab
-rw-r--r-- 1 root root 2.0K May 28 18:52 access.log_outputac
-rw-r--r-- 1 root root 2.0K May 28 18:52 access.log_outputad
-rw-r--r-- 1 root root 2.0K May 28 18:52 access.log_outputae
-rw-r--r-- 1 root root 1.8K May 28 18:52 access.log_outputaf
```
### wc:
```bash
wc # Word Count (Number of Lines, Words & Bytes)
wc -l # Count lines
wc -l File
```







