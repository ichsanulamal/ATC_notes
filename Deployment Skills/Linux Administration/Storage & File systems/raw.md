CompTIA Linux+: Storage & File systems
Managing Linux storage devices, partitions, and file systems is a required skill for Linux technicians. Most Linux distributions have similar file system hierarchies, and performance and fault tolerance improvements can be realized by configuring redundant array of inexpensive disks (RAID) disk levels. Linux storage is not limited to local mass storage devices but can also include network storage. Begin this course by discovering how Linux treats mass storage devices, partitions, and file system types. Then you will examine the Linux file system hierarchy standard and learn when to use specific Linux file system management commands, and how to partition and format Linux storage. Next, you will learn how to mount and unmount Linux file systems, and when to use hard and soft, or symbolic, links. Finally, you will explore how to implement RAID disk levels in Linux, and you will work with Linux logical volume management (LVM) and network storage using an Internet Small Computer Systems Interface (iSCSI). This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_02_enus_01)

    2. Video: Linux Storage Concepts (it_oslsys_02_enus_02)

    3. Video: The Linux File System Hierarchy (it_oslsys_02_enus_03)

    4. Video: Linux Storage Command Line Management Tools (it_oslsys_02_enus_04)

    5. Video: Creating Linux File Systems (it_oslsys_02_enus_05)

    6. Video: Mounting Local Linux File Systems (it_oslsys_02_enus_06)

    7. Video: Mounting Remote Cloud-based File Systems (it_oslsys_02_enus_07)

    8. Video: Linux File System Hard and Soft Links (it_oslsys_02_enus_08)

    9. Video: Working With Hard and Soft Links (it_oslsys_02_enus_09)

    10. Video: Managing Linux File Systems (it_oslsys_02_enus_10)

    11. Video: RAID Disk Levels (it_oslsys_02_enus_11)

    12. Video: Configuring Software RAID in Linux (it_oslsys_02_enus_12)

    13. Video: Linux Logical Volume Management (LVM) (it_oslsys_02_enus_13)

    14. Video: Configuring LVM (it_oslsys_02_enus_14)

    15. Video: Storage Area Networks and Network Attached Storage (it_oslsys_02_enus_15)

    16. Video: Configuring a Linux-based iSCSI Initiator (it_oslsys_02_enus_16)

    17. Video: Course Summary (it_oslsys_02_enus_17)

    Course File-based Resources

1. Video: Course Overview (it_oslsys_02_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance. [Video description ends]
Hi, I’m Dan Lachance. Managing Linux storage devices, partitions and file systems is a required skill for Linux technicians.

Most Linux distributions have similar file system hierarchies and performance and fault tolerance improvements can be realized by configuring raid disk levels.

Linux storage is not limited to local mass storage devices, but can also include network storage.

In this course, I will begin by discussing how Linux treats mass storage devices. We’ll discuss partitions and file system types, followed by covering the Linux File system hierarchy standard.

I’ll then discuss when to use specific Linux file system management commands, followed by partitioning formatting Linux Storage.

Next, I will cover how to mount and unmount Linux file systems. And I’ll cover when to use hard and soft, or symbolic links.

Lastly, I will cover how to implement RAID disk levels in Linux, and I will work with Linux Logical Volume management or LVM, and network storage through iSCSI.

This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: Linux Storage Concepts (it_oslsys_02_enus_02)

Upon completion of this video, you will be able to recall how Linux treats mass storage devices, partitioning and partition types, and file system types.
recall how Linux treats mass storage devices, partitioning and partition types, and file system types
[Video description begins] Topic title: Linux Storage Concepts. Your host for this session is Dan Lachance. [Video description ends]
As a Linux technician, it's absolutely crucial to have a solid understanding of Linux storage.

In Linux, when we talk about mass storage devices, we are talking about devices that are referenced as files that live under /dev. Dev, of course, being for Device. Examples of this would include /dev/sda. That would be the first mass storage device. /dev/sdb would be the second storage device.

But we know that storage media can be carved up or partitioned into multiple sections. And so when we talk about Linux storage, partitioning begins numbering at one, not zero.

So, therefore, if we go back to our first example of /dev/sda, the first partition on that disk would be /dev/sda1. The next partition would be sda2, and so on. If we've got a second mass storage device in the machine, then we would have /dev/sdb and the first partition would be simply numbered as partition number one.

And when we partition mass storage devices in Linux, we have to consider whether we want to treat the devices as Master Boot Record or MBR initialized disks where the maximum individual partition size is two terabytes, and you can have a maximum of four partitions on an MBR initialized disk. Or we could initialize the disk as a GUID Partition Table or GPT type of disk. There are different implementations depending on operating systems and versions which have limitations on sizes. So, we’re just going to say here that there’s basically no practical disk size limit or to the number of partitions with GPT.

Some implementations might have a limit, let’s say, of 128 partitions, but that’s going to be pretty much unlimited compared to MBR’s limit of four partitions.

Now, if you were to partition Linux disks because you want to use them in a RAID array, let's say for software RAID on a Linux host, you could use the fdisk command line utility to set the partition types to Linux RAID autodetect.

So when you’re in fdisk for the given disk device, you would press T for type and then put in FD, which sets the partition type to Linux RAID autodetect. So you might do that on numerous physical disks and then group that together into a logical volume. Maybe you might set it up as a RAID 0 stripe or a RAID 1 mirror depending on what you’re doing. We’ll talk more about RAID levels later on.

So now that we know how to reference a mass storage device in Linux and how the partitioning works.

The next thing would be to talk about file system types. In other words, formatting those partitions so we can actually use them. There are a number of different types of file systems that you can configure, such as ext2, ext3, or the newer, ext4. ext stands for extended file system. And this is pretty standard and common in Linux to use this.

You also have the XFS type of file system. This is designed to be a high performance, very fast file system that can be used in some UNIX and Linux distributions.

And then we’ve got another example Reiser4FS. Now newer file systems like ext4, Reiser4, and XFS, XFS is not really a new file system, but they will support journaling which records disk transactions so that if there's a failure of some kind, it'll roll back out of a transaction that hasn't yet been written to disk.

Managing Linux file systems and storage devices means using a number of different built-in operating system commands, such as lsblk to list block devices. [Video description begins] A new page opens with the title: Linux Storage Management. There are five command lines that the presenter will elaborate on now. [Video description ends] That will give you a listing of devices like SCSI devices that you can work with that are recognized by the Linux kernel.

You can use the fdisk command line tool to partition disks or to view the partitioning that's already been done. You can use the mkfs to make a file system. That’s like formatting a disk partition on the Windows side of things. And depending on the file system type that you want to format, you might also use a special tool like mkfs.reiser4, so it’s specific to a file system type. Once you have formatted a file system, once you’ve made a file system, the next thing you need to do is make it accessible in a mount point directory. So, you create an empty subdirectory on the machine somewhere and then mount the partition, such as /dev/sda1, into that directory.

Pictured on the screen, we have an example of issuing the lsblk command. [Video description begins] A new page opens with the title: lsblk Command. A screenshot is presented on it. The heading reads: cblackwell@ubuntuserver1: / A list of commands is displayed underneath. [Video description ends] What’s been passed here as a command line parameter to that is --scsi. What it will then do is list any SCSI devices. Here in the output, we have sda, and we also have sr0, which is an optical device like a DVD drive.

The second command we have shown here is sudo fdisk -l list and then /dev/sda. In other words, please show me how device SDA has been carved up.

And then down below towards the bottom left we’ve got references to sda1, sda2, and sda3.

Now, of course, you can use the fdisk command without -l to interactively manage partitions on that mass storage device. Whether you're creating new partitions or whether you are removing partitions, that type of thing.

3. Video: The Linux File System Hierarchy (it_oslsys_02_enus_03)

After completing this video, you will be able to outline the purpose of various Linux directories such as /boot, /proc, /dev, /var, and so on.
outline the purpose of various Linux directories such as /boot, /proc, /dev, /var, and so on
[Video description begins] Topic title: The Linux File System Hierarchy. Your host for this session is Dan Lachance. [Video description ends]
Let’s take a few minutes to talk about the File system Hierarchy Standard or FHS in Linux. The whole idea here is that we have a standard setup for the file system directory structure on UNIX and Linux machines. That way there's some kind of familiarity or similarity between different versions and different distributions.

But the thing to bear in mind, of course, is that some Linux distribution directory structures will vary a little bit from the Linux file system hierarchy standard, but in my experience, it will only be very slightly.

So let's talk about the normal file system hierarchy standard. In other words, what kind of subdirectories can we expect on most Linux distributions and what kinds of things go into those subdirectories.

The first is the root directory. Just a / now that's the root file system. Every file and directory for the Linux host will appear there, even if it's from storage devices, different ones that might be available locally. You might have multiple disks, a bunch of partitioning, maybe you’ve got network storage available over the network. It doesn’t matter. All of it will appear somewhere under the root file system because you will make a subdirectory as a mount point location to mount local and remote file systems.

The next directory is /bin for binary. [Video description begins] A page opens with the title: Linux FHS. A table is displayed on it. There are two columns with the headers: Directory name and Directory description. The presenter describes the directory names and their descriptions. [Video description ends] so binary command line tools, commands like password, passwd, cat, grep would exist under bin.

You’ve then got a /boot directory. As you might guess, this will have boot loader files. Most Linux distributions these days use the GRUB boot loader, GRUB version two. You might have older Linux variants that still use the Linux loader or Lilo, LILO. But either way, that’s the purpose of the /boot directory. The boot directory usually points to a separate disk partition, a smaller disk partition just enough to contain the boot files.

Then you’ve got /dev. In Linux, when we refer to hardware devices, each one is represented to the Linux kernel as a file under /dev. So whether we’re talking about devices that point to mass storage devices or optical storage like DVD. Or even other things like random number generators, there’s even a device under /dev called Null that you can redirect unwanted command line output to just to get rid of it or to suppress it.

Next, we have /etc. /etc contains configuration files. Now these would be for Operating System components as well as any additional packages you might have installed. Often you will have a separate subdirectory under /etc for a given service or component where its config files would then live in that subdirectory under /etc. Configuration files don't have to but often have either a .conf, CONF, file extension, or perhaps .cfg, but they don’t have to.

The next part of the Linux file system hierarchy standard is /home. Of course, this is where user home directories would exist, including for the built-in root superuser account.

Then we’ve got /lib. This stands for library. You’re going to have what are normally binary files in here. These are library files that are used by various items installed in the Linux OS. So they might make function calls, for example, to something in /lib.

Then you’ve got /media for removable storage media. So when you plug in, for example, a removable USB thumb drive into a Linux host, normally that will automatically pop up an automount and be available under /media.

/mnt is a way for you to get a list of mounted file systems that are already mounted and made available in mount point directories.

Then you’ve got /var, which stands for variable. Now variable means variable length files. First thing that comes to mind here is log files. This is where you're going to get both Linux operating system log files as well as log files for other services that you might be using on that host. And sometimes, they’ll have their own subdirectory under /var. Just like for config files, they might have their own subdirectory under /etc.

The standard file system hierarchy also will include /opt. These can contain files for optional or other software packages that you might have installed. It depends on the software package specifically. You might install an additional software package, it might just put a config file or two somewhere under etc, maybe a couple of files under bin or sbin, which is our next listing by the way.

So System binaries, usually more admin type tools, so commands like fdisk, useradd, mkfs. But if you install additional stuff it might go under /opt.

You’ve got /srv, these are service files for different services you might choose to install on that host like an FTP server or an HTTP web server.

/tmp, of course, is for temporary files. /usr stands for UNIX system resources. This might contain other binary utilities like the mount command or the nano text editor.

And you can also expect to find /proc. This is for processes currently running in Linux known by the Kernel. And you might even have references to various devices and CPU information, RAM information, directories for running services. The directory would be named with the services process ID or PID.

So pictured on the screen, we’ve got an example in Ubuntu Linux of typing PWD or print working directory. [Video description begins] A new page opens with the title: Ubuntu Linux Root Subdirectories. A screenshot is presented below. A list of directories is displayed under a header: cblackwell@ubuntuserver1 :/$ pwd [Video description ends] In this case, it returns just a front /, which means we're in the root of the file system. Remember, everything’s contained from this point on under root.

And if we do an LS, we get a lot of the standard subdirectories according to the file system hierarchy standard like bin, boot, dev, etc, home, lib, opt, media, mnt, and so on.

Next, we have a screenshot of running LS in /proc. [Video description begins] A new page opens with the title: Contents of /proc/. A screenshot is presented below it. A list of numbered subdirectories is displayed on it. [Video description ends] Notice all the numbered subdirectories. These numbers are process identifiers or PIDs assigned by the Linux kernel to a running process.

The contents of the proc directory will vary. It’s dynamic. It depends what's running at the time when you go into that directory. But also notice we have a number of files like disk stats, CPU info, mem info, and so on.

So being familiar with the file system hierarchy standard or HFS means you're going to be familiar navigating through the file system in pretty much any Linux distribution.

4. Video: Linux Storage Command Line Management Tools (it_oslsys_02_enus_04)

Upon completion of this video, you will be able to recognize when to use Linux file system management commands such as lsblk, fdisk, mkfs, parted, and partprobe.
recognize when to use Linux file system management commands such as lsblk, fdisk, mkfs, parted, and partprobe
[Video description begins] Topic title: Linux Storage Command Line Management Tools. Your host for this session is Dan Lachance. [Video description ends]
There are plenty of Linux storage command line tools available, some of which we've briefly mentioned already, but we'll go into a bit more detail here now.

Some of these commands will require root privileges. Actually, quite a few of them will. Either you log in with root to issue these commands because it’s not recommended to be logged in as root all of the time. Because it’s such a powerful account. It’s the super account in Linux.

So often, we’ll instead use the ‘sudo’ prefix in front of the command to run it with elevated privileges. Now, of course, not anybody can do that. You have to be specifically listed in the sudo’s file to be able to use the sudo utility.

Normally, when you install most Linux distributions, you’re asked to create a user account. And that user account that you specify is allowed to run the sudo command.

Now, while many of these commands will be exactly the same in different Linux distributions, some of the parameters on the command line for these commands might vary slightly. But as an example, you can expect to find the fdisk command line tool available in all Linux distributions.

So let’s go through some common Linux storage command line tools, starting with lsblk for listing block devices.

Now, we've mentioned that this is a command that will show you your storage devices. And if you use the --scsi command line parameter, it’ll show you SCSI devices. Most mass storage devices are treated as SCSI devices by the Linux kernel. And if you’re wondering what SCSI stands for, it stands for Small Computer System Interface. SCSI is an old standard for linking multiple devices, usually storage but not limited to storage, together in a chain.

Then we have, of course, the fdisk utility for managing the partitions on a given disk. Whether you want to manage them or whether you want to view them.

So viewing is possible if you use the -l parameter when you run fdisk. Bear in mind that these command line parameters are case-sensitive. -l is going to mean something totally different than -L, for instance, when it comes to fdisk.

Another common storage command line tool is mkfs, MKFS, for making a file system. So given that you might have already, let's say, used the fdisk utility to create a partition or more than one partition, you can then format those partitions so they’re ready to be used for file storage. So you could use mkfs to format a partition for, let’s say, ext4, or a reiser file system, and so on. You’ll sometimes have variations of commands to do that, like mkfs.reiser

Now we’ve mentioned that you can use the fdisk command for managing partitions on disks, which is correct. But you can also use the parted tool. One of the interesting things about the parted utility is it also lets you expand a partition, given that there is adjacent free space on a given disk, and it can allow you to shrink partitions, which can be very important and very powerful, in some cases.

You also have the partprobe command. This command is used to instruct the Linux kernel to reread device partition tables, if you've made changes that haven't yet been picked up by the OS. Of course, rebooting the system would allow the kernel to pick up those new changes. But if you don’t want to reboot the system, partprobe can be very handy indeed.

Here we’ve got a screenshot of the parted command. [Video description begins] A new page opens with the title: Parted Command. It displays a screenshot. The header inside it reads: cblackwell@ubuntuserver1 :~$ sudo parted. A list of devices is given below. [Video description ends] Notice what it’s doing is listing our devices like /dev/sda, sdb and so on, so that we can manage the partitioning on those given devices.

Now, if you've got a Linux distribution with the GUI such as Ubuntu desktop shown in this screenshot, you can also use whatever disk management utility is available in the GUI to manage disk partitioning. [Video description begins] A new page opens with the title: Ubuntu Desktop Graphical User Interface (GUI) Disk Management. It displays a screenshot of disks divided into two sections: Disks and 86 GB Hard Disk. On the Disks section, a list of Drive names a seen. On the 86 GB Hard Disk section, the partitioning details are provided. [Video description ends] In this case, a hard disk has been selected in the left-hand side of the screen and the partitioning layout of that disk is shown over on the right.

If you're using a virtual machine to run the Linux OS, then you're going to be using one or more virtual disks. [Video description begins] A new page opens with the header: Virtual Disks for Linux Virtual Machines VMs. A screenshot is displayed below. It has two columns with a list of names. The headers read: Device and Summary. [Video description ends] The first screenshot we have here is from within VMware Workstation, where we’ve got four disks shown here, four hard disks, all SCSI of varying sizes. So, the Linux kernel then will see all of these devices, /dev/sda, /dev/sdb, and so on.

The second screenshot here to the right shows us the disk layout for a Microsoft Azure cloud based virtual machine. At the top we've got an OS disk, an operating system disk, but down below we’ve got two data disks that have also been added. To the Linux operating system kernel, it’s simply going to see three mass storage devices.

5. Video: Creating Linux File Systems (it_oslsys_02_enus_05)

During this video, you will learn how to manage disk partitions and formatting using Linux commands.
manage disk partitions and formatting using Linux commands
[Video description begins] Topic title: Creating Linux File Systems. Your host for this session is Dan Lachance. [Video description ends]
This demo is all about creating Linux file systems. Now while we will be focusing on doing that at the command line, it’s also important to note how you might do that if you have a desktop GUI on your Linux machine.

Here I’ve got Ubuntu Linux desktop. Now, one of the things that I could do here is click my little show applications button in the left hand bar and I could search for the word disk, and I could choose the Disks tool. Here, for example, I would be able to get a list of my disks and when I select it on the left, I get a sense of how it's laid out over here on the right. [Video description begins] A new page opens with the title: Disks. It is divided into two sections. On the left-hand pane, a list of disks is shown. On the middle pane, the details of the first disk are displayed, such as: Model, Size, Volumes, and more. [Video description ends] And if I had additional disks, they would show up over on the left. Of course, you can also select a given partition. And if I click the configure or the gear icon, I can format the partition, [Video description begins] The gear icon is shown on the middle pane, under the category: Volumes. It shows a list of format options. [Video description ends] I can edit the details related to the partition and the file system. I could resize it, I could run a check on it.

And if there's any corruption detected, I can run a repair. I can configure mounting options for that file system. So depending on the desktop GUI environment you have will determine exactly what the tool will look like. And there are plenty out there, but that gives us an idea of that.

Let's switch over to the command line on a different host. [Video description begins] A blank Linux host page opens with the header: cblackwell@ubuntuserver1 :$ [Video description ends] In Linux, we can always rely on the fdisk command. I’m going to run sudo fdisk -l for list. In the output, it is breaking down the configuration on this machine for the disk subsystem. So if I scroll back up in the output, I’m interested primarily when we get to the SDA section.

The first disk, in this case, it’s about 80GB, and we have a display on how that disk has been carved up into three partitions, sda1, sda2, and sda3. We have the type of the file system, whether it's for booting or just a Linux file system. [Video description begins] The Device: sda1 the type is BIOS boot. For the devices: sda2 and sda3, the type is Linux filesystem. [Video description ends] Then we have device SDB shown here, which is about 20GB, but there are no partitions. And the same goes for device SDC and also SDD.

So I’m going to run sudo fdisk /dev/sdb, and I’ll press Enter. Now it tells me here that this disk is currently in use. And specifically, I get the sense here that it’s being used by logical volume management, LVM. However, I have the option of wiping the disk.

Now, I know I don’t need anything on this disk. So I’m going to press N for new. And for the partition type, I’ll type in P for primary. Now it asks, do you want this to be partition 1, 2, 3, or 4? So classic master boot record or MBR type of options. I’m going to leave the default of one by pressing Enter. And I’ll press Enter to accept the default starting sector and ending sector. [Video description begins] The starting or the first sector default reads: 2048. The ending or last sector default reads: 41943039. [Video description ends]

So I've now got a Linux partition which is 20GB in size. Now I have a message down below. It says, Partition number 1 contains an ext4 signature. That means that it's in use by a file system. Now you won't get that if it's a brand new empty disk.

However, this had something on it before, so it asks, do you want to remove the signature? I’ll type in the letter Y for yes and press Enter. It says, the signature will be removed by a write command. So I’ll type in W to write my partition changes back to device SDB.

If I run sudo fdisk -l for list of /dev/sdb. Notice we’ve now got our 20GB Linux partition, sdb1. Now once you’ve got a partition, the next order of business, of course, is to make a file system on it so you can actually use it.

I’m going to run sudo mkfs, make file system, -t for type. It’s going to be ext4 /dev/sdb. Now not just SDB but sdb1 to specify the partition. Okay! So it looks like our ext4 file system has been created on sdb1. What I want to do is I want to make sure I can mount that.

So I’m going to run sudo mkdir, maybe on the root, I’ll make a folder called data1. And I’m going to run sudo mount /dev/sdb1, and I want that available under /data1.

So if I run sudo mount and grep it for sdb1, it's showing here that we currently have a mounted file system, sdb1, which is available under /data1. That’s kind of like a drive letter in Windows that points to a file system.

So you can work with files and directories under data1. And what you’re really doing is making changes to the underlying partition one on device SDB.

6. Video: Mounting Local Linux File Systems (it_oslsys_02_enus_06)

Find out how to manage local Linux mount points using mount, umount, and /etc/fstab.
manage local Linux mount points using mount, umount, and /etc/fstab
[Video description begins] Topic title: Mounting Local Linux File Systems. Your host for this session is Dan Lachance. [Video description ends]
In this demo, we're going to be working with mounting local Linux file systems. Local in this context means from local storage. In other words, not network attached storage, not storage that we're accessing through a storage area network. [Video description begins] A blank Linux host page is open with the header: cblackwell@ubuntuserver1 :~$ [Video description ends]

Now, to get started here, it's important, of course, to run sudo fdisk -l to list how the disks are carved up. For example, device SDA has three partitions. One is a boot partition. It’s pretty small, about one megabyte. We’ve got a 2-gig Linux file system. And then in the third partition, sda3, we’ve got a 78-gig Linux file system again.

Device SDB is carved up into one partition, which uses pretty much the whole disk, it's just a Linux type of partition. Then we’ve got device SDC with nothing on it and SDD again with nothing on it. [Video description begins] The size of the device: sdb1, is 20G [Video description ends]

Now if I type mount, and let’s say, for example, we pipe that to the grep line filter, I'm interested in device SDB. It appears that we've got partition one on device SDB that’s been mounted under /data1. So if I do an LS of the /data1 directory, all we see is lost and found. So really, there’s nothing there, but it is mounted in read-write mode. So RW is here. Okay!

Well, let’s build a new partition and mount it. And then we’re going to make sure that these mounts are persistent between reboots. Because by default, when you use the mount command to mount something, it'll mount it in the current system session. But that's not remembered unless you put it in the appropriate file, which gets read on startup.

So, we’ll take a look at that after. First things first, sudo fdisk /dev. I want to work on SDC. I want to press N for a new partition. The default is P for primary partition. I’ll press Enter to accept the default partition number of one and I’ll also press Enter to accept the default starting and ending sector for the partition. At this point, I need to press W to write that to disk.

So if I clear the screen and run sudo fdisk -l, for list, /dev/sdc, notice, of course, we’ve now got our SDC partition one which is about 20GB in size, just a standard Linux type of partition. [Video description begins] For the Device: /dev/sdc1, the following details are displayed: Boot Start 2048, End 41943039, Sectors 41940992, Size 20G, ID 83, and Type Linux. [Video description ends]

From here, I could run sudo mkfs Make a file system, let’s say -t is ext4 and that would be on /dev/sdc1, and it’s done.

So next I would make a directory, [Video description begins] The presenter clears the screen to run the new command. [Video description ends] let’s say on the root called data2. And I could run sudo mount /dev/sdc1 on /data2. And if I run sudo mount and pipe that to grep. Let’s look for SDC, it’s currently mounted. So we can now work with the /data2 subdirectory, create folders, create files, and it’s all being written to partition one on device SDC.

The thing is, if we restart the system, sdc1 will no longer be mounted to /data2. We stated earlier that you had to write that to the appropriate config file that gets read upon startup.

Well, that file, and I’ll just open it using nano, is under /etc and it’s called fstab, file system tab. It’s tab separated. [Video description begins] A new page opens with the title: GNU nano 6.2/etc/fstab. A column is seen with the following six headers: file system, mount point, type, options, dump, and pass. [Video description ends]

In here, we’ve got a couple of entries to mount what we already have. But the first thing I would do here is specify what I want mounted. That would be /dev/, in this case, let’s say sdc1. Now that, of course, corresponds to column one up above here that’s shown as being the file system. Now you need a space or a tab to separate that from the mount point it should be mounted into. So if I press Tab, I can tell it I want that to go under /data2. What type of file system is it? Well, that’s ext4 in our case. Then I can specify options such as read-write. I want it to be readable and writable. [Video description begins] The presenter writes the read-write option as: rw [Video description ends] Of course, people still have to be granted permissions to the file system to be able to do those things.

I can determine if I want it to be picked up by the Linux dump utility. For backup purposes, I’ll put a 0 for no. And I can determine the order I want this checked when the system boots up. If there’s problems with the file system, I’ll put in number 2, so after the other existing entries.

Okay! So I’m going to press control X. Save modified buffer, type in Y for yes. It wants to write it to the fstab file, perfect, Enter!

Now I’m going to run sudo init 6, that’s just another way to say reboot. Of course, you’d only do this if you knew the system wasn’t in use and didn’t need to be left up and running. But I want to do this because I want to test to see if the fstab file is read correctly and the sdc1 file system is mounted under /data2. Here we go!

Okay, The Linux system has rebooted. Now, if I do an LS of /data2 that doesn’t tell me anything. Unless we knew there were files in there already, they would only appear when the file system is mounted. [Video description begins] The output appears on the screen: lost + found [Video description ends] If I type sudo mount and pipe that to grep and just look for SDC. Indeed, sdc1 is mounted in /data2.

So if I were, let’s say, to run sudo nano /data2/newfile1.txt. This is sample data. And then we’ll just write that file out to disk. So if we do an LS of /data2, of course, newfile1 shows up. Now, if we were to run sudo umount to unmount /data2. We’ll just use our up-arrow key here. If we run the mount command and take a look for SDC, it no longer shows as being mounted. Well, that's because we unmounted it.

And if we do an LS of /data2, of course, we see nothing. newfile1.txt is not there because it’s not mounted.

So, of course, if we run sudo mount /dev/sdc1, partition one, on device SDC, and we mount that under /data2. Now if we do an LS of that mount point directory, newfile1.txt shows up once again.

7. Video: Mounting Remote Cloud-based File Systems (it_oslsys_02_enus_07)

In this video, discover how to manage remote Linux mount points.
manage remote Linux mount points
[Video description begins] Topic title: Mounting Remote Cloud-based File Systems. Your host for this session is Dan Lachance. [Video description ends]
All right! In this demonstration, we’re going to talk about how to mount a remote cloud-based file system. What does this mean? Well, that could mean a lot of things.

But what we're going to be doing in this particular example is we're going to be creating a shared folder within the Microsoft Azure Cloud. More specifically, we're going to create it within a storage account. We can then map to it from Linux. Now when I say map, I mean we just make a mount point connection to a local directory on a Linux host that points to this cloud-based shared folder. [Video description begins] A Microsoft Azure Home page is open. Under Azure services, there are some tabs, such as: Create a resource, All resources, Storage accounts, and more. [Video description ends]

So the first thing I'm going to do here in Microsoft Azure, I’m signed into the GUI portal tool already, is I’m going to click Create a resource.

I want to create a new storage account where I will create this shared folder. Now I could create it within an existing storage account. It doesn't have to be a new one, but that's why I'm choosing to do it here.

So I’ll click Storage account, and I’ll click Create. I’ll have to specify some details like a Resource group where I want to create the storage account. Like the name implies, a resource group is simply used to organize your cloud resources like virtual machines, storage accounts, virtual networks, and the like. [Video description begins] The presenter clicks on the drop-down button on the Resource group. He selects the option: East. [Video description ends]

What should we call this? We’re going to call it storacceastyhz765. So it needs to be a unique name. It’ll be in the East US region. Ideally, that is where anyone that needs to make a connection to the shared folder and the storage account will reside. Otherwise, we could change it.

And I’m not going to change anything else here. So I’ll just click the Review button and then I’ll click the Create button. So the creation is in progress. After a moment it says, Your deployment is complete. And we could either click the Go to resource button to open the storage account. You could also, of course, do it in other ways.

You could navigate in your left hand menu bar down to storage accounts. There it is! Storaccteastyhz765. I’m going to click to open that up. Now within a Microsoft Azure cloud-based storage account, you can store many things. Under containers, you can create folders and files and just store regular files or binary large objects, otherwise called Blobs.

You can work with File shares, which we’re going to do. Software developers might be interested in message queues to exchange messages between software components. And you can work with basic key value table storage.

I’m going to go to File shares, and I’m going to click the Add file share button at the top. Let's call this projects. [Video description begins] A dialog box opens with the title: New file share. The presenter types the name, projects, in the Name field. [Video description ends] I'm not going to change any of the other settings here. I'll just click Create. All right, so now we have a projects shared folder. If I click to open that up, I could then click Browse on the left, for example, to see if there are any files here. [Video description begins] In the middle pane, a toolbar with some options is seen, such as: Connect, Upload, Add directory, and more. [Video description ends]

Now from here, I can upload files directly into the root of this share, or I could add a directory. I'm going to add a directory. Let’s say current_year. I’ll click Ok. So there's the folder or directory. If I click on it to open it up, I can make an entire subdirectory hierarchy. Or I can just upload content, which I will do here.

I’ll upload a couple of sample files into our directory. So I’ll click the Upload button. Okay, I’ve specified a few files. I’ll just click upload. [Video description begins] A dialog box opens with the title: Upload files. A message is displayed: 3 files selected: Project_A.txt, Project_B.txt, Project_C.txt [Video description ends] And after a moment we’ve now got content uploaded into our projects share. Now that’s great.

The next thing we have to do is somehow connect to it from Linux. Well, that’s where this Connect button comes in as being useful [Video description begins] A dialog box opens with the title: Connect projects. It has three categories: Windows, Linux, and macOS. [Video description ends] because I can select the Linux tab. The mount point is called projects. I can choose Show script. Here, I’ve got an entire script for making a mount Point directory on my Linux host called Projects. It's even using the sudo prefix.

Now the connection type we're making here is going to be an SMB type of connection. The same type of way that a Windows client might make a connection to a shared folder, except we’re doing it from Linux. So it's going to be working with an SMB credentials file to allow authentication to this in the cloud.

And at the end of the day, what we're really interested in here is the sudo mount command, where the file system type is -t cifs. And notice the nomenclature. It’s going to refer with two front // to the DNS name assigned to our storage account /projects, which is our shared folder name, space. And that’s going to go locally on our Linux host under /mnt/projects. [Video description begins] A page of code is displayed. The presenter points to the following command: sudo mount -t cifs //storeaccteastyhz765.file.core.windows.net/projects/mnt/projects -o [Video description ends] And then it’s going to use -O for options and specify our credentials file.

Wow! So the script is generated for me, and you could, of course, make changes to it and tweak it.

So I’m going to click the Copy button in the bottom right to copy that script to the clipboard.

Now here in the Azure portal, I’m going to go back Home and click Virtual machines. I’ve got an Ubuntu Linux virtual machine that’s running here in the East US location. So I’m going to be using this virtual machine to connect to that shared folder.

And if I go to Overview on the left, I also have the public IP here for this Linux Host, I’ll copy that as well. [Video description begins] The Public IP address reads: 20.84.40.117 [Video description ends] And I’m going to open a connection to that public IP address using the PuTTY utility. Okay!

So once I’ve made a connection over SSH into that Linux host, this is where I can run the copied script. [Video description begins] The presenter opens a Linux host page titled: cblackwell@ubuntu1 :~$ [Video description ends] So I’m just going to go ahead and paste it in here and press Enter.

So if I were to run, let’s say sudo tail against /etc/fstab, notice that we’ve got an entry here for mounting our shared folder in the Azure cloud. [Video description begins] The presenter highlights the following outcome on screen: //storaccteastyhz765.file.core.windows.net/projects [Video description ends] So because it’s in the fstab file, it, of course, will be read after every reboot.

And if I were to do an LS of /mnt/projects, there's current year, if we actually dig a little bit deeper in current year, notice the files that we uploaded into the cloud shared folder in that storage account show up here. [Video description begins] The three project files for cblackwell are displayed: Project_A.txt, Project_B.txt, Project_C.txt [Video description ends]

8. Video: Linux File System Hard and Soft Links (it_oslsys_02_enus_08)

After completing this video, you will be able to distinguish between hard and soft or symbolic links in Linux.
distinguish between hard and soft or symbolic links in Linux
[Video description begins] Topic title: Linux File System Hard and Soft Links. Your host for this session is Dan Lachance. [Video description ends]
Managing Linux file systems requires a knowledge of filesystem links, of which there are two types. We need to be able to distinguish the difference between file system hard links and also soft links. Soft links are often also called symlinks. Symlinks stands for symbolic link.

Now if you’re wondering, what are these? Why are they used and what is the difference between them? We’ll be covering it!

To properly discuss hard links and soft links, we first have to understand the concept of inodes in the Linux file system. So what is an inode? Well, it’s a 128-byte entry in the file system table that describes a file or a directory stored on that disk partition in that file system. So it’s metadata.

Now, what does this contain? What's the purpose of the inode? Well, it, first of all, contains pointers to the actual disk data blocks. Well, that makes sense. If we've got a file, the inode points to where the actual data resides on disk.

But there’s a lot more. The inode contains other metadata which would include things like the owning user, the owning group, the permissions related to that file or directory entry and date and timestamps, which basically encompasses what you get if you type ls -l for a long listing. Or, of course, if you just type in LL. Interestingly, if you were to type ls -i, that’s a lowercase I, it would show you file system entries along with their assigned inode numbers.

Now if you're wondering what the relevance of having this knowledge is, bear with me. It's going to make itself apparent.

So let's talk about hard links. So this is a type of a filesystem link where it creates a new filename that points to an existing inode.

Now we know that the inode contains pointers to where the data resides on disk. But what's interesting is that let's say we've got one filename, so that means you have an original inode. Then you have a hard link. You create that points to that same inode so you can access any of those filenames, either the original filename or the hard link to modify the file data. And you would be modifying the same file data. It's not a copy of the file because remember we're using a single inode and that single inode has pointers to disk data blocks. And you can have numerous hard links. You're not limited to just having one hard link to an original file.

Now what about deleting the file? How does that work when you have a bunch of hard links? Well, the file data is removed when the last hard link is removed. But the thing about hard links is they are limited to being within a single disk partition. They cannot span disk partitions.

So as an example, let’s look at the syntax that would be used to create a hard link. It would be done using the LN command in Linux. Of course, that stands for Link. [Video description begins] The command example reads: ln /budgets/file1.xls /home/cblackwell/file1.xls [Video description ends] So let’s say in /budgets, we have an existing file by the name of file1.xls. Okay. So it’s going to have an inode already. Well that would be the first parameter to the LN command, where it's the source file.

The second parameter is, where would you like to create the hard link? The hard link in this example is being created in /home/cblackwell. And it’s being given the same filename, file1.xls. It certainly does not have to use the same filename. So now we’ve got two file1.xls files in different subdirectories. Well, how do you tell which one is the original? There really is no way. Well, maybe if you look at the date and time stamps. But other than that, there's no way to tell which one is the “original”. They’re all pointing to the same inode.

And so pictured on the screen here. [Video description begins] A new page opens with the title: Hard Links and Inodes. A screenshot is displayed below. A Linux page is seen with the header: cblackwell@ubuntuserver1 :~$ ls -li A list of commands is seen below it. [Video description ends] The technician has issued the ls -li command. Well, we know that the L means long listing. We know the i means inodes. Notice for in this example in our screenshot file1.txt, the inode number is shown here as being 1835021. That’s assigned by the Linux operating system.

Now the technician has already used the LN command here to create a hard link and that's not shown in the screenshot. But what is shown is that there is a file1.txt in the TMP directory. Now it could have been created with a different filename for this hard link.

But notice that when you do an ls -li, the hard link is using the exact same inode number, which in this case is 1835021.

In our next screenshot, the technician has issued the ls -l command, so long listing. Well notice that in the second column to the right because the leftmost column shows whether it’s a directory or not and the permissions for the owning user, the owning group and other. But in the next column, this numeric value is showing the amount of hard links to this file or directory, whatever the case might be. [Video description begins] In the screenshot, a list of directories is displayed. The hard link amount numbers are highlighted in the middle row that the presenter indicates. [Video description ends] Okay, so that's hard links. So for convenience to modify the contents of the same file, you might create a hard link in a convenient location.

Let's get into symbolic links or symlinks. So this is a type of filesystem link, just like a hard link is. And it's a new filename just like a hard link is. But here’s what’s different! With a symlink, you get a new inode and that inode points to an existing filename.

Wait a second! What does that mean? Well, the new inode points to the same data blocks of an existing file. However, file data can be modified using any of the symbolic links, just like with a hard link. And the file data is deleted when the last symlink is removed, again, similar to our hard links.

But symbolic links can span disk partitions. You can have a symbolic link on one disk file system that points to a filename in a totally different file system. You can’t do that with hard links.

Let’s look into an example of this. [Video description begins] The command example reads: ln -s/budgets/file1.xls /home/cblackwell/file1.xls [Video description ends] We would use the LN command with the -s parameter to create a symbolic link. In this example, the original file we’re pointing to is in /budgets, it’s called file1.xls. And we’re just creating the symbolic link in a user home directory. Now because we have a new inode, that means we can have, for this symbolic link, different file owners, different group owners, different permissions.

So we have a new set of metadata. But in the end, we’re still pointing to the same original data blocks on disk.

9. Video: Working With Hard and Soft Links (it_oslsys_02_enus_09)

Learn how to work with hard and symbolic links in the Linux file system.
work with hard and symbolic links in the Linux file system
[Video description begins] Topic title: Working With Hard and Soft Links. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I’ll be working with hard and soft links in the file system.

Now remember, what these essentially provide is an alternative way to access a file. For example, you might have a file in another location on a server or elsewhere locally in another file system, but you would prefer to access it with a link in your home directory.

Now, that could be true whether you're using the command line in Linux or whether you're using a desktop GUI. [Video description begins] A blank Linux host page is open. The header reads: cblackwell@ubuntuserver1 :~$ [Video description ends] So we’re going to go ahead and work with both hard and soft or symbolic links.

Now, first things first. Let's get started with looking at what we have. If I type pwd, for Print Working Directory, it’ll return that I’m currently in my home directory.

If I type ls, notice I have a number of sample files here. For example, I’ve got a file here called customers.txt If I cat the customers.txt file, just got some sample customer information along with their related cities. [Video description begins] A list of four cities and the customer names appear as the output, namely: Codey Blackwell - London, Lucas Brenner - Toronto, and so on. [Video description ends]

Let’s start by making a hard link to customers.txt And for this example, I’ll just be making the hard and soft links here in the same home directory where the customers txt file is for demonstration purposes.

Now we’ll explain hard links again in detail. Once we create the link, let's first create the link and then we'll examine what's happening.

LN is the command we use in Linux to create both hard and soft links. So I'm going to create a link. So ln, the source file is in the current directory, so I don’t have to specify the path, it’s called customers.txt And I want to create what we’re going to call hard link_customers.txt. That’s it! You specify the source and the target where you want the link to exist. Now in this example, again it's all in the same subdirectory. Normally that wouldn't be the case, but it'll make it easier for us to talk about it.

All right, let's clear the screen and do an LS. Now notice if we look at customers.txt and the hard link file to it, they just look like text files. There's nothing special about it. If I cat the hard link file, I get the same thing as if I were catting the original customer’s file.

Let’s make a change to the customer’s file, sudo nano customers.txt Let’s change Cody Blackwell’s city from London to Toronto. So Cody Blackwell is in Toronto. This is in the customer’s file. So why don’t we just cat the customer’s file again? Sure enough, Cody Blackwell is in Toronto.

If we cat the hard link file, notice that it also picks up the change. We have more than one way to access the same core data. Now, to explain this properly, let’s begin by running, ls -li [Video description begins] The presenter clears the screen to run the new command. [Video description ends] Now the L means long listing, but the I means we want to view the inodes. If we take a look at the inode, which is a number assigned to this file entry in the file system customers txt, notice that the inode, in this case, is 1835074.

Notice for the hard link that we made, it’s using the same inode number. [Video description begins] The hardlink_customer inode number is: 1835074. It is the same as the customers.txt [Video description ends] Now the inode, if you think about it as an entry in the file system with metadata about a file. Like the owner, the owning group, the permissions, the date and timestamps and pointers to the actual data blocks on disk.

So when you make a hard link, you’re using the same inode number, which means the same permission sets, and so on. Hard links cannot span disk partitions though, that’s important.

Okay, let's create a symbolic link or a soft link, otherwise also called a symlink. All we do for that is ln, and we add the -s parameter that makes it a symbolic link. As usual, we specify the source. Let’s work with the customer’s file again, and let’s call this softlink_customers.txt [Video description begins] The customer's file reads: customers.txt [Video description ends] If we do, let’s say a ls -li, let’s say for *customer* So that way we only have customer stuff shown here. While the customer’s txt file shows up again with the same inode number as the hard link to it. [Video description begins] The customer.txt number reads: 1835074 [Video description ends]

But when you create a symbolic link, so here’s our soft link file. First of all, the color of the text here in Ubuntu Linux is different and notice it has what appears to be an arrow symbol pointing to customers.txt

So you're creating a link that points to a file, but it gets its own new assigned inode. [Video description begins] The softlink_customers inode reads: 1835021 [Video description ends] Notice the inode numbers are different from the hard link and the original file versus the symbolic link. The symbolic link has a new inode.

Now it still points to the exact same data blocks on disk. But what's different is because it has a different inode, it means you can have different permission sets, a different owning user, a different owning group, and so on. Let's see if this is true.

If I were, let’s say to run sudo nano, the text editor, against our soft link file. Why don’t we change our user Maxwell Bishop here currently in London to the city of Halifax, and we’ll go ahead and save that out. So if we cat the soft link customers file, it's showing that Maxwell Bishop is in Halifax. So, I wonder what would happen if we catted the original customer’s file, should be the same. cat customers txt, Maxwell Bishop is in Halifax.

So just because you have a new inode for that file system entry doesn’t mean the data is different. You’re still pointing to the same data blocks with a symbolic link. The other great thing about symbolic links, remember, is that they can span different file systems, they can span partitions.

So the source file might be on one file system and the link might be on a totally different file system.

10. Video: Managing Linux File Systems (it_oslsys_02_enus_10)

In this video, find out how to manage and repair Linux file systems using commands such as fsck and tune2fs.
manage and repair Linux file systems using commands such as fsck and tune2fs
[Video description begins] Topic title: Managing Linux File Systems. Your host for this session is Dan Lachance. [Video description ends]
In this demo, we’ll be taking a look at a few Linux commands that we can use to manage Linux file systems.

When I say managing a Linux file system, I'm not talking about making a file system such as formatting a partition. We've already talked about that.

What I’m really focusing on here is checking Linux file systems to make sure that they aren’t corrupt. Because sometimes a corrupt file system entry can actually prevent a file system from being mounted into a Mount Point Directory. So naturally, that’s a big problem.

So not only can we run some of these commands to check for corruption in the file system, but in some cases, it can also repair damaged file system information. [Video description begins] A blank Linux host page is open. The header reads: cblackwell@ubuntuserver1 :~$ [Video description ends]

So let’s take a look at some of these commands, starting with the file system Check command, man fsck, that’s the file system check command. [Video description begins] A new page opens with the header: FSCK System Administration. It has some categories, namely: Name, Synopsis, Options, and so on. [Video description ends]

If we look at the man page, the Help page, it talks about here that it can check and repair a Linux file system. And then, of course, as we go through the help, it explains it further. Along with the exit status returned by the file system check. And that can be very important, if you’re scripting, you want to capture what the result of running a file system check was. [Video description begins] A list of conditions for the fsck exit status is displayed, including: File system errors corrected, System should be rebooted, Operational error, and so on. [Video description ends]

But also as we go further down, we have the command line options -l versus -r, and so on. Okay, so it’s just a regular man page.

So I’ll type Q to get out of that, and let’s start using file system check. I’m going to run sudo fsck, file system check, /dev/sdb. So what I'm doing here is pointing only to a device. Watch what happens when we press Enter. We get strange error messages about bad magic numbers, the superblock in the file system being invalid. Okay, well that’s because we’re not pointing to a partition, so of course, there’s no file system there. It’s just a disk device.

If I were to clear the screen and use the up-arrow key to bring up that previous command, and let’s say, I point to a partition that I know exists on storage device SDB. So sdb1. This time it reports back that our partition is clean. It also reports how many files we have out of how many potential files could be there as well as blocks. The key here is that there are no error messages resulting from corruption.

If I were to run sudo mount and let’s pipe that to grep and let’s look for SDB. Is it mounted at all? Nothing. What if it were mounted? How would that behave? sudo mount /dev/sdb1, under a directory on the root I already have called data1. So if we now check to see if it’s mounted, sdb1 indeed is mounted. It's an ext4 file system and all that good stuff.

Let’s use the up-arrow key to go back to our file system check command against /dev/sdb1. And so when we press Enter, we get an error because it says that it’s mounted. It cannot continue aborting. Okay, so the default behavior is that it doesn't want the file system to be mounted. And again, if you're having problems with the file system, if you know you already have issues, you probably can't mount it anyway.

Let’s cat /etc/fstab, file system tab. [Video description begins] A list of outputs appears on the screen. A column is shown with the following six headers: file system, mount point, type, options, dump, and pass. [Video description ends] This is a file where you can put in persistent mount points, things that you want mounted at boot every time the system starts.

I'm interested in the sixth column or sixth field to the right. Now on the left, of course, we've got the device, then we've got the mount point, the file system. Some options like read, write, whether the disk dump utility will look at this file system. That’s the zero in this case.

And then you will have either a 0, 1, or 2. And what that means is whether FS check should perform a quick check on bootup of the file system. 0 means no, but for the root file system shown up above here, [Video description begins] The presenter highlights the root file system. It reads: /ext4 defaults 0 1 [Video description ends] notice that it’s got a value of 1. That means that the root file system will have FS check run against it automatically at boot time before any other ones listed with the value of 2.

Now we can verify this by doing a man 5 fstab. Putting the 5 there means that we want help not on a command but on a configuration file. And as I go further down here, when it talks about the sixth field, it talks about whether FS check will perform a check at boot time and in what order. So that’s a bit about FS check.

I'll press Q to quit out of that. Another command of interest is going to be the tune2fs. For example, sudo tune2fs -l, for list, /dev/sdb1 What this does is it lists some detailed information about that particular file system. Now, if I scroll back up, we're primarily interested in here in the file system state, which is showing here as being clean.

Of course, there are many other interesting attributes being shown here for that file system.

If we were to take a quick look at the man page for that man tune2fs, this is a command that allows you to modify some settings or file system parameters for ext2, ext3, and ext4 file systems. [Video description begins] The page header reads: System Manager's Manual. The presenter indicates the file systems names given in the Name category. [Video description ends]

Okay. Well, what kind of stuff might we do? Well, you might do something like this.

You might say, is there a volume label assigned to the partition sdb1? I could run sudo tune2fs -l /dev/sdb1, like we did before, but I could say I only want to see the line that has volume on it. And there is no volume name, so we can set one. I can do that with sudo tune2fs -L let’s say we call it HQData, for headquarters data, /dev/sdb1, Enter. Just sdb1, Enter.

There we go. Let’s clear the screen, and let’s go back to where we were listing the volume label. Notice now the volume label shows. [Video description begins] The File system volume name reads: HQData [Video description ends] So all that does is helps make it much more readable on a system where you're dealing with a lot of different file systems. Sometimes meaningful names make file systems easier to identify.

And finally, the last thing I’ll do here is run sudo tune2fs -i 1w this means I want to perform a file system check once a week. Okay! Of /dev/sdb1 So if you want to schedule this type of thing without using other commands like file system check and creating cron jobs, you can go ahead and do this using the tune2fs command.

11. Video: RAID Disk Levels (it_oslsys_02_enus_11)

Upon completion of this video, you will be able to define common redundant array of inexpensive disks (RAID) disk levels for performance and fault tolerance purposes.
define common redundant array of inexpensive disks (RAID) disk levels for performance and fault tolerance purposes
[Video description begins] Topic title: RAID Disk Levels. Your host for this session is Dan Lachance. [Video description ends]
Well, you can’t have a complete discussion about storage without talking about RAID, R A I D. Which stands for Redundant Array of Independent Disks, or in some cases, depending on which literature you refer to, maybe inexpensive disks. It doesn’t matter. What matters is knowing what it is.

Let's go through it. So what is RAID? RAID is a group of physical disks working together. Now, physical disks, well, if you’re using a virtual machine, you could have multiple virtual disks added to it, and you could still configure software RAID. So we'll take that with a grain of salt.

It's not always necessarily literally physical disks, but it is multiple disks working together. Now, why would we want to organize multiple disks working together? Why not just have one large disk?

Well, one of the reasons is for improved performance. You have multiple disk subsystems working together instead of just one. So you have improved performance, but you also get improved availability depending on how you configure RAID, whereby, for instance, if you have a failure of one disk and you’ve mirrored or you have an up-to-date copy of that data on a second disk, well, then you still have the second disk available and up and running.

In the enterprise, with high-end servers, we’re talking about physical high-speed disks and a hardware RAID controller. Whether this is a network storage appliance of some kind or whether it’s a single individual physical server, the RAID controller might be built into the motherboard. If it’s a server class piece of hardware, or it could be an add-on card.

And, of course, the disks would be connected to the hardware RAID controller. That means that when you power on that physical server, you would press a specific keystroke, which will vary depending on the type of controller you’re using to enter the configuration utility to configure hardware RAID on that machine.

Now, even though it might be multiple disks working together to the operating system, it will look like a logical disk or a number of logical disks, depending on how you configure it.

And we're going to be talking more about that. So that's hardware RAID, but you can also configure software RAID within the operating system within Linux.

Hardware RAID is always way more reliable and performs better than software RAID because the hardware RAID controller is firmware that’s designed for a specific purpose, as opposed to software running in an operating system that's designed to do many, many things.

However, both can be used either independently or at the same time. Usually, it doesn't make sense to use it at the same time in most cases.

There are many levels of RAID. We’ll just touch upon the most common here, starting with RAID level 0, which is called disk striping. So we’ve got two disks or more working together. So data, when it needs to be written to disk, is broken into smaller chunks or stripes. And each of those stripes is written across all of the disks in the array. In this case, there are only two disks in the array.

What's the benefit here? Performance. You've got multiple disks doing the work. However, with RAID 0, if you lose one of the disks in the array, everything is inaccessible. All data is inaccessible.

So with RAID level 1, otherwise called disk mirroring, when we write something to disk, a complete copy is written to each disk configured in the RAID 1 disk mirroring array. In this case, for example, two.

Now the benefits are multifold here. You’ve got performance as a benefit because you have two disk subsystems, at least at the disk level, handling the writing, but you also have the availability component as a benefit because if the first disk fails, then you can simply activate the second mirrored disk as being the active one. And you’ve got an up-to-date copy of the data.

Depending on the environment, the solution you’re using will determine whether disk mirroring can automatically switch to the mirrored copy in the event of a failure. But it’s certainly possible and common.

Next, we’ve got RAID 5. This is called disk striping with distributed parity. Parity information is error recovery information. So just like with RAID 0 striping, with RAID 5, data written to disk is broken down into smaller chunks or stripes, and then each chunk is written across the disks in the array. Now with RAID 5, you need at least three disks. But not only is the data written across all of the disks in the array, but also parity or error recovery information is also written on a different disk than the related data.

So we never write a stripe of data, let’s say on the first leftmost disk along with its related parity or recovery information. [Video description begins] The presenter indicates a diagram displayed on the screen. It shows a folder and three array disks. The folder is sending data across the disks. [Video description ends] Because if disk 1 fails the first disk in our example, we lose the data, and we lose the parity information. How do you rebuild that?

The purpose of RAID 5 is, of course, you get a performance benefit, but also it can tolerate the failure of one disk in the array. One disk fails in the array, because the parity for the data on the failed disk is stored on alternate disks, we can reconstruct the missing data on the fly when it's requested. Of course, it's going to be a bit of a performance degradation as a result of that until you replace the failed disk and rebuild the array.

RAID Level 6 uses what’s called double-parity RAID. This means that you need at least four disks configured in the array, whereas, for RAID 5, you only need three. So as usual, with striping, data that’s being written to disk is broken down into blocks or stripes that are evenly written across all of the disks in the array. In this case, at least four disks.

However, two parity stripes are written on each disk. Hence, double-parity, double-error recovery information. As with RAID 5, the parity or error recovery information is never written on the same disk for the related data because that would make no sense at all.

The benefit of RAID 6, besides performance, is that it can tolerate two disk failures, unlike one disk failure with RAID 5. And just like with RAID 5, it can reconstruct data in memory on demand based on the parity or error recovery information. But things are slower than when all of the disks in the array were fine and functional. There’s a lot of math to compute the missing information from the parity information.

Then we have RAID level 10, which really combines RAID level 1 disk mirroring and RAID 0 disk striping, in that order. So, disk mirroring occurs first followed by striping. The benefit here is, of course, fault tolerance, but definitely a performance benefit as well because you're striping across multiple disks.

So RAID 10 requires a minimum of four disks, whereas RAID 1 mirroring only would require two. So data is striped then across the mirrored pairs. And this can tolerate multiple disk failures as long as they are not in the same mirrored pair.

So when you have a busy read-and-write environment, so let’s say a database that gets queried heavily but also gets updated heavily, RAID 10 can be very useful for that type of situation.

12. Video: Configuring Software RAID in Linux (it_oslsys_02_enus_12)

Discover how to configure software RAID in Linux.
configure software RAID in Linux
[Video description begins] Topic title: Configuring Software RAID in Linux. Your host for this session is Dan Lachance. [Video description ends]
In this demo, I'm going to be configuring software RAID within Linux. We know that there are many different levels of RAID, and that they can either provide performance benefits or increase availability if we have a failure of some kind at the disk subsystem level.

We're going to be configuring disk mirroring. Now RAID level 1 disk mirroring requires two disks. Anything written to what will appear as one disk in the operating system is actually being written to two for availability purposes. [Video description begins] A blank Linux page is open with the header: cblackwell@ubuntuserver1 :~$ [Video description ends]

The first thing I’m going to do here in Linux is run sudo lsblk, list block, I’m going to show block storage devices, --scsi. I am primarily interested in devices SDC and SDD. And what I really want to do is check out how they're partitioned, if at all.

So to do that, I’ll run sudo fdisk -l, for list, /dev/sdc and then /dev/sdd, Enter. Okay! So device SDC is 20GB in size, but there are no partitions and the same thing is true for device SDD. Perfect! [Video description begins] The presenter runs the Clear command to clear the screen. [Video description ends]

What we have to do is create a partition and flag it as being used for software RAID on each of the disks. Then we can configure the mirror across those two disks. How do we go about this? Well, let's start with the first disk device.

One thing at a time, sudo fdisk /dev/sdc. I’ll press N to create a new partition. The default is P, a primary partition, which I’m okay with. Enter. I will also press Enter for the default partition number of one [Video description begins] There are four partition levels on screen. The presenter selects the default number 1. [Video description ends] and the default value for the first and the last sector of that partition. [Video description begins] The first sector default reads: 2048. The last sector default reads: 41943039. [Video description ends] I'm asked if I want to remove an existing signature on the disk. I’ll type in Y. It was used by something else previously.

But the next thing I need to do is press T. When I press T here within fdisk, it allows me to select the partition type. I can type a L to list all of the partition types.

But I know what I need to do is type in FD, which will set that to a Linux RAID autodetect type of partition. That’s all I need to do for that disk. W to write that to the partition table.

Then I’m going to do the same thing but for the second disk that will be in the array. [Video description begins] The presenter runs the Clear command to clear the screen. [Video description ends] So sudo fdisk /dev/sdd This time I’m going to repeat the same steps. N for a new partition. I’ll just keep pressing Enter to create partition 1, a primary partition. I’ll press T to set the type to FD, which is Linux RAID autodetect. And I’ll write that out to the partition table by typing W.

So now our two disks are set up at least at the partitioning level. If I use my up-arrow key, I can go back to where we were listing how those two devices were carved up, and notice that we’ve got sdc1 Linux RAID autodetect, and also, sdd1, same thing, the type is Linux RAID autodetect. That’s what we want to see. [Video description begins] The presenter runs the Clear command to clear the screen. [Video description ends]

The next thing I’ll do is install the software we need to manage mirrored disks, so I’m going to run sudo apt install mdadm, mirror device administration. And before you know it, it’s done. It’s installed. So I'll clear the screen.

Now I'm going to run sudo mdadm because I want to create a mirrored device. I want to create a disk mirror. So --create /dev I’m going to call it /md1, mirrored device one, --level = 1 because remember, RAID level 1 is disk mirroring, -- raid -devices = 2 and I will list them here as being /dev/sdc1 and /dev/sdd1, Enter. Continue creating the array, Yes. Okay!

So it says the /dev/md1 array was started. So let’s check the progress here, sudo mdadm --detail for /dev and we know it’s called md1, that’s how we refer to it. [Video description begins] The presenter runs the Clear command to clear the screen. [Video description ends] It's currently at 20% complete for synchronizing the two partitions. Now, even though they're empty, this is just what it does initially. [Video description begins] A page of details is shown as the outcome of creating the array, such as: Raid devices: 2, Total devices: 2, State: clean resyncing, Consistency policy: resync, and Resync status: 20% complete [Video description ends]

So what we would now do is we would make a mount point directory. [Video description begins] The presenter runs the Clear command to clear the screen. [Video description ends] So let’s say sudo mkdir / I’ll just call it, mirror, for the sake of clarity. So, of course, now we have to run sudo mkfs, to make a file system, let’s say -t, for type of, ext4 on /dev/md1

And then, of course, we can run sudo mount to mount /dev/md1 or mirrored device, into the /mirror folder. And it’s done! So we now have access to writing to the disk mirror by accessing the /mirror mount point directory.

13. Video: Linux Logical Volume Management (LVM) (it_oslsys_02_enus_13)

After completing this video, you will be able to define the purpose of LVM in the Linux environment.
define the purpose of LVM in the Linux environment
[Video description begins] Topic title: Linux Logical Volume Management (LVM). Your host for this session is Dan Lachance. [Video description ends]
In Linux, Logical Volume Management, or LVM, allows you to pool together or to group together storage media. Now it doesn't necessarily have to be physical. If it's a virtual machine running Linux, they could be virtual disks.

But what you do is you pool those disks together, all of the space together, so you combine the storage space across the disks.

Now, why would I do that? Because we could then create a logical unit based on that combined storage space so that the operating system would see what is a logical volume.

There is some terminology here that’s very important when you work with logical volume management.

Now, in some cases you might not have to work with it because it might automatically be set up when you initially install Linux, it might use LVM by default. But you can also manage it for data disks as well.

So the first term is a physical volume or a PV. This represents a storage device. It says physical storage device. But we know that that could also mean a logical disk for a virtual machine.

The next LVM concept is a volume group, a VG. So this is, of course, as the name implies, a collection or its pooled storage space from your physical volumes. And when you pool all of the physical volume space together into a volume group, you can either create one or more volumes in that volume group.

Of course, then you have the logical volume itself, LV, which is presented to the operating system, which is similar conceptually to a disk partition seen from the perspective of the OS.

Now if this sounds like using a RAID disk solution, it's different because LVM does not have any provisions for things like data redundancy and parity information like some levels of RAID do, like RAID level 5. LVM just gives us a way to manage disk space, perhaps a little bit easier, when it spread across many disk devices.

So when you're configuring logical volume management, the first thing you do is you use the pvcreate command to mark storage devices so that they can be used by LVM.

Next, you then create a volume group from those marked storage devices and you do that using the vgcreate command.

Once you've got a volume group, as you know, you can create one or more logical volumes and this is done using the lvcreate command.

The next thing you have to do is format that logical volume so it has a file system and it's usable.

And then as usual, with any new file system, you need to mount it to make it accessible into an empty Mount Point directory.

In our screenshot, the technician has issued the sudo lvmdiskscan command, logical volume management disk scan. Now anything that’s already designated as an LVM PV, a physical volume, will be listed as such in the rightmost column. Here we have one that would be /dev/sda3 shown that way.

However, notice what’s highlighted here are devices sdb, sdc, and sdd. These are each 20-gigabyte drives. So what we could then do as a result of the LVM disk scan command is say, okay, I want to use those disks to create a volume group.

So the volume group command then in our next screenshot. The technician has issued the sudo pvcreate command and pointed to /dev/sdb, /dev/sdc, and /dev/sdd. What this does is marks these physical volumes as such so they can be used to create a volume group. [Video description begins] In the screenshot, the three devices are listed with the message: Physical volume successfully created. [Video description ends]

We can verify that this has been done correctly with sudo pvs [Video description begins] A new screenshot appears. It displays a list of volume group devices. [Video description ends] because in the third column, those devices will have a format of lvm2.

Now the sudo vgcreate, as we know, is used to create the volume group now that we’ve marked those disks. So, the vgcreate command here is creating a volume group called VolGroup1 from /dev/sdb, /dev/sdc, and /dev/sdd.

And then if we run the sudo vgs command to get a summary of volume groups, VolGroup1 shows in the list. And notice that the size is approximately 60-gig. That's the three 20-gig physical volumes that were lumped into the volume group.

We know that the next step now that you've got the volume group is to actually create the LVM logical volume and that can be done with the sudo lvcreate command. Here -L is being passed, and we’re specifying we want to use, let’s say, 50 gig for that. -n for the name. We want to call the logical volume projects. And it’s being created in VolGroup1. [Video description begins] The command reads: cblackwell@ubuntuserver1 :~$ sudo lvcreate -L 50G -n projects VolGroup1 [Video description ends]

So the next thing you would do is mount it. So you might use the mkdir command, if you don’t already have a directory to create a directory. In this case, /projects

You would then use sudo mount to mount /dev/the volume group name, /the logical volume name, which is projects. And then after a space, you tell it where you want it mounted. In this case, /projects

And then you might use the nano command to edit /etc/fstab to make that a persistent mount point that persists between reboots.

14. Video: Configuring LVM (it_oslsys_02_enus_14)

During this video, you will learn how to configure LVM in Linux.
configure LVM in Linux
[Video description begins] Topic title: Configuring LVM. Your host for this session is Dan Lachance. [Video description ends]
In this demo, I'm going to be working with Logical Volume Management or LVM. The general purpose here in Linux is for us to take physical storage space from numerous physical storage devices, lump it together into what's called a volume group, and then from that volume group we can then choose to create one or more logical volumes. [Video description begins] A blank Linux host page is open with the header: cblackwell@ubuntuserver1 :~$ [Video description ends]

So a logical volume gets mounted to a mount point. And when you're working with a logical volume, you might actually be utilizing storage space from multiple underlying storage devices.

So let’s get started with this. The first thing I’m going to do here in Linux is run sudo lvmdiskscan I want to see if I have any physical storage devices that are suitable for use with logical volume management.

I am interested primarily not in device SDA, but rather in devices SDB, SDC, and SDD. I’ve got three 20-gig drives available for this purpose.

So I’m going to run sudo pvcreate, this stands for physical volume create. This is how you mark underlying physical storage devices as being usable within an LVM volume group.

So /dev/sdb, but also /dev/sdc and /dev/sdd Okay, so I have marked these devices as physical volumes. [Video description begins] The three devices are listed with the message: Physical volume successfully created. [Video description ends]

Let’s clear the screen with Clear, and I’m going to run sudo pvs, physical volume summary. Well, it looks like there’s one that’s already there on SDA that was created by my Ubuntu Linux installer. [Video description begins] The device name reads: /dev/sda3 ubuntu-vg [Video description ends] Notice that the format column shows LVM version two. However, we are interested in devices SDB, SDC, and SDD. And they’re showing up here each being 20-gig in size.

The next step is to go ahead and create a volume group. This I can do with sudo vgcreate, volume group create. I’m going to call it VolGroup1. It will consist of /dev/sdb, /dev/sdc, and /dev/sdd

Now I can make multiple volume groups to split up that space, but in this example, I am choosing to use the free space on all of those devices for this single volume group. You don’t have to do it that way.

Now we can run sudo vgs, volume group summary or show. And so there’s VolGroup1 Under the number of physical volumes, or number of PV column, it says 3 But there’s no logical volumes, no LVs, at least not yet. Notice that the volume size is approximately 60GB in size.

So the next thing I do is create a logical volume. Now, I can have a single logical volume that will consume the entire 60-gig or approximately 60-gig of space. Or I could create multiple, smaller logical volumes in VolGroup1.

In this case, I'm going to create just one logical volume. So sudo lvcreate, logical volume create, -L Let’s say, I want to use the 59.99G Capital G for gigabytes, -n for name I want to call this logical volume projects, and I want to create it on VolGroup1. Enter.

Now I get a message saying that VolGroup1 has insufficient free space, so I'm using too much of it.

Okay, well, I'm going to bring up that previous command. We're cutting it a little too close here. Let’s go ahead and just use 50-gig of that space. I’ll press Enter. LVMs need a bit of space left free to function correctly. So now we've got our project's volume created.

Now the next thing I would do is run sudo mkfs, makefile system, -t ext4 let’s say is the file system type I want to create So I'll go to format that volume.

But the way I refer to it here is /dev/mapper/VolGroup1 -projects. Enter. Okay! It looks like it’s creating the file system, allocating group tables and inode tables, creating a journal. Everything’s good!

So to actually gain access to that file system, I need a standard mount point. So I’m going to run sudo mkdir / let’s say on the root, we’ll create a directory called projects and then I’ll run sudo mount /dev/VolGroup1/projects. Enter! -projects with this nomenclature. Let’s try that again.

Then I’ll run sudo mount /dev/VolGroup1/projects and then I’ll tell it where I want to mount it into. So projects is my logical volume name. I want to mount it into a folder on the root called /projects.

If I were now to run sudo mount and pipe that to grep looking for projects, it is successfully mapped into our mount point directory. Now that mount is only currently while Linux is up and running. It’s not persistent. It won’t persist between reboots unless we add it.

So I’ll use the nano text editor unless we add it to /etc/fstab. [Video description begins] A new page opens with the header: /etc/fstab. A column is seen with the following six headers: file system, mount point, type, options, dump, and pass. [Video description ends] So I’ll add /dev/VolGroup1/projects That’s what I want to mount. That’s the device, that’s the LVM. And then space, I want to mount that in /projects just like we did on the command line. File system type is ext4, so I’ll add that after a space. And we’ll just use a lot of the default setting here, so defaults. Defaults would include things like the fact that we want this to be the read-write file system. Of course, depending on permissions will really determine what users can do.

I’ll put in a zero, I don’t want to use the dump utility for this file system. And my last zero will simply be used here, which just means don't check the file system using the file system check utility. Okay!

Control X to write that out. Save modified buffer. I’ll type in Y for yes and press Enter, and it’s done! So now that Mount point will be persistent every time we boot up this server.

15. Video: Storage Area Networks and Network Attached Storage (it_oslsys_02_enus_15)

Upon completion of this video, you will be able to recognize how Linux can use network storage.
recognize how Linux can use network storage
[Video description begins] Topic title: Storage Area Networks and Network Attached Storage. Your host for this session is Dan Lachance. [Video description ends]
In the enterprise, there are plenty of cases where you might connect a Linux host to network storage.

So let's take a few minutes then to discuss storage area networks. Storage Area Network is often just referred to as a SAN, spelled SAN. What is it? Well, a storage area network is a dedicated network for storage communications.

In other words, there isn't any other type of traffic. It’s just dedicated to the transmission of the commands for reading from disks and writing to disks over a network infrastructure.

So storage consumers like our Linux server, for example, would access shared storage over the network. And there are different types of networks, we’ll cover that.

But the storage consumer, again, perhaps a given Linux server can also use local storage. Local storage that we’re all familiar with on a local server is simply referred to as direct attached storage or DAS.

Depending on your SAN solution, it’s also possible for the server to actually boot over the SAN.

Now when you have storage available over a network, that means you have centralized storage arrays, and that's often where backups occur. It’s also great as a centralized location for auditing backup activity as opposed to having to check logs on each and every individual server.

And if all storage is centralized on SAN devices, it means that you don’t necessarily need to have a backup agent then on each and every server. You might just be backing it up at the storage appliance level. So it depends on what you're doing and what your needs are.

iSCSI, Internet Small Computer System Interface. Now, traditionally we know that SCSI is an older standard for connecting devices together, and that evolved to primarily be storage devices for reading and writing.

With iSCSI, what we have is a SAN. This is a type of storage area network that uses standard equipment, standard storage that might be plugged into servers, or attached to the network. Standard network equipment like network switches, network interface cards, whatever the case might be. It's all standard equipment, not specialized in any way.

When you configure iSCSI on consumers and also storage providers, what happens is the SCSI disk I/O commands get embedded within IP packets, and then sent over the iSCSI SAN over the standard network here that would use TCP IP. But it would be dedicated for this purpose. You don't want to have your regular IP traffic like checking email, connecting to databases, on this same network for performance reasons, it should be dedicated for iSCSI.

Now you can use iSCSI hardware controllers as a way to connect to an iSCSI SAN and access shared network storage, or it can be done within the operating system by installing a software agent known as an iSCSI initiator.

Let's take a look at a diagram of an iSCSI SAN. So here, we’ve got a standard Ethernet switch that’s configured with an isolated data zone VLAN. [Video description begins] In the diagram, an Ethernet switch is connected with two initiators: Windows Server iSCSI and Linux Server iSCSI. TheEthernet switch is also connected to port TCP 3260. The iSCSI target is configured with logical unit numbers (LUNs). [Video description ends] An iSCSI SAN should be dedicated for that purpose and that purpose only.

To the right of our diagram, we’ve got a number of iSCSI targets. In other words, this is your network storage that might come in the form of a storage array connected to the network. It could be storage connected to a server that’s on the network and the server might be configured with iSCSI target software. And normally, iSCSI targets listen for connections on TCP port 3260.

So the iSCSI target provides the storage, but the consumers are called iSCSI initiators shown at the top of our diagram.

We can have Windows Server iSCSI initiators, Linux server iSCSI initiators, either in the form of a software agent in the OS or a specialized iSCSI controller card plugged into the server.

And what happens is the iSCSI initiators access the storage from the targets by embedding SCSI disk I/O commands and IP packets as we mentioned.

To the Linux server, it just looks like local storage, although, of course, really it’s not. And so, you would treat it as such. You would carve out partitions and manage it however you see fit the way you normally would with a locally attached mass storage device.

And then we have the Fibre Channel or the FC SAN. Now, this is designed to be a high-speed storage area network designed for enterprise use, which means it doesn’t use standard equipment like Ethernet switches, and so on. It uses very specialized equipment designed for this purpose, specifically. That equipment would include things like host bus adapters or HBAs that plug into each server consumer and Fibre channel switches that interconnect the storage providers with the storage consumers, not standard Ethernet switches.

As you might guess, it’s much more expensive than an iSCSI SAN solution would be. In our diagram of a Fibre channel SAN, we’ve got servers shown in the diagram. Each one would have a host bus adapter card plugged in and configured. Now what we can then do is configure those HBAs in each of those two servers to connect to each of our two switches, as opposed to just connecting to one. So we have multiple paths to storage.

For redundancy purposes in the event, for example, that we have a failed Fibre channel switch, the Fibre channel switches in turn would be connected to storage arrays. [Video description begins] In the diagram, the HBA servers are interconnected to FC switches for storage. The FC switches, in turn, are connected to storage arrays backup units. [Video description ends] So the storage that's made available over the network, which in the end would be accessible by the servers with their HBAs.

Now the storage arrays on the Fibre channel SAN would probably have backup units that would back up those storage arrays.

You can enable LUN masking, logical unit number masking, for the carved disk space in the storage arrays to limit which servers can see which disk space as being available over the network.

From a security perspective, you would then have to think about things like, Should we be encrypting data at rest in the storage arrays? If so, what solution should be used because the storage array isn’t tied to a server OS like the consumer is with the HBA.

Should we enable file access auditing? And if so, what should the scope be? You don’t want to audit everything that everyone does, it’s overwhelming. There’s too much noise. And usually, that’s done to be compliant with specific types of regulations.

So we’ve got that type of technical security, but also physical security for this equipment. It should be behind locked doors and only accessible by authorized personnel.

Another aspect of network storage, of course, is network attached storage or NAS. NAS! A NAS device is a specialized storage appliance. It’s got its own RAM, it’s got its own CPU or CPUs, and it can connect to the network in various ways, whether it's wireless or wired.

The purpose of a NAS device is to share files over a network, and it’s accessible from consumers using normal file sharing protocols like Server Message Block, SMB, or Network File System, NFS.

The NAS appliance actually contains disks, and you can update or remove and add disks as you see fit. Normally, it supports what's called JBOD, which is just a bunch of disks, which means not using RAID.

Or some NAS appliances will support various levels of RAID at the hardware level like RAID 0 disk striping or RAID 1 disk mirroring.

16. Video: Configuring a Linux-based iSCSI Initiator (it_oslsys_02_enus_16)

In this video, find out how to configure an Internet Small Computer Systems Interface (iSCSI) initiator in Linux.
configure an Internet Small Computer Systems Interface (iSCSI) initiator in Linux
[Video description begins] Topic title: Configuring a Linux-based iSCSI Initiator. Your host for this session is Dan Lachance. [Video description ends]
In this demo, I will be configuring a Linux-based iSCSI Initiator. Now, before you can use an iSCSI initiator to connect to network storage, the network storage has to be made available first on the iSCSI target.

What we’re going to use, in this case, for this demo is a Windows Server as the iSCSI target and the Linux will be a client that consumes that disk space as an iSCSI initiator.

So the first thing we should do here in Windows is make sure we have that support installed for iSCSI. So, I’m going to go to my Start menu, I’m going to fire up Server Manager. [Video description begins] On the Server Manager dashboard, a tab is displayed with the title: Configure this local server. It has four options, namely: Add roles and features, Create a server group, and so on. [Video description ends] And then I’ll click Add roles and features. I’ll keep clicking Next to go through all of these settings until I get to the Roles screen, Select server roles, where down below I can expand File and Storage Services. [Video description begins] A dialog box opens with the title: Select server roles. It has two sections: Roles and Description. Under the Roles sections, a list of names is displayed, such as: DHCP Server, File and Storage Services, and more. [Video description ends]

I can expand file and iSCSI services. Some of the components here are turned on, like the File Server, File Server Resource Manager, but I want to turn on the iSCSI Target Server. So I’ve got that turned on, I’ll click Next. And I will keep clicking through this until I get to the install part. Once that’s installed, I’ll click Close. [Video description begins] The presenter returns to the Server Manager dashboard. [Video description ends]

And on the left, what I want to do is go to file and storage services, iSCSI. Now it says to create an iSCSI virtual disk, start the new iSCSI virtual disk wizard. So under Tasks, on the right, I’ll choose New iSCSI virtual disk. [Video description begins] A dialog box opens with the title: Select iSCSI virtual disk location. It has two sections: Server and Storage location. [Video description ends]

In the list down below, I’ve got drive F available with nothing on this machine, so I’m going to select it to host my iSCSI virtual disk files. I’ll click Next. I’ll call this iSCSI_Vdisk1, iSCSI virtual disk one. [Video description begins] The presenter types the name in the Name field. And clicks Next. [Video description ends] Let's use up the 9.91 gig dynamically expanding as we start putting file content on there.

Then I'm asked to add a new iSCSI target. I’ll click Next. And I’m going to create a target called LinuxHosts. Now, the terminology isn’t great here. What this really means is an allow list. Who should be allowed to connect over the network to this server where iSCSI storage will be hosted? So, Specify access servers. Click Add to specify the iSCSI initiators. Okay!

And down below I’ll Enter a value, I’ll select IP address. And I’ll Enter the IP address of the Linux host down at the bottom and I’ll click Ok. So it will be allowed to connect. [Video description begins] The value of the IP address reads: 192.168.2.41 [Video description ends] I’ll continue by going to Next.

I'm not going to enable any authentication on this example, so I’ll just click Next. And Create and then close.

Okay, now we've got some iSCSI storage available here in Windows. Now having that iSCSI virtual disk selected down below under iSCSI targets, I can right-click on it and choose Properties where I can copy the IQN. [Video description begins] The IQN reads: iqn.1991-05.com.microsoft:win-m6cgn1mfjlq-linuxhosts-target [Video description ends] This special name is going to be important.

We're going to need to connect to it from our Linux host in a minute, so I'm going to go ahead and copy it to my clipboard. [Video description begins] The iSCSI Virtual disk name reads: F:\iSCSIVirtualDisks\iSCSI_Vdisk1.vhdx [Video description ends]

The next thing I’ll do here, back on my Linux host, is I’ll run sudo iscsiadm, that’s a Linux command, --mode discovery --type sendtargets --portal and this is the IP address of the Windows host which is serving as our iSCSI target. I’ll press Enter. [Video description begins] The IP address for the Windows host reads: 192.168.2.167 [Video description ends]

What it’s doing is saying that it’s listening for iSCSI on port 3260, that’s TCP. And here’s the IQN here that we saw over on the Windows side, so it can see it.

To attempt to make a connection to it, I will run sudo iscsiadm --mode and this time I’ll specify node, I’ll set --targetname to the IQN, which is shown above. I’ll then set --portal once again to the IP address of our Linux host and then I’ll use --login. I’ll press Enter. Okay! It says that the login was successful. Let’s clear the screen.

Now If I run the lsblk, list block devices command, --scsi and then if I pipe that to grep and look for iscsi, notice that it knows that we’re connected to an iSCSI disk somewhere over the network.

So now if I run sudo fdisk -l and press Enter, our 10 gig, or really it’s 9.91 but close enough, our 10 gig iscsi disk shows up to Linux to the kernel as being a device locally called /dev/sde

While at this point it's business as usual, just partition it, format it and mount it, and you’re ready to go. Let’s do it! [Video description begins] The presenter runs the Clear command to clear the screen. [Video description ends] sudo fdisk /dev/sde. Okay, perfect! N for new partition, P for primary.

I’ll just press Enter to accept the defaults for the partition number in the sectors. And I’ll press W to write that out to disk, [Video description begins] The presenter runs the Clear command to clear the screen. [Video description ends] and then I’ll run sudo mkfs, make file system, -type ext4 for /dev/sde1. All right!

And then I’ll run sudo mkdir, on the root. For the sake of clarity in this demo, let's just call the directory that we're creating on the root /iscsi and let’s do a sudo mount of /dev/sde1 into /iscsi.

So now if we do an sudo mount, let's say we just pipe that to grep look for iscsi, we can verify indeed that the file system is mounted.

So that in the Linux kernel, the network storage actually just appears to be a local storage, even though really it’s being accessed over the network.

17. Video: Course Summary (it_oslsys_02_enus_17)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary. Your host for this session is Dan Lachance. [Video description ends]
So, in this course, we’ve examined how to manage local and remote Linux file systems, including network storage.

We did this by exploring Linux storage concepts, the file system hierarchy, and storage command line management.

We created and mounted Linux file systems. We managed remote mount points, and we worked with hard and soft links and managed file systems.

Next thing we did is we discussed RAID disk levels, and we configured Software RAID, and LVM, Logical Volume Management, in Linux.

We then discussed storage area networks and network attached storage, and we configured an iSCSI SAN in Linux.

In our next course, we’ll move on to explore how to manage Linux file system permissions, compression, and archiving.

Course File-based Resources
•	Managing Linux File Systems
Topic Asset

•	Configuring LVM
Topic Asset

•	Configuring a Linux-based iSCSI Initiator
Topic Asset
© 2024 Skillsoft Ireland Limited - All rights reserved.