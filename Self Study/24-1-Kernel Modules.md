# Kernel Modules:


```sh
/lib/modules # Installed Modules
lsmod # Display all installed modules & the status of modules & its dependencies
rmmod # Remove installed module
insmod # Insert modules into the kernel using absolute path
modprobe # Insert modules with dependencies
modprobe -r Module # Remove installed module
modprobe -n Module # Dry-run
modprobe -D Module # Show dependencies of a module
modprobe -c Module # Show config of a module
modinfo # Information of modules
depmod -a # Update all dependencies of modules (In module.dep file)
```
```sh
root@server:~# ls -l /lib/modules

drwxr-xr-x 2 root root 4096 Jul 15 06:32 6.8.0-45-generic
drwxr-xr-x 2 root root 4096 Jul 20 07:01 6.8.0-60-generic
drwxr-xr-x 5 root root 4096 Jul 15 06:31 6.8.0-63-generic
drwxr-xr-x 5 root root 4096 Jul 20 07:00 6.8.0-64-generic
```
```sh
root@server:~# ls -l /lib/modules/6.8.0-64-generic/
lrwxrwxrwx  1 root root      39 Jun 15 07:53 build -> /usr/src/linux-headers-6.8.0-64-generic
drwxr-xr-x  2 root root    4096 Jun 15 07:53 initrd
drwxr-xr-x 17 root root    4096 Jul 20 07:00 kernel
-rw-r--r--  1 root root 1678510 Nov 20 15:00 modules.alias
-rw-r--r--  1 root root 1635092 Nov 20 15:00 modules.alias.bin
-rw-r--r--  1 root root    9714 Jun 15 07:53 modules.builtin
-rw-r--r--  1 root root   10690 Nov 20 15:00 modules.builtin.alias.bin
-rw-r--r--  1 root root   11907 Nov 20 15:00 modules.builtin.bin
-rw-r--r--  1 root root   87768 Jun 15 07:53 modules.builtin.modinfo
-rw-r--r--  1 root root  863919 Nov 20 15:00 modules.dep
-rw-r--r--  1 root root 1145825 Nov 20 15:00 modules.dep.bin
-rw-r--r--  1 root root     353 Nov 20 15:00 modules.devname
-rw-r--r--  1 root root  263012 Jun 15 07:53 modules.order
-rw-r--r--  1 root root    2786 Nov 20 15:00 modules.softdep
-rw-r--r--  1 root root  734031 Nov 20 15:00 modules.symbols
-rw-r--r--  1 root root  891939 Nov 20 15:00 modules.symbols.bin
drwxr-xr-x  3 root root    4096 Jul 20 07:00 vdso
```
```sh
root@server:~# lsmod
Module                  Size  Used by
tls                   155648  0
intel_rapl_msr         20480  0
vmw_balloon            28672  0
intel_rapl_common      40960  1 intel_rapl_msr
snd_ens1371            36864  0
btusb                  77824  0
snd_ac97_codec        196608  1 snd_ens1371
btrtl                  32768  1 btusb
gameport               20480  1 snd_ens1371
btintel                57344  1 btusb
```



