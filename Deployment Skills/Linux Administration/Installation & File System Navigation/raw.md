CompTIA Linux+: Installation & File System Navigation
There are many varying distributions of Linux available for personal and enterprise use and embedded in a large variety of devices. Linux technicians must have the ability to install Linux and navigate and search Linux file systems. In this course, you will explore Linux components and distributions, and how those distributions can address specific business needs. Then you will discover how Linux interacts with the basic input/output system (BIOS) and Unified Extensible Firmware Interface (UEFI). Next, you will examine the various ways to boot and install Linux, learn how to install a Linux server and desktop from an ISO image, and deploy a cloud-based Linux virtual machine. Finally, you will use Linux commands to manage hardware and navigate and search Linux file systems. This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_01_enus_01)

    2. Video: Linux Overview (it_oslsys_01_enus_02)

    3. Video: Linux Distributions (it_oslsys_01_enus_03)

    4. Video: BIOS, UEFI, and the Linux Startup Process (it_oslsys_01_enus_04)

    5. Video: Linux Installation Sources (it_oslsys_01_enus_05)

    6. Video: Installing a Linux Server (it_oslsys_01_enus_06)

    7. Video: Installing a Linux Desktop (it_oslsys_01_enus_07)

    8. Video: Deploying a Cloud-based Linux Server (it_oslsys_01_enus_08)

    9. Video: Managing Linux Hardware (it_oslsys_01_enus_09)

    10. Video: Using Linux File System Navigation Commands (it_oslsys_01_enus_10)

    11. Video: Navigating the Linux File System (it_oslsys_01_enus_11)

    12. Video: Searching the Linux File System (it_oslsys_01_enus_12)

    13. Video: Filtering Data with Linux Commands (it_oslsys_01_enus_13)

    14. Video: Course Summary (it_oslsys_01_enus_14)

1. Video: Course Overview (it_oslsys_01_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance [Video description ends] Hi, I’m Dan Lachance.
There are many varying distributions of Linux available for personal and enterprise use, as well as being embedded in a large variety of devices. Linux technicians must have the ability to install Linux and navigate and search Linux file systems.

In this course, I’ll first cover Linux components and Linux distributions and how those distributions can address specific business needs.

I’ll then cover how Linux interacts with the BIOS and the UEFI followed by discussing various ways to boot and install Linux.

Next, I will install a Linux server and desktop from an ISO image and I will deploy a cloud-based Linux virtual machine.

Lastly, I will use Linux commands to manage hardware and navigate and search Linux file systems.

This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: Linux Overview (it_oslsys_01_enus_02)

Upon completion of this video, you will be able to define Linux OS components such as the kernel, libraries, the command line, and user interfaces.
define Linux OS components such as the kernel, libraries, the command line, and user interfaces
[Video description begins] Topic title: Linux Overview. Your host for this session is Dan Lachance [Video description ends] The Linux Operating System. Linux is based on the older Unix Operating Systems. Therefore it shares many similarities.
If you have experience with Unix, then you're going to feel pretty at home already in Linux if you're not already familiar with Linux.

So Linux then was developed by Linus Torvalds in the early 1990s and there are many different flavors or distributions otherwise called distros of Linux.

Most distros are free and open source. However, you'll come across a few every now and then that will charge for downloading and using their product. Usually what you're really paying for is security updates and support.

So there are server distributions of Linux like Ubuntu server for example, and there are many different workstation distributions that are designed to have end user productivity software packages installed, usually along with the graphical desktop such as Ubuntu desktop.

Linux is very widespread and so there are many specialized distributions, including those that you would find embedded in firmware chips in many kinds of devices like IoT devices or elevators or security monitoring systems at the commercial or enterprise levels, to name but just a few.

The Linux Operating System consists of a number of components, including the Linux Kernel. Then when you apply updates to a Linux computer, often you are applying updates either to software packages installed on that machine and or you're applying updates to the heart of the Operating System, the Linux Kernel.

When you're reading documentation for Linux, it's always important to determine which version of the Linux Kernel it applies to, especially when it comes to things like how to configure settings or how to troubleshoot problems. The details will vary from one Linux Kernel version to another.

The Linux Operating System also consists of library files, often called Shared Libraries. These are usually binary files, they’re not readable with the text editor that are used by various software packages and Operating System components built into the system.

The Linux OS also consists of many configuration files, not only for the behavior of the Operating System and its components themselves, but also configuration files for additional packages you might choose to install.

Then we have the notion of daemons or background running programs in the Linux OS. For example, if you set up an Apache web server, then you're going to have a related daemon, at least one daemon running in the background.

Managing the Linux OS can be done using any combination of command line tools or shells where you can issue Operating System commands. You can also use the GUI if your distribution of Linux has a GUI component installed and in many cases you can install the GUI X Windows system on an existing Linux host that only has command line support installed currently.

So let's break down each of these Linux OS components in a bit more detail, starting with the Linux Kernel. So what do we know about this? We already know because we've stated that it's the heart of the Linux OS. Now you can view the version of the Linux Kernel.

We discussed why that’s important with the uname -a command; depending on the version of Unix or the version and distribution of Linux you're using, that command syntax may vary slightly and that's always true. All we're doing here is citing a common example.

The Linux Kernel starts up an initial process called init which exists in the sbin directory in the root file system, and this is the first background process that the Kernel will start. The init process always has a process ID, a numeric ID for that running process of 1 because it’s the first process that is launched by the Kernel.

And we mentioned that Linux also has a number of shared library files. Normally, these will be found under /var var stands for variable /lib of course, for library. Here we’ve got a screenshot of the contents of /var/lib on a Ubuntu Linux Server [Video description begins] A screen is displayed with the output of the command ls run at the command prompt. Several output contents are in blue color. [Video description ends] Now with Ubuntu Linux, the color blue as we have listed here in many names, means that it’s a subdirectory as opposed to an actual file. So you'll often have libraries for different software packages or components organized into their own subdirectories.

Another Linux OS component configuration files. Normally you’ll find these in /etc either as an individual configuration file or if a software package has numerous config files, then you might have a sub directory for that product under /etc where you’ll find the config files for that product.

Linux configuration files, nine times out of ten, they are text files and so you can use any text editor that you choose to edit those files. Of course you'll have to have permissions to the file and the file system. So you might use tools like vi or vi or vim or even the nano text editor, which tends to be built in to a lot of modern Linux distributions. These are command line text editing tools.

While it's not always the case, often Linux configuration files will end with .conf It doesn't have to be that way, but that's pretty standard. So we're going to go with that. So when you make a change to a conf file, normally what it means is that you need to restart the related daemon so that it reads that config file and picks up the changes.

Now some daemons will allow you to reload them, which is quicker than restarting the entire daemon, which means reread the configuration from the conf file.

And when we talked about files or separate directories, we already mentioned that installed software packages may have more than one conf file. So that’s configuration files.

In Linux, we also have this notion of daemons. Daemons are background running processes that are not tied to a user terminal. In other words, they're not spawned by the user. They might be while you're testing a configuration, but most of the time a Linux daemon is started automatically by the Operating System, such as a web server or a DHCP service or something along those lines.

So you could say then that a Linux daemon is pretty much the equivalent of a Windows service that runs in the background. And like a Windows service also here in Linux, a daemon will have a script startup file. Depending on what the daemon does, it might need to be assigned a user account, a dummy user account that has permissions to files and the file system that the daemon needs to be able to see. And we know that there are variations on Linux distributions and we already know that the syntax will vary between them.

If I'm using Ubuntu Linux for example, I can control daemons using the service command as an example, I might type in service sshd status to see if the ssh the secure shell daemon is running. ssh of course allows remote command line management of a Linux host. Some distributions will have it turned on automatically, others will not. So if we can check the status of the ssh daemon then we can also use service sshd start to start it If it’s not running or service sshd stop if we want to terminate that daemon, which would only be for the current session. There are other ways to control whether these things start up automatically or not or just controlling it at the command line at this level.

Managing Linux can be done using command line tools. Now in Linux we have a variety of different types of shells. This is specified in a config file for the user account so that when a given user signs in, a specific command line shell environment loads up.

Now common shells would include Bash, that’s the Bourne again shell, the Korn shell, the C shell to list, but just a few. There are many other ones as well. What you'll find is that the command line syntax, the handling of variables and stuff like that will vary from one shell to another.

Of course, we then have a graphical user interface or a GUI environment available for some Linux distributions, whether it's automatically installed or whether you choose to install it manually.

The Linux GUI is based on the X-windows standard. Now the X-windows standard uses a daemon called startx to fire up the GUI environment. You can even enable remote x forwarding, for example, through an SSH connection. It’s possible, for example on a Windows desktop to use SSH to remotely manage a Linux server or desktop. And if that remote Linux server or desktop has a GUI environment with remote x forwarding, you can actually type in commands that would spawn a GUI app on the Linux side and it would actually pop up on the Windows side.

Now there are of course desktop managers and that’s where you get into things like Gnome or gnome G N O M E or the KDE desktop. These sit on top of the X-windows standard and actually give you the GUI representation of your Linux machine.

Here we've got a screenshot of the Linux command line. We’ve got a user by the name of cblackwell signed into a server called ubuntuserver1 where the command ip a has been issued. So IP addressing and of course it returns back network interfaces and IPv4 and IPv6 addresses assigned to those interfaces.

In our next screenshot, we've got an example of a Linux desktop. This is specifically Ubuntu desktop where the LibreOffice writer word processing tool has been launched.

So that gives us a sense then overall of what Linux is about and what its core components are.

3. Video: Linux Distributions (it_oslsys_01_enus_03)

After completing this video, you will be able to recall when to use specific Linux distributions to address specific use cases.
recall when to use specific Linux distributions to address specific use cases
[Video description begins] Topic title: Linux Distributions. Your host for this session is Dan Lachance. [Video description ends] In the Linux world, Linux distributions are really just variants of the Linux Operating System and many of them are based on some core Linux distros such as Debian, Red Hat and SUSE.
Over time, this has evolved to the point where there are many, many specialized Linux distributions for special case use, for industrial usage, for music and video production, for cybersecurity, penetration testing and so on.

If you've got a specific requirement and you want to use the Linux OS, whether it's security monitoring for video surveillance systems or music recording and production in a studio, you will find a specialized Linux distribution specifically for that.

So why are there then so many Linux distributions? Because that's very unlike the Windows family of products.

One reason is because the Linux kernel is free. It’s open source. An entire OS can be built at literally no cost other than the investment in time.

And we know that many new Linux distributions are simply based on existing distributions. One of the things about open source is that yes, the source code is openly available for free to anybody that chooses to download it and you can go ahead and modify it if you're a software developer. But the thing is, you need to upload your modifications for the open source community to then have available for others. But it's a pretty good deal when you think about it.

So some distributions are very similar, but what makes them different, at least on the desktop Linux side of things is the GUI, whether it’s GNOME or KDE or other variations on those that differ slightly and of course the available software packages that get installed or can be installed.

In other words, if you know one Linux distribution well both at the command line and in the GUI, I'm going to say that 98% of that translates to other Linux distributions. They're all very similar.

So what are some examples of common Linux distributions? Well, the first and foremost, one of the first that comes to mind is Debian. Debian is an older Linux operating system and I say it's universal because many distros since have been based on this big ones like Ubuntu, which some people will pronounce u buntu. It doesn’t really matter, but Ubuntu is based on Debian.

So Ubuntu Linux and there’s another Linux distribution Fedora Linux, Arch Linux, SUSE Linux, Peppermint OS, Kali Linux.

And there are so many that aren't even mentioned like CentOS and Red Hat Enterprise Linux. There are literally hundreds of Linux distributions out there.

Pictured on the screen, we’ve got a screenshot of the GUI and the menu has been opened in Kali Linux.

Kali Linux in the past was called the Linux auditor. It’s a collection of cybersecurity penetration testing tools all lumped together and installed and ready to go within one Linux distro that you can even boot from a live CD. Or you could choose to install it.

So here in the menu we've got different categories of tools like for example, item 5 in the menu on the left, Password Attacks, Wireless Attacks, Reverse Engineering, Exploitation Tools and so on. So this is a specialized Linux distribution.

But of course in this particular case where you have a lot of security tools that actually can be used to exploit vulnerabilities, you want to make sure you don't do that in an environment where you do not own the systems. Otherwise you could find yourself in some serious trouble legally.

At any rate, our next screenshot is a Linux distro called 64 Studio. This one is commonly used for creating and editing media, audio and video, and these types of Linux distributions will often have specialized kernel modules for drivers for things like audio recording interfaces and high end video cards.

And there are so many specialized Linux distributions. An example of which would be AsteroidOS. This one is designed for smartwatches. Those fitness watches that healthy people like to wear, where it tracks metrics and gives them summaries on their heart rate and their overall exercise routine. And of course that can be shared up on the internet to put together with other people's information for statistic analysis purposes.

Then for the music lover, for audio files, there are high end or high quality music player Linux distributions. Yes, Linux distributions that have been tweaked and optimized and have specialized kernel modules for the utmost in high fidelity sound. So audio file is one of them.

Then there’s Apertis. Apertis is a vehicle infotainment system type of Linux distribution. Think about modern vehicles with their screen displays where they have environmental controls, GPS and map navigation, media options for songs. Everything's been digitized. You fire up the car and you wait a moment for this to boot up. So it’s a highly specialized and optimized type of Operating System, many times Linux based, that allows this to happen.

Other specialized Linux distributions would include Raspbian. This is for Raspberry Pi devices. Raspberry Pi’s are like small computers that are small circuit boards that can be used for specialized purposes, and they can be customized whether it's for gaming, for robotics, for video surveillance and so on.

Now, if you're not a software developer, you don't have to worry about downloading the source code for a Linux distribution just because it's open source. You can simply download and use open source and free prepackaged Linux distros. And in many cases you can use it in a business environment without paying anything unless you want to pay it for support. Some software packages might require payment, but generally when we say open source, it normally means the components are free.

4. Video: BIOS, UEFI, and the Linux Startup Process (it_oslsys_01_enus_04)

Upon completion of this video, you will be able to determine how Linux interacts with the basic input/output system (BIOS) and Unified Extensible Firmware Interface (UEFI) and use related commands such as mkinitrd, dracut, vmlinuz, and grub bootloader.
determine how Linux interacts with the basic input/output system (BIOS) and Unified Extensible Firmware Interface (UEFI) and use related commands such as mkinitrd, dracut, vmlinuz, and grub bootloader
[Video description begins] Topic title: BIOS, UEFI, and the Linux Startup Process. Your host for this session is Dan Lachance. [Video description ends] One important skill for Linux technicians is to understand the Linux Startup process. Not only will this help you configure Linux accordingly for a specific requirements, but it will also help you troubleshoot any Linux startup problems.
The first thing we have to talk about are things like the BIOS, the Basic input output system. Of course this is firmware or hardware level stuff, not directly a part of the Linux OS. So you could say that BIOS is one or more firmware chips on a circuit board like a motherboard or an add on card, like a SCSI RAID controller card. Either way, the firmware chips interact with the Operating System installed on that device, usually because the OS has a driver that lets it talk to the underlying hardware.

But in the case of BIOS, this kicks in before the Operating System starts. It's what gives the machine the ability to boot up electronically in the first place to get to the point where it loads the OS.

The Unified Extensible Firmware Interface, otherwise called UEFI or UEFI, is a successor to the legacy BIOS. So it still does the same type of thing that the BIOS does - retains the date, time and the configuration of the device like the amount of RAM installed. It checks memory upon boot up, hands off control to the Operating System.

But, the UEFI has some extra features, one of which is Secure Boot, which means that the Operating System only boots from trusted digitally signed Operating System files. It supports Trusted Platform Module or TPM, which is most commonly used for full disk encryption on a machine where the TPM module, which can sometimes be an add on chip onto a motherboard, actually stores decryption keys.

UEFI also allows for configuration through a GUI mouse supported environment. The old BIOS if you've ever pressed the appropriate keystroke on a computer, which varies depending on the vendor of the BIOS. When you're in the BIOS configuring settings like which boot devices you want to support, if you want to support network PXE boot and so on, that's usually done through a text based navigation utility.

Well, the UEFI supports a GUI, plus the UEFI supports larger disks than the old BIOS does.

Before we talk about these specific sequence of events that take place during Linux Startup, let's first talk about Linux Runlevels for a moment. The Linux Runlevel designates what is running on the machine, what is supported or what state the machine is in.

For example, Runlevel 0 means you want to power off the machine. Runlevel 1 is referred to as the rescue or emergency single-user mode for the root user account. So you can boot a machine into Runlevel 1 for that purpose. Or if there’s a problem it might automatically boot into Runlevel 1. Runlevel 3 is multi-user network mode but with no GUI. Whereas, Runlevel 5 is multi-user network mode, which means multiple users can be signed in simultaneously, such as from different stations or different terminal sessions, but it does support a desktop environment.

Runlevel 6 is reboot. Now you can issue the runlevel command in most Linux distributions to view the current runlevel that the machine has been booted into. But you can also control that either if you're logged in as root or if you have sudo privileges. For example, you can reboot the system by issuing the sudo init 6 command, which of course, reboots the machine. Along that same vein of logic, if you were to type in sudo init 0 It’s just another way to shut down the Linux host. Now this is important to understand these Runlevels particularly Runlevels 3 for example. That’s very common for a Linux server because you can configure services, network daemons or even just regular daemons that don't offer a network listening port. You can configure them to be running in a given Runlevel.

Here we’ve got a screenshot of Runlevel 3 symbolic links, otherwise called symlinks. We'll be talking about symbolic links and hard links later. For now, just understand it's generally similar to a Windows shortcut in that it points to a file elsewhere. Here we have a number of files in the /etc/rc3.d directory. The Runlevel 3 directory. [Video description begins] A screenshot of the output of the ls command, run at the command prompt is displayed. There are filenames listed in the output content. [Video description ends]

These all start with the capital letter S, which means it's a start script. You want to start this given daemon when entering Runlevel 3. Scripts that have a capital K at the beginning of their file name are kill scripts to shut down any daemons for that given runlevel.

In this case all we have are start scripts and they’re all S01s and they get run alphabetically the way they appear. So notice here we've got examples to start the cron daemon at Runlevel 3, to start the SSH daemon and others.

Now, if you want to customize the Linux Startup process in any way, you can do this using the dracut utility - d r a c u t.

But let’s go through the standard Linux Startup process. Number 1, depending on the machine, either the BIOS or the UEFI is initialized. That’s at the hardware level which then seeks the Master Boot Record or the MBR and loads it into memory. When you install Linux on a machine, it installs code into the Master Boot Record to initiate the startup of the Linux OS.

So in Step Number 2, the Master Boot Record loads the Grand Unified Boot Loader or GRUB, which has a config file under /boot/grub It's called grub.cfg at least on Ubuntu Linux depending on the version of Linux you’re running, the distro will determine which boot loader is used. The older LILO L I L O boot loader is prevalent on older Linux distributions, but GRUB, specifically GRUB version 2 seems to be pretty much the standard across many distros now. Now the GRUB boot loader can present a menu such as if you've got emergency mode as a separate startup option, assuming that the machine is well enough to get to that point in the first place. Otherwise you could use a startup disk. Or if you've got a multi boot machine, you can select the menu entry for the OS you want to boot into. So assuming we select a Linux installation or maybe there's only one on the machine.

The next part of the Linux Startup process, Step 3, is after the menu entry is selected, the selected compressed Linux kernel, which is called vmlinuz v m l i n u z it runs something called mkinitrd to make the initialization RAM disk in order to mount the root filesystem.

So continuing on with Step 4 in the /sbin directory, which is where a lot of admin utilities reside in the Linux file system, init is then started. This is the init process which always has a process ID of 1. It's one of the first processes launched by the Linux kernel. Now this is used to establish a temporary RAM disk using something called initrd, init RAM disk, until the kernel is fully booted. After that, then the kernel can determine what the startup runlevel should be on this host, you can determine what the default startup runlevel is and then it will launch runlevel-configured programs.

Remember we talked about the start scripts in a runlevel directory? That’s what happens in Step Number 5. Now you also might have other items that inject themselves into the Linux Startup process or prior to that. Such as, the involvement of the Trusted Platform module or TPM. Remember that the TPM provides local hardware cryptographic processing in that host. It’s a specialized firmware chip. You might have to add it to the motherboard. It might be built into the motherboard. Either way, the functionality is exactly the same. So the Linux kernel then will detect that a TPM is present. TPM is often used for OS disk encryption, but it can also be used for data disk encryption. The encryption is tied to the machine that contains the TPM chip because it contains decryption keys.

That means that if anyone were to remove the encrypted storage devices from that Linux host, they would not be able to decrypt those storage devices even if they place it in another machine that has a TPM, because it will be a different TPM and It won’t have the correct encryption key. If you choose to boot the OS, if you choose to encrypt the OS disk file system and you’re using TPM, this means that the OS disk needs to be decrypted before the Linux OS can fully boot up.

Sometimes it might require the entry of a pin, so someone would have to be present at the machine to do that. If it's a virtual machine, then as long as you can get to the console, the hardware level console, you're good. If it's a physical server, again, if you have the infrastructure to allow remote connectivity at the hardware level prior to OS boot, you’re fine.

You might also opt to enable Secure Boot for your Linux host. Now this works in conjunction with UEFI firmware. In other words, if you have an older machine that only supports legacy BIOS, then you cannot enable Secure Boot. What does this mean? You'll recall that Secure Boot means that the machine will boot the Operating System and it will only allow digitally signed OS files to be executed and loaded into memory ultimately. That means then that with Secure Boot at the firmware level, there must be a store somewhere that contains things like trusted certification authorities whose signature is trusted. And that's true. But we'll be covering Secure Boot in more detail later.

Now, if you decide, for example, that you want to install an older Linux distribution, it might not work in conjunction with Secure Boot being enabled in the UEFI. And so you might need to disable Secure Boot for compatibility purposes or in some cases for dual boot configurations on the same machine.

5. Video: Linux Installation Sources (it_oslsys_01_enus_05)

After completing this video, you will be able to list various Linux boot sources such as USB, hard disk drives, ISO, and the preboot execution environment (PXE) commonly used for installation.
list various Linux boot sources such as USB, hard disk drives, ISO, and the preboot execution environment (PXE) commonly used for installation
[Video description begins] Topic title: Linux Installation Sources. Your host for this session is Dan Lachance. [Video description ends] As a Linux technician, you might be responsible for installing Linux based servers or desktops, or you might inherit an environment where they're already installed. Either way, it's important to know how to get Linux installed.
So manual installation sources include things like an ISO DVD image, so you can download this from the appropriate site. You could then use that on bootable media.

You could actually burn a DVD from the ISO image you've downloaded. You might put it on a USB startup drive, you might use the ISO to install a virtual machine.

There are many ways in which you would use that source installation to get Linux up and running. You might also have the extracted installation files available somewhere, whether it's in a local storage location, in a local subdirectory or on a removable USB drive, or maybe stored in a shared folder centrally on a network file server.

You might also use a Preboot execution environment or PXE boot solution whereby essentially what you’re really doing is booting from the network card hardware on the machine.

You're not booting from an OS that's installed anywhere and it pulls down a small OS over the network from a PXE boot server and then that's running in memory on your local machine.

And then you can perform a number of actions like perhaps manually installing Linux, whether from a local source or from a network file server source. Needless to say, a manual Linux installation takes longer than an automated installation.

Now automated installation is a pretty big umbrella. What does that mean?

There are plenty of details, so automated installation of Linux could be done via a pre-installed virtual machine. Otherwise just called a virtual machine appliance. The Linux OS is pre-installed. You just download the virtual machine and load it in your virtual machine environment and away you go. It's already configured and ready to go.

You might also have a scripted installation. Different Linux distributions will have different details on where scripted installation files should reside, what they should be called and the directives within them. But you can go with a scripted type of installation solution and you just spawn the script and the install happens, or you start the installer for the OS and maybe pass it to command line parameter, which references a script. That's another way to do it as well.

PXE Boot shows up here under automated installation as well as manual, and that's because you could have PXE Boot set up so that when the device performs a PXE boot, maybe what you've configured server side is an automated multicast session that will deploy an OS image. Or maybe you have a scripted installer that you launch once PXE Boot has completed.

In larger networks, you might do both PXE Boot and the application of an OS image to the machine that performed the PXE boot. So the OS image was already created from a Linux installation.

If you're in a cloud computing environment, you might also use a cloud template. Microsoft Azure uses what are called ARM templates, A R M whereas Amazon Web Services uses what are called CloudFormation templates.

This is really referred to as infrastructure as code, because you've got all of the directions in these template files which are really, at the end of the day, just text files that are used to deploy cloud based resources in an automated way.

We mentioned Linux scripted installations' automation, and we said it varies from one Linux distro to the other. So if you're using Ubuntu Linux for example, you would create what’s called an autoinstall config file, but that's going to be completely different on another distribution such as Red Hat Enterprise Linux otherwise called RHEL, because Red Hat Enterprise Linux would require what's called a Kickstart automation configuration file.

Either way, a scripted installation would specify all of the Linux installation details you would normally have to specify manually. Doing a manual installation things like the language for the installation and the keyboard layout, the type of installation. Maybe you’re doing a full installation of the Operating System and all software packages available, or maybe just a minimal installation. And again, that will vary depending on the Linux distribution.

When you install Linux manually, you will always have the option to specify any third-party device drivers that might not automatically be detected and loaded by the kernel. Maybe for a disk RAID controller or a specialized audio interface for studio recording of music, you can specify network connectivity settings such as for the network card and whether you want to use DHCP or a manual IPv4 or IPv6 configuration.

Then of course, mass storage configuration and how you want to partition your disks.

You'll have to specify some credentials for your installation, like a username and a password.

And if you're not doing a full installation, you might get an option depending on the Linux distribution installer to add additional software packages to your installation at that time, you can always do that later.

You might also, during the Linux installation, have the option of saying that you want to apply updates immediately. So all of this can be automated in many ways, such as with a scripted answer file, or if you did this installation once and created a golden reference image from it, you then apply to new Linux machines.

So here we've got a screenshot of a manual Ubuntu Linux Server installation from an ISO DVD image. In this particular case, not that it really matters, but this is a VMware virtual machine that I configured to boot from the downloaded ISO DVD image. Notice the GRUB boot loader has started. [Video description begins] A terminal screen titled GNU GRUB version 2.06 is displayed. There are three options to choose from. [Video description ends]

Now we can just use the Try or Install Ubuntu Server for a basic installation, but notice the second GRUB menu option Ubuntu Server with the HWE kernel. The HWE kernel gives a much wider variety of support for different types of hardware devices, so this is especially useful if you've got some kind of specialized hardware like we’ve mentioned, like a RAID controller or a special type of video adapter where you want to be able to use all of its features.

Notice also that from the boot media, we can opt to Test memory if we suspect we have a memory fault of some kind in the physical memory chips on the device, assuming it's a physical server.

So installing Linux can be done with a local installation. That means the installation source is local. So whether we've got scripted files or not really doesn't matter. We might specify additional software packages, additional device drivers. We could have all of these files available locally, meaning not over the network.

So maybe we've got a second hard disk in all of our machines where we've got all of these installer files or USB attached storage that we can just quickly take with us and plug into a machine and do an installation from. And it might also have scripted automation files or a golden reference image that we apply.

Maybe you’ll do a network PXE boot just to get a minimal OS and memory on the machine, and then from there you would read local USB attached storage to apply an image.

There are so many hybrid variations of how this can actually be done. We’ve already mentioned the Preboot execution environment or PXE Boot type of installation. So what this means is that we have to enable this in the BIOS or the UEFI. It’s got to be an available boot option usually after checking to see if we can boot from a local disk inside the machine. This might be a boot of last resort, so to speak.

So PXE Boot works with DHCP, the Dynamic Host Configuration Protocol, so that when you boot up the machine there are no local disks with a bootable OS, then PXE boot would kick in. You're booting off of the firmware from the network card to do a DHCP broadcast to go through the normal DHCP process of acquiring an IP configuration on the machine. That all happens without an operating system installed.

Once that DHCP component has completed, the device can then talk to a PXE installation server, which might also be the DHCP server. It could be a different box. Maybe it’s a different box that hosts a number of images that you want to apply.

Once you've done the PXE boot and you at least have a minimal OS in memory, whether it’s a Windows command line based OS or a Linux Bash shell OS, whatever the case is. Something minimal in memory where you can type in commands and do stuff. So then you would actually perform your Linux installation, whether it's manual or scripted, whatever the case might be.

So it's important to be aware then of the various methods by which we can get Linux installed on a host.

6. Video: Installing a Linux Server (it_oslsys_01_enus_06)

Find out how to install a Linux server OS from an ISO image.
install a Linux server OS from an ISO image
[Video description begins] Topic title: Installing a Linux Server. Your host for this session is Dan Lachance. [Video description ends] In this demonstration, I will be manually installing a Linux Server. Now, whether you’re installing the Linux Server on a physical host or whether it's going to be installed as a virtual machine, once you have the virtual machine hardware determined the amount of virtual CPUs and RAM and virtual disks you’ll need.
After that's been determined, there's not really much of a difference during the installation at all between installing on a physical host and installing it as a virtual machine once you get going with the installation.

But first we need installation media. In this example, I've navigated to Ubuntu.com that's the distribution of Linux I will be using to install a server, but it could be many other distributions, could be SUSE, Linux Enterprise Server or Red Hat Enterprise Server. It really doesn’t matter. At the end of the day, they're all very similar with slight subtle changes [Video description begins] A web browser tab is displayed with the URL https://ubuntu.com/download/server The page header says Get Ubuntu Server and the next line says Option 1: Manual server installation. There is a Download Ubuntu Server button displayed below. [Video description ends] and maybe with different packages installed.

Okay, so I’m going to go ahead and click the Download Ubuntu Server button at the bottom and it's going to be downloading an ISO DVD installer image which I will save into my local downloads folder and ultimately I will be using that to install my VMware Workstation Ubuntu Linux Server.

So I'll just go ahead and save that and wait for the download to complete. The download is approximately 1.8GB or so, so depending on your internet connection will determine how long it takes for that to come down. Okay.

So now that the download of the ISO installer has completed here in VMware Workstation, I’m going to Create a New Virtual Machine. It will be Typical. I’ll click Next. I’ll select the disk image file, the ISO by clicking the Browse button.

So I'm going to specify my server ISO. I’ll click Next and give it a name and I can specify a storage location on my local host to store the virtual machine files.

Next, let's give this an 80 gig hard disk size. Now you have to think about what workload services will be running in this Linux Server to really determine some of the details, such as, how much disk space you'll need and if you want that spread out across multiple virtual disk files or just have a single large disk file, a lot of those questions will be answered when you think about how you will be using the server down the road and you can always change the config at any point anyhow.

I’ll click Next. I’m going to customize the hardware because I want the network interface card, the network adapter to bridge directly to the network and not through NAT, Network Address Translation. Click Close and Finish.

So it's going to power on the virtual machine, which should boot up automatically from that ISO image.

So I want to Try or Install Ubuntu Server. I’ll press Enter on that.

So it's in the midst of detecting the underlying hardware. That's part of what the job of the Linux kernel is. With modern Linux distributions you should not have a problem supporting most hardware. There might be the odd ball situation like if you've got a hardware RAID controller from a nonstandard vendor or an audio interface card, there might be some of those cases where you might have to configure the appropriate support for those devices. But generally speaking, the installation should be quite smooth when it comes to detecting the underlying hardware.

So English is going to be the language. [Video description begins] The screen displays a list of languages to choose from. English is highlighted by default. The instruction line says Use UP, DOWN and ENTER keys to select your language. [Video description ends]

It says that there is an Installer update available. Okay, that’s fine. I'm going to choose the keyboard layout. That's all fine.

We’re going to install Ubuntu Server. Notice you have Ubuntu Server (minimized) but I want the standard set of software packages already installed. Press Enter. Notice that you do have under Additional options, the ability to search for third-party drivers. Again, that should be rare, but if you need to do it, this is where you can do it during the installation.

Down at the bottom I’m going to select Done and press Enter. It’s detected my network Ethernet interface and it wants to use DHCP to assign an IP to it. That’s fine. I’ll press Enter.

I'm not using a proxy server to get on to the internet, so I'm not going to fill anything in on that screen.

I’ll press Enter to accept the default mirror for Ubuntu packages for the installation.

Then it comes to the storage layout. Currently it's set to use the entire disk. In this case /dev/sda which is an 80 gig virtual disk that we set up in VMware.

It's also configured by default to set this disk up as an LVM group. We'll be talking about that, of course, in detail. But for now, let's accept that default.

We really could go all the way down to a Custom storage layout if we wanted to partition or carve out the disk in a certain manner. But I’m okay with this. I’m going to press Enter.

So for my file system summary at the top I have the root mount point which will be close to 40GB. Then I've got my boot mount point which will be about two gig and way down at the bottom I’ve got the partition layout on /dev/sda.

I’m okay with all of these default settings, so I will press Enter.

It says Selecting Continue will begin the installation process and could result in the loss of data on those disks. I know it's an empty virtual disk. So Are you sure you want to continue? I will choose Continue and press Enter.

I'll have to fill out these personalization details like my name, server, name, username and password. I’ll fill that out and then I’ll press Enter.

I don’t want to enable Ubuntu Pro, so I’m going to leave this as it is and skip for now. I’ll press Enter.

I do want to install the OpenSSH Server to allow remote SSH management over an encrypted connection. So I'll press the space bar to put an x in the box for that. And I'm not changing anything else.

So I’m going to go down to Done at the bottom and I’ll press Enter. Then I've got a number of other packages I might choose to install. How convenient; like having Microsoft PowerShell available here in Ubuntu Linux or installing the Docker container engine. I'm not going to change any of these though, so down at the bottom I'll select done.

And at this point it's going through the installation of my server. Okay. Once it's completed down at the very bottom we would go down and select Reboot Now and press Enter. Okay.

Once it reboots, I'm prompted to login, which I will do. And one of the first things I would do here is perhaps run ip a for IP address, take note of the IP and maybe in PuTTY make an SSH connection to the IP of that host. The first time I connect, [Video description begins] The presenter enters the IP address in a pop-up PuTTY Configuration window and clicks the Open button at the bottom right. [Video description ends] of course I have to accept that I trust its signature, so I'll sign in with my user account and I’m now into my Ubuntu Server remotely over SSH.

7. Video: Installing a Linux Desktop (it_oslsys_01_enus_07)

In this video, you will learn how to install a Linux desktop OS from an ISO image.
install a Linux desktop OS from an ISO image
[Video description begins] Topic title: Installing a Linux Desktop. Your host for this session is Dan Lachance. [Video description ends] There are times when you may want to have a Linux installation with a desktop environment with a GUI.
So in this demo I will be manually installing a Linux desktop. There are plenty of Linux distributions that include a Graphical User Interface. In this case I happen to have chosen Ubuntu Linux.

So I’m on the Download Ubuntu Desktop page where what I’ll do is scroll down [Video description begins] A web browser tab is displayed with the URL https://ubuntu.com/download/desktop The page header says Download Ubuntu Desktop [Video description ends] on the page and on the right I've got a download for a specific version, so I'm going to go ahead and click to download it.

So what I'll be downloading here is an ISO DVD image of the installer, so I'm going to go ahead and save that on my local machine because ultimately I could either burn that to a DVD and boot from it and install it on a physical host.

But what I’ll be doing is installing it in a VMware Workstation virtual machine locally. Okay. Going to go ahead and save this. Okay.

So I fired up VMware Workstation 16 Pro. That's what I happen to have on my machine. But you can use pretty much any virtualization software to install an Ubuntu Linux virtual machine from an ISO.

So what I’ll do here is I’ll choose Create a New Virtual Machine. I’ll leave it on Typical. I’ll click Next. [Video description begins] The New Virtual Machine Wizard window is displayed. [Video description ends] I’m going to select Installer disk image file (iso)

All right, so I'll select my downloaded Ubuntu Desktop ISO image. I’ll click Next and I’ll fill in some personalization details. Then I’ll click Next and I’ll give this virtual machine a name. I’ll call it Ubuntu Desktop and I can specify the location where I want that stored. I’ll accept the default location. I'll click Next.

Let’s give this an 80 GB disk size for the virtual disk. I'll go Next. It looks like the Network Adapter here will use Network Address Translation. NAT. I’ve got 4 gigs of RAM, but I want to change the hardware.

I’ll click Customize Hardware because what I want to do is select the Network Adapter to be a bridged connection directly on my real network. Okay, I’ll choose Close and I’ll click Finish.

So I’ve created the shell for the Ubuntu Desktop virtual machine. So it’s going to fire up and boot from the ISO. It’s already happening.

Okay, so the first thing I’m prompted with in the GUI installer is the Keyboard layout I’ll leave it on English (US).

I’ll click Continue and for which apps I would like to install, I’ll do a Normal installation. So as it states that I'll include a web browser, various utilities, office software, games, media players. Let's do all of that and we'll also make sure it downloads the latest updates when it's doing the installation. We know it's always important to apply the latest updates for new features, to fix bugs and to close any security holes.

I’ll click Continue. It’s defaulted to Erase the detected disk and install Ubuntu, which I want to do. I know it's a virtual disk that has nothing on it already, so I’ll just go ahead and click Install Now.

It gives me a summary of the changes it'll make when it writes to disk. So it’s telling me it’s modifying the partition table for my disk, a sda. And that it's going to partition it in the listed manner. For example, partition #3 on sda will be an ext4 type of file system. That’s fine. I’ll accept all the defaults. I’ll click Continue.

It should have detected my time zone, so I’ll click Continue. And even though at the VMware level I filled in some personalization information that doesn't translate into the OS configuration. So I'll fill in some of that stuff here. All right. [Video description begins] A screen titled Who are you? is displayed with input boxes to enter details and other options to select. [Video description ends]

So I've specified my name, my computer's name, a username, and I've specified and confirmed a password for it. I'm not going to set login automatically. I want to require my password to log in. Notice we could also integrate this with Microsoft Active Directory, but in this case I'll just do a local login on this Linux host. So I’ll click Continue. [Video description begins] A Welcome to Ubuntu window is now displayed with the title Install. [Video description ends]

And at this point, it's copying files to the newly created file systems. You can't ask for an easier installation process than that. Very similar to how you might install a modern Windows OS. Okay.

After a few minutes it'll state that the installation is complete and that I need to restart the computer, in this case my virtual machine to use the new installation. How exciting! That’s perfect. Let’s do it. I’m going to click Restart Now.

Now, in some cases you might have some difficulties during the installation, such as the installer detecting mass storage devices if they're perhaps plugged in through USB or even internal disk devices. Now that would be very rare.

You might have to switch hardware settings, perhaps the UEFI to use BIOS legacy mode in some cases for backwards compatibility. But again, honestly, that should be rare.

Let's sign in as Cody Blackwell. So this is local authentication. We're not using a server anywhere to authenticate our account, although notice the first thing it does prompt me with is to connect online accounts to Ubuntu Linux, whether it's Google or Microsoft and whatnot. But I’ll click the Skip button.

It’s prompting me to enable Ubuntu Pro, but I’m going to skip that. I’ll just click Next and for Help improve Ubuntu I’ll choose. No, don't send system info. Next, I'm not going to turn on location services and that's it. We're done.

Here is our beautiful fresh installation of Ubuntu Linux desktop where we have a left hand navigator. We can fire up apps like the Firefox Web Browser.

Let's see if we have internet connectivity. I'll just click skip this step to configure the browser and skip this step. Again, we don't want to bring in any settings, we just want to get up and going.

Now it's prompting me that there is updated software since Ubuntu in this case 22.04 was released. Do you want to install it now? Oh definitely Install Now.

Once the software updater is completed we can choose to Restart Later or Restart Now. I want to restart right away and I’ll sign back in. Now where were we? We wanted to verify that we at least had internet connectivity on our host.

So for example, if I go to YouTube, it looks like it's working. It pulled up the page perfect. And we've got a number of tools in the left hand Navigator because we installed the apps, we can browse the file system, use Thunderbird Mail.

It also includes LibreOffice, which is very similar and even compatible with file formats from Microsoft Office. If I were to click LibreOffice Writer, you might look at it and wonder, isn’t this very similar to Microsoft Word? It is. A lot of people don't realize that these days the desktop graphical versions of Linux rival the Mac OS and Modern Windows versions.

I can also click the show applications button in the bottom left to get a list of all of my applications. I can also search. If I search for the word terminal, I can start a terminal or command prompt here where, for example,

I might type ip a for IP address where I could view my IP address. I could type hostname to view my hostname and it returns what we entered upon the configuration in this case ubuntudesktop1

So that gives us an idea then of how incredibly quick and easy it is to install a desktop version of Linux.

8. Video: Deploying a Cloud-based Linux Server (it_oslsys_01_enus_08)

Discover how to install a Linux cloud-based virtual machine.
install a Linux cloud-based virtual machine
[Video description begins] Topic title: Deploying a Cloud-based Linux Server. Your host for this session is Dan Lachance. [Video description ends] In this demonstration, I will be deploying a cloud-based Linux Server so you can deploy Linux in any cloud environment.
In this case, we'll be using Microsoft Azure. The great thing about it is that we already have OS images on which we can base our cloud-based Linux Server. So it's really just a few clicks to get up and running with Linux in the cloud or just a few commands at the command line if you're opting to do things that way.

To get started here in the Microsoft Azure Portal, [Video description begins] A Microsoft Azure home page is displayed on the screen in a web browser tab. The URL shown is portal.azure.com/#home. The Azure services are all listed on the top. The services starting from the left side are: Create a resource, All resources, Virtual machines etc. The Resources are listed below in the next section. [Video description ends]

I'm going to click Create a resource in the upper left. Now right away I've got Virtual machine available and on the right I've got a number of common virtual machine types, including Ubuntu Server.

However, next to Popular Marketplace products on the right, I'll click the link that says See more in Marketplace and I'll filter the list based on the word linux.

So I've got options here like Kali Linux, which is a Penetration Testing type of Linux distribution containing many security related tools. We’ve got Oracle Linux, Red Hat Enterprise Linux, Amazon even has their own distribution of Linux, Arch Linux, the list goes on and on and on.

If I were to search for a specific Linux distribution, let's say Ubuntu, then we have those specific types of variants available. Notice that we've got some variants that also include the GUI, the Graphical User Interface.

I'm going to choose one of the newer variants Ubuntu Linux 23.04 so I can read the details about it.

I can take a look at what the pricing is on an hourly basis [Video description begins] The page for Ubuntu 23.04 is displayed. The Plan name is displayed in a dropdown followed by a Create button to its right. Below this, the details are displayed under Overview, Plans + Pricing, Usage Information + Support, and Ratings + Reviews [Video description ends] and if I’m happy with it I can go ahead and click Create.

I'm going to have to specify some details here in Microsoft Azure, including things like the Resource group into which I want to deploy this virtual machine.

The Resource group, like its name implies, is just a way to group related cloud resources together, maybe by department or by app or by project.

In this case, I've got a Resource group called East so I'm just going to deploy this in that Resource group. I’m just going to call this Ubuntu1.

It’ll be deployed in the East US region and down below for Image. Ubuntu 23.04 is selected.

I can determine the virtual machine size, which means the amount of horsepower So the number of virtual CPUs and the amount of RAM. Maybe I’ll choose four virtual CPUs 16 gigs of RAM.

You can also determine if you want to authenticate to this host using SSH public key authentication. The public key would be stored here in the Azure cloud with the VM, but the related private key you would download and you would need to authenticate. Or you can go with just basic username and password authentication. For this example, that's what I'm going to do. So I'll fill in a username and I'll specify and confirm a password.

It wants to allow inbound ports for SSH port 22 for remote management. I'll leave it that way. You could also use a jump box or a jump server, which is the public connection point over the internet. And from it you can launch to internal virtual machines to manage them, if they only have private IPs.

In Azure, that type of solution is called Azure Bastion. But in this case, I'll just leave the Server publicly visible over the internet on Port 22. When I click Next Disks, I can determine how many disks I want to use for this virtual machine.

I’m not going to change that. I’ll click Next for Networking. It wants to create a new virtual network. I’ll let it create a VNet and a subnet with default IP addressing. Of course I could change those things, but I'm going to accept them as they are and there's nothing else I'll do.

So I’ll click Review and create in the bottom left.

And to deploy the virtual machine, I will click Create. So that will create the virtual machine in Azure and a couple of other resources like the public IP address and any disks, those are separate resources and it will also start virtual machine automatically for me. Okay.

Before too long the deployment is complete. If I click the Home link in the upper left and let’s say then I go to All resources, I filter the list for Ubuntu.

I’ve got my Ubuntu1 virtual machine that is its own type of cloud object or resource, but I've also got the public IP address for it. A network security group which in the Azure cloud allows me to control network traffic to and from virtual machines and subnets. I've got the virtual network that was created. You need a network if you're going to deploy a virtual machine.

I've got a network interface for that virtual network and I've got a disk.

The subnet is contained within the properties of the virtual network.

If I click on Subnets, there’s a default subnet that was created that uses the 10.0.0.0/24 range.

I go to the Home view again and we can even just filter down to Virtual machines, if I click on my Ubuntu1 virtual machine, on the Overview page on the right, notice it’s got a Public IP address. We can also view this by clicking Networking under Settings, in the left hand navigator. Here we have the Public IP, but also the Private IP address, for that virtual machine.

I need the public IP if I’m going to connect to it remotely to manage it and I'm going to connect to it remotely and manage it using the Free PuTTY Tool p u t t y.

So here in PuTTY, I’ve specified the public IP address of the Ubuntu1 Azure based virtual machine port 22 for SSH.

And I've saved this as a setting here called Azure-Ubuntu. [Video description begins] The PuTTY Configuration screen is displayed. He enters the Host Name and Port number. He selects SSH for Connection Type. The Saved Sessions list box is displayed with Azure-Ubuntu selected from the list. The Open and Cancel buttons are at the bottom right. [Video description ends]

Now I can't connect to the private IP address unless I were to go through a jump server or I were to first connect to the VNet where that virtual machine is running perhaps through a VPN.

All right, let’s click Open. Now because it’s the first time I've connected of course over SSH. It asks if I trust the unique fingerprint of the server, I will accept it and it wants me to log in.

Well, this is where I would specify the credentials that I set up when I deployed the virtual machine.

So I'll enter the username and the password and we're in. Probably type ifconfig to display network information. It says this isn't included with this distribution of Linux, but you could run sudo apt install net-tools. I could do that. Or I could run ip a to show the IP address information.

I’ve got my local loopback of course, lo, in IPv4 the local loopback is always 127.0.0.1 In IPv6 the equivalent is ::1

But I’ve also got ethernet 0 interface eth0, where I've got an IPv6 link local address that was assigned. It always has an fe80 prefix, but I've also got the private IP address which was given from the subnet.

Notice the public IP does not show up here within the Linux OS as that's an Azure resource associated with the VM, but it doesn’t show up within the VM Operating System itself.

And there you have it, just like that. We’ve got an Ubuntu Server virtual machine running in a cloud environment.

9. Video: Managing Linux Hardware (it_oslsys_01_enus_09)

In this video, find out how to manage hardware using Linux commands such as lspci, lsusb, and dmidecode.
manage hardware using Linux commands such as lspci, lsusb, and dmidecode
[Video description begins] Topic title: Managing Linux Hardware. Your host for this session is Dan Lachance. [Video description ends] In this demo, we’re going to take a few minutes to talk about commands related to Linux hardware management.
So let’s start here in Linux by doing an ls of the /dev directory that’s part of the Linux Filesystem hierarchy standard. So that means that you will find a /dev directory on every Linux distribution. dev stands for device and there are many types of devices here, such as, our terminal screen devices, but also references to hardware devices like CD ROM, CPU related information, mass storage devices like sda and then it’s partitions sda1, 2 and 3.

Each of the partitions are actually showing up as a device in /dev. Remember that Linux interacts with hardware through device files.

So of course we can do an ls a /dev/sd? where the question mark is a wild card for a single character. And it shows us our mass storage devices on this machine.

So it means our machine recognizes sda, sdb, sdc and sdd.

Now, if you need to install a specialized driver in this example, if I need to install an Nvidia video adapter drivers here in Ubuntu Linux, I can go ahead and install the appropriate driver packages so sudo apt install. And in this case I'll reference a couple of Nvidia driver files that I might want to install and I could press enter and it then prompts me if I want to continue with it. Now I don't have that hardware so I will not continue with the installation, but it's important to understand that this is a way that we can install the drivers using the command line method. I'll press n for no, I don't want to install that.

Of course, you can also specify third party drivers or any type of hardware upon installing the OS normally, depends on the version of Linux and the distribution, but generally you’ll have that option upon install too.

Let’s do an ls of /proc proc is for processes, so this is a dynamic subdirectory whose contents will change.

Notice, for example, all of the subdirectories here that have numeric values. These are process IDs or pids assigned by the Linux kernel to running processes.

Now remember, we can also view running processes by typing ps or you want to see them all, aux so they’re not tied to a particular Linux terminal login session.

However, let’s go back and let’s cat /proc/cpuinfo In here we have information about our CPU hardware, okay, so the model name is an AMD type of CPU. The megahertz speed rating is about 3293 It’s got a 512 KB cache. Okay. So we can get some details about that type of stuff. If I clear the screen, I can also ls the proc directory on the root, maybe go and look at bus and the pci directory.

So here we've got a couple of subdirectories and a devices file.

So why don’t we actually cat /proc/bus/pci/devices to see what the kernel, the Linux kernel thinks is connected via the PCI bus.

Usually there's some kind of a sound device, maybe an Ethernet adapter. There might even be disk drives that are connected. So we're determining this by just looking at the names that are referenced here in our devices file.

But really, if you want to look at PCI devices, you should be using the lspci command list pci. If I do that with the -v for verbose and then pipe it to more so it stops after the first screenful, immediately, we know that this is a VMware virtual machine.

It's using the VMware virtual machine chipset. We’ve got some details about the PCI bridge and the ISA bridge. PCI and the older ISA are standards for connecting adapter cards on a machine for extended functionality, sound cards, network cards and so on.

I've got some IDE disk interface information, then I’ve got some SCSI storage controller information and then USB controller information and so on.

So the lspci command will show us what is recognized by the system and sometimes we can use that to help troubleshoot why, for instance, a piece of hardware is not working correctly within Linux. and also use the list USB, lsusb command -v,

This will give me some details about what's connected to the USB bus in my machine as well.

If I clear the screen you can also run sudo dmidecode. DMI stands for Desktop Management Interface. The purpose of this command is to show us some BIOS or UEFI Information. So let’s pipe that to more stops after the first screenful

Immediately, I have some BIOS information. It’s a Phoenix Technologies Limited, BIOS Version 6. There’s the release date. That's always important because we need to be able to determine the version of the BIOS firmware that we are running and the revisions. The BIOS revision is also shown down here.

So with these types of commands, we can begin to get a sense of what kind of hardware resides in the machine, which can be important. For example, if we need to update the BIOS or check to see if we need to update the BIOS on a given Linux host.

10. Video: Using Linux File System Navigation Commands (it_oslsys_01_enus_10)

After completing this video, you will be able to recognize when to use Linux file system commands such as ls, cd, cp, mv, mkdir, rmdir, and touch.
recognize when to use Linux file system commands such as ls, cd, cp, mv, mkdir, rmdir, and touch
[Video description begins] Topic title: Using Linux File System Navigation Commands. Your host for this session is Dan Lachance. [Video description ends] The purpose of this demo is to familiarize ourselves with Linux file system navigation commands. How do we move about and what are some common commands that might be issued to learn about the file system and work with files and directories.
So let's go ahead and get started here. I’ve SSH’d using the free PuTTY tool into my Ubuntu Server.

The first thing we need to be able to do in Linux is determine what our current position in the file system hierarchy is. For example, I can issue the pwd command that’s not password. That means print working directory. Notice it shows that we are in /home/cblackwell

So if I were to type in change directory cd / which means go back to the root of the file system and then etc let’s say etc shows up in my command prompt. And if I were to type pwd of course it reflects we are in /etc

Now when it comes to user home directories at the command prompt, we can quickly return to the user home directory simply by typing cd enter You don't have to tell it anything else. So I can verify this of course with pwd and indeed it shows I'm in my user home directory so I'll type in clear to clear the screen.

Probably one of the most frequently issued Linux commands would be ls for list. That's kind of like typing dir on a Windows machine to get a directory listing of files. Now in this case, because we didn't pass it any parameters, it shows the current directory's file listing. Now the blue highlighted words.

Now the words in blue are subdirectories in this particular distribution of Linux Ubuntu where the bright green names are those that have the execute permission bit set and just the regular listed files are just regular files that are not directories and do not have the execute permission set.

We can also type ls -l for a long listing or you could type for short ll Same thing, long listing. But the key here is it’s showing, yes, the entries in the file system.

So our blue subdirectories, our green files, which are presumably scripts or binaries of some kind because the execute permission is set. And notice that for the directories. If we take a look at the permission set, the first character is a d which means it’s a subdirectory.

If we go to a file that we know is not a sub directory, notice that the first position here is just a - so it’s not a directory.

But when you look at a long listing, it’s also important to understand the permissions, we’ll focus on permissions a bit later, but for now, it’s important to know you’ve got three sets of standard permissions for any given file system object.

You’ve got a set of permissions for the owning user, which is shown in the third column from the left here. when we type in ll long listing.

Then you’ve got a set of permissions for the owning group, which here is shown as being the same. When you make a user account, in most Linux distributions, a group is also created with the same name. So in this case, I’ve got a user called cblackwell and I also have a group called cblackwell. So we’ve got two sets of permissions for that.

The third set would be for everybody else. So read, write, execute. rwx in this case, for the file that we are focusing on, it’s called hello.sh

And our example, cblackwell, that user gets read, write and execute permissions. The second set of permissions are for the group, which is also set to rwx So whoever’s a member of the cblackwell group would get rwx to this file, and then we’ve got just r and x read and execute for anybody that is not user cblackwell or not a member of the cblackwell group.

We’ve also got a reference in the next column to the right of the number of hard links, but we'll talk about hard links later. We've already talked about the owning user and the owning group.

We've also got the size of the file in bytes and we've got a date timestamp and of course the name of the file system entry.

We can also issue the ls -a command, -a means all, even hidden files and directories. A hidden file or directory in Linux is simply one where the first character is a . whether it’s a subdirectory or a file. It means it’s simply hidden from the regular ls display.

Now, of course, another important part of working in the file system is creating directories. We can do that with the make dir mkdir command. So if I want to make a directory here called projects, I could go ahead and do that. [Video description begins] The host types in a command mkdir projects at the command prompt in the home directory. [Video description ends] Now, if I do an ls, we’ve got a projects folder shown in the output and of course we can change directory into projects.

If we wanted to copy some content, maybe I'll make another directory first within projects called scripts,

I could even put in a hierarchy of subdirectories I want to create all at once. So scripts, which is going to be in the current location projects/east let’s say.

But if I just press enter it says I can’t create east because scripts doesn't exist yet. [Video description begins] He types in the command mkdir scripts/east at the command prompt from the projects subdirectory. An error text is displayed by the system mkdir: cannot create directory 'scripts/east': No such file or directory [Video description ends] But if I use the up arrow key and bring that up and add a -p in other words, to build the entire path, no problem.

If I do an ls here in projects, there’s scripts. If I go into scripts and do an ls here, we’ve got east, so I'll just change directory to east.

So what I could do, for example, is copy using the cp command .. means go back one level that will put us in scripts because we’re currently in east /.. again, we’ll put us in projects /.. again would put us in our home directory where I can specify /*.sh

I know I've got a number of files up here. We see it in the output of ls that end with .sh and they’re in the home directory. sh is normally used to notate that that file is a shell script. It's not required, but it's commonly done.

So I can say I want to copy all those shell scripts from that location into the current directory, which I can simply reference with the . and I can press enter.

If I type ls there are the shell scripts that have been copied into our new east subdirectory.

I can also create new files in here. For example, using the touch command, I could say touch backupscript1.sh enter If I clear the screen and do an ls what we’ve got, actually, let’s do an ll what we’ve got is a new file called backupscript1.sh it’s a zero byte file. That's all the touch command does.

From here, if you wanted to edit that, you could use the vi command. Or maybe you want to use the nano command and specify that file name and work with the contents of the file. I'll get out of nano by pressing ctrl x. I don't want to do that right now.

You can also move files we copied with cp, but you can also move. So let’s clear the screen and do an ls of ~ What’s ~? ~ means home directory. Remember how we did cd and we pressed enter and it was a shortcut to get into the user home directory for the current signed in user? You can also reference that with the ~ symbol. It also means home directory.

So let’s say I want to bring over this test.txt file from its current location and I want to move it, not copy it, into the east folder.

So I can type mv for move. We know that we have to go a couple levels back in the file system to get to test.txt and we also know we can specify the current directory with just a dot. So in this case I'm moving it. [Video description begins] He types in the command mv ../../../test.txt . at the command prompt from the east subdirectory. [Video description ends] So if I use the up arrow key here, this is handy to go through my command line history. Go back to ls ~ Notice that the test.txt file is no longer there. If I type ls here in east, it now shows up here because we have moved it.

The last thing we should know about is removing directories. For example, if I do a cd .. to go back one level that puts me in scripts. I want to remove the east folder or directory. So rmdir remove directory east, but it says, well that's great, but I can't do it. It's not empty.

What I could do is just use the rm the remove command. That's a command that will allow me to delete files or in this example, a directory. If I were to say rm east, it says, well, it’s a directory, but if I use the up arrow key and add -r to the end, then I’m being prompted. Do you want to remove that? Specifically notice what it’s telling me. [Video description begins] He types in a command rm east -r at the command prompt in the scripts subdirectory. The system displays a question rm: remove write-protected regular file 'east/test.txt'? followed by an input waiting prompt. [Video description ends] It’s telling me, would you like to remove that file in there? test.txt I’ll type in the letter y for yes and enter. I do an ls now in scripts. Notice that the east folder is now gone.

If I type man rm to open up the help page, the manual page for the remove command, [Video description begins] The screen displays the help page for rm command. It has three visible sections - Name, Synopsis and Description. [Video description ends] and if I type a / in the bottom left, it shows a / This allows me to search for something specifically in here, like -f enter -f as shown in the man page here, allows me to force the removal of items without being prompted for everything like we just were. And that was only one file. You can imagine if there were hundreds of files in the east directory.

So that gives us a sense then of some basic file system navigation commands that can be very handy when you're managing Linux systems.

11. Video: Navigating the Linux File System (it_oslsys_01_enus_11)

Learn how to navigate Linux file system using common Linux OS commands.
navigate Linux file system using common Linux OS commands
[Video description begins] Topic title: Navigating the Linux File System. Your host for this session is Dan Lachance. [Video description ends] All right, in this demo, we’re going to focus on navigating the Linux file system. We’ve begun to look at this already, but we’re going to take it a few steps further by looking at some more command line parameters, for instance, for the ls command.
We’ll take a look at how to use the fdisk command, the mount command, the df or disk free command, du or disk usage command.

So let’s go ahead and let’s get started. The first thing I’ll do here is pwd We know that that means print working directory. It'll show where we are. We also know that we could type in cd for change directory and just press enter to go into the user home directory.

Now we also know that we can do ls -l to get a listing, a long listing of each entry in the current location because we didn't specify a path. And that will also show us things like subdirectories shown here in Ubuntu Linux's blue and of course we have a d in the first placeholder which indicates that it is a directory.

If we just do an ls of the budgets subdirectory, we've got a couple of files in there. This is where things get interesting. Let’s say we just did ls of things that start with the letter b, so ls b*

Notice what it does, it shows the contents in this case of the budgets folder. For instance, one of the returned files is download.

That’s the name of the file that doesn’t start with b, so why is it showing up? Because it’s in a subdirectory that starts with the letter b, How do we change that behavior? That's probably not what I intended to do.

What we can do is the following. We can do an ls -d to not go into subdirectories. Then in this case, b* enter. This time it shows us only the entry for items that start with b in the current file system location in the hierarchy. So it shows us only budgets.

You can extend that perhaps by doing ls -l for a long listing if you wanted to do that. So you could add -ld you can put the parameters together like that. Enter. Now we have the budgets folder listing. It didn't show us what's in it and we have all of the details, the permission sets, the number of hard links, owning, user owning group and so on.

And we know that Linux is case sensitive, so how can we work with that in the file system using ls, for example, let's make another directory in the current location. We already have budgets.

Let's create one here called Budgets. [Video description begins] The host types a command mkdir Budgets at the command prompt. [Video description ends] Notice it had no problem with that. So if I were to use the up arrow key to do ls -ld b* it still only shows budgets and if I change that to a capital B, it shows only Budgets. [Video description begins] He runs a command ls -ld B* at the command prompt. [Video description ends]

What if I want all entries that match either lower or uppercase budgets? But I want to do that with the single command. Well, with ls we can do this. What we would do is enclose the variants, the variables within square brackets. So B, followed by a b, close the square bracket, and then after that our standard wild card * character.

If we press enter notice now it's returning both of them, [Video description begins] He runs a command ls -ld [Bb]* at the command prompt. [Video description ends] so that could be handy. I'm going to clear the screen.

I’m just going to go ahead and run the lsblk list block devices --scsi [Video description begins] He runs a command lsblk --scsi at the command prompt. [Video description ends]

One of the items I notice here is item sda, so if I want to, I can run fdisk against /dev/sda and I can also use -l for list. Now I get a permission denied because this requires elevated permissions. Therefore I need to prefix that command with sudo, that, or sign in as root. [Video description begins] He runs a command sudo fdisk /dev/sda -l at the command prompt. [Video description ends]

When I do that, it gives me the breakdown for sda, which is an 80 GB drive. So it’s got partitions 1, 2 and 3 of the size shown here respectively. 1 MB, 2 gig and 78 gig.

If I were to bring up that previous command but remove the -l it takes me into an interactive fdisk where I can actually repartition the disk and make changes. However, I don't want to do that, so I’ll type q for quit to go back to the command line. I’ll clear the screen.

We can also type mount to get a list of mount points. Mount points means that we've got file systems, whether they're local or remote, over the network that are made available in a local sub directory.

The same way that Windows would use a local drive letter to point to a file system, whether it's mapped to a local file system or it's a network drive mapping to something on a server somewhere else over the network.

For example, if I were to type mount and pipe that to the grep line filtering command and look for the word boot, I can see that in /boot, which is a directory, a mount point directory. When I go into the /boot directory, I’m actually viewing what’s on /dev/sda2 partition 2 on device sda.

We’ll be working more with these commands in more detail in other demonstrations.

Another handy command is df or disk free. It'll show me my mounted file systems. It’ll show me the used space and available space and the % in use. You can also see the mount point shown in the last or rightmost column.

If I run df -h that’s a lowercase h. That’s for human readable. So instead of displaying, for example, the used and available and number of one kilobyte blocks, instead it's just shown in megabytes, for example. So the size, the used and the available, that's usually much more readable than trying to figure it out in one k blocks. It just makes it easier to look at it. I'm going to clear the screen.

Another interesting command that we can run is du for disk usage. And just like with the df command disk free, we can also pass it a -h to make it human readable. Reading units that are in blocks. We can see the units here in kilobytes or K or megabytes M.

What this is doing is showing me the space utilization on my machine in the current working directory. So I’ve got 12 K in the hidden .ssh directory, 2.1 MB in budgets. Notice it’s all with a ./ . means current directory. We know of course that we can run pwd to see what that is. If I were to go to the root of the file system, let’s say change directory to root sudo. du disk usage -h.

Notice it’s going through, recursively going through, the entire file system or the root file system, which contains everything else on this machine and breaking down the space utilization.

But what about if I want to view the disk usage and sort it by the size? I can run du -s to summarize the output, h for human readable. I’m going to put it in a * for everything, all files. I'm going to pipe this using the vertical bar symbol. That's a pipe. So take the result of the command on the left, feed it into the command on the right, which is going to be the sort command line utility where I want to sort make it -h and r,

I want to make sure I sort it by the largest numbers. So reverse sort. Enter. [Video description begins] He types a command du -sh * | sort -hr at the command prompt. [Video description ends] And if we take a look here at the output. Notice that it's pretty easy to identify what is using the most space on the machine as we go down through the listing in reverse sort order.

12. Video: Searching the Linux File System (it_oslsys_01_enus_12)

During this video, discover how to search Linux file systems using the find and locate commands.
search Linux file systems using the find and locate commands
[Video description begins] Topic title: Searching the Linux File System. Your host for this session is Dan Lachance. [Video description ends] In this demo, we're going to focus on how to search the Linux file system. Over time, you can end up with thousands or even millions of files. We're talking data files here.
So that means that we need an easy way to locate files in a hurry. And we can do that in a variety of ways.

We can use the find command in Linux or we can use the locate command.

Let’s start by working with find. So of course, there's always a manual page for these things. If I type man find, it'll show me the help page or the manual page for the find command with a description of how it works and of course the command line options, whether it’s a - and an uppercase letter or a lowercase letter. However, I’ll just press q to get out of there.

Now, if I type ls actually, if I type pwd first for print working directory, I'm in my user home directory. I’m signed in as user cblackwell as evidenced by the output of the id command. So if I type ls, I've got a bunch of sample files here, but I also have two subdirectories. One is called budgets with a lowercase b, the second is called Budgets with an uppercase B, that’s interesting.

So if I were to type sudo find let’s say we start from the root of the file system / -name I’m looking for file names ” I’m going to start with, in square brackets, capital B lowercase b close square bracket. In other words, match any one of those, not both. Then the rest of the word budget* something after the word budget as well, if it exists and I’ll close my double quotations. If I do that, it returns back everything that would be related to [Video description begins] The host types the following command at the command prompt sudo find / -name "[Bb]udget*" [Video description ends] the word budget. Okay, so there's some entries here for text files and a subdirectory and then some library modules in Linux that have the word budget in their file name. Let's take that a step further.

I'm going to use the up arrow key to bring up that previous command. But I want to add to it because you're not limited to just searching by name.

You can search on any attribute of a file or a directory entry in the file system. Basically any of the metadata, such as the owning user. If I type -user to add to that existing command, lbrenner this is a user account on this Linux host that I know has been given ownership of at least one file, when I press enter, how do we get a much smaller output?

Apparently in the budgets folder with the lowercase B, there are two budget files that are showing up.

Well, that makes sense for the name matching part of the find command, but apparently they are owned by user lbrenner. Let’s take a look. If I change directory into the budgets folder and do a long listing. [Video description begins] He runs the command cd budgets at the command prompt. He then runs the ll command at the command prompt. [Video description ends] Indeed, if we look at the budget1.txt and the Budget2.txt file. lbrenner is listed as the owning user. So in other words, the command succeeded. It showed us exactly what we asked it to show us.

Now on a larger Linux host if you're doing this, if you're doing a find, depending on what you're searching for, it might take a while to go through the entire file system. What you can do is you can send a command output, as we know, using the output redirection symbol. The > sign to a file. For example, lbrenner_owner_results.txt. And in case we get any errors in the output, I can also suppress that with 2> that means redirect errors, either to a file or to /dev/null just to discard them.

And I can tell this to run in the background by adding a space and an & at the end. Why would I do this? If this is a long running command, it means it immediately sends it into the background and so I don't have to wait for it to finish. I get my command prompt immediately and I can continue doing something else. [Video description begins] He types in the command sudo find / -name "[Bb]udget*" -user lbrenner > lbrenner_owner_results.txt 2>/dev/null & [Video description ends]

So it returns here that it's been assigned a job ID and a background running process. Of course, we know that that's going to run very quickly. And if I cat the lbrenner_owner_results file, it returns back the contents of that. Now, of course, the job is done here. That's what this message here is telling us. So that’s an important aspect to think about when you’re working with find.

Now, there are other examples of find I’d like to do here. Let’s say I want to do sudo find from the root -type d I want to look for directories, not files, directories. Naturally, if you put -type f, you’re looking for file entries, -name let’s say apache2. Okay. So what this is doing then is searching from the root of the file system and seeking any subdirectory with the name apache2.

Notice we’ve got in a couple of places like /etc for configuration, /var/lib for binaries related to the apache2 web server, /var/log for logging and so on. As if that weren’t useful enough already, we can also search based on permissions.

If I were to do an sudo find of / so from the root -type files f -perm as in permissions. Let’s say I look for 0740 [Video description begins] He types in the command sudo find / -type f -perm 0740 [Video description ends]

We haven’t talked about the special bits, so we’re not going to get into the first 0 yet. But, but 740 are the permissions for the owning user that’s the 7, the owning group is the 4 and everyone else is 0 7 means read, write, execute because read has a value of 4, write has a value of 2, execute has a value of 1 and 4 + 2 + 1 = 7 means the owner has read, write, execute.

The 4 would mean that the owning group to a given file entry, has only read permissions and the 0 means everyone else would have nothing. Maybe that’s what I want to look for, if I press enter.

First of all, I get a couple of references under /proc. Now /proc is a dynamic process subdirectory, so I've got no such file or directory listed there, but I do have one valid entry shown. And remember, what you can do is when you're running a command, any errors that you want to suppress. If you don't care about the output, just use 2> and redirect it to somewhere like a file, if you want to store the output of errors in a file or in this case, just discard them to /dev/null

So what this is telling me is that in my current user home directory in the budgets folder, the budget1.txt file has the permission set of 740. Let's see if that's true. If I do an ll long listing of budget1.txt read write execute, that’s the 7. read, that’s the 4. And the absence of anything else for everyone else is 0. That is correct. [Video description begins] He types in the command ll budget1.txt In the output, the first column contains the following text -rwxr----- [Video description ends]

The next thing we're going to do is take a look at a different search type of command called locate. However, on some Linux distributions, you might have to install it sudo apt install let’s see plocate is what it’s called. It looks like we’ve already got plocate installed and it is the newest version. Otherwise we would have to proceed with installing it so that the locate command is available.

So when I type locate, I know it’s working because it says no pattern to search for. Now the way that this works is if I do an ls of /var/lib/plocate here we’ve got a plocate.db file.

The locate command uses a database which contains an indexed listing of file entries in the file system. And when you use a locate command, you’re actually searching that database file. The find command actually just searches the file system, which is slower than searching through an indexed database. However, the locate database needs to be up to date with the newest changes in the file system. So you have to consider that.

Now I can run sudo updatedb to update that database. However, there is a scheduled cron job that automatically occurs daily to do that. That’s not enough, just make sure you run updatedb before you run the locate command to make sure you’re searching through the most recent file system changes.

So what I could do, for example, is say locate mysql what entries do we have in the file system for mysql? It's very fast and here it's showing us all the items that match our search criteria. You can do that for, let’s say, apache2 where it’s everything related to apache2.

Of course, we can also use it to search for data files, maybe ignoring case. So -i to ignore case. Let’s say I want to look for budget* So it’s showing me in my current location that I’ve got a file that matches my criteria. The file is called budget1.txt.

The interesting thing too is you can also add other parameters, like -c what this will do is count the occurrences of the results found by the locate command, in this case, 1 [Video description begins] He runs the command locate -c budget* at the command prompt. The output displayed is 1 [Video description ends]

13. Video: Filtering Data with Linux Commands (it_oslsys_01_enus_13)

In this video, you will learn how to search for and filter data using commands such as grep, sed, and awk.
search for and filter data using commands such as grep, sed, and awk
[Video description begins] Topic title: Filtering Data with Linux Commands. Your host for this session is Dan Lachance. [Video description ends] In this demonstration, we’re going to be working with pattern matching to try to find things that might be otherwise more difficult to find or to manipulate within text files.
Specifically, we'll be looking at three commands, so we'll just be scratching the surface by looking at the grep command. We’ll look at sed s e d and awk a w k.

So the focus here is searching for and filtering out data, that type of thing. The first thing we should do is take a look at what we've got for a couple of sample files that we will be referring to.

I’m going to cat a file I have here in my home directory called cities.txt Within it, I’ve got two column headings. One is City Code and I’ve got a bunch of city codes under that and the next is City Name. And of course I have a bunch of city names there.

I have another file here too if I cat customers.txt it’s just a sample file. It’s got a City column header with a couple of cities listed under it and it’s got a Customer column with Last name, First name for a few sample customers. Okay, well, let’s get to work then.

We're going to start with the grep line filtering tool. If man grep comes back under the description and it says that it search for patterns in each file. And of course, as we go through the help or the man page, we've got all the command line parameters that we might want to use to change the behavior of the grep command. Okay, let's do an example.

We’ll do a basic one. I’m going to run cat cities.txt which we know returns the contents of that file in its entirety. But what I can do if I bring that command back up is I can pipe it with my vertical bar symbol that pipes results of the command on the left to whatever's on the right. And what I can do here is pipe that to grep. And I can say I want to do a case insensitive. So ignore case -i for the word london in lowercase letters [Video description begins] The host types in the command cat cities.txt | grep -i london [Video description ends] and notice it found London with the city code of A09 with an uppercase L. If I didn’t have -i to ignore case, we would get no results. So that can always be very important when you're using the grep line filter command.

However, another way to use grep is not just to pipe commands to it, but it as the leftmost command. The main command. I can just type grep, let’s say -i ignore case london and I can use the input redirection symbol which is a less than sign and tell it bring in the contents of something called cities.txt our little text file. That too will also work and yield the result that we had previously. [Video description begins] He types in the command grep -i london < cities.txt [Video description ends]

So there are a few ways to do the same thing and that’s important to understand if you’re looking at help files or if you’re on the internet searching through forums on how to accomplish something at the command line, or if you're looking at shell scripts, whatever the case is, there's more than one way to do things. We could also do the following.

We could run grep -i let’s stick with the same example london then I could just put in an * what does that mean? it means all of the files in the current directory. So notice it found a couple of occurrences of the word london in different files, one in cities.txt and two occurrences in customers.txt. Of course, notice that what a grep is doing is returning the entire line within that file.

Now there's more you can do with grep, but the purpose here is to get a general familiarity with searching and filtering, in this case the file system.

Let’s move on and take a look at the s e d command sed, if I man sed, then it talks about it being a stream editor to do basic text transformations, maybe to delete text that you're searching for within a file or maybe to substitute or replace it.

There are so many things you can do with this. And again, we have all the command line parameters available here, so I’ll press q to get out of here. And let’s just do a few basic examples.

So I’m going to run sed, s e d and in single quotes I’m going to put in s/London/Liverpool/ and then single quote and then customers.txt. What does this mean?

What are we trying to do here? Well, what we’re trying to do here with sed is we’re trying to substitute. That's where the lowercase s in the expression comes from. We want to substitute London when we find occurrences of it in the customers.txt file and we want to replace it with or substitute it with Liverpool.

Now that's only going to be in the command line output. We aren't writing the change to the file. Let's see how that works. Enter. Okay, so I've got two occurrences of Liverpool now shown in this output. One for Cody Blackwell, the second for Maxwell Bishop. If we just cat that source file customers.txt notice that London is still in that customers.txt file. So all we’ve done is manipulated the output on the screen. Now of course you can capture that to a file.

If I use the up arrow key to go back to our sed command, maybe what we’ll do is use an output redirection symbol the greater than sign let’s call this new_customers.txt enter so we get no output on the screen, of course. But if I cat the new_customers.txt file. We've now got Liverpool that has replaced the value of London under the city column for those two customers.

Now there's so much more that you can do with that, but let's move on and take a look at our final tool here for filtering data. And that’s going to be awk. a w k. Let’s type man awk Let’s look at the man page for awk. So it talks in the description about how it's based on the awk programming language. It gets very powerful.

You can do some very complex things with the awk command. We're only going to scratch the surface and do some very basic things for filtering. But again, down under options, we've got a lot of command line parameters that can be specified to control the behavior of the awk command. However, I’ll type q let’s clear the screen and let’s do a few examples. awk a w k and then space and within single quote I'm going to start with an open curly bracket and I'm going to put in the word print meaning I want to print back or display something on the screen. $2, $3

So columns 2 and columns 3 close the curly brace, close the single quote. But we need a source for that. Where’s the data come from that we want to print? It's going to be coming from, let’s say customers.txt notice what it’s done it’s returned columns 2 [Video description begins] He types in the command awk '{print $2, $3}' customers.txt [Video description ends] and 3, which would include the last name and then the first name.

Now we can also and sometimes this will be handy when you have large output display line numbers next to each entry. So I’m going to run awk space single quote within an opening curly brace. I’ll then type print NR my line numbering , $0 Close my curly brace, close my single quote and again customers.txt Now the $0 simply means we don’t return column 1, 2 or 3. We want everything. So it returned everything along with line number shown in the leftmost column. Let’s say we were to cat /etc/passwd p a s s w d that's the user account file on this local Linux host. And of course notice the delimiter between each chunk of information is a full colon. All right. So let's work with this a little bit.

What I’m going to do is run awk space -F: meaning my field delimiter is a colon. Then single quote, open curly brace print. Let’s say the first column $1 close curly brace single quote Then I want to run this against /etc/passwd. Notice all it's doing is returning what's in column one. We told it that the delimiter in this particular case was a colon, [Video description begins] The output displays a list of words, one word in each line, such as: list, irc, gnats, nobody, and so on. [Video description ends] so it's very easy for it to determine what information we want to pull out of that entry. So that will give you a general idea of some filtering commands and some of the basic things that you can do with them. But of course they can get much, much more complex if needed.

14. Video: Course Summary (it_oslsys_01_enus_14)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary. Your host for this session is Dan Lachance. [Video description ends] So in this course, we've examined how to select and install the appropriate Linux distribution.
We also saw how to navigate and search Linux file systems. We did this by exploring various Linux distributions and their use.

We discussed the BIOS, the UEFI and the Linux startup process and boot sources. We then manually installed a Linux server and a desktop and we deployed a Linux cloud based virtual machine.

Next, we discussed Linux hardware management and file system navigation commands.

We then navigated and searched the Linux file system and used regular expressions with file systems.

In our next course, we'll move on to explore how to manage local and remote Linux file systems, including network storage.

© 2024 Skillsoft Ireland Limited - All rights reserved.