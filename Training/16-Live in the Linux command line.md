# 15-Live in the Linux command line

* `cat`
* `tac`
* `tr`
* `nl`

### cat:
```bash
cat File1
cat > File1 # Write in the file before open it. Until`Ctrl+d`.
cat File1 File2 > File3 # Merge Files to another File.
cat File1 - File2 > File3 # Write anything between merging two files.
cat -n File1 # Show content with all line numbers.
```
### tac:
```bash
tac File1 # Reverse cat.
```
### tr:
```bash
tr # Translate
#Example1:
echo "This is for test" | tr is IS # Replace every 'i' & 's' with 'I' & 'S'.
"ThIS IS for teSt"
#Example2:
echo "This is for test" | tr is TZ # Replace every 'i' & 's' with 'T' & 'Z'.
"ThTZ TZ for teZt"
#Example3:
echo "this is for test" | tr [:lower:] [:upper:] # Replace all lowercase to uppercase.
"THIS IS FOR TEST"
#Example4:
echo "this is for test" | tr [:space:] "\t" # Replace all spaces with TAB.
"this   is  for     test"
#Example5:
echo "this is for test 123456" | tr -d [:digit:] # Delete all digits.
"this is for test"
#Example6:
echo "this is for test 123456" | tr -dc [:digit:] # Delete all except digits.
"123456"
```
### nl:
```bash
nl -n File1 # Show content with line numbers except Empty lines.
```







