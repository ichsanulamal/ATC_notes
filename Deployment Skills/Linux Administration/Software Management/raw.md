CompTIA Linux+: Software Management
Linux software management involves configuring software package repositories and keeping them updated. Sometimes, this also requires compiling software from source code to run on a Linux host. In this course, examine how Linux software management components work together, such as repositories and packages. Next, discover how to manage software packages using the yum, pacman, and apt command line tools. Finally, learn how to build software packages from source code using Linux commands such as configure, make, and make install. This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_07_enus_01)

    2. Video: Linux Software Management (it_oslsys_07_enus_02)

    3. Video: Configuring the Linux Kernel (it_oslsys_07_enus_03)

    4. Video: Managing Linux Repositories and Updates with yum (it_oslsys_07_enus_04)

    5. Video: Using pacman to Manage Linux Repositories and Updates (it_oslsys_07_enus_05)

    6. Video: Utilizing apt to Manage Linux Repositories and Updates (it_oslsys_07_enus_06)

    7. Video: Building Linux Software from Source (it_oslsys_07_enus_07)

    8. Video: Course Summary (it_oslsys_07_enus_08)

1. Video: Course Overview (it_oslsys_07_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance. [Video description ends]
Hi, I’m Dan Lachance. Linux software management means configuring software package repositories and keeping them updated, as well as sometimes compiling software from source code to run on a Linux host.

In this course, I'll start by discussing how Linux software management components such as repositories and packages work together. I’ll then manage software packages using the yum, pacman, and apt command line tools.

Lastly, I will build software packages from source code using Linux commands such as configure, make, and make install. This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: Linux Software Management (it_oslsys_07_enus_02)

After completing this video, you will be able to recognize how to work with repositories, package signatures, package management with yum, pacman, apt, and compiling from source code.
recognize how to work with repositories, package signatures, package management with yum, pacman, apt, and compiling from source code
[Video description begins] Topic title: Linux Software Management. Your host for this session is Dan Lachance. [Video description ends]
Managing software, installation and software sources in Linux is a critical skill for a Linux technician. We're going to focus here on Linux software management. The first thing we're going to be getting into is a quick discussion on package repositories. A package repository is a centralized collection of software that can be installed on a Linux host. These package repositories might be hosted within the enterprise on repository servers, or you might pull them from public repositories over the internet.

Most modern Linux distributions are automatically configured to pull from public repositories when you choose to install the software. We can also build software from a source. This means that we’ve actually got the source code, perhaps it’s written in C, and then we can actually use a compiler as long as we have all the dependencies that are called upon for that and actually compile the source code to binaries and thus have software built from source.

In this day and age of cybersecurity attacks, one must also be careful to think about the software sources. Where are you getting the software from, and do you trust it? It might be necessary in alignment with organizational security policies to only use trusted package repositories where software is digitally signed, and also only using trusted source code from reputable software vendors or internal software developers.

So we know then when it comes to package repositories, these can be public available on the Internet. And we said that most Linux distros install with automatic references to public repositories. You can also have private repositories on internal servers. You can configure Linux hosts with any number of repositories. And also any mixture of both public and private repositories so that when you go to install software when you go to upgrade packages already installed on a Linux host, you can have it configured to look at both public and private software repositories.

So when you choose to install software packages on Linux, such as when you use command line tools or if you're using GUI tools, those packages are pulled from public or private repositories down to the Linux host, and then you can choose to install them. Depending on which tool you're using, will determine how automated that is.

It's important then naturally, to make sure that your list of package repository worries, whether they be public or private, is kept up to date. And that means making sure that the index of available software packages from those software repositories is known to your Linux host.

So which command line tools might we use then to manage Linux software packages? One would be the apt command apt. You'll find this on Debian based Linux distributions such as Ubuntu, where you could run things like apt update to update your list of repositories and the index of software available on them.

apt install to install software, apt upgrade, of course to upgrade already installed software packages on the host, and apt remove, which of course, lets you remove an installed software package, apt list, if you would like to see the software packages installed. This is just a basic subset of what you can do with the apt command.

But on other Linux distributions such as Red Hat Linux, Fedora Linux, which uses RPMs, Red Hat Package Manager, or RPM packaged files, you can use the yum command line tool where you could run yum install to install software, yum remove to remove software, yum update for making sure it’s up-to-date, yum list or yum info for package on specific installed RPMs.

For Arch Linux, you might use the pacman utility, where you can pass it various command line parameters to control its behavior. The -S parameter means you want to install a package, whereas -Ss means you want to query for a package name, -Qs means you want to query for a package name, but one that's already installed on the local Linux host and of course -R, which means you want to remove a package that's installed. So the general concept is the same, but the specific details will vary depending on the type of Linux distribution that you’re managing.

Here we’ve got a screenshot on an Ubuntu Linux host, and Ubuntu, of course is Debian based, where we are using the sudo apt update command. What this is doing is updating our package repository listings. It then even tells me at the bottom, how many packages, in this case 62 that could actually be upgraded if we wanted to. It also tells me I can run ‘apt list --upgradable’ to see which packages would be updated.

In our next screenshot, we are using the apt command line set to install something, so we're running sudo apt install and the name of the package is docker.io, and down below, it's reading the package lists building the dependency tree to see what other packages might need to be installed for Docker application containerization to work correctly.

And then, down at the very bottom, it asks Do you want to continue? [Y/n] You can type in a Y or an n. It also tells you that, in this particular example, it would take 287 MB of additional disk space for this software to be installed.

Now that’s using package management tools, we can also as we know, compile software from source code. In some cases, that's the only way to install certain software packages they might otherwise not be available within any repositories in any other form. So what would you do? You would download the file(s) you might use, for example, the wget command to do that in Linux.

If the file you’ve downloaded is compressed, for example, as a tar.gz file, you might decompress it with the tar command, perhaps using the - zxvf parameters, z meaning it’s compressed, x meaning extract, v meaning verbose and f meaning file, where you would then point to the path and file name.

You would then change the directory to the extraction directory that was created because it will contain a file called configure. You would then run ./ because you’re in the current directory and run configure, which would create what’s called a makefile. The next thing you would do is run the make command. The result of this is that it would compile the Linux binary installer files.

You have installed the software, but you’ve at least got binary installation files. In step 6, you would then run make install which would actually install the software. So this gives us a sense then on a Linux host of how we might manage packages and repositories and also how to compile software from source code.

3. Video: Configuring the Linux Kernel (it_oslsys_07_enus_03)

During this video, discover how to configure Linux kernel options.
configure Linux kernel options
[Video description begins] Topic title: Configuring the Linux Kernel. Your host for this session is Dan Lachance. [Video description ends]
The Linux kernel is the heart and soul of the Linux operating system. It manages resource access, it deals with kernel modules, which includes hardware drivers, and essentially it makes Linux work. So there are a few things that we should know then about managing the Linux kernel. It’s not something that we would do very often, but when you're troubleshooting or if you need to manually update the Linux kernel, then this is important to know. [Video description begins] The Ubuntu Linux terminal screen displays. [Video description ends]

So the first thing we’ll go over then is the uname command. If I issue the uname command here, I’ll put sudo uname -mrs, this returns Linux kernel information. So in this case, the Linux kernel is version 5.15.0-76-generic, and of course, the platform here is 64-bit. Knowing the specific version of the Linux kernel can be very important for compatibility, especially with specialized equipment or certain types of software.

For example, in a medical environment, in order to interact properly with certain types of medical diagnostic equipment, you might have to have a minimum version of a Linux kernel. And so it's important to know how to check it, of course. Now it's important also to be aware that we can run sudo apt update to update our package repository listing, in this case, here in Ubuntu Linux. So Debian based Linux distros will use apt for package management. Why is this important? It's important because you can also run sudo apt install and specify a specific kernel package that you want to install.

So you can manually choose to install the Linux kernel, it’s always recommended to take a backup and to ensure you know what you're doing when you do this. Because if you incorrectly apply a Linux kernel, it's possible you could prevent the system from booting up properly. Now, another way to check details about the Linux kernel is to run sudo and cat against /proc/, and the file is called version_signature.

Here again, we get a return listing of the Linux kernel, this one says Ubuntu 5.15.0-76.83. So this is giving us further detail about the Linux kernel version information. You could even have multiple Linux installations on one machine, such as in different disk partitions, and upon boot up, you could select the appropriate menu entry to start different installations of Linux. You might even have the same version of Linux like Ubuntu Linux, but different versions of the kernel, maybe for testing purposes, you would select from your grub boot menu.

So if I were to run sudo cat /boot/grub/grub.cfg. Let’s pipe that to more, as we get further down to the various menu entries in the grub config file, notice we’ve got references to specific menu entry items that can be selected. And as we keep looking at them, they'll be references to the Linux kernel version that will be started when that menu entry is selected. Okay, so that’s important to know.

You can also show any kernel modules or plug-ins that are loaded by typing lsmod, list module. Here we have a list of all of the kernel modules that are loaded. Now I can also pipe that, let's say, to grep and look for something specific. [Video description begins] The presenter types a line of code and run's it. Code reads: lsmod | grep raid10 [Video description ends] For example, notice that we’ve got a raid10 kernel module loaded.

Now when you're troubleshooting, you might use some of these commands like lsmod or modprobe. So sudo modprobe -r to remove a loaded kernel module. Let’s say we want to remove the raid10 module, so raid10, Enter. Now if I use my up arrow key to go back to the lsmod command where we grabbed it for raid10, notice it’s no longer loaded in memory. So basically what we’ve done is removed that plug-in from being active right now while the kernel is loaded and Linux is running.

Now we can also run commands like sudo modinfo raid10 to get some details about that specific kernel module. If I just scroll back up a bit, then we'll get some details like the actual file name and the location of that kernel module. We'll get a description and any dependencies that might be related to it. Of course, if I want to actually load a kernel module if I'm troubleshooting or testing a configuration, I can do that with the modprobe command, but this time I simply won’t use -r.

So let’s say I want to load the raid10 kernel module again. [Video description begins] He clears the previous screen and then types a line of code. Code reads: sudo modprobe raid10 [Video description ends] We’ll just go back to our lsmod command, and now it’s up and running once again as part of the kernel.

Now in some cases, when you want to install or update, especially to custom kernel versions and you want to be careful with that as it might not be recommended for stability purposes. But often, what you’ll be doing is adding an additional repository and then installing it from that newly added repository. But we’ll take a look at how to manage repositories and work with that using apt in another demo.

4. Video: Managing Linux Repositories and Updates with yum (it_oslsys_07_enus_04)

In this video, find out how to search for, install, update, and remove packages using yum.
search for, install, update, and remove packages using yum
[Video description begins] Topic title: Managing Linux Repositories and Updates with yum. Your host for this session is Dan Lachance. [Video description ends]
In this demo, we're going to take a look at how to manage Linux repositories and updates using yum. Yum Is a command line tool, it’s a utility that’s designed to work with RPM, or Red Hat Package Manager packages so that you can work with installing and updating software on a host. Now, in our example, we're going to be using a Red Hat Enterprise Linux host because it uses yum natively.

The first thing we’ll type in is yum -help. So from here, I get command line parameters that can be used with the yum command line utility to manage packages and to manage repositories. For instance, if I were to type, let’s say, sudo yum repolist, I get a list of repositories. Notice that they are designed in this case for this distribution of Linux as Red Hat Enterprise Linux version 7.

But I have a list of repositories, this means these are the places that will be checked out on the internet when I choose to install software packages, or if I want to upgrade anything that I already have installed locally from new updates available out in these repositories. If I were to do an ls here in Red Hat Enterprise Linux of /etc/yum.repos.d, that’s a default subdirectory.

Notice we’ve got a number of files that are here. For example, one is called redhat.repo. So if I cat that file, cat /etc/yum.repos.d/redhat.repo, I get a message here stating this is an auto-generated file that is managed by the Red Hat Subscription Manager (rhsm). So some Linux distributions will have their own specialized way of managing some of these packages and repositories.

Another important aspect here of working with yam is checking to see what’s installed, so if I were to run sudo yum list installed, there's a space between each of those words. Let's say I pipe that to the more command. Here I have a list of all of the specific packages that are installed on this host, and what’s important besides the name of it, of course, is the version string that goes along with that shown in the second column from the left.

Now what I could do is run that same command but pipe it to the grep line filtering utility and let’s say we’re checking to see which Python packages are installed. So I'll specify python as my criteria. So here we have a listing then of the installed packages that yum was able to identify are installed on this host related to Python. It's always important to make sure that your repository listing and the indexes of available software packages are kept up-to-date.

You can do that here with sudo yum check-update, and if you wanted to apply updates for things that are already installed, you could run sudo yum update, I’ll press Enter. So I'm being told that the Total download size if I choose to update the install packages is 339 M. Is this ok? I’ll type in the letter y for yes, and I’ll press Enter. And after a few moments, it says Complete!.

So we've updated the packages installed on this machine from the repositories. But what about if we want to install something new? Let's say we were to run sudo yum search docker, want to install the docker service so that I can run containerized applications. So here I have all kinds of options shown here, including things like the Docker Client, Docker Tooling toolkits, and various other utilities related to Docker.

If I were just to type sudo yum info docker, just on the Docker package itself, then I get the details related to it. So the Name, the architecture, the Version, which is always of paramount importance, and the Release string, the Size, which is important as a consideration as it will use or consume disk space on this Linux host.

And if I decide I want to install it, I can go ahead and do that with sudo yum let’s say -y because it’s going to prompt me, are you sure you want to install this? And I just want to force yes into the command install docker, Enter. Okay, so it’s in the midst of installing the Docker service on this host, and before long, it says it's Complete!.

So if I were to run sudo service docker status to see if the daemon is running or not, it says inactive (dead). So we can go ahead and just use the up arrow key and change status to start, to start the service, and then we check the status now it’s showing as being active and running. So the Docker daemon is up and running, which means it’s active, on this host, also if I were to type in docker for the docker CLI, the command line interface, it gives me the next level commands in terms of help, which is telling me of course that Docker is installed on this host but we already know that.

If we wanted to update just the Docker package, we could run sudo yum update and we can name the package by name, in this case, docker, but then it returns here that there are no packages marked for update, as there are no updates because we've just installed it. Of course, it's also important to know how to remove stuff here. If I run sudo yum -y since it’s going to ask me yes or no, remove docker, Enter.

It shows that it has completed the removal of the Docker service. So if I were to run sudo yum list docker, notice it shows what’s available in terms of packages to be installed, so it's no longer installed here. Now if you're working with Red Hat Linux systems, it’s also important to know, of course, that you can just also use the rpm, the Red Hat Package Manager command line tool such as rpm - i for installing packages, rpm -e, that’s a lowercase e for erasing packages.

And of course, there are many other command line parameters available for rpm. You can get a listing of those with descriptions by viewing the man page for rpm, man rpm.

5. Video: Using pacman to Manage Linux Repositories and Updates (it_oslsys_07_enus_05)

Upon completion of this video, you will be able to use pacman to locate, install, update, and remove packages.
use pacman to locate, install, update, and remove packages
[Video description begins] Using pacman to Manage Linux Repositories and Updates. Your host for this session is Dan Lachance. [Video description ends]
Let's take a few minutes to talk about repositories and software package installation using the pacman utility. That’s pacman, kind of like the video game, except here we're talking about it in the context of being a command line utility that we can use to manage repositories and software on some Linux distributions such as Arch Linux.

So I’ve got an Arch Linux host ready here. Let’s begin here by running sudo cat of /etc/pacman.com, so the configuration file for the pacman package manager. Notice one of the things it’s doing within this file is it’s including /etc/pacman.d/mirrorlist. Okay, so we need to take a look at that, let’s run sudo cat /etc/pacman.d/mirrorlist. This is what we’re looking for, this gives us the specific repositories, the URLs of some of which begin with https, others are http, others are rsync repositories.

But these are the standard Arch Linux repositories that will get checked when we choose to install software packages on this Arch Linux host or if we choose to update them. Now of course, you can also add custom repositories to this list if you so choose. As an example, here in my web browser, I’ve navigated to wiki.archlinux.org, and I’ve searched for Unofficial user repositories.

And this gives me a list of them, of course, you want to be very careful with this, especially from a security standpoint you want to install software from something that might not have been properly vetted and deemed as being trustworthy. But nonetheless, here we have a lot of references to some URLs for different package repositories, which means you would get access to different software packages that you otherwise might not have access to.

Let me aware that you might have a Keyring file here. In other words, you might have to download a public key for some repositories that use digital signatures so that your machine trusts the digital signatures from that provider. And that is true not only in Arch Linux but using a variety of different repositories, even let’s say if you’re using yum with Red Hat Enterprise Linux.

Some of the repositories might use digitally signed software packages you might need the related public key installed on your machine so that your machine trusts those packages, otherwise, they may not be allowed to be installed. Okay, so back here in Arch Linux, let’s run sudo pacman -Syu. What this is going to do is check to see what needs to be updated in terms of packages installed on this host.

So it’s determined that there are many packages installed for example, we have a number of references here to different Python utilities with the version strings, and down below, it gives me the Total Download Size, which here is about 550 MiB. Then the Total Installed Size, once we extract and install those updates, and then the Net Upgrade Size. So it asks proceed with the installation, I’ll type in Y, and I’ll press Enter.

Now for some software packages already installed, we might be prompted whether or not we want to trust the PGP signatures by importing a PGP key. If we've got errors, we might be prompted to delete corrupt versions of keys that could prevent certain packages from being validated, and as a result, installed or updated.

Some other important things here, of course, would include installing packages using pacman, sudo pacman -Ss. What I’m doing here is I am searching, I’m querying is Docker available to be installed because I’ve specified the docker software. So here I get a list of all kinds of different software packages related to the word Docker. So yes, there’s plenty here that can potentially be installed. Is it already installed? Well, we can do that with sudo pacman -Q for query s, and then I’ll tell them I’m looking for Docker.

Now we get no returned output, so of course, that’s telling us that there are no Docker components installed. The Docker package is not installed on this machine. Let’s go ahead and install it sudo pacman -S, and then the name of the package, in this case docker. I’m given the Total Download Size as opposed to the Total Installed Size, and I'm asked if I'd like to proceed with the installation. I’ll type in capital Y for yes and press Enter. It's downloading and installing Docker.

Once that’s been completed, we’ll be given back our command prompt, here it looks like it’s created some system user accounts, and we are ready to go. [Video description begins] The presenter types clear in the terminal, and the terminal gets cleared. [Video description ends] So here in Arch Linux, I could then issue the command sudo systemctl status docker, is docker up and running or not? Well, it knows about the Docker application container engine, but it's currently inactive.

So I could use the up arrow key and go back to that previous command and change the word status to start. And if we use our up arrow key again and go back and check the status of Docker. Notice of course, now it’s active and running. So we know that it’s there also at the command line, if I simply type in docker, the next level command set is shown as help, which tells me that the Docker CLI has been successfully installed.

And lastly, if I decide I want to remove a package that I've installed from a repository, I can run sudo pacman -R for remove s docker. It asks would you like to remove these packages? It gives me the Total Removed Size, I’ll type in a capital Y for yes and press Enter, and then the software is now removed from this host.

6. Video: Utilizing apt to Manage Linux Repositories and Updates (it_oslsys_07_enus_06)

During this video, you will learn how to utilize apt to find, install, update, and remove packages.
utilize apt to find, install, update, and remove packages
[Video description begins] Topic title: Utilizing apt to Manage Linux Repositories and Updates. Your host for this session is Dan Lachance. [Video description ends]
In this video, I'll be working with Linux repositories and software packages and updates using apt. apt is a command line tool that’s built into most Debian based Linux distributions. We're going to be using Ubuntu Linux here, which is Debian based, and so therefore apt is available automatically as a package management tool.

So apt uses repositories, and of course, just like other tools like pacman and yum, those software management tools also refer to repositories, centralized collections of software packages to get software to install on Linux hosts or to update as changes are made in the repositories. And repositories can either be a server available over a network like over http, or it could be a local subdirectory where you’ve got installation files available.

So to examine repositories a little bit here on my Ubuntu Linux machine, I’m going to run sudo cat /etc/apt/sources.list. And here I’ve got a number of different sources here for Debian based packages. Now of course, if you wanted to, you could add other repositories to this list so they too would be used when you query for software packages and then install them, update them, that type of thing. If I run sudo apt update, those are all separate words.

Then what it's doing is checking all of my configured sources in the sources.list file my repositories to make sure that they are available and up-to-date and that I have an index of the software packages available from each of them, which is also up-to-date.

Notice it automatically tells me down at the bottom here that we've got 61 packages that can be upgraded. Notice that the command we used up above was update, not upgrade. So if I were to run sudo apt upgrade, this will upgrade all of the installed software packages on this host to their newer versions. And normally, before you perform an apt upgrade, you should perform an apt update to make sure your package repository indexes are up-to-date.

So it asks if I want to continue because it's going to download a certain amount of files and it's going to use a specified amount of additional disk space. I’m going to type in Y for yes, let’s do it. Let’s get things up to date here. Okay, before too long, it’s been completed, the updates have been applied, and as we're required, some services have been automatically restarted. I’ll clear the screen.

We can also run the sudo apt list command to get a list of installed packages on this host. We also get the version string along with it, which is always important. I can also run sudo apt install. In this case, let’s say I want to install docker.io, I know that’s the name of the package, it asks do you want to continue? I’ll type in the letter y for yes and Enter.

When you're managing software packages in Linux and also working with repositories from which that software is pulled, it's important to understand how to install and also remove software components. So if I were to run sudo apt list pipe that to grep and look for docker.io, docker.io is now shown here. [Video description begins] The presenter clears the screen and then type the code. Code reads: sudo apt list | grep docker.io [Video description ends]

If I were to type in the docker command, it knows what it is. So the CLI is installed, if I were to run sudo service docker status, the daemon has automatically been launched, so it's now shown as being active and running, so we can now run our containerized applications. Of course, if we want to remove that software we can also run sudo apt remove in this case, docker.io.

As you might expect, it tells me how much disk space will be freed up if I were to proceed with the removal. So I'll type in the letter y to do just that. Now I can use the command line to add additional software package repositories. For example, sudo add-apt-repository, and that would have to know what the string was for that, so it’s going to be a Debian package archive with a 64-bit amd architecture. I’ve got the URL, and down at the bottom, it asks me to press ENTER to continue or Ctrl-c to cancel.

Okay, so it tells me that it’s adding some of these entries here to the sources.list file. But notice it says it couldn’t verify certain number of signatures because the public key is not available. Okay, well, when you’re working with software package repositories and signed software, the signature is done or created with the private key you need the related public key on your Linux host to be able to trust those items.

And note here in my web browser, there are many different instruction sets on how to import public keys depending on what software you might be interested in from a particular repository. So here, I’m going to use the sudo apt-key command to add a key. [Video description begins] He types the command in the Ubuntu Linux terminal screen. [Video description ends] And what I've done here is I've installed the public key for MongoDB, that database package.

So if I were to use my up arrow key to go back to the command where we were running add-apt-repository, if I press ENTER to continue with that, it will have been added. So now you have the ability to pull down software from a different location.

7. Video: Building Linux Software from Source (it_oslsys_07_enus_07)

Discover how to compile and install Linux software from source using ./configure, make, and make install.
compile and install Linux software from source using ./configure, make, and make install
[Video description begins] Topic title: Building Linux Software from Source. Your host for this session is Dan Lachance. [Video description ends]
A well-rounded Linux technician should have the ability to build Linux software from source. What this means is that we've got the source code created by the developer, but it's not yet been compiled. So as Linux technicians, we can take it upon ourselves to download that source code, install the appropriate dependencies and perhaps even install a compiler for the appropriate language, compile the installation files, and then actually install them.

In some cases, with some software, that is what you will need to do. Ideally, you’ll simply be able to use a package manager tool like apt or yum, or pacman to install software packages, but unfortunately, it's not always quite that simple. [Video description begins] The Ubuntu Linux terminal screen displays. [Video description ends] So the first thing I'll do here on my server is I will make a directory in my current home directory called downloads. [Video description begins] The presenter types a code of line. Code reads: mkdir downloads [Video description ends]

I'll change the directory into the downloads directory, and then I'm going to download some source code. [Video description begins] He changes the directory by typing a line of code and then clears it. The code in first line reads: cd downloads/ [Video description ends] In this case, I’m going to download the source code for git. Git is often used by software developers for software version control when programming, although it's not limited to only that use.

So I'm going to use the built-in curl command to download the source file, which means I need to know the URL. So curl --output, I’ll give it the file name, which is going to be, in this case, git.tar.gz, so it’s a compressed archive. Then I’ll give it the URL, which in this case starts with https://, and I’ll point all the way down to the actual file itself.

So the file is now downloading into the current directory. [Video description begins] He types the code ls and then presses Enter. [Video description ends] So there’s the git.tar.gz file. So naturally, now I’m going to run tar -zxf, the z means it’s compressed, x is extract, and the file is the file name which will specify here. What it will have done is created a git subdirectory.

If I change the directory into that new subdirectory and do an ls, there's all kinds of programming files here. We’ve got some .c files, for example. Let’s just cut the lockfile.c file for fun. So cat lockfile.c. This looks like C programming language code, and indeed it is. This is the actual code that's used for that particular functionality.

So there's a lot of them in here. What I want to do is check for a configure file, and there is a configure file here. [Video description begins] He types the code ls config* and presses Enter to check the configure file. [Video description ends] If I do a long listing for configure notice, it’s got read, write, execute for the owner, of course, I am listed as the owner as I downloaded it and extracted it here in my home directory.

The purpose of the configure script here, in this case, is to check to make sure that we have the appropriate compiler. So we're going to need a C compiler in this case to compile that to binaries and that any dependent software that is referenced is also available. So if that all checks out, then the configure script will generate a make file.

So here's what we're going to do, we're not going to change anything, we’re just going to run ./configure. Now, in some cases, you might have to install some other dependencies first. So notice it's telling us that there's no acceptable C compiler found within our $PATH variable, so I’m going to run sudo apt install gcc. This is a standard C compiler, it asks do you want to continue? I’ll type in y for yes. It’s pretty hard to compile source code if you don’t have a compiler installed.

Okay, let’s run ./configure again. This time things look quite different because we have a C compiler installed. Then I’ll run the sudo make command. So what this is doing is actually generating the binary installation files. Now, if you get any errors when you run ./configure or make, be sure to check the installation instructions.

So for example, here we've got the installation instructions for installing the required packages. [Video description begins] The browser with the website: phoenixnap.com/kb/build-linux-kernel displays. [Video description ends] 

It's quite crucial that these packages are installed in order for building from source to be successful, and you can't predict exactly what will be required unless you go through all of the programming code. [Video description begins] He points toward the installation packages on the website. [Video description ends] It’s much easier to refer to the appropriate documentation to install the packages that are needed.

So once that's completed, and we've run make install, if we were to run git --version, it reports back the version of git that is installed. [Video description begins] The Ubuntu Linux terminal screen displays, and the presenter types the code. Code reads: git --version [Video description ends] So in times when you need to build software from source code, you can do it using this method.

8. Video: Course Summary (it_oslsys_07_enus_08)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary. Your host for this session is Dan Lachance. [Video description ends]
So in this course, we’ve examined how to manage software repositories, packages and how to build software packages from source code. We did this by exploring Linux software management and managing the Linux kernel. We managed Linux repositories and dealt with updates using command line tools including yum, pacman, and apt depending on the Linux distribution you’re using.

And we finally built Linux software from source code. In our next course, we'll move on to manage Linux configuration files, shells, environment variables, and we'll also see how we can manage Linux through Ansible and Puppet.

© 2023 Skillsoft Ireland Limited - All rights reserved.