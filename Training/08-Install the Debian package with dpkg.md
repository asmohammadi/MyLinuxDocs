# 08-Install the Debian package with dpkg

### Debian Package Management:

```bash
dpkg -l # List all installed packages
dpkg -L InstalledPackage # List files & paths of installed package
dpkg -i Package.deb # Install package from local file. (Need dependencies)
dpkg -r Package # Remove installed package
dpkg -p Package # Remove and purge installed package
```

```bash
dpkg -C PackageFileName # Shows the content of the package
```
![alt text](<08-Assets/05-dpkg -C.png>)

```bash
dpkg -s Package # Show status of installed package
```
![alt text](<08-Assets/07-dpkg -s.png>)

```bash
dpkg -S File/Path # Shows which package this file or path belongs to
```
![alt text](<08-Assets/04-dpkg -S.png>)

**Aria2c** -> Package Management Tool (Like wget)

```bash
aria2c PackageFileURL # Download Package file
```
![alt text](08-Assets/02-Aria2c.png)




