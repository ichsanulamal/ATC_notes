CompTIA Linux+: Daemons & Processes
A crucial part of managing the Linux OS is controlling how processes and daemons run. The cron facility can be used to schedule maintenance tasks. Using cron to view and manage logs, including log forwarding, leads to a secure and performant Linux environment. Begin this course by discovering how processes and daemons work in Linux, and how to manage them using command line tools. Then you will explore Linux foreground and background jobs and find out how to schedule recurring tasks using cron. Next, you will view and manage Linux logs using logrotate. Finally, you will configure log forwarding using rsyslog. This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_05_enus_01)

    2. Video: Linux Processes and Daemons (it_oslsys_05_enus_02)

    3. Video: Managing Linux Startup and Shutdown (it_oslsys_05_enus_03)

    4. Video: Managing Linux Processes and Daemons (it_oslsys_05_enus_04)

    5. Video: Configure Linux Jobs (it_oslsys_05_enus_05)

    6. Video: Configuring Linux Daemon Startup Scripts (it_oslsys_05_enus_06)

    7. Video: Scheduling with Cron (it_oslsys_05_enus_07)

    8. Video: Managing Cron jobs (it_oslsys_05_enus_08)

    9. Video: Linux Logging Facilities (it_oslsys_05_enus_09)

    10. Video: Viewing Linux Logs (it_oslsys_05_enus_10)

    11. Video: Managing Linux Log Rotation (it_oslsys_05_enus_11)

    12. Video: Configuring Linux Log Forwarding With rsyslog (it_oslsys_05_enus_12)

    13. Video: Course Summary (it_oslsys_05_enus_13)

1. Video: Course Overview (it_oslsys_05_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance . [Video description ends]

Hi, I'm Dan Lachance. A crucial part of managing the Linux OS is controlling how processes and daemons run.
The cron facility can be used to schedule maintenance tasks while viewing and managing logs, including log forwarding leads to secure and performant Linux environments.

In this course, I'll start by discussing how processes and daemons work in Linux, followed, by managing them and runlevels using command line tools.

I will then work with Linux foreground and background jobs and I will schedule recurring tasks using cron.

Next, I will view Linux logs and manage them using log rotate. Lastly, I will configure log forwarding using rsyslog. This course can be used to prepare for the Linux plus XK0-005 certification exam.

2. Video: Linux Processes and Daemons (it_oslsys_05_enus_02)

Upon completion of this video, you will be able to recall how the init process and runlevels work in Linux.
recall how the init process and runlevels work in Linux
[Video description begins] Topic title: Linux Processes and Daemons. Your host for this session is Dan Lachance . [Video description ends]

It's important to understand how Linux processes work. So let's talk about how Linux processes and daemons are configured, how they behave in Linux. We'll start here by talking about Linux programs. So really we're talking about running a process, a task within the operating system.
Now, if that process or task results in a service that stays up and running in the background for an extended period of time, and that's normal behavior such as an apache web server or the ssh daemon, well, then we call it a daemon. It's a program that's always running. And if it's a network type of service, it's waiting for connections on a given port number. The apache web server might listen on ports 80 or 443, whereas ssh normally listens on port 22.

With Linux processes, we’re talking about a program that you launch within Linux that could even be a command that you type at the command line. Even ls temporarily runs as a Linux process while it’s doing its thing, whether it's milliseconds or hours. So when we type ls, the Linux kernel is going to assign that process even if it runs for a very short period of time.

A unique ID called a process ID or a PID, a PID, and that PID will show up as a running process. If you use other command line utilities to look at running processes only while, in our case, the ls command is executing. You might recall that one of the first things that is launched by the Linux kernel is init. The init process always is assigned by the kernel, a process ID or a PID of 1.

The PIDs are important because they are what are returned as output with a lot of Linux commands that we’ll be taking a peek at. So you can use the PID to not only monitor but also manage processes. For example, you can kill a process, you can bring it down in a variety of different ways by giving it a specific signal. For example, if we type kill 45222, the 45222 is the PID of the process that we want to kill.

Now by default, even though the kill command sounds like it might just abruptly stop something, it actually tries to bring down that named process. When I say named, I mean by PID, it tries to bring it down gracefully. If you start passing command line parameters like -9, for example, to the kill command, it means to bring down the process immediately, but otherwise, it tries to bring it down cleanly.

The ps command for a process is used to show running processes. There are command-line parameters so that it will allow you to see processes that are running outside of the currently logged-in user context.

You can run the pstree command to get kind of a hierarchy starting from the init process of all of the running processes that can be helpful if you want to see what spawned a given process, and you can use the top command to get the top consumers of things like per cent CPU utilization and per cent of memory or RAM.

Pictured on the screen, we have the output from the ps command. Notice that the parameters that have been passed are -aux, so we want all processes that are displayed and the x means, even processes that are not tied to a terminal to a teletype terminal or TTY. In other words, doesn't have to have been spawned by a user. If the kernel spawned a process running in the background, it's not tied to a specific terminal or login session.

And that’s why, here in the output of the ps command, if you take a peek under the TTY column in our screenshot, we have a series of question marks, which means, it’s a background running process. It’s not tied to a user login session. In the leftmost column, under the user column, we have the name of the user under which the process is running, such as the user root. We have the PID. Notice the first PID shown here is number 1. And if we go to the far right, the command that spawned that is, /sbin/init. We can also view the %CPU column, the %MEM column and so on. So the ps command is a very important command to know as a Linux technician.

So we know that a Linux daemon is a type of running Linux process. It's a program that just stays running in the background, whether it's the cron daemon for job scheduling, to run things at certain points in time during the day or every certain number of days or certain days of the month and so on. The ssh daemon for remote host management, the http web server stack that can be a background daemon and there are plenty of other ones. Normally the start-up script that starts up that daemon lives under /etc/init.d.

And that leads us to a discussion of runlevels. We've alluded to this, but it's important to understand how that works in the context of daemons. So, a daemon has a startup script for a specific runlevel. Now runlevel 3, for example, in Linux, means we have multi-user support. We can have multiple users signed in simultaneously and also we have network support, but no GUI support. Runlevel 5, is the same as runlevel 3, but it has added GUI support. You can choose to have a GUI desktop environment running on top of the X-windows framework. Why is that relevant? Because you can determine which daemons should be running in a given runlevel.

You can also control runlevels at the command line. For example, if I run sudo init. So that's referring to the init process. And if we tell it 0, well runlevel 0 means it’s another way to shut down the system. Whereas sudo init 6, means that we want to reboot the system. Runlevel 6 is reboot. On the Linux server side, you’ll find that runlevel 3 is commonly set as the default runlevel. And so, for daemons that will start when the server starts in runlevel 3, that means there would be startup scripts for daemons inside of a specific subdirectory.

So, in our case here, let's say that we're talking about having the ssh daemon running when the server enters runlevel 3 on bootup. That means then that we would have a symbolic link, a symlink or soft link, whatever you’d like to call it, that points to the ssh daemon binary, but the link itself would be in the appropriate runlevel directory. On Ubuntu Linux as an example and Debian-based distros, that would be under /etc/rc3 for runlevel 3.d.

And if it’s a startup script because we want ssh to run in runlevel 3, it will start with a capital S. If you disable a daemon from running in a given runlevel, it'll have a kill script that starts with a capital K. Here we've got capital S01. The numbering helps determine the order in which these daemons start. Sometimes that's important. And then, in this case, ssh. So remember then, the symlink in the runlevel directory points to the actual binary, so it actually loads something.

In our last screenshot here, we have the result of running the sudo service ssh status. As you might guess, this will show us the status of the ssh daemon. Is it running, is it not? Is it encountering a problem? Here, it states that, in fact, this daemon is active and running and we can see when: it says since and then it’s got a date and timestamp. So we know how long that daemon has been up and running and we can determine if it just restarted or whatever the case might be.

So what's important then also to understand how we could use these service command and we don't have to just check the status, we could stop the service, we could start it. Of course, when we check the status, we can reload its configuration. So there are many options beyond just checking the status of this. And that's important to know when it comes to managing Linux daemons.

3. Video: Managing Linux Startup and Shutdown (it_oslsys_05_enus_03)

In this video, you will learn how to manage Linux startup and shutdown using init and runlevels.
manage Linux startup and shutdown using init and runlevels
[Video description begins] Topic title: Managing Linux Startup and Shutdown. Your host for this session is Dan Lachance. [Video description ends]

In this demo, we're going to be taking a look at how to manage Linux startup and shutdown. Now, this means that we have to experiment [Video description begins] A window named cblackwell @ ubuntu 2 : / is open. The screen displays a command: cblackwell @ ubuntu 2 : / $ [Video description ends] a little bit with runlevels.
Remember, there are various numeric runlevel states in Linux that mean different things. For example, if I were to issue the command sudo runlevel 0, that means that we want to shut down the system. If we were to do sudo runlevel 6, that means that we want to switch to runlevel 6, which really means what we want to do, is restart the system. You can run just the runlevel command all by itself to return the current runlevel. Here is returning runlevel 5. [Video description begins] The host runs the runlevel command and the following appears on the screen: N 5 cblackwell @ ubuntu 2 : / $ [Video description ends] If we wanted to, we could issue init 3.

Now what that has done, is switched from our current runlevel of 5. The N means there was no previous runlevel, but now if we type runlevel, the current runlevel is 3. Of course, the previous runlevel is showing now as 5. What does that do? [Video description begins] The host runs the command cblackwell @ ubuntu 2 : / $ sudo init 3. This gives a result: [ sudo ] password for cblackwell : cblackwell @ ubuntu 2 : / $ . He further runs the runlevel command and the numbers 5 and 3 along with cblackwell @ ubuntu 2 : / $ gets displayed. [Video description ends]

It doesn't look like anything changed. Well, you can have different startup scripts to determine which daemons run in different runlevels. Of course, runlevel 5 supports a GUI, runlevel 3 doesn’t. So, if I were, for example, to change the directory into /etc/rc3.d that’s the runlevel directory for runlevel 3. If we did a ls, notice we’ve got a number of files here, that start with a capital S. So, S01 apport numerically and alphabetically would come before S01dbus so that daemon would start before the dbus daemon would start when we enter runlevel 3.

Notice we have S01ssh. Ssh is also going to start within this runlevel. If we were to do a ls of . . / to go back one level, rc5.d, then we would have the scripts that determine which daemons will start when we are entering runlevel 5.

Just for fun, why don't we go ahead and run the sudo apt install? Why don't we install the apache2 web server and experiment with its startup on this machine? So do you want to continue? I’ll type in the letter y for yes. And just like that, we've got the apache web server stack running. We can verify that of course with sudo service apache2, it's called status. Okay, it’s active and running. Notice here, it also says enabled. Well, that means it's enabled on system startup. So, therefore, if we do a ls of the rc3.d directory, we’re going to have a new entry for starting the apache2 daemon.

What’s interesting is, if you do [Video description begins] The host points to the entry S01apache2 [Video description ends] a long listing with l l, notice that these are symlinks that point to the appropriate scripts. Now you might also have the presence remember of kill scripts to kill certain types of daemons when entering that runlevel. So they will not be running. But we can manipulate it beyond the default, such as when we install a package, we could run sudo systemctl, disable apache2. Okay.

So now if we do a ls of our current directory, notice that we no longer have a symlink to start apache2 but instead to kill it. Capital K is the prefix on that file name. [Video description begins] He points to the symlink K01apache2 [Video description ends] Of course, we could re-enable it, by changing disable to enable. [Video description begins] He types cblackwell @ ubuntu 2 : / etc/ rc3.d$ sudo systemctl enable apache2. [Video description ends] And now if we clear the screen once again and do a ls of the current directory rc3.d under etc, we’re back to having our start symlink for the apache2 daemon.

Now, the other thing to think about too is really how often will we be switching between runlevels. That's actually kind of rare. It might be much more common of course, to determine whether you want certain daemons to run or not.

I mean really what you could do for runlevel 3 if you really wanted to, you could simply delete any of these symlinks in here, to prevent those from starting again when the machine boots. The same goes for the kill files in here that start with the capital K, so using the systemctl command is just really manipulating these symlinks.

You can do it yourself at the command line because they are files if you wish. We can also determine what the default runlevel for a given Linux host is, by running sudo systemctl set-default for example, multi-user.target. What we're doing here is setting the default runlevel to be runlevel 3, whereas if you set it to graphical.target, you would be setting that to be runlevel 5. Now let's once again do a l l in the runlevel 3 directory so we know that we've got symlinks here.

For example, for S01apache2, and we set it points to a daemon startup script under etc.init.d, in this case, apache2 is it. So let’s take a look at that. Let’s change the directory to /etc. /init.d. Clear the screen. Let’s do a ls-ld of things that start with apache. Now the -d means do not show me what’s in directories that start with the text apache, just show me the entry itself.

Okay, so we don't have directories, but we've got two files. Let’s cat the apache2 script file and pique that to more. So this is a shell script as shown at the top here with this directive that tells it what to execute with. So under /bin/sh standard bash shell. So this contains the instructions on actually starting the apache web server daemon.

This is what the symlink in the runlevel directory is pointing to. So if you really want to customize the behavior of daemons in terms of how they start, and how they stop; you can go ahead and modify the appropriate file here if you know what you're doing to get the desired behavior that will then impact the symlinks or the references to these daemon startup scripts for given runlevels.

So this will give us a sense then of how we might work with background daemons and determine how they behave with given runlevels as well as how to set the default system runlevel.

4. Video: Managing Linux Processes and Daemons (it_oslsys_05_enus_04)

Find out how to manage Linux processes and daemons using commands such as ps, top, kill, and service.
manage Linux processes and daemons using commands such as ps, top, kill, and service
[Video description begins] Topic title: Managing Linux Processes and Daemons. Your host for this session is Dan Lachance. [Video description ends] In this demo, we're going to focus on how to manage Linux processes and daemons. Let's start, first of all, by taking a look at some very common commands that help us achieve this.
I’m going to issue the ps command for processes. When I press enter, it only shows me the processes that are relative to my current user login session. Notice the column headings. [Video description begins] After the host runs the ps command, a table gets displayed. The table has the following headers: PID, TTY, Time and CMD. Under the PID column, numbers 1312 and 6314 are given. The TTY column has pts/0 under it. The Time column displays the time 00 : 00 : 00 and the CMD column has bash and ps under it. [Video description ends] We’ve got a PID, the process ID, and then we have the TTY, the terminal from which this occurred. pts/0 is pseudo terminal 0, which is the console of the machine itself.

And so, one of the running processes of course to allow this to be possible in the first place is my shell, my bash shell. So bash shows us the command, after which at the time we issued the ps command, the ps command itself was running and it was assigned a process ID by the kernel. However, if we take a look at the man page for the ps command down below in the help, it says to see every process on the system using BSD syntax, you can do ps axu. Okay, Q for quit, ps axu. We are getting a list of all of the running processes on this machine. Let's just scroll up to see what the column headers are, of course. So, these are not only those tied to the current user login session of course.

Under the user column, [Video description begins] The column headings the host refers to are: User, PID, % CPU, % MEM, VSZ, RSS, TTY, Stat, Start, Time and Command. [Video description ends] we have the user under which the process is running. Notice that we have quite a few of them here running under the root and that's normal for system services. But as we go further down, you'll notice that there are variations on Linux user accounts that are being used for various items.

Now, of course, we’ve got the process ID or the PID column, the init process shown here on the far right in the command column for the first entry, which is /sbin/init is always spawned first by the kernel, but it's not tied to a user terminal session, is it? So, therefore, under the TTY column, we have a question mark and that's what that means.

Of course, what’s important here when we manage processes and daemons, is we can take a look at the %CPU, %MEM columns, which can be very useful if you've got some kind of a resource hog process running on your machine that seems to be consuming way too much CPU time, way too much memory beyond our normal baseline of normal activity. This will help you identify that item. However, it’s only as up-to-date as when you last ran this ps command.

And so what we can also do, is run the top command. [Video description begins] The host runs the top command and information such as the number of users, load average, tasks, running, sleeping and so on, along with a table with headers such as PID, User, PR, NI, VIRT, RES, SHR, S, % CPU, % MEM, Time+ is displayed. [Video description ends] This keeps changing every few seconds. I think the default is about 3 seconds, although we can change the delay to make it more frequent or less frequent, but it's always updating the list to show me the top running processes consuming resources.

And so in this way, if we're trying to solve a problem to find out which process is consuming much more or abnormal amounts of CPU time and memory, this would be really a great command to run because you don’t have to keep issuing the command as you would with ps. This also gives some interesting items up at the top, such as the number of tasks, in this case: 211 in total. There are a number of them in a sleeping state that are idle, they're not actually performing work right now.

If I were to press D while I’m on top, there in fact, it is 3 seconds as the default delay. We could change that, for example, to 0.5, every half second and notice the update will be much quicker. I’ll go back to the default of every 3 seconds. What I can also do when I'm on top is I can press the letter F. F stands for fields. What I can do is determine which fields I want to be displayed in the output, the fields that are currently shown, these columns across the top are shown here with an asterisk to the left.

Maybe I'm interested in the PID and the user under which [Video description begins] The host refers to the header of the previous table. Here, header options such as PID, USER, % CPU, PPID and so on are given. There are several items displayed against each header options. [Video description ends] a process is running, but maybe PR for the priority, I don't want that. I'll hit the space bar to remove it and the asterisk is removed. Plus it becomes unbolded. Same with the nice value and I in virtual memory. I'll get rid of all that. Maybe all I want to do is see a handful of items here.

I can press enter, I can press escape to get back to my top screen, it's still running, of course. And now I only have the columns across the top that perhaps I would find relevant when using top, maybe to monitor my Linux host or to troubleshoot any problems like resource hogs. I'll type Q for quit to get out of the top command and I'll clear the screen.

We talked about the ps command. There’s also a useful command called pstree. However, on some Linux distributions, you might be prompted to install it. In any case, if I take a look at the output from the pstree command, at the top, it starts with systemd. We've made multiple references to init with a process ID of 1 which is still valid, but newer Linux distributions will show it as systemd here. Under which all other processes are spawned.

For example, notice the apache2 web server is spawned under systemd, and so is cron, so is the ssh daemon. So, this can be a handy way to see if there are subordinate daemons started by daemons like ssh. But to make that output make even more sense in a hierarchy, you could issue pstree, but you could add the -p parameter. Then this is what you get: All of the subordinate processes are very, very easy to see indented underneath their parent. For example, notice all of the child processes running for the apache web server component.

The other thing to think about is the kill command. We know that when we run, for example, ps axu, we get a list of everything running. And, what's important here is of course that we take note of the process ID, which is shown here in the second column starting from the left. You can also pique the output from ps to grep if you want to be able to filter it in some way, such as maybe looking for apache.

If, for example, one of the apache processes you’ve been able to identify is not being responsive or consuming too much CPU or memory, you could take note of its process ID. In this example, let’s say we’re going to use 5614 and you could use the kill command to terminate it. Now I'm going to need to prefix that with sudo of course.

If I run sudo kill 5614, now remember, the default behavior here is it will try to shut that down gracefully so that if we go back in our history of commands here using the up arrow key and go back to our command where we grepped it, notice that process 5614 is no longer running. If we take a look at the man page for kill, notice that one of the options you can pass on the command line is a - and the signal. Now the signal lets you control how that process will be killed, whether it’s abrasively, immediately or whether it’s gracefully and giving it time to shut down and perhaps write things to disk and whatnot.

So this gives us a sense then of how we might manage Linux processes and daemons using built-in command line tools.

5. Video: Configure Linux Jobs (it_oslsys_05_enus_05)

During this video, discover how to manage Linux jobs using the bg, fg, and jobs commands.
manage Linux jobs using the bg, fg, and jobs commands
[Video description begins] Topic title: Configure Linux Jobs. Your host for this session is Dan Lachance. [Video description ends]

In Linux, we’ve talked about the fact that we can run processes in the foreground simply, for example, by typing a command such as ls. Ls itself is a process and we even saw that we can view that information with the ps or the process command. So the bash shell is shown here and the ps command as well.
But what are Linux jobs? We're going to focus on Linux jobs and what these really are. These are commands, whether they’re individual commands that we issue, or it could be the result of commands executing from within a shell script. It doesn't matter. But what it means is that we have standard Linux commands of some kind doing something, but it's running in the background.

So it could be a single command line that we forced into the background because it takes so long to run. It could be a shell script that we’ve forced into the background, maybe it’s a cron job that runs on a schedule that in turn runs things in the background. Whether it’s a command line or shell script, it doesn’t matter how you do it.

A job is something that you are forcing to run in the background because it normally does not. The way that you force something to run as a background job, as it's called in Linux, is by suffixing the command or the reference to invoking a script with an ampersand. So as an example, let’s just go ahead and use the ping command, which will continue with output on the screen until we tell it not to. But let’s say I ping, www.skillsoft.com. Whether we get replies back or not is not the point here.

The point is that we’ve got some command running, that is tying up our command prompt that's running in the foreground.

Now we didn't force it to run in the background. We didn't suffix this with an ampersand. What we can do, is we can press control z, when we do this, what we are doing is we are stopping the process and we are sending it to the background. If I type in jobs, notice that the job shows up in the background, it's job number 1, but it shows as being stopped. If I were to type fg, foreground, now I’m not going to tell it which job number. There's only one job and it's the most recent one.

Foreground without any parameters brings up the most recent job sent to the background notice. We’re back running ping www.skillsoft.com. Let’s exit that with control c. This time, what I’d like to do, is run the ping command again, except add an ampersand at the end of it.

Now notice we're still getting the output on the screen, although the other thing that we see here is that it's been sent in the background as job number 1, 6750 is the process ID. Now I'm just going to go ahead and press enter and type jobs. Now pressing enter got us our command prompt back. So what's happening here then, is that the job is now running in the background and doesn't show as stopped. Of course, we also see the actual command that is running. Now, if we were to start getting replies, it would start interrupting the foreground.

So yet again, let's bring up that previous command. But after the skillsoft.com part of that command, I'm going to redirect the output with the > to a file in the local directory let’s say called ping results.txt. The ampersand will follow that. I’ll press enter. This time we get nothing in the foreground. Of course, we can cat the ping results file and we’ll start seeing anything that might come back as a result. Again, if we type in jobs, we now have it running as job number 2.

And again, to bring it to the foreground, we could just type fg or fg 2. There’s our command. Now, that’s fine, I’ll press control c to end that. But when you have jobs that are running, so, press control c to stop that second job. Job 2 is gone. The first one is still there.

Now we know that job number 1 is running, and we want to get rid of it. One way to do that is by using the kill command and using %1, where 1 is the job number. Now, if we run the jobs command notice, the job is showing in the list, but it's showing as having been terminated.

Now let's run our ping command in the background yet again. So I'm going to use the up arrow key to go back to it and press enter. So once again, if we type in jobs, there it is running in the background. Let's use the up arrow key to go back to that command. Let's say that what we had done is we had run a command or a script, but forgot to suffix it with the ampersand to run it in the background. So of course, runs in the foreground. We know we can press control Z or control Z. It shows us a stopped job. If we type jobs, it shows up there as being stopped. So, it’s been suspended. So it’s not running right now.

But let's say not only do I want it to run in the background, I want it to actually run like right now it’s not running. It’s showing in the background list of jobs, but it stopped. What we could do, is use the background command bg. Followed by, in this case, a 2, job number 2, enter. It returns back job number 2, but what it’s done is added an ampersand at the end for us.

So now if I type jobs yet again, notice that job number 2 is now running, where previously it was suspended. So if you don't think to run something in the background immediately and then you decide you want to do something else at the command prompt, you can force it into the background quite easily with the bg command.

Now I'm going to use the up arrow key yet again to bring up our ping command where we had the ampersand at the end to send that as a background job and keep it running. Except for what’s different this time, at the beginning, I’m going to prefix it with the nohup command. N-o-h-u-p, no hang up. What this means is that we want to keep this running in the background even if we close our terminal window and open yet another one. Now, that doesn't mean that if we sign back in, we're going to see it when we type the jobs command. However, we would see it if we use the ps command.

Just to make sure we can tell the difference here, I’m going to change the output file name here, which, in essence, is changing our command line to ping_results_nohup.txt. We’re just changing the file name so there’s no functional difference in what this will do. Enter. Okay, and you get the standard message ignoring input and redirecting standard error to standard output. Okay, that’s fine.

If we type jobs, then of course we do see it listed here currently right now. There’s nohup in the file name for the output redirection. If we were to exit our terminal session and sign back in, if we issue the jobs command as expected, nothing is there. So let’s say we run ps axu and we grep for the word ping because we know that’s the command that we sent to the background. We'll ignore the second entry here, which is really just showing us that we were grepping for ping. [Video description begins] The host points to the second entry grep --color=auto ping. [Video description ends]

But notice the above command which is using ping www. skillsoft.com. It’s got its own process id. This was left running in the background [Video description begins] He points to the process ID 6855. [Video description ends] as user cblackwell because we used the no hang-up or nohup command.

So there are times when you want things that might take a really long time to run, to continue running, despite the fact that you want to sign out of a system. So this gives us a sense then of how we can manage Linux background jobs.

6. Video: Configuring Linux Daemon Startup Scripts (it_oslsys_05_enus_06)

Learn how to configure daemons startup scripts.
configure daemons startup scripts
[Video description begins] Topic title: Configuring Linux Daemon Startup Scripts. Your host for this session is Dan Lachance. [Video description ends]

In this demo, we will be configuring Linux daemon start-up scripts. Now in Linux, we know that a daemon is a background running program that stays running even if users aren't signed into a particular terminal session. And a daemon might commonly be in the form of something like a web server stack; or the background cron daemon which runs scheduled tasks, that type of thing.
What we’ll be doing here is, we’ll be taking a look at daemons and their start and kill scripts in the appropriate runlevel directories. We’ll actually take a look at the daemon startup script itself.

The first thing I'll do here at the command line in Linux is, I’ll verify that we have the apache2 web server installed. One way to do that is to run sudo service apache2 status. Well, it knows about the apache http server. However, it is currently showing as inactive. So I’ll press Q, and what I’ll do is I’ll run sudo service apache2 start. I'm just going to use the up arrow key to go back so that we can check the status now that we've told it to start at the command line.

And of course, now the web server is showing as active and running and we’ve got the date and time stamp for when that occurred, which is just a few seconds ago. Notice the references down below to /usr/sbin/and then the apache2 binary. Also, notice the reference upon the loaded line here to /lib/systemd the system controls processes on the Linux machine /system.

And then notice the reference to the file system called apache2.service. We're going to take a look at that in a moment. Also notice after that it says enabled, meaning that the apache web server is enabled to start automatically at a certain runlevel. If I type Q for quit, we can then change the directory into /lib, /systemd/system. Why? Because we want to take a look at the apache2.service file. [Video description begins] The host runs a command cblackwell @ ubuntu 2 : / lib/ systemd/ system$ ls apach* to obtain the service file. [Video description ends]

So, I’m going to go ahead and cat apache2.service, we’ll pique that to more, so it stops after the first screen full of information. Okay, so the description is the apache http server. Then we have a directive here, a keyword. It says: After=. So this means any other dependent services that should be started before this one starts. So this one, the apache http server should start after the network. target, remote-fs.target and nss-lookup.target. Okay, well, that’s interesting! So, there’s an order to these demons in terms of their start-up, which can be important.

Naturally, you won’t be able to start the apache web server until you’ve got the underlying network service running on Linux so that you can use the IP address and bind to port number 2 to make a socket. Down under the service section and the sections here are denoted of course within square brackets, we’ve got ExecStart. [Video description begins] He refers to the sections titled Unit, Service and Install. [Video description ends]

So how do we execute the start-up of this demon? /usr/sbin/ apachectl start. Okay, and at the bottom, under the install section, we've got a keyword stating WantedBy= and it says multi-user.target, which references runlevels 2, 3 and 4. In other words, when should this daemon startup? That means then if I were to do a ls of /etc/ rc3.d we've got a start script file here, S01apache2, which is actually a symlink.

If we were to do a l l of /etc/rc3.d notice that the script for apache2 is pointing to the init.d directory under /etc and apache2. That’s a script. Let’s go examine that one: change the directory to /etc/init.d and let’s cat the apache2 file here and pique that more.

Okay, so this is a script, of course, which controls whether or not the apache web server has a valid configuration and whether or not it will actually start. Okay, so there is a dependency on how these demons, in this case, we’re focusing on the apache web server, actually, fire up or stop. You can imagine what might happen if I were to issue a command like this: sudo update-rc.d apache2 disable. That looks like it’s probably going to disable the apache2 web server daemon from starting. Let’s press enter.

If I were to go back through my command history to where we ran ls of / etc/rc3.d that’s the runlevel 3 directory. Notice that we no longer have a start script for apache. Instead, we have a kill script to ensure that that daemon is not running when we are in runlevel 3. Back in our command line history, [Video description begins] The host refers to the kill command K01apache2. [Video description ends] if we change the directory once again to /lib/systemd/system and if we and if we cat the apache2.service file.

Now, if we type runlevel at the command line, it will tell us our current runlevel. Currently, our runlevel is 3. The 5 here references the previous runlevel we were in before runlevel 3. Now, even though it's not very common at the command line, you can also switch between runlevels as we know, by using sudo init and then let’s say 5 to start runlevel 5.

Now if I type runlevel it returns that we are now in runlevel 5 where previously it was runlevel 3. When you switch runlevels either this way manually or when the system starts up and fires up the default runlevel, it will read the appropriate start scripts for daemons and make sure that they are running for that given runlevel.

7. Video: Scheduling with Cron (it_oslsys_05_enus_07)

After completing this video, you will be able to use cron to schedule tasks in Linux.
use cron to schedule tasks in Linux
[Video description begins] Topic title: Scheduling with Cron. Your host for this session is Dan Lachance. [Video description ends] Let's take a few minutes to discuss cron task scheduling in Linux. What we're talking about here is using crontab files. These are tab-separated entries in files in a certain order from left to right that can be applied to individual users or it can be set up at the system level with the system crontab file.
But what is its purpose? Its purpose is to schedule commands or scripts to run on some kind of a schedule, whether it's multiple times per day or a certain time of the day or weekly or monthly. Anything along those lines can be scheduled for the system and for user crontab files. And think of the things that this might be handy for. Backups comes to mind, any type of system maintenance you want to apply to the system like checking for updates or cleaning up temporary files, the purposes are endless.

In our screenshot, we are viewing the status of the cron daemon. So cron runs in the background as a daemon and it will be checking to see what needs to be run on a minute-by-minute basis. Here the technician has issued the sudo service cron status command, where returns back that it is active and running. And normally in Linux distributions, this happens automatically. You don't have to enable cron. It's already set to go.

Now we mentioned that you have both a system crontab file and individual user crontab files for each user on the system. Let's take a look at the crontab file for the system. So the command that was issued here was sudo nano/etc/crontab. We've got a screenshot of the contents of that file. Conveniently, we have comments that explain what each of the fields from left to right mean when it comes to scheduling jobs. So the leftmost column allows us to define the minute at which something should run that's scheduled here, in the crontab file. The next column is the hour at which that should run. If we have an asterisk, it means every hour. The next item we have is the day of the month.

Again, an asterisk would mean every day of the month, whereas a 1 would mean the first day of the month. Then we have the month number. So where January is 1, February is 2 and so on. An asterisk would mean every month, then the day of the week numerically. Notice that it states that when you look at the day of the week, Sunday is day 0, Saturday is day 7. You could specify that. Or again, you can use wildcards like an asterisk, which means every day of the week. You then have the username under which the job should run. Because this is the system crontab file and it’s not tied to an individual user, we need then to specify the user account that will execute the command and that account of course have to have the appropriate privileges to carry out whatever it is the command is doing.

The next column, of course, is the actual command to be executed, whether it's just commands that we would normally enter in a shell environment, or it could be a reference to a script. Now, another thing to bear in mind is that if we wanted something to run, let’s say every 30 minutes under the minute column, we would use /30. So you can even get a little bit more detailed about the timing of when these jobs should run in that way.

So that's the system crontab file. Then we've got individual user crontabs. So when a user is logged in, they can edit their own crontab by issuing the crontab -e command. And when you specify the details in the user crontab file of when something should be scheduled to run, there is no user name column, because it will run under the user that is creating the specific user crontab.

So it's a little different from a system crontab in that way. User crontab files are normally stored under /var/spool/cron /crontabs whereas the system crontab as we know is stored under the /etc directory. We can also issue the crontab-l command to list any specific crontab jobs which have been done here. Down below we have a listing for a job that is scheduled to run. Now because this is an example of what would be inside the job list for a user crontab, notice the absence of the user name column. [Video description begins] The host points to the command 0 2 * * l tar-zcf/backups/cblackwell backup.tar.gz /home/cblackwell [Video description ends]

Now, when you're managing crontabs, the first thing to think about is how do I remove jobs. I know how to add the jobs. You can do it at the command line instead of editing the crontab file directly. Either way is valid, but you can use crontab -r that will remove the user crontab. Remember cron jobs run in the background as a result of the cron daemon which is running, but there's no terminal output.

So if the command you are issuing or the script you are executing results in output on the screen, you're going to want to redirect that to a file or to something using the > or the >> for appending to an existing file. The same goes for errors. So when you need something to run on a periodic and recurring basis, schedule it as a cron job.

8. Video: Managing Cron jobs (it_oslsys_05_enus_08)

In this video, find out how to schedule tasks in Linux using cron.
schedule tasks in Linux using cron
[Video description begins] Topic title: Managing Cron jobs. Your host for this session is Dan Lachance. [Video description ends] In this demo, I'm going to be managing cron jobs. Remember that cron is a background daemon. We can check its status with sudo service cron status and it shows as being active and running. This is a background service or daemon, that is used to run scheduled jobs.
Now the job might be a Linux command line expression or it could be a shell script and we can schedule that job to run all the way down to the minute level. So hourly, daily, weekly, monthly, whatever the need is. I'll press Q to get out of this output clear the screen. Now I’m going to run sudo nano/etc/crontab. This is the system-wide crontab file. When I say system-wide, what I mean is it's not tied to a specific user. We'll look at user crontabs afterwards. If I open up the crontab file, in it I’ve got a bunch of comments. These are prefixed with the pound symbol or the hashtag symbol that tells me from left to right what each of the columns is.

So the minute that I want something to run, is the first column on the left. Then the hour followed by the day of the month, followed by the month number and then the day of the week where 0 is Sunday and 6 would be Saturday. Because it’s the system crontab file, you’ll recall that we have to specify the user under which this should run. That's the next column. That user has to have the correct permissions to be able to run the command or read the script and execute it in order for that to run correctly.

And then, of course, we have the command to be executed, whether it's just a Linux command line expression or a reference to a shell script somewhere. Bear in mind that if the command results in output on the screen, you'll have to redirect that to a file, for example, so the output is stored somewhere.

So if I wanted to add a job here, I could just go to the bottom. Let’s say I want something to run every minute. That would be /1. I could use a tab or a space and then in the next column, specify the hour, let's say every hour. Then the day of the month, the month number, the day of the week, the user under which it should run, let's say root, [Video description begins] The host types the asterisk symbol under the hour, day of the month, month and day of the week columns. He also types in root under the user-name column. [Video description ends] and then the command. Let’s say, I’m simply going to run the ls command of against /home/cblackwell and we’ll just redirect that with the > to /home/cblackwell/filelist .txt. It’s not an extremely useful command, but all we're looking at here is the construct of how we would get that command to run.

Now, what I can also do, instead of just the single greater than sign for output redirection, depending on what your requirements are, is append to an existing file. So with the double greater than sign, I'm going to go ahead and press control X. Yes, to write that out to the system crontab file and it's done.

Now, if I type print working directory, pwd, we’re in home cblackwell. If I type ls, we don’t yet have our filelist file that was created because we have to wait for at least one minute to pass by. And if I wait, within a minute I should see the filelist file. If I cat filelist.txt, it simply gives me a list of the files in the current directory, user home directory for cblackwell. [Video description begins] The host runs the cat filelist.txt command and several jobs appear on the screen. These include filelist.txt, mbishop_xls, nohup.out and so on. [Video description ends] If I wait at least one more minute, I will notice that the output will have doubled because it keeps appending to it. It's running every minute. We had */1 which means every minute.

Now remember that the purpose of scheduling jobs is to do something automatically, normally on a recurring basis, like some kind of cleanup task to clean up temporary files or maybe to check network connectivity or to start and stop daemons on a scheduled basis if you have that requirement. So notice if I cat the filelist txt file yet again, it has been appended automatically because that job is running every minute in the background. Okay,

I'm going to clear the screen. Let's work on the user crontab file. If I type ID, I’m logged in as user cblackwell. So when I type crontab-e to edit the crontab, I’m editing it for user cblackwell. So then it says there’s no crontab for that person, at least not yet. Using an empty one, select an editor. I’m going to type in the number 1, so I can use the nano text editor. That's just a preference. [Video description begins] A page of code titled GNU Nano 6.2 is shown. It contains a page of code. Underneath there are several tabs including Help, Exit, Write Out, Read File, etc. [Video description ends]

Now remember that with a user crontab one of the difference is that we do not have a user name column under which the scheduled, task or command should run because it knows it should run as user cblackwell in this particular case. [Video description begins] He points to the column m h dom mon dow command [Video description ends]

So from left to right, it would be minute. So maybe I’ll put 56. I know that’s just a few minutes from now and I know it’s going to be 7: 56 in a few minutes. I’ll put in 7 and for the day of the month put in an *. Same with the month number. You can put at least one space to separate these things, that’s all you need.

You can put more, you can tab separate it. But maybe what I'll do now is echo the text "User Crontab Test" and we will append that to a file home/cblackwell called usercrontest.txt. Okay, I’ll control x to write that out and I will save it. So now if we do an ls of /var /spool/cron and then take it one step further into cron tabs, of course, we’ll have to put sudo in front of it, notice we've got a cblackwell crontab file.

A user can type crontab-l to list whatever is in their crontab. And notice down below we've got our little echo command that's going to write to that file or append to that file. If I type date to get the date and time, notice it’s 7: 55 A.M. so it’s not quite 7: 56 but we’ll just wait a few moments, at which point when we do a ls, we will have the user crontab file that will have been created.

So let's just hang out for a moment. So if I type ls notice the presence now of the usercrontest file. And of course, if I were to cat that file it simply shows the User Crontab Test. So tomorrow at 7:56 A.M., it will append the same thing to that file. Of course, these are silly examples in that they aren't really doing anything useful. But what we're trying to understand is the underlying infrastructure that makes this work. If we can understand how to force something to run on a scheduled basis, then the sky's the limit. You could have a script or a command that performs any task that you need to occur at a certain time.

9. Video: Linux Logging Facilities (it_oslsys_05_enus_09)

Upon completion of this video, you will be able to describe how logging works in Linux.
describe how logging works in Linux
[Video description begins] Topic title: Linux Logging Facilities. Your host for this session is Dan Lachance. [Video description ends]

One important part of managing a Linux system is to monitor its performance and the behavior of the services running on it. And that means that we should be familiar with Linux logging facilities. You'll find that most Linux logs across many distributions are stored in or under /var/log. Specifically with Ubuntu Linux, the system log file is called syslog and it exists as a text file under /var /log. You can also filter log data because the nature of logs is that you'll have a lot of items that get logged into files.
And so to weed out the noise, so to speak, to find out what you really need, you might need to filter out log contents. There are many ways to do this. One way is to use a regular expression such as with the sed command. So sed-e for expression and in single quotes, we have /cron/ that’s what we’re looking for. The d within that expression means we want to delete references of cron and then we tell it the subject or the source of the data, which is /var/log/syslog.

Of course, there are many other ways that we could do the same thing. But the point is that we should be able to filter out log content at the command line to be more efficient and to save time. Pictured on the screen, we have the result or the output of the last log command. This is an important command in Linux because it shows user accounts on the Linux host and when they last logged in.

Notice in our screenshot, most of the user accounts shown here have never logged in. However, our highlighted entry here for user cblackwell logged in from pts/1. That’s pseudo terminal /1. So, an ssh session is normally what that means. We have the client IP address from which that occurred in this case: 192.168.2.11 And of course, we have the date and the timestamp.

So one part of managing logs in Linux, [Video description begins] The highlighted entry on the screenshot displays the following information: cblackwell pts/1 192.168.2.11 Sun Jun 12:02:21 +0000 2023. [Video description ends] and reviewing them, is determining who logged in when. We now have a screenshot of the result or the output of the d message command, spelt: dmesg. The d message command is designed to show you kernel log messages. So messages from the Linux kernel itself. So some of it's pretty internal and cryptic, but often you'll find it's related to the discovery of devices and applying drivers in that type of thing.

So here we have a lot of references, for example, to new USB devices being found on the Linux host. This can be useful if you're troubleshooting Linux kernel errors and not just limited to working with devices and their drivers. But the other important aspect of logging in Linux is log rotation. What does this mean? Well, the first thing to bear in mind is that when we talk about logs in Linux, and the more software packages you have installed, the more logs you will have.

Of course, the busier the Linux host, such as a Linux server, the more log entries you will have. So logs will consume space over time. So you can’t keep all log entries in all log files forever. There's just not enough space.

And that's where the Linux log rotate tool comes in. This is a command line tool, but it also is something that will automatically rotate logs. Now rotating logs means that we can configure things like compression for older logs, and tell it to keep only a certain number of logs. While we have the most recent log as being active and being written to.

So log rotation is all about rotating out what's the current log to be the previous log and determine how many are kept, whether they're compressed and so on. Bear in mind to remain compliant with relevant laws or regulations, you might have to keep logs for a certain period of time and you might even keep them on a centralized logging host that gets backed up.

The way that Linux log rotation works is that in /etc we’ve got a file called logrotate.conf. Among other entries in it, there is a statement that says: include/etc/logrotate.d which is a subdirectory. And so within that logrotate.d subdirectory, you can have individual log rotation configuration files for different types of logs that you want to control that determine how many copies of logs should be kept, whether the log should be compressed, and of course a reference to what it is that you want to log, which log file?

So here we have an example of one of those log rotation config files in the /etc/logrotate.d directory. So if we were to cat that file, in this case, we’re catting the apache2.conf file in the logrotate.d location. So we’ve got an open curly brace, then we have the missingok statement. This just means that if we don't have the log file for apache, then don’t worry about it. Then we have daily, which means that we want to rotate log files in this case for apache, every single day.

Rotate 3 means we want to keep only three copies of older logs or rotated logs. Notifempty means don’t bother rotating logs, if the current log file is empty, then we can choose to compress log files. Now this would be compressing older log files, not the current ones, and the default is to compress it using gzip And then we have a closing curly brace.

Now, if we wanted to, we could force Linux log rotation checking immediately at the command line by typing logrotate-d and then point to the respective log rotation config file. You could also control when exactly this runs by automating it with the cron job, but the default is, it will run every day to check to see if any Linux log rotation should take place.

10. Video: Viewing Linux Logs (it_oslsys_05_enus_10)

Discover how to view the contents of various Linux logs.
view the contents of various Linux logs
[Video description begins] Topic title: Viewing Linux Logs. Your host for this session is Dan Lachance . [Video description ends] In this demonstration, we’ll be taking a look at some standard Linux log files. It’s important to be able to know where log files are, so you can quickly locate any messages that might be relevant for troubleshooting or for security threat hunting or to check on the performance of some kind of a service in Linux.
The first thing we’ll do here is change the directory to /var/log. According to the Linux file system hierarchy standard, the HFS, this is where log files should reside. And in most cases across pretty much all Linux distributions, this is true. You'll have the log files for just about anything you might choose to install, in addition to standard log files somewhere under var log.

If I type ls, notice that we have a number of log files like auth.log, we have the dmesg file, the faillog, kern.log, the kernel.log, lastlog, syslog and so on. But notice we also have subdirectories for various packages like the apache2 web server. There’s a separate sub-directory for it, so if I were to ls the apache2 subdirectory, itself has a number of logs for the web server. Like a standard access.log file, an error.log file.

And if you've configured virtual hosts for your web server stack, you have an other_vhosts_access.log file. If you're responsible for managing a given service like an apache web server on Linux, you need to make sure you know where the log files are. Notice that we also have what appear to be copies of older log files that have a .gz or gzip compressed file extension. For example, [Video description begins] The host points to the following entries: dmesg.1.gz , dmesg.2.gz ,dmesg.3.gz [Video description ends] with dmesg log rotation has automatically kept older versions of the dmesg log, whether it’s when they reach a certain size, it just depends on how log rotation is configured for that.

Let’s take a look, for example, at the authorization log, auth.log. I’ll clear the screen and I’ll cat auth.log. When you’re viewing log entries of course, what’s crucial, is that the date and time on the system be correct because log entries are date and time-stamped. And that can be very important in determining when exactly something occurred, whether it's for security, troubleshooting or performance reasons.

So here we have a number of entries here showing that sessions were opened and closed for various users, such as user root. If I were to cat the syslog file, the main system log file, here we have a log of everything that was happening, such as the issuing of commands like the ls command, being issued for user root.

Now notice that we have multiple repetitions of running the exact same command. And if you look at the date and time stamps, because we said that was very important, it looks like it's approximately every minute. What this would be telling us is that there is a cron job, it would appear, that is running the ls command and redirecting the output, actually appending it to a file.

If I were to run sudo nano/etc/crontab and go to the bottom, indeed we do have an entry here for a scheduled job that’s set to run every minute, / */1. I'm going to comment that out and I'll go ahead and write that out to the file. [Video description begins] He enters a # before */1 [Video description ends] So this is handy, we can determine if things are running that may be perhaps should not be. Important commands that you might be interested in here include the head command. If I were to run the head command against syslog, by default, it shows me the first ten lines in that file.

You can specify the lines if you really want to the number of lines. Or we could display the last ten lines with the tail command. Tail syslog shows me the ten most recent log entries here. And notice that one of the most recent entries is related to the reloading of the /etc/crontab file since we just made a change. We commented out that job. Now we can also of course filter logs. If I were to cat syslog I could pique it, to grep-i, so, case insensitive. And maybe I’m looking for apache2.

So here we've got all the log entries that are related to that. But bear in mind that some services like the apache2 web server, have their own log files in their own log directory. Which would have more detailed log messages for the running of that particular service. So if I were to change the directory, let’s say into apache2 and cat, let’s say the access log, well, there’s been no access to that server.

What about the error log? Well, we have a few entries here that are date and time stamps related to that. And if I've configured virtual hosts, then I could view the other virtual hosts access log to look for activity. Back here in /var/ log, if I do a ls, it’s also important to take note of the d package.log, dpkg. Which of course is related to software packages on the system.

So if I were to cat d package dpkg.log, we’ve got entries related to doing things like installing software whether that was successful. And of course, we could also grep that looking for anything specific.

For example, in apache2, here we’ve got some details about installing and unpacking all the files related to the apache2 service. You can also run the sudo dmesg command to view the kernel log. And again, we could grep it or head or tail it, depending on what we want to do. Of course, what you can also do is if you pique the result of, let’s say, sudo dmesg to more, which stops after the first screenful, you can type in a front / which shows up in the bottom left and type in what you want to search for, let's say USB.

It'll find occurrences of USB and I can press the letter N to keep going to the next occurrence. So that can also be handy when you need to sift through something in a log file with built-in command line utilities. If we type the last log, we'll get information about when various user accounts were last logged in.

And of course, the details related to that. If we were to type in journalctl and press enter, here again, we get some more kernel output that gets logged, that can be handy if you're troubleshooting some kind of hardware-based issues. So if you're not already familiar with where log files are, and what the log files are called, on your Linux system or systems that you're responsible for, it's important to know this information because it will definitely serve you well in maintaining the system and troubleshooting it quickly.

11. Video: Managing Linux Log Rotation (it_oslsys_05_enus_11)

During this video, you will learn how to manage Linux log rotation using logrotate.
manage Linux log rotation using logrotate
[Video description begins] Topic title: Managing Linux Log Rotation. Your host for this session is Dan Lachance. [Video description ends]

In this demo, I will be configuring Linux log rotation. We’ve discussed log rotation briefly. In that, we have a sense that we know that we can't keep log files forever. Depending on what you've got installed on the Linux host and how much activity there is, we'll determine how quickly log entries get added to log files and in turn how much disk space gets used up.
So what we can do is, configure log rotation to determine when log files should be rotated. In other words, when the current log file should be saved as a backup and starting a new log file. Perhaps even compressing older backup files and how long to keep them or how many copies of them that should be retained. And you might have organizational policies that dictate how long logs need to be kept, which might be influenced by laws or regulations.

The first thing I’m going to do here is change the directory to /var/log. If I clear the screen and do a ls here, we've got a number of log files such as the main syslog file, but we've also got subdirectories for log files like the apache2 web server package. And notice for the dmesg log file, the kernel log file, we’ve got a number of rotated or backup copies such as dmesg.1.gz. It’s been compressed using gzip that can be configured in your log rotation config file, in this case for dmesg.

Of course, we can type l l to get a long listing of all the file metadata, including things like the sizes of the files. [Video description begins] The host points to a column mentioning sizes of several files in numbers such as 4096, 145956, 26974,27279 and so on. [Video description ends] Let’s change the directory to /etc/logrotate.d and clear the screen and type ls. For example, we've got a config file here for the apache2 web server whose logs are stored by default under /var /log/apache2.

We’ve got an access log for access to the web server and an error log and then a virtual hosts access log. If we want to configure how log rotation works for apache2, then here in the etc/logrotate.d directory, we would simply use the text editor of our choice to open up that file. [Video description begins] He uses the command sudo nano apache2. [Video description ends]

Now, if the file doesn't already exist, we can go ahead and create it. So what's happening here, in the log rotation configuration file for this particular service, is we have a reference to the log file or log files that should be checked. Here it’s /var/log/apache2/*. log. So it applies to all of the log files we just mentioned, the access log, the error log, and the virtual host log for the apache web server stack.

After that reference, we have an open curly brace and then we have a number of directives to control log rotation. And then we have a number of directives controlling log rotation, such as checking daily, missingok, which is okay if there’s not a current log file. Rotate 14, so keep 14 copies, compress which means compress with gzip. Don't bother log rotating if it's not empty. Also, there's a create statement here that's creating the rotated logs, the backup logs with certain permissions, 640. And then the only user being set as root and the only group being set as adm.

So the 6 of course, means read and write 4 + 2, for the owning user. The 4 here means just read for the owning group adm, and 0 means no one else has permissions to rotated logs. You can also specify if you want something to execute certain commands or a script before log rotation occurs for this. Or after, there’s a pre and post-rotate set of directives. [Video description begins] The host refers to prerotate commands: if [-d /etc/logrotate. d/httpd-prerotate ] ; then run-parts /etc/logrotate . d/httpd-prerotate fi endscript and postrotate commands: if pgrep -f ^/usr/sbin/apache2 > / dev/ null; then invoke-rc.d apache2 reload 2>&1 | logger -t apache2. logrotate fi endscript. [Video description ends] And then it would close off with the closing curly brace.

So I’m just going to exit out of that file and I’ll do a ls. If we were to cat, let’s say the dpkg configuration file for log rotation, which is related to software packages on the system, it's got the same type of structure.

The first reference here is to the log or logs it applies. The log rotation applies. In this case, it’s just the dpkg.log file, the same syntax, [Video description begins] The host points to the command: /var/log/dpkg.log. [Video description ends] open curly brace and the closing curly brace at the bottom and the directives in between. [Video description begins] He refers to the directives including monthly, rotate 12, compress, missingok and so on. [Video description ends]

Now how does it know to look at the files in log rotate.d? If we go one directory level back, so that means if we’re in the /etc directory. In here, we’ve got a file called logrotate.conf. This is the global log rotate file. But what's interesting is as we go towards the bottom, notice the include statement to include config files and /etc/logrotate.d. So that’s how it knows to go into that directory and to look for those files.

So what the files are called in there really doesn't matter because they're all going to be checked anyhow. It's just a way to keep things a little separated and clean as opposed to having all of the log rotation statements in this global logrotate.conf file. Notice you can also at the command line issue the log rotate command on demand, we can specify a -d and point it to a specific configuration file like /etc/logrotate.d/ apache2.conf. Of course, if you really want to fine-tune and control how often this runs, you could create a cron job for it as well.

So you could do the same type of thing against any of the config files such as dpkg.conf in that location. So that's how we would start to manage log rotation in a Linux environment.

12. Video: Configuring Linux Log Forwarding With rsyslog (it_oslsys_05_enus_12)

In this video, discover how to configure centralized log collection with rsyslog.
configure centralized log collection with rsyslog
[Video description begins] Topic title: Configuring Linux Log Forwarding With rsyslog. Your host for this session is Dan Lachance. [Video description ends]

Okay, we’ve spent some time so far discussing various Linux log files, the entries within them, how to filter them, and also how to configure log rotate. But what we can also do is we can forward some or all log entries for various types of log files to a centralized logging host elsewhere on the network. In a larger enterprise, this scales well, because instead of having to monitor logs on a multitude of servers, you can monitor logs on one centralized server that collects the logs from that multitude of servers.
So how do we do this? Well, let's start here on our centralized logging server. I’m going to begin by running sudo service rsyslog status. What we’re doing is checking the rsyslog daemon to ensure that it’s active and running as this is what is going to be used for our log forwarding on the server as well as for clients that send their log information to this host. You can even configure some types of network appliances like wireless routers to forward their logs to a syslog service running in Linux. So it will vary from device to device, but some of them will support it even outside of a Linux operating system that you install.

If I do a ls of /etc/rsyslog.d so that’s a sub-directory. Notice here that we’ve got a couple of config files. I’m interested in one here for the default configuration. If I were to cat these /etc/rsyslog.d/50-default.conf file, what it's doing is specifying the various Linux facilities, whether it's for authorization, whether it's for cron, whether it's for the kernel, we can determine which types of messages. So kernel.* means all types of messages, not just warnings, for example. We can determine where that will be written to, such as to /var/log/kern.log. That’s on the local host. Okay. But what I want to do is run sudo nano because I want to edit these, /etc/rsyslog.conf file.

One of the first things I want to do here is determine if I want to allow syslog forwarding over UDP or TCP. Assuming I want that over UDP, I would make sure I uncomment the module and the input lines related to imudp. Notice the default listening port here will be 514. [Video description begins] The host removes the hashtag symbol that was placed before the module and input lines related to imudp. [Video description ends] That's commonly used for log forwarding in Linux. [Video description begins] He points to the listening port number 514 in input ( type="imudp port ="514" ). [Video description ends]

Now I'm going to go to the very bottom and add a couple of lines. The first of which will be *.*. This means, all facilities, so kernel, mail and so on. And the second asterisk is all types of messages, whether they're warnings and so on. I want all messages for everything. Then I’ll add a space ? to be put into a local folder called RemoteLogs.

Then after that, I’ll add another line with an & and a ~. Now what I'm also going to add before the remote logs line here is a template directive. $template RemoteLogs, “/var/log/%HOSTNAME% /Remotelog.log”. What does this mean?

Well, if I've got numerous other clients, we'll call them that will be configured to forward their logs to this centralized logging host. I want to create a sub-directory unique to that hostname like client 1, client 2, client 3. And within those unique subdirectories, I want the log from that client device to be called Remotelog.log. Okay, so that’s the reference down below then to ?RemoteLogs.

I’m going to press control x and write that file out to the rsyslog.conf file. I’m also going to run sudo ufw for an uncomplicated firewall, assuming I'm using that software firewall solution on this host to allow 514 as a port number / for udp. Okay, it says rules were updated. Well, that’s good. Then I’m going to run sudo service rsyslog restart to re-read the new configuration and that's it for the server-side config.

Let's go to a client. I'm calling it a client. It could also be another server, but I'm going to call it a client device. Let's go to it and configure it to forward its log entries to this host. The only thing I’m going to do here first is type ip a, so that we know the IP address of this central logging server. It's 192.168.2. 42. Okay, so I’m using an Ubuntu desktop. Machine as the client, [Video description begins] The window displays an ubuntu desktop titled:cblackwell@ubuntudesktop1:/. The username cblackwell@ ubuntudesktop1:/$ is displayed on the screen. [Video description ends] but again, it doesn’t have to be a client OS. It can just be another server running some variation of Unix or Linux. And what I’m going to do here, is I’m going to run sudo nano / etc/rsyslog.conf, the same file that we modified on the server.

So at the bottom, I’ll add a new line. *. *. So all types of Linux facilities and types of log messages on this Linux desktop, I want to forward that to our logging server. So, after a space, I’ll put @, an @ symbol, 192.168.2. 42. That’s the IP of our centralized Linux logging host, : 514. Remember it’s listening on port 514. So I’ll close that and save it.

Then I’ll run sudo service rsyslog restart here on the client, just like we did on the server. And I can test this by running sudo logger so I can force a log message using the Linux logger command. And I'm going to send a message to the log on this host, which should be forwarded to our central server and it will say "Testing log forwarding - does it work?" I’ll press enter.

Back here on the server in the /var/log directory, if I type ls, notice that I’ve got not only a sub-directory for the local server but also for ubuntudesktop1. If we change the directory into ubuntudesktop1 and do a ls, there’s our Remotelog file and if we cat that file, we’ve got all kinds of log entries including if I scroll back up far enough, our forced message testing log forwarding- does it work?

13. Video: Course Summary (it_oslsys_05_enus_13)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary. Your host for this session is Dan Lachance. [Video description ends]

So, in this course, we’ve examined how to manage Linux processes, daemons, scheduled tasks and logging. We did this by exploring how to manage Linux processes and daemons as well as Linux startup and shutdown.
We configured Linux jobs and daemon startup scripts. We worked with scheduling and we managed cron jobs. We discussed Linux logging facilities, we viewed logs and we managed log rotation and configured log collection centrally using rsyslog.

In our next course, we'll move on to manage various network services such as DHCP, DNS, NTP, SSH, and also we’ll talk about how to transfer files using SCP and SFTP.

© 2024 Skillsoft Ireland Limited - All rights reserved.