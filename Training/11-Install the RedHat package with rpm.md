# 11-Install the RedHat package with rpm

### Redhat Low-level Package Management (RPM):

```bash
rpm -i Package.rpm # Install package locally
rpm -iv Package.rpm # Install package with verbose
rpm -qa # Query the list of all installed packages
rpm -ql InstalledPackage # Query the list of files & paths of installed package
rpm -qi InstalledPackage # Query the information of the installed package
rpm -qpR InstalledPackage # Query the dependencies of installed package
rpm -qc InstalledPackage # Query the config files of installed package
rpm -Uv Package.rpm # Update (or install) a package
rpm -e InstalledPackage # Remove an installed package
```


