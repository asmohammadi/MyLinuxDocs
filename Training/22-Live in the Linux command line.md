# 22-Live in the Linux command line

* `zip`
* `unzip`
* `gzip`
* `gunzip`
* `bzip2`
* `bunzip2`
* `xz`
* `tar`
* `dd`

### zip:
```bash
zip ZipFile.zip file.txt
zip -r ZipDir.zip /dir/ # Recursive
zip -v filename.zip file.txt # Verbose mode
zip -d filename.zip file.txt # Removes the file from the zip archive
zip -u filename.zip file.txt # Updates the file in the zip archive
zip -m filename.zip file.txt # Deletes the original files after zipping
zip -x filename.zip file_to_be_excluded # Exclude the files in creating the zip
```

### unzip:
```bash
unzip ZipFile.zip
```

### gzip:
> `Gzip (GNU zip)` is a compressing tool, which is used to truncate the file size. 
> By default original file will be replaced by the compressed file ending with extension (.gz) and `gzip` removes the original files after creating the compressed file. 
> `gzip` keeps the original file mode, ownership, and timestamp.

```bash
gzip file.txt
```

### gunzip:
> To decompress a file we can use `gunzip` command and the original file will be back.

```bash
gunzip file.gz
```

### bzip2:
> Like gzip, `bzip2` is used to compress and decompress the files. It uses different compression algorithm so it compress files better than gzip, but It has a slower decompression time and higher memory use.

```bash
bzip2 file.txt
bzip2 -k input.txt # Does compression but does not delete the original file.
```

### bunzip2:
> `bunzip2` is used for decompression bzip2 files.

```bash
bunzip2 file.txt.bz2
```

### xz:
> `xz` is new data compression utility. It is more faster and has more better compression.

```bash
xz file.txt
xz -d file.txt.xz # Decompress the file.
unxz file.txt.xz # Decompress the file.
xz -k file.txt # Prevent deleting of the input files
```

### tar:
> `tar` stands for tape archive, and used to create Archive and extract the Archive files. Common use cases of the tar command:
* Backup of Servers and Desktops.
* Document archiving.
* Software Distribution.
```bash
tar -cvf myarchive.tar myfiles # Create Tar file
tar -xvf myarchive.tar # Extract files

tar -zcvf myfiles.tar.gz myfiles/ # Create Tar Archive using Gzip
tar -zxvf myfiles.tar.gz # Extract all files
tar -zxvf myfiles.tar.gz FILENAME # Extract one file

tar -jcvf myfiles.tar.bz2 myfiles/ # Create Tar Archive using Bzip2
tar -jxvf myfiles.tar.bz2 # Extract files

tar -tf file.tar.gz # List Archive content
tar -tg file.tar.gz # List Gzip Archive content

```

* `-c` : Creates Archive
* `-x` : Extract archive
* `-f` : Creates archive with given filename
* `-v` : Verbose
* `-t` : Lists files in archived file
* `-u` : Archives and adds to an existing archive file
* `-A` : Concatenates the archive files
* `-z` : Create tar file using gzip
* `-j` : Create tar file using bzip2
* `-W` : Verify an archive file
* `-r` : Add file or directory in already existed `.tar` file

### dd:
> `dd (Disk Destroyer)` stands for Convert & Copy. `dd` takes an input file (ex:/dev/sda) and writes it to the out put file (ex:/dev/sdb) we specify.
```bash
dd if=/dev/sda of=/dev/sdb # Backup entire Disk.
dd if=/dev/hda1 of=\~/partition.img # Backup a partition.
dd if=/dev/hda of=\~/hdadisk.img # Create an image of a Hard Disk.
dd if=hdadisk.img of=/dev/hdb # Restore using Hard Disk image.
dd if=/dev/cdrom of=tgsservice.iso bs=2048 # Create CD-Rom backup.
dd if=/Path/ubuntu.iso of=/dev/sdb bs=1M # Create bootable usb drive from image.
dd if=textfile.ebcdic of=textfile.ascii conv=ascii # Convert the data format of a file from EBCDIC to ASCII.
dd if=/dev/random of=/tmp/rand_file # Testing Read/Write speed on a hard disk.
dd if=/dev/zero of=/tmp/rand_file # Testing Read/Write speed on a hard disk.
dd if=/dev/zero of=/tmp/rand_file bs=1M count=1000
```
* `if` : Input file
* `of` : Output file
* `bs` : Block Size
* `count` : Number of Blocks
* `conv` : Convert



