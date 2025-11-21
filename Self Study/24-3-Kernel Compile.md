# Kernel Compile:

```sh
# Get kernel from kernel.org
# Extract the kernel file to /usr/src/
usr/src/
usr/src/linux/
```

### Install Tools for Compile Kernel:
```sh
# Installing Development tools for Compile Kernel in Redhat:
yum groupinstall "Development Tools"
yum install ncurses-devel qt-devel

# Installing Development tools for Compile Kernel in Ubuntu
apt install build-essential libncurses-dev bison flex libssl-dev libelf-dev
# Extra tools for initramfs, manage modules, and kernel:
apt install fakeroot bc kmod cpio rsync liblz4-tool
# Tools for creating Deb packages:
apt install kernel-package dpkg-dev
# Tools for menuconfig in GUI:
apt install libgtk2.0-dev libglade2-dev
```

### Compile Kernel:

1. Linux Kernel Source
2. Select modules
3. Split Kernel bzimage
4. Split Modules bzimage
5. Install Kernel & Modules

* `bzimage` : Kernel image which will Boot new kernel in RAM
* `dracut` : Will put the compiled kernel in Grub(BootLoader). Compiled source => Installed source. Compiled kernel => Installed kernel.

```sh
make clean # Remove generated files, but keep config
make mrproper # Remove all generated files + config + various backup files
make distclean # mrproper + remove editor backup & patch files
make config # line oriented program
make nconfig # ncurses menu based program
make menuconfig # menu based program
make xconfig # QT based frontend
make gconfig # GTK based frontend
make oldconfig # provided .config as base
make bzImage # Create bzImage
make modules # Create bzImage for modules
make modules_install # Install created modules
```

```sh
# Compile a Kernel:
make clean
make mrproper
make xconfig
make bzImage # Create bzImage
make modules # Create bzImage for modules
make modules_install # Install created modules
ls /lib/modules/
```
* Put changes in /boot directory
* Put the new kernel version in Grub(Bootloader)
* dracut will do these last steps
```sh
make install # Will do dracut process
reboot
```
```sh
make -j$(nproc) bzImage # Create kernel image using all CPU cores
cp /boot/config-$(uname -r) .config # Copy the current kernel .config file
yes "" | make oldconfig # Sync configs with new config, Answer Yes for all questions
```










