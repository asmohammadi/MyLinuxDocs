# 18-Live in the Linux command line

* `head`
* `tail`
* `less`
* `more`
* `cut`
* `paste`

### head:
```bash
head File # Show beginning of the file (By default first 10 lines)
head -n 5 File # Show first 5 lines of the File.
```
### tail:
```bash
tail File # Show end of the file (By default last 10 lines)
tail -n 5 File # Show last 5 lines of the File.
tail -f File # Show and follow (Continuous)
```
### less:
```bash
less File # Show content of File page by page.
```
### more: *(Not recommended)*
```bash
more File # Show content of File page by page with percentage.
```
### cut:
```bash
cut -b # Cutting sections in Bytes.
# Examples:
[root@centos7-1 ~]# echo "linux" | cut -b 1
l
[root@centos7-1 ~]# echo "linux" | cut -b 1,5
lx
[root@centos7-1 ~]# echo "linux" | cut -b 1-4
linu
```
```bash
cut -c # Cutting sections based on Characters.
# Examples:
[root@centos7-1 ~]# echo '♣foobar' | cut -c 1,7
♣r
[root@centos7-1 ~]# echo '♣foobar' | cut -c 5-7
bar
```
```bash
cut -d # Cutting sections based on Delimiters.
cut -f # Cutting sections based on Field.
# Examples:
cat File1.txt
1:a,w
2:b,x
3:c,y
4:d,z
[root@centos7-1 ~]# cut File1.txt -d: -f1
1
2
3
4
[root@centos7-1 ~]# cut File1.txt -d: -f2
a,w
b,x
c,y
d,z
[root@centos7-1 ~]# cut File1.txt -d, -f1
1:a
2:b
3:c
4:d
[root@centos7-1 ~]# cut File1.txt -d, -f2
w
x
y
z
```
### paste:
```bash
paste # Join two files contents side-by-side.
# Example:
cat File1.txt 
a
b
c
d
cat File2.txt
e
f
g
h
[root@centos7-1 ~]# paste File1.txt File2.txt
a    e
b    f
c    g
d    h
```
```bash
paste -d # Join two files content side-by-side with Delimiter.
# Example:
[root@centos7-1 ~]# paste -d: 1.txt 2.txt
a:e
b:f
c:g
d:h
```






