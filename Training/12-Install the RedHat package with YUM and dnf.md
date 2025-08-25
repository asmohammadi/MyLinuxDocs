# 12-Install the RedHat package with YUM and dnf

### Redhat High-level Package Management (YUM, DNF):

```sh 
/etc/yum.repos.d/ # Yum repositories path
```
![alt text](<12-Assets/01-Yum Repositories.png>)

```bash
yum repolist # Show active repositories
```
![alt text](<12-Assets/02-Active Repositories.png>)

```bash
yum install PackageName # Install package
dnf install PackageName # Install package
yum remove InstalledPackage # Remove installed package
yum search PackageName # Search repositories for a package
yum deplist PackageName # List dependencies of installed package
yum list # List all packages in all active repositories
yum list install # List all installed packages
yum check-update # Check package update
yum update # Show and install updates for installed packages
yum update PackageName # Update specific package
yum history # Get the history of Yum command
```

```bash
# Download rpm files of a package:
yum install yum-utils
yumdownloader --destdir /DownloadPath PackageName
# or
dnf download PackageName
```
```bash
# Download rpm files of a package with dependencies:
yumdownloader --destdir /DownloadPath --resolve PackageName
# or
dnf download --resolve PackageName
```


