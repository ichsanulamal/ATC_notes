CompTIA Linux+: Shells, Variables, & Configuration Files
The Linux OS and installed packages normally use text configuration files that control their behavior, and various Linux shells can be used to interact with the OS where some commands and environment variables can behave differently. The centralized configuration management of Linux hosts can be controlled using solutions like Ansible and Puppet. In this course, explore how Linux configuration files work and how to use commands to work with configuration files. Next, learn how to use various shells to interact with the Linux OS. Finally, discover how to work with Linux environment variables and manage configurations through Ansible. This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_08_enus_01)

    2. Video: Linux Configuration Files (it_oslsys_08_enus_02)

    3. Video: Managing Linux Configuration Files (it_oslsys_08_enus_03)

    4. Video: Linux Shells (it_oslsys_08_enus_04)

    5. Video: Managing Linux Shells (it_oslsys_08_enus_05)

    6. Video: Manipulating Linux Environment Variables (it_oslsys_08_enus_06)

    7. Video: Using Ansible to Manage Linux Configurations (it_oslsys_08_enus_07)

    8. Video: Course Summary (it_oslsys_08_enus_08)

    Course File-based Resources

1. Video: Course Overview (it_oslsys_08_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance. [Video description ends]
Hi, I'm Dan Lachance. The Linux OS and installed packages normally use text configuration files that control their behavior. Technicians can use various Linux shells to interact with the OS, where some commands and environment variables can behave a little bit differently.

The centralized configuration management of Linux hosts can be controlled using solutions such as Ansible and Puppet. In this course, I'll start by discussing how Linux configuration files work, including their standard file system locations, followed by using commands such as grep, head, tail, cat, vi, and nano to work with configuration files. Next, I will discuss and use various shells to interact with the Linux OS. Lastly, I will work with Linux environment variables and configuration management through Ansible. This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: Linux Configuration Files (it_oslsys_08_enus_02)

Upon completion of this video, you will be able to identify common Linux locations for configuration files and their management using grep, cat, head, tail, vi, nano.
identify common Linux locations for configuration files and their management using grep, cat, head, tail, vi, nano
[Video description begins] Topic title: Linux Configuration Files. Your host for this session is Dan Lachance. [Video description ends]
Many Linux services and software packages are configured through specific configuration files for that software. On a Linux host, normally these are text files that have a .conf file extension. Now that may vary, but that is the standard. So, the idea is that we can find most configuration files for installed Linux software on the host in or perhaps in the subdirectory under /etc/. Some installed software packages will create a subdirectory under etc because they consist of numerous configuration files. Pictured on the screen, we are taking a peek in the screenshot at the etc directory located off of the root of the file system. Notice we've got some configuration files such as adduser.conf, but notice there are other config files here that do not end with the .conf file extension.

Also, notice that we've got a number of subdirectories here under /etc. Here in Ubuntu Linux they are showing up as blue text. In the right-most column, notice also all of the subdirectory listings beginning with rc. We've got 0, 1, 2, 3, 4, 5, 6, and so on. These are run-level directories, for example, rc3.d is where you would have start and kill scripts to start and kill daemons running in the background when run level 3 is entered or exited. So, even those type of configuration files show up here. Notice in the L's, we have logrotate.d. This is a subdirectory because there are a number of config files in here that can be enabled, but notice directly above it we have the global logrotate file called logrotate.conf.

This is pretty common in Linux, where you'll have a global or a parent config file directly in etc that is configured to include additional configuration files if they exist in another subdirectory. In this screenshot, we are viewing the contents of /etc/apache2/apache2.conf. So, what we've got here is the Apache web server configuration file where there are a number of directives like the LogFormat, how the log files will be created in terms of their nomenclature and what will be contained within them, and so depending on the nature of the config file will determine exactly what you will see within it and what you should type in if you want to make changes.

When you're working with these config files at the command line, you have a number of ways you can work with them. If you just want to view a config file, you could just issue the cat command and point to the file, such as with cat /etc/apache2/apache2.conf. You might want to pipe that to the more command if there's more than one screen full of output so it stops after the first screen full of output, otherwise it would scroll by too quickly.

You might even use the grep command to look for something within a config file such as grep and in double quotes log followed by the path and name of the file where you want to search in this case for the text log in lowercase letters. grep is the line filtering tool, so what would be returned are any lines within the apache2.conf file that contain log. You can also view the first couple of lines in a text file with the head command. In most Linux distributions the default is the first 10 lines unless you tell it otherwise. So, for example, head /etc/apache2/apache2.conf if you want to see the last 10 lines or you want to specify the number of lines, you can use tail. Maybe you want to view the newest entries at the bottom of a config file. So, for example, tail /etc/apache2/apache2.conf. To edit the contents within the configuration file, you can use any text editor tool. You might use the vi tool, vi, or its newer variation vim, vim.

This is a text editor that's built into all Linux distributions. It stems way back from the Unix days. However, it's more complex to use than simply using the newer nano text editor. Mind you, vi is also very powerful, but issuing commands in it takes some getting used to. For example, when you're in the vi text editor, if you type in a colon, it's ready to accept commands for the vi tool as opposed to content you're typing in the text file. So, w would mean write. Typing in :q would mean quit to get out of the vi editor or you could do two things at once. You could type :wq to do both writing and quitting.

The nano text editor is a newer type of text editor included with many modern Linux distributions. It's not there, you simply need to install. It's just another software package to be installed, but instead of typing :w to make a write such as you would in vi, you would simply press Ctrl+X for exit for example, and then it will ask you if you want to write that out to a file. That would allow you to write to the file and exit out, kind of like in vi typing in :wq.

Pictured on the screen, we've got an example of the apache2 web server configuration file that's been opened up in the nano editor. Notice at the bottom it gives us a bit of help such as exit with Ctrl+X or Ctrl+K for cut, and so on.

3. Video: Managing Linux Configuration Files (it_oslsys_08_enus_03)

In this video, you will learn how to manage common Linux configuration files.
manage common Linux configuration files
[Video description begins] Topic title: Managing Linux Configuration Files. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I'm going to be managing Linux configuration files. Now depending on what you've got installed on your Linux host will really determine how many configuration files you have. Of course, there are plenty of config files there by default with any Linux system, regardless of distribution. So for example, we know that Linux config files live in or under etc. So if I change directory into etc and just do an ls to list, we've got all kinds of config files here.

[Video description begins] A terminal window appears with the heading cblackwell@Ubuntu1:~. The following command reads: cd /etc. [Video description ends]

In many cases, config files end with .conf conf or .cfg, but they don't have to. However, in some cases, some products that you've installed might have their own subdirectory, like the uncomplicated firewall here or ufw where if I change directory into ufw and if I were to do an ls in there, then we get a list of the config files for that particular software, that particular service in this case for the ufw firewall. So, let's go ahead and go back into etc, and what I'm going to do is change directory to ssh so Secure Shell for remote management.

[Video description begins] The command reads: cd ufw. [Video description ends]

[Video description begins] The following command reads: cd ssh. [Video description ends]

Here if we do an ls, we've got a number of files like an ssh_config versus an sshd_config. Now, in some cases, with some network services if you have a client and a server component, the server component is often referred to with the D as in daemon.

It's a background daemon that's always running and listening, in this case with SSH on TCP port 22. So the sshd_config is for the daemon the server, and ssh_config is for the client. So, if I were, for example to cat ssh_config, we'd be looking at settings for the SSH client if we're going to be using this as a client machine or reach out to other devices to manage them. Whereas if I cat sshd_config, of course what we'd be looking at are server settings.

[Video description begins] The following command reads: cat ssh_config. [Video description ends]


[Video description begins] The following command reads: cat sshd_config. [Video description ends]

Now, if we look through our sshd config file, notice that what it's doing is including a number of configuration files in its own subdirectory under, /etc/ssh called sshd_config.d looking for conf files in there. And that's normally the case with a lot of modern Linux services that you install. You'll have a parent or a global config file such as what we are in right now that includes a reference to config files in another location. However, there are still some settings that we can modify here, like the listening port number.

These are all listed default settings like port 22, but it's commented out. You could uncomment it by removing the hashtag symbol or the pound symbol at the beginning, change it to something else, and restart the service or the daemon. However, if we do an ls in here, notice that we also. So let's change directory to sshd_config.d and in here let's do an ls.

[Video description begins] The following command reads: cd sshd_config.d. [Video description ends]

OK, so here we've got a conf file that is used by our ssh daemon. If we were to run sudo cat against that config file, there's not much in here other than saying PasswordAuthentication yes.

[Video description begins] The command reads: sudo cat 50-cloud-init.conf. [Video description ends]

So, in other words, the SSH server is not configured solely for public key authentication, where the public key is on the server, connecting technician has the private key on their machine. PasswordAuthentication is allowed as well. Let's go ahead and run sudo apt install apache2 to install the apache2 web server.

[Video description begins] The command reads: sudo apt install apache2. [Video description ends]

I'll type in Y for yes to get it installed. Then we'll take a look at its configuration files. OK, so I'm going to change directory into /etc/apache2 which will now exist.

[Video description begins] The command is added: cd /etc/ apache2. [Video description ends]

Because we've installed the Apache Server, if I do an ls, here we've got an apache2.conf file, let's cat that.

[Video description begins] The command reads: cat apache2.conf. [Video description ends]

So, like most config files, it's got a bunch of comments. It's got a couple of active items. As we go further down through the config file, as is common, we have an include statement, for example here referring to the ports.conf file in the same subdirectory. If we do an ls, indeed there is a ports.conf, and if we cat that file, actually, let's edit it just for kicks, sudo nano ports.conf.

[Video description begins] The command reads: sudo nano ports.conf. [Video description ends]

Currently, it's set to Listen on port 80. Let's test connectivity to this server. If I type ip a, this server's address is 10.0.0.4. So, if I were to type wget http://10.0.0.4. So, if I were to type sudo wget http://10.0.0.4 and press Enter.

[Video description begins] The command is added: ip a. [Video description ends]


[Video description begins] The command is added: wget http://10.0.0.4. [Video description ends]

 It made a connection to our web server. [Video description begins] The command is added: sudo wget http://10.0.0.4. [Video description ends] The default is port 80 and we've got the index.html file. That's great.

Let's go back into the ports.conf file and change the listening port, let's say to 82. So we're making a change to a config file. I'll go ahead and save that and we're going to run sudo service apache2 restart. Restart the web server. I'll clear the screen.

[Video description begins] The command reads: sudo nano ports.conf. [Video description ends]


[Video description begins] The command reads: sudo service apache2 restart. [Video description ends]

We're going to run our sudo command. I've used the Up-arrow key to go back through our command history where we ran wget, but this time it says failed: Connection refused.

[Video description begins] The command is added: sudo wget http://10.0.0.4. [Video description ends]

Well, that's because the default listening port is 80 and it's implied. But if we were to run our wget command against that URL, but at the end add let's say: 82 for port 82 since that's what the web service configured to listen on. This time it worked, so naturally the details about making changes to configuration files will vary wildly depending on the nature of the software or the service, but it's important to get used to the fact that most config files exist in or under /etc.

[Video description begins] The command is added: sudo wget http://10.0.0.4:82. [Video description ends]

Most of them are text files. You can use a text editor if you have permissions to make a change to the config file and save it, and if there's a software component running in the background, like a daemon, just be sure to restart it to put those new changes into effect.

4. Video: Linux Shells (it_oslsys_08_enus_04)

After completing this video, you will be able to list the similarities and differences between common Linux Shells.
list the similarities and differences between common Linux Shells
5. Video: Managing Linux Shells (it_oslsys_08_enus_05)

During this video, discover how to manage Linux shells.
manage Linux shells
[Video description begins] Topic title: Managing Linux Shells. Your host for this session is Dan Lachance. [Video description ends]
Let's talk about how to manage Linux shells. So, what is the shell? Well, as we've discussed, a Linux shell is used either interactively by users, by typing in commands. It's what gives you a Command Prompt. Or, of course, a shell might be invoked by a specific shell script. You might be using a Bash Shell on your Linux system, for example, and you might launch a shell script that uses a different shell, like a Korn Shell or a C Shell, only while the script is running. So, you can switch back and forth between shells through scripts or manually at the command line. Of course, the binaries for those shells would have to be installed. Let's start here by doing a cat of /etc/passwd, passwd, the user account file. Let's pipe that to grep because I have a user in mind.

I'm looking for user mbishop. Now what I'm interested in in the returned output is the very last field,

[Video description begins] A terminal window appears with the heading cblackwell@Ubuntu1:/. The following command reads: cat /etc/passwd | grep mbishop. [Video description ends]

the field delimiter in /etc/passwd is a full colon, of course, so this is for the user account mbishop. Well, the last field defines the shell that should be spawned when that user signs in, so notice here it's /bin/sh. If I were to type whereis sh, it tells me it's in /usr/bin and there it is, if I do an ll of /usr/bin/sh, it's a symbolic link pointing to something called dash. 

[Video description begins] The command reads: whereis sh. [Video description ends]

[Video description begins] The command reads: ll /usr/bin/sh. [Video description ends]

Dash is kind of like a Bash Shell, but kind of a newer version of Bash, and depending on the Linux distribution you're using and the version of will really determine if the sh command is actually symbolic link or not and what it's pointing to. But, in this case, with Ubuntu, that's what the case is.

Now that stems from the 1970s where the shell command or sh, that was the standard shell used in Unix environments. And so, it persists to this day even though nowadays, it's actually pointing to something else. So, if I were to type sh right here in my Linux Command Prompt, it takes me into a dash environment. Notice my Command Prompt changes, I get just a dollar sign as opposed to having the dollar sign with the prefix of my username and the host on which I am connected. If I type exit, I'm back up my regular shell. If I were to try to launch a different shell like ksh, a Korn Shell, it says it's not here. No problem, we can install it, sudo apt install mksh, and after a moment, it's installed.

[Video description begins] The command is added: ksh. [Video description ends]


[Video description begins] The following command is added: sudo apt install mksh. [Video description ends]

So now if I were just try to switch to the Korn Shell by typing ksh, I'm now in.

I'm in a different Command Prompt environment. I could type exit to get out of it. In the same way, if I wanted to start a C Shell, csh same thing, it's not there and just like that, it's done.

[Video description begins] The command reads: csh. [Video description ends]

Let's just get installed for fun, sudo apt install csh,

[Video description begins] The command reads: sudo apt install csh. [Video description ends]

 So, if I were to launch a C Shell, csh, notice this one's a little bit different. Instead of a dollar sign for a Command Prompt, I get a percent symbol when I'm in a C Shell. Now remember, some of the differences between these shells will include things like how they handle variables, some command line syntax, how they handle looping, such as within shell scripts. And speaking of shell scripts, let's just exit out of here. If I were to run, let's say sudo nano, let's create a script called script1.sh, it doesn't have to have an sh extension normally for convention purposes, so it's standard.

[Video description begins] The following command is added: sudo nano script1.sh. [Video description ends]


If it's a C Shell written script written for that command interpreter, then it will have a .csh extension. If it's written to use the syntax specifics of a Korn Shell, it might have a ksh extension, it doesn't have to, but that's the norm. Let's go ahead and create a new script. The first thing you should do within a script is start with an exclamation mark, a hashtag, or a pound symbol, and then the script interpreter you want to use, such as /bin/bash, or it could be a reference to the C Shell, the Korn Shell, whatever the case might be. 

[Video description begins] A new script labelled script1.sh appears in the terminal. The following command is displayed: !#/bin/bash. [Video description ends]

Now, this is important because that shell interpreter needs to be installed on the machine where you're going to run this script. So, for example, imagine that we make a reference to a different type of shell, like a Korn Shell that isn't installed. Well, then the script won't be able to run correctly.

This line at the top of the script where you define the shell interpreter is called the shebang line. That's what they call it. So, the script might do any one of the million things. It could be anything. Let's say all we want to do is echo back the $CostCenter variable, variable names are case-sensitive, so let's assume we've already got a variable defined somewhere called CostCenter. 

[Video description begins] The following command reads: echo $CostCenter. [Video description ends]

Maybe we'll just add a clear statement at the beginning to clear the screen. At any rate, the script might do much more, we'll focus on that later on. But the point is the shebang, the first line within that shell script, make sure you put that at the top of all of your scripts.

Now there are some other small little things that will vary from one shell type to another. For example, if I go back into my C Shell by typing csh, if I type ls, well, that command works. If I were to type sudo nano and type in scr, and then press tab for tab completion, it doesn't work in the C Shell, of course.

[Video description begins] The command reads: sudo nano scr. [Video description ends]

 If I go back to my regular Bash Shell and type sudo nano, type scr, and press tab, it has tab completion, spells out the file name for me. So, you'll see some other tiny little feature variations like that between different shells.

[Video description begins] The following command is added: sudo nano script1.sh. [Video description ends]

If, for example, you prefer to use the Korn Shell. The Korn Shell is considered to be faster than a standard Bash Shell, so depending on what you're doing with scripting, it might be important to use that.

It's got more programmer like flexibility and features which can also make it less readable than Bash scripts, but you can do it. But if you wanted to switch what a user signs in with, don't forget that the /etc/passwd file defines the shell that will be used by users, so if you want to control that, you can do it.

[Video description begins] The command reads: tail /etc/passwd. [Video description ends]


So, sudo nano /etc/passwd.

[Video description begins] The following command is added: sudo nano /etc/passwd. [Video description ends]

So, all the way down to the line for mbishop, let's change the default shell for that account. So, let's say I want to set the login shell for mbishop to be /usr/bin/csh, the C Shell. OK, I'll get out of here and save that change and we're going to sign in with switch user, su. 

[Video description begins] The following line is edited: mbishop:x:1001:1002: : /home/mbishop:/usr/bin/csh. [Video description ends]

I want to keep my current login session active, dash to run the entire login environment, and then the name of the account mbishop. And then I'll enter the password and just like that, we're signed in as user mbishop. 

[Video description begins] The following user is added: su -mbishop. [Video description ends]

But notice our Command Prompt is just a percent sign which indicates that we are now signed in automatically using a C Shell type of environment. I can simply type exit to get back to my previous shell.

[Video description begins] Topic title: Managing Linux Shells. Your host for this session is Dan Lachance. [Video description ends]
Let's talk about how to manage Linux shells. So, what is the shell? Well, as we've discussed, a Linux shell is used either interactively by users, by typing in commands. It's what gives you a Command Prompt. Or, of course, a shell might be invoked by a specific shell script. You might be using a Bash Shell on your Linux system, for example, and you might launch a shell script that uses a different shell, like a Korn Shell or a C Shell, only while the script is running. So, you can switch back and forth between shells through scripts or manually at the command line. Of course, the binaries for those shells would have to be installed. Let's start here by doing a cat of /etc/passwd, passwd, the user account file. Let's pipe that to grep because I have a user in mind.

I'm looking for user mbishop. Now what I'm interested in in the returned output is the very last field,

[Video description begins] A terminal window appears with the heading cblackwell@Ubuntu1:/. The following command reads: cat /etc/passwd | grep mbishop. [Video description ends]

the field delimiter in /etc/passwd is a full colon, of course, so this is for the user account mbishop. Well, the last field defines the shell that should be spawned when that user signs in, so notice here it's /bin/sh. If I were to type whereis sh, it tells me it's in /usr/bin and there it is, if I do an ll of /usr/bin/sh, it's a symbolic link pointing to something called dash. 

[Video description begins] The command reads: whereis sh. [Video description ends]

[Video description begins] The command reads: ll /usr/bin/sh. [Video description ends]

Dash is kind of like a Bash Shell, but kind of a newer version of Bash, and depending on the Linux distribution you're using and the version of will really determine if the sh command is actually symbolic link or not and what it's pointing to. But, in this case, with Ubuntu, that's what the case is.

Now that stems from the 1970s where the shell command or sh, that was the standard shell used in Unix environments. And so, it persists to this day even though nowadays, it's actually pointing to something else. So, if I were to type sh right here in my Linux Command Prompt, it takes me into a dash environment. Notice my Command Prompt changes, I get just a dollar sign as opposed to having the dollar sign with the prefix of my username and the host on which I am connected. If I type exit, I'm back up my regular shell. If I were to try to launch a different shell like ksh, a Korn Shell, it says it's not here. No problem, we can install it, sudo apt install mksh, and after a moment, it's installed.

[Video description begins] The command is added: ksh. [Video description ends]


[Video description begins] The following command is added: sudo apt install mksh. [Video description ends]

So now if I were just try to switch to the Korn Shell by typing ksh, I'm now in.

I'm in a different Command Prompt environment. I could type exit to get out of it. In the same way, if I wanted to start a C Shell, csh same thing, it's not there and just like that, it's done.

[Video description begins] The command reads: csh. [Video description ends]

Let's just get installed for fun, as you do apt install csh,

[Video description begins] The command reads: sudo apt install csh. [Video description ends]

 So, if I were to launch a C Shell, csh, notice this one's a little bit different. Instead of a dollar sign for a Command Prompt, I get a percent symbol when I'm in a C Shell. Now remember, some of the differences between these shells will include things like how they handle variables, some command line syntax, how they handle looping, such as within shell scripts. And speaking of shell scripts, let's just exit out of here. If I were to run, let's say sudo nano, let's create a script called script1.sh, it doesn't have to have an sh extension normally for convention purposes, so it's standard.

[Video description begins] The following command is added: sudo nano script1.sh. [Video description ends]


If it's a C Shell written script written for that command interpreter, then it will have a .csh extension. If it's written to use the syntax specifics of a Korn Shell, it might have a ksh extension, it doesn't have to, but that's the norm. Let's go ahead and create a new script. The first thing you should do within a script is start with an exclamation mark, a hashtag, or a pound symbol, and then the script interpreter you want to use, such as /bin/bash, or it could be a reference to the C Shell, the Korn Shell, whatever the case might be. 

[Video description begins] A new script labelled script1.sh appears in the terminal. The following command is displayed: !#/bin/bash. [Video description ends]

Now, this is important because that shell interpreter needs to be installed on the machine where you're going to run this script. So, for example, imagine that we make a reference to a different type of shell, like a Korn Shell that isn't installed. Well, then the script won't be able to run correctly.

This line at the top of the script where you define the shell interpreter is called the shebang line. That's what they call it. So, the script might do any one of the million things. It could be anything. Let's say all we want to do is echo back the $CostCenter variable, variable names are case-sensitive, so let's assume we've already got a variable defined somewhere called CostCenter. 

[Video description begins] The following command reads: echo $CostCenter. [Video description ends]

Maybe we'll just add a clear statement at the beginning to clear the screen. At any rate, the script might do much more, we'll focus on that later on. But the point is the shebang, the first line within that shell script, make sure you put that at the top of all of your scripts.

Now there are some other small little things that will vary from one shell type to another. For example, if I go back into my C Shell by typing csh, if I type ls, well, that command works. If I were to type sudo nano and type in scr, and then press tab for tab completion, it doesn't work in the C Shell, of course.

[Video description begins] The command reads: sudo nano scr. [Video description ends]

 If I go back to my regular Bash Shell and type sudo nano, type scr, and press tab, it has tab completion, spells out the file name for me. So, you'll see some other tiny little feature variations like that between different shells.

[Video description begins] The following command is added: sudo nano script1.sh. [Video description ends]

If, for example, you prefer to use the Korn Shell. The Korn Shell is considered to be faster than a standard Bash Shell, so depending on what you're doing with scripting, it might be important to use that.

It's got more programmer like flexibility and features which can also make it less readable than Bash scripts, but you can do it. But if you wanted to switch what a user signs in with, don't forget that the /etc/passwd file defines the shell that will be used by users, so if you want to control that, you can do it.

[Video description begins] The command reads: tail /etc/passwd. [Video description ends]


So, sudo nano /etc/passwd.

[Video description begins] The following command is added: sudo nano /etc/passwd. [Video description ends]

So, all the way down to the line for mbishop, let's change the default shell for that account. So, let's say I want to set the login shell for mbishop to be /usr/bin/csh, the C Shell. OK, I'll get out of here and save that change and we're going to sign in with switch user, su. 

[Video description begins] The following line is edited: mbishop:x:1001:1002: : /home/mbishop:/usr/bin/csh. [Video description ends]

I want to keep my current login session active, dash to run the entire login environment, and then the name of the account mbishop. And then I'll enter the password and just like that, we're signed in as user mbishop. 

[Video description begins] The following user is added: su -mbishop. [Video description ends]

But notice our Command Prompt is just a percent sign which indicates that we are now signed in automatically using a C Shell type of environment. I can simply type exit to get back to my previous shell.

Let's talk about how to manage Linux shells. So, what is the shell? Well, as we've discussed, a Linux shell is used either interactively by users, by typing in commands. It's what gives you a Command Prompt. Or, of course, a shell might be invoked by a specific shell script. You might be using a Bash Shell on your Linux system, for example, and you might launch a shell script that uses a different shell, like a Korn Shell or a C Shell, only while the script is running. So, you can switch back and forth between shells through scripts or manually at the command line. Of course, the binaries for those shells would have to be installed. Let's start here by doing a cat of /etc/passwd, passwd, the user account file. Let's pipe that to grep because I have a user in mind.

I'm looking for user mbishop. Now what I'm interested in in the returned output is the very last field, the field delimiter in /etc/passwd is a full colon, of course, so this is for the user account mbishop. Well, the last field defines the shell that should be spawned when that user signs in, so notice here it's /bin/sh. If I were to type whereis sh, it tells me it's in /usr/bin and there it is, if I do an ll of /usr/bin/sh, it's a symbolic link pointing to something called dash. Dash is kind of like a Bash Shell, but kind of a newer version of Bash, and depending on the Linux distribution you're using and the version of will really determine if the sh command is actually symbolic link or not and what it's pointing to. But, in this case, with Ubuntu, that's what the case is.

Now that stems from the 1970s where the shell command or sh, that was the standard shell used in Unix environments. And so, it persists to this day even though nowadays, it's actually pointing to something else. So, if I were to type sh right here in my Linux Command Prompt, it takes me into a dash environment. Notice my Command Prompt changes, I get just a dollar sign as opposed to having the dollar sign with the prefix of my username and the host on which I am connected. If I type exit, I'm back up my regular shell. If I were to try to launch a different shell like ksh, a Korn Shell, it says it's not here. No problem, we can install it, sudo apt install mksh, and after a moment, it's installed. So now if I were just try to switch to the Korn Shell by typing ksh, I'm now in.

I'm in a different Command Prompt environment. I could type exit to get out of it. In the same way, if I wanted to start a C Shell, csh same thing, it's not there. Let's just get installed for fun, sudo apt install csh, and just like that, it's done. So, if I were to launch a C Shell, csh, notice this one's a little bit different. Instead of a dollar sign for a Command Prompt, I get a percent symbol when I'm in a C Shell. Now remember, some of the differences between these shells will include things like how they handle variables, some command line syntax, how they handle looping, such as within shell scripts. And speaking of shell scripts, let's just exit out of here. If I were to run, let's say sudo nano, let's create a script called script1.sh, it doesn't have to have an sh extension normally for convention purposes, so it's standard.

If it's a C Shell written script written for that command interpreter, then it will have a .csh extension. If it's written to use the syntax specifics of a Korn Shell, it might have a ksh extension, it doesn't have to, but that's the norm. Let's go ahead and create a new script. The first thing you should do within a script is start with an exclamation mark, a hashtag, or a pound symbol, and then the script interpreter you want to use, such as /bin/bash, or it could be a reference to the C Shell, the Korn Shell, whatever the case might be. Now, this is important because that shell interpreter needs to be installed on the machine where you're going to run this script. So, for example, imagine that we make a reference to a different type of shell, like a Korn Shell that isn't installed. Well, then the script won't be able to run correctly.

This line at the top of the script where you define the shell interpreter is called the shebang line. That's what they call it. So, the script might do any one of the million things. It could be anything. Let's say all we want to do is echo back the $CostCenter variable, variable names are case-sensitive, so let's assume we've already got a variable defined somewhere called CostCenter. Maybe we'll just add a clear statement at the beginning to clear the screen. At any rate, the script might do much more, we'll focus on that later on. But the point is the shebang, the first line within that shell script, make sure you put that at the top of all of your scripts.

Now there are some other small little things that will vary from one shell type to another. For example, if I go back into my C Shell by typing csh, if I type ls, well, that command works. If I were to type sudo nano and type in scr, and then press tab for tab completion, it doesn't work in the C Shell, of course. If I go back to my regular Bash Shell and type sudo nano, type scr, and press tab, it has tab completion, spells out the file name for me. So, you'll see some other tiny little feature variations like that between different shells. If, for example, you prefer to use the Korn Shell. The Korn Shell is considered to be faster than a standard Bash Shell, so depending on what you're doing with scripting, it might be important to use that.

It's got more programmer like flexibility and features which can also make it less readable than Bash scripts, but you can do it. But if you wanted to switch what a user signs in with, don't forget that the /etc/passwd file defines the shell that will be used by users, so if you want to control that, you can do it.

So, sudo nano /etc/passwd. So, all the way down to the line for mbishop, let's change the default shell for that account. So, let's say I want to set the login shell for mbishop to be /usr/bin/csh, the C Shell. OK, I'll get out of here and save that change and we're going to sign in with switch user, su. I want to keep my current login session active, dash to run the entire login environment, and then the name of the account mbishop. And then I'll enter the password and just like that, we're signed in as user mbishop. But notice our Command Prompt is just a percent sign which indicates that we are now signed in automatically using a C Shell type of environment. I can simply type exit to get back to my previous shell.

6. Video: Manipulating Linux Environment Variables (it_oslsys_08_enus_06)

Find out how to manipulate Linux environment variables at the command line and in scripts.
manipulate Linux environment variables at the command line and in scripts
[Video description begins] Topic title: Manipulating Linux Environment Variables. Your host for this session is Dan Lachance. [Video description ends]
In this video, the focus is going to be on working with environment variables in Linux. Now that means working with them both at the Command Prompt, and that may vary from one shell to another, such as a C Shell, a Korn Shell, or a Bash Shell. Environment variables might be handled a little bit differently. We'll also see how it's handled within a shell script, so let's take a look at this. Now what is an environment variable? Well, an environment variable is essentially a storage location of memory that retains a value that you store in that variable. What could that value be? It could be anything. It could be the name of a cost center, the name of a city, an employee ID, an IP address of a server. It could be anything.

So, here in Linux, I'm using Bash where I can just type env, which, of course, stands for environment to return a list of all of the environment variables set right now in my login session followed by their values.

[Video description begins] A terminal window appears with the heading cblackwell@Ubuntu1:~. The following command reads: env. [Video description ends]

For example, I have an environment variable called SSH_CONNECTION. Notice in uppercase letters when you refer to variables, it is case-sensitive in Linux, so you have to be careful of that. And I've got a value stored after the equals sign, it's shown right here in the output. So, we've got a lot of variables here.

Of course, the PATH variable is always important as well as it's used, of course, to locate binaries that we might type in from any location in the file system hierarchy. I could use the env command and pipe that to grep and if I know what I'm looking for, let's say PATH uppercase or if I don't know if it's uppercase or not, of course, with grep, I can use -i for case insensitive. There's the PATH variable again along with its value.

[Video description begins] The command reads: env | grep -i PATH. [Video description ends]

Looks like there are a couple of references to PATH here. I can also display the value stored in a variable here in a Bash Shell just by typing echo $PATH and it returns only the value stored within that variable.

[Video description begins] The following command is added: echo $PATH. [Video description ends]

Now those are existing variables that are set when I log in, but I can also create my own variables. Let's say I want to create a variable called CostCenter and I'm using a capital C for Cost, capital C for Center, and as we know when we refer to this, it is case-sensitive.

To write a value into that, a literal text string, let's say I could put an equals sign and in double quotes, let's say I'm going to put in the word Toronto. So, that's all we need to do.

[Video description begins] The following command is added: CostCenter="Toronto". [Video description ends]

If I want to echo it back, well, we now know we can echo back dollar sign so a dollar sign is a prefix when you want to work with an existing variable's value. But notice if I put costcenter in lowercase letters, we get a whole lot of nothing.

[Video description begins] The following command is added: echo $costcenter. [Video description ends]

If I were to correct that and use the correct case, so a capital C for Cost, capital C for Center, of course, it correctly returns Toronto.

[Video description begins] The following command is added: echo $CostCenter. [Video description ends]

But there are also times where you might need to store the result of a Linux command in a variable, not the text for the command itself, the result of the command.

For example, consider this command ip a. Let's show my IP address information for my interfaces. I'm going to grep it for the word inet, which I'm then going to in turn grep for broadcast, brd. OK, well, that worked OK.

[Video description begins] The command reads: ip a | grep inet | grep brd. [Video description ends]

It returned only what I wanted to, what I told it to. Let's say I want to store that in a variable, that entire line. Well, let's use the Up arrow key to bring up that previous command. Let's say I'm going to create a variable called capital IP and it will equal that command, but when I press Enter, it says a: command not found, OK. So, it's treating a as a separate command, that didn't work. What if we put it in double quotes? Well, you might be able to predict what will happen here. No error.

[Video description begins] The command now reads: IP=ip a | grep inet | grep brd. [Video description ends]

[Video description begins] The command now reads: IP="ip a | grep inet | grep brd". [Video description ends]

But when I echo back $IP capital letters, it literally stored that as a text string. Not my intention.

[Video description begins] The following command is added: echo $IP. [Video description ends]

I want the result of that command stored in the IP variable. Here's what you do. If we go back with our Up arrow key to our previous main command instead of double quotes around the command or the expression, use backticks. That's not a single quote, it's a backtick, usually, that's available on the upper left of your keyboard somewhere wherever you would press the tilde key. What that means is take the result of that expression and store it in the variable. 

[Video description begins] The command now reads: IP=`ip a | grep inet | grep brd`. [Video description ends]

So, if I do an echo now of $IP, what do we get? We get the result of that statement and not the statement itself. So that could be a very important aspect of working with variables. Now if I clear the screen and type env, where is our IP variable? Where is our CostCenter variable? Well, we know that we can pipe the result of env to grep and look for something like IP, nothing.

[Video description begins] The following command is again added: echo $IP. [Video description ends]

[Video description begins] The following command reads: env | grep IP. [Video description ends]

What if we grep it for CostCenter? And I know I'm spelling these correctly, nothing.

[Video description begins] The following command is added: env | grep CostCenter. [Video description ends]

So, environment variables are those that are set for your system and can be set also during login, of course. What we can do then to view all of our variables is use the set command instead. Now it also shows any function definitions that are available, which is what we're seeing here. We've got these names space, open and close parenthesis, open and close curly braces. Those are functions, you can also define your own custom functions, but grep to the rescue. If I run set and pipe that to grep, let's say, IP uppercase, there is our IP variable. In the same way, if I grep for CostCenter with the capital Cs, there it is.

[Video description begins] The following command reads: set | grep IP. [Video description ends]

[Video description begins] The following command is added: set | grep CostCenter. [Video description ends]

So, that's going to be very important to work with as well. The last thing I want to do is talk about how variable scope works when you invoke scripts, OK. What I mean by that is if I type ls, I've got nothing in my home directory. So. I'm going to create a new script, sudo nano newscript.sh, we'll call it. The first line will be the shebang line, which is going to define the shell interpreter that I want to use to run the commands in the script. 

[Video description begins] The following command reads: sudo nano newscript.sh. [Video description ends]

So, !#/bin/bash, in this case, we'll have the screen cleared with clear, we'll have a blank line with echo, and then I'm going to echo back $CostCenter, and then another echo line.

[Video description begins] A new script labelled newscript.sh appears in the terminal. The following command is displayed: !#/bin/bash. [Video description ends]

[Video description begins] The following line is added: echo $CostCenter. [Video description ends]

Now we know that CostCenter is a valid variable right now in our current shell. Now, if you needed that to be persistent across login sessions or reboots, put it in a login script or some kind of startup file on your Linux host.

But the CostCenter variable was not defined within this script. Let's see what's going on here. Let's Ctrl+X to save this out to that file. Let's run sudo chmod +x to add the execute permission to new script sh.

[Video description begins] The terminal window appears again. The following command is added: sudo chmod +x newscript.sh. [Video description ends]

If I run ./newscript.sh, we get nothing, but wait a minute.

[Video description begins] The following command is added: ./newscript.sh. [Video description ends]

If I do echo $CostCenter, it does have a value of Toronto, but when you start a script, you are spawning a new shell. 

[Video description begins] The following line is again added: echo $CostCenter. [Video description ends]

It's kind of like me typing bash to start a new shell environment. And if I echo $CostCenter, nothing, it's a different shell. Well, then how do we make sure variables are visible in child shells that might be spawned, whether manually like I've just done by typing in bash or by executing a shell script?

The answer is you export the variable. If I were to type export CostCenter, I could have used this syntax when I was initially setting the value of it, but I can do it also after the fact, export CostCenter, no dollar sign.

[Video description begins] The following command is added: export CostCenter. [Video description ends]

So, if I echo right here at the command line, echo $CostCenter, we still have the value of Toronto. If I run my script, newscript.sh, it now returns Toronto. It's now visible, the variable is visible to my script because I exported it so therefore, it is now available in child-spawned shells.

7. Video: Using Ansible to Manage Linux Configurations (it_oslsys_08_enus_07)

During this video, you will learn how to use Ansible to centrally manage Linux configurations.
use Ansible to centrally manage Linux configurations
[Video description begins] Topic title: Using Ansible to Manage Linux Configurations. Your host for this session is Dan Lachance. [Video description ends]
In this demo, I'm going to focus on how to install and do a very basic configuration to get Ansible up and running. What is Ansible, you might wonder? Ansible is one of those centralized configuration management tools that you might use in the enterprise so that you can centrally manage numerous hosts, in our case, numerous Linux hosts. Now, of course, you could go around to each and every Linux host that required the same configuration and do it manually.

Obviously, that does not scale well when you talk about dozens, hundreds, or even thousands of Linux hosts. What you're doing with Ansible is reaching out over the network and applying some kind of configuration or commands to be run on a multitude of managed hosts. So, to get started here in Linux, we first will add a software repository from which we can then install Ansible.

So, to do that, I'm going to run sudo apt-add-repository and I'm going to add a ppa repository for Ansible. PPA stands for Personal Package Archive. It usually means that you've got a repository that might not be widely accepted as a public package repository on the Internet, but it might be maintained by an individual or a group of individuals. And, of course, you have to make sure that that makes sense in your environment in terms of security. Do you trust the software from it? In this case, I know I do, and I'll press Enter to add that repository.

[Video description begins] A terminal window appears with the heading cblackwell@Ubuntu1:~. The following command reads: sudo apt-add-repository ppa:ansible/ansible. [Video description ends]

And now that I've done that, I can run sudo apt install ansible. OK, once that's done, I'm going to change directory to /etc/ansible.

[Video description begins] The following command is added: sudo apt install ansible. [Video description ends]

If that directory is not there, just go ahead and make it. In here, I've already got a file called hosts.

Again, you might have a sample file placed there. If I run sudo nano hosts, then it opens up my file.

[Video description begins] The following commands are added: cd /etc/ansiblew, ls, and sudo nano hosts. [Video description ends]

So, I've got a header section here defined with the open and close square brackets, and then underneath it, I've listed the IP address of one of my other servers I want to manage here. And I've also added a couple of directives here. I've added ansible_user equals and I've provided a user account to use on that remote server. What's going to happen here is Ansible is going to make an SSH secured connection over the network to that host to manage it. But I've also specified ansible_ssh_pass and provided the password for that account. Now that might be considered a security risk because you're storing a password in clear text in a file in the file system.

If you wanted to, there are other alternatives with Ansible Playbooks that might use SSH public key authentication, which means private keys would need to be available to the Ansible server because the public key that's related to it will be stored on each host that needs to be managed. But in this example, we're going to stick with this. I've also got an all : vars header section where I'm telling it I want to use a specific version of the Python interpreter on those remote hosts. Now in a realistic enterprise environment, you would have numerous hosts added here, I only have one in this example. I'm going to go ahead and get out of there.

[Video description begins] A screen appears that displays the title: GNU nano 7.2, hosts. Below, the highlighted command reads: 10.0.0.7 ansible_user=cblackwell ansible_ssh_pass=Pa$$w0rdABC123. The next line reads: ansible_python_interpreter=/usr/bin/python3. [Video description ends]

Now, also if you want to be able to use the SSH password that way for Ansible management, you'd have to make sure that you install the sshpass package. I've already got it installed so we are good to go.

The next thing I can do is test remote connectivity.

[Video description begins] The following command is added: sudo apt install sshpass. [Video description ends]

One way to do that is to use the built-in Ansible ping module by running sudo ansible all, meaning I want to try to execute this type of statement on all machines, -m and ping. When I press Enter, what I'm looking for for output is green text where it says SUCCESS, and we should get a return listing that looks similar to this output with the SUCCESS and the IP of the server, you should get that for each and every server in the Ansible inventory file. Well, now this is exciting. We know we've got connectivity over the network through SSH to manage nodes. So, now we might test, for example, running regular Linux commands. You can also have more complicated sets of instructions through playbooks, but here with the command, we might do this, sudo ansible all -a, and then, we'll pass it our Linux command in double quotes, let's say ls / which means let's get a listing of what's in the root of the file system.

And because I've got all in my command line, this will be performed against all Ansible-managed nodes. Of course, we only have one, but you get the picture. Let's press Enter. So, now we've got our return listing of everything on the root, and if we go back at the top, of course, the header part shows the IP address so that if we had many listings, we'd be able to tell what is what. Now, of course, you can also use output redirection to place that in a file.

[Video description begins] The following commands are added: sudo ansible all -m ping, and sudo ansible all -a "ls /". [Video description ends]


So, if I bring up that Ansible command that we just ran, but at the end, if I tack on a greater than sign, let's say, I'll specify in /home/cblackwell, I want to create a file called rootlisting_ansiblenodes.txt. I'll just go ahead and press Enter.

If I press cd and just enter to go to my home directory, do an ls, there's the root listing file, let's cat the root listing file, and everything is stored within a file now. So, output redirection can definitely be your friend if that's the type of thing you might be doing with Ansible. We are talking about having a scriptable and automated way to remotely manage configurations. As a last example, I'm just going to open up a file here in nano that I've called ansible_aptupdate.yaml so it's YAML syntax.

[Video description begins] The following series of commands are added: sudo ansible all -a "ls /" > /home/cblackwell/rootlisting_ansiblenodes.txt, cd, ls, and cat rootlisting_ansiblenodes.txt. [Video description ends]

And this is a playbook file so I've got it formatted the way it needs to be formatted here to be used by Ansible where it applies to all of the hosts and it's going to use sudo on remote hosts. Now down under the tasks section, I give it a meaningful name of some kind, but I'm calling upon the built-in apt module part of Ansible, which, of course, is used for package management on Debian-based Linux machines.

[Video description begins] The following command is highlighted: sudo nano ansible_aptupdate.yaml. [Video description ends] 

I'm telling you to update the cache and I'm giving it a couple of timeout items as well. There are many built-in modules, we don't have time to cover them all here. Of course, as we're just touching or scratching the surface related to Ansible, you might want to use the built-in file directive or service directive to work with the file system or maybe to restart services to list but only a tiny fragment of what is possible with Ansible. Well, let's go ahead and get out of here and let's run sudo ansible-playbook and then we simply give it the path and name of our Ansible Playbook file.

I'm going to go ahead and press Enter and we can see based on the output everything is OK for the listed IP address of the remote Ansible node. Of course, it could be more than one where nothing was failed or skipped. Now, Ansible isn't the only game in town. It works well for smaller to medium-sized deployments in terms of number of managed nodes. For very large enterprise deployments, you could use something similar like Puppet or even tools like Terraform. While the details will certainly be different, the overall underlying concept is the same, centralized desired configuration management.

[Video description begins] The following command is added: sudo ansible-playbook ansible_aptupdate.yaml. [Video description ends]

8. Video: Course Summary (it_oslsys_08_enus_08)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary [Video description ends]
So, in this course, we've examined how to manage Linux configuration files, shells, environment variables, and how to manage Linux through Ansible. We did this by exploring how to manage Linux configuration files and how to use various types of Linux shells. We managed Linux environment variables and we managed Linux configurations using Ansible. In our next course, we'll move on to learn how to mitigate common Linux security threats and also how to work with user cryptography to secure Linux.

Course File-based Resources
•	Using Ansible to Manage Linux Configurations
Topic Asset
© 2023 Skillsoft Ireland Limited - All rights reserved.