CompTIA Linux+: File Systems & Permissions Management
Managing Linux file system permissions is crucial for proper IT security governance for legal, contractual, and regulatory compliance. Partial or entire Linux file systems can be compressed and archived for retention or backup purposes. Begin this course by discovering how standard Linux file system permissions work in relation to file system object owners, groups, and others. Then use standard Linux command line tools to manage Linux file system permissions. Next, explore how extended access control lists (ACLs) for file system permissions allow flexibility by granting multiple groups different permissions to the same file system resources. Finally, you will manage extended ACL permissions and work with Linux file system compression and archiving. This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_03_enus_01)

    2. Video: Standard Linux File System Permissions (it_oslsys_03_enus_02)

    3. Video: Managing Standard Linux File System Permissions (it_oslsys_03_enus_03)

    4. Video: Extended ACL File System Permissions (it_oslsys_03_enus_04)

    5. Video: Managing Extended ACL Linux File System Permissions (it_oslsys_03_enus_05)

    6. Video: Linux File Compression and Archiving Tools (it_oslsys_03_enus_06)

    7. Video: Managing Linux Compression and Archiving (it_oslsys_03_enus_07)

    8. Video: Course Summary (it_oslsys_03_enus_08)

1. Video: Course Overview (it_oslsys_03_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance. [Video description ends]
Hi, I'm Dan Lachance. Managing Linux file system permissions is crucial. Proper IT security governance for legal, contractual, and regulatory compliance. Partial or entire Linux file systems can be compressed and archived for retention or backup purposes. And so in this course, I'll start by discussing how standard Linux file system permissions work in relation to file system object owners, groups, and others.

I will then use standard Linux command line tools to manage Linux file system permissions. Next, I will discuss how extended ACLs for the file system permissions can allow flexibility in the sense of granting multiple groups different permissions to the same file system resources. And lastly, I will manage extended ACL permissions and work with Linux file system compression and archiving. This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: Standard Linux File System Permissions (it_oslsys_03_enus_02)

After completing this video, you will be able to recognize how to use Linux file system security commands such as chmod, chgrp, and chown.
recognize how to use Linux file system security commands such as chmod, chgrp, and chown
[Video description begins] Topic title: Standard Linux File System Permissions. Your host for this session is Dan Lachance. [Video description ends]
Let's talk about Linux filesystem permissions. The first thing we want to do here is discuss the fact that this of course is used to control access to files and directories on Linux filesystems. It also allows us to adhere to some security concepts like the principle of least privilege, whereby we only grant the required permissions to perform a given task and no more.

For example, we don't want to allow users to log in with the root credentials just to do basic filesystem management on a Linux host. Now, in order to manage Linux filesystem permissions, we have to take a look at a few command line utilities, notably the chmod or change mode command. But first let's talk about the standard permissions available on Linux filesystems.

They are read, which has a numeric value of 4. Write, which has a numeric value of 2, and execute, which has a numeric value of 1. You'll see why the numbers are important. For a given file for example, if you have read, write, and execute permissions numerically, that would equal 7, 4 + 2 + 1.

Anyways, you can set these permissions using GUI tools if you have a GUI desktop on your Linux machine or you can always use the change mode or chmod command at the command line which is standard in all Linux distributions. Let's take a look at Linux filesystem permissions on a Linux machine. Now we can do this by issuing the ls -l command, long listing. If you don't use the -l, if you just type in ls, you won't see the permission sets.

We're looking at the permission sets here in the left first column in the output of ls -l. Now the permissions from the left to the right would be for the owning user. Now you'll notice that some of these start with a d, which means it's a directory, but after that you'll have a variation of read, write, or execute. Those are the permissions for the owning user of that file or directory. The owning user is shown in column three, in this case it's user root. So if we pick the first file in the output here, which is named adduser.conf, the root user has rw.

They have read and write. But what about the next permission set for that file, in our screenshot only shows r, read, that's for the owning group shown in column four. So there is also a group by the name of root. Whoever is a member of it would only have read access to adduser.conf.

The last set of permissions again for that same file only showing a letter r for read is for everyone else. So anyone other than the root user and anyone other than a member of the root group, they would be able to read adduser.conf. Now when new files are created or copied to a Linux filesystem, the default permissions that are assigned whether it's a file or a directory, are controlled by something in Linux called the umask.

Now the default umask is 0002, so if we were to create a new file for example, the new permissions would be rw-rw-r. So, read/write for the owner, read/write for the owning group, and read for everybody else. Now the umask is used to take away permissions. The Linux kernel wants to assign default file permissions for new files of read and write. Now remember, read has a value of 4, write has a value of 2. 4 + 2 is 6. Now let's forget the leading 0 in the umask. We'll talk about special bits later.

So really, we're talking about 002. So the first 0 is for the owning user, the next 0 is for the owning group, and the 2 is for other. Assuming that the Linux kernel wants to assign a 6 read and write, 6 -0 for the owning group leaves us with 6. So rw, read and write for the owning group. But 6-2 leaves us with 4. Well, we know that 4 is the numeric value for read, and that's why these are the default file permissions.

You can modify the umask, but we're just discussing here what the default is and why it is that way. We've mentioned that we can use the chmod command to modify and manage permissions. This stands for change mode and you might for example use the chmod command followed by some numbers and then the subject, the file or the directory you want the permissions applied to. So here we have chmod 740 file1.txt.

Well, I understand chmod is for permissions and I understand the file name. But what's the 740? Well, remember the numeric values for read, write, and execute. Read is 4, write is 2, execute is 1. If you have all of those permissions, that's 7, 4 + 2 + 1. Well, 7 for who, for the owning user. The 4 in our example means that only the read permission is being granted. Who is that for? That's for the owning group. And the 0 means no permissions. You guessed it for everybody else.

Now instead of using chmod with the numeric values, you can also use letters, for example I could use chmod u=rwx, that means the owning user gets read, write, execute, I'm setting it, the group or g is being added the read permission, so any permissions they have already such as execute would be retained and that would apply to file1.txt.

So, that would be another way you might use the chmod command. In another example, we've got chmod 755 /budgets, so budgets is a subdirectory slash -R. So we're setting read, write, execute, or 7 for the owning user as we know, read and execute 4 + 1 is 5 for the owning group and everybody else would also get read and execute, a value of 5.

Now that would occur for the budget subdirectory and everything within it because the -R means recursive. So in other words, you don't need to set filesystem permissions solely for individual files one at a time. This is an important concept. If you have a GUI desktop environment in Linux, of course, you can go into the GUI and set file permissions here. [Video description begins] A slide appears with the heading Filesystem Permissions Using the GUI. It displays a file called file1.txt Properties. It contains the following sections: Basic, Permissions, and Open With. The Permissions section contains the following fields: Owner, Access, Group, Access, Others Access, Execute, and Security context. [Video description ends]

The properties of a file called file1.txt have been popped up on the screen and the Permissions tab at the top has been selected, where the Owner here shows the word Me, whoever you're signed in has read and write, the Group, that would be the owning group is listed here as cblackwell has Read-only and then you can also enable Others. You can determine what the execute permissions are down at the bottom, so you can set it using the GUI and the GUI will vary slightly from one Linux distribution to the other.

3. Video: Managing Standard Linux File System Permissions (it_oslsys_03_enus_03)

Find out how to manage standard Linux file system permissions using common Linux OS commands.
manage standard Linux file system permissions using common Linux OS commands
[Video description begins] Topic title: Managing Standard Linux File System Permissions. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I will be managing standard Linux file system permissions. Managing file system permissions is important to understand at the command line level. You can manage file system permissions using the GUI, for example here in Ubuntu Desktop. And it doesn't have to be Ubuntu, it could be any Linux distro with a GUI environment installed on it.

But if I were to go into my Files icon on the left. And again, the specific area you would click, the way the GUI would look, it will vary from one desktop GUI environment to another, but the concepts remain the same.

[Video description begins] A Homepage appears. It contains the icon bar on the left. It contains a search bar on the top. The left pane contains the following folders: Recent, Starred, Home, Documents, Downloads, Pictures, Videos, Trash. CDROM, Floppy Disk, Other Locations, and so on. The main pane displays the following folders: Desktop, Documents, Downloads, Music, Pictures, Public, snap, Templates, Videos, and file1.txt. [Video description ends]

If I were to open, let's say, Documents, currently, we have nothing in it. Let's create a sample document. So, maybe on the left, I'll go into LibreOffice Writer. I'll just type in some sample text. This is a sample document.

And I'll Save it in my local Documents folder, which of course, is in my Home directory. I'll call it SampleDocument1, I'll click Save. So, now in the Documents folder we've got SampleDocument1. I can right-click on a document or a directory for that matter here in the GUI, I can go to Properties and from here I can set Permissions. 

[Video description begins] A drop-down appears underneath the SampleDocument1.odt. It contains the following options: Open With LibreOffice Writer, Open With Other Application, Cut, Copy, Move to, Copy to, Move to Trash, Rename, Compress, Send to, Star, and Properties. [Video description ends]

[Video description begins] A dialog box appears with the heading SampleDocument1.odt Properties. It contains the following sections: Basic, Permissions, and Open With. The Basic section contains the following fields: Name, Type, Size, Parent folder, Accessed, Modified, and Created. [Video description ends] The Owner is showing as Me, my current signed-in user where I could determine what access is allowed, whether it's Read-only or Read and write. Because remember, there are three sets of standard Linux file system permissions.

There's the owning user, there's the owning Group, which we can change from the drop-down list and set permissions for members of that group. And then there's Others, everybody else. Well, we could set the Access to None, Read-only, Read and write, and we can also determine if we want to Allow execute permissions. Now that's using the GUI.

[Video description begins] The Permissions section contains the following fields: Owner, Access, Group, Access, Others, Access, Execute, and Security context. [Video description ends]

Let's go back to the command line.

Back here at the command line, if I do an ls in the user's home directory, there's nothing here. Now this is on a different machine. This is not a desktop GUI Ubuntu Linux installation, rather it's a server installation. So, here I'm going to make a directory and I will call it budgets, and I will change directory into budgets and I will create a file, let's say using the touch command called budget1.txt. If I clear the screen and do an ls, there's budget1.txt.

[Video description begins] A terminal window appears with the heading: cblackwell@ubuntuserver1:~. The following command is added: mkdir budgets. [Video description ends]

[Video description begins] The command reads: cd budgets. [Video description ends] 

[Video description begins] The command reads: touch budget1.txt. [Video description ends]

The first thing about permissions is what are the defaults? We haven't set it yet, we just created a file.

If I run ls -l a long listing for budget1.txt, we've got read and write shown here for the owning user, read and write shown for the owning group, and only read for everyone else.

[Video description begins] The following command are added. Line 1 reads: ls. Line 2 reads: ls -l. [Video description ends]

If I type umask, I get 0002. Well, let's forget about the leading 0, let's think about the 002. The Linux kernel wants to assign read and write permissions to everything by default.

So, that's r and w, which is a value of 6 because read is 4, w is 2. So, the second 0 here applies to the owning user. In other words, which permissions do we want to take away? 0 OK, so then read and write is applicable for the owning user. The next 0 after that same thing, read and write is applicable then by default from the owning group. But then we have a 2. We're taking away the 2. Well, we know that read is 4, write is 2, so we're taking away the write permission that the kernel assigns by default, which leaves us only with read.

That's where the default permissions kick in. But let's change it. So, let's say we want to run change mode chmod 740 budget1.txt.

[Video description begins] The command reads: chmod 740 budget1.txt. [Video description ends]

The 7 would be 4 + 2 + 1. That's read, write, and execute for the owning user shown above. The 4 means we want to have read for the owning group, and the 0 means no permissions for other.

If we were to apply that by pressing Enter and then do an ls -l or you can just use the ll command, it's another way to do that. For budget1.txt notice that we've got read, write, execute which is our 7, we've got read which is our 4, and then we've got 0 for everyone else because it's executable in Ubuntu Linux, it shows up green. We can also set permissions using this type of syntax.

Let's say chmod u=rw, g=rw, and maybe o+r. Notice we can use equals to overwrite the current setting. We can also use the + and - to add/or remove individual permissions. Then of course, we specify the subject, in this case, budget1.txt.

[Video description begins] The command reads:chmod u=rw, g =rw, o+r budget1.txt. [Video description ends]

If we do a long listing, now the user has read and write, same with the owning group read and write, and other has read.

I'm going to use the sudo groupadd command to add a group called eastadmins, so I could use the sudo command chgrp for the eastadmins group applied to let's say budget1.txt. 

[Video description begins] The command now reads: sudo groupadd eastadmins. [Video description ends]

[Video description begins] The command reads: sudo chgrp eastadmins budget1.txt. [Video description ends]

I've changed the group. If I do a long listing, notice that for budget1 eastdmins is now shown as the owning group. Therefore, the permissions for the owning group, which in this case are read and write apply to whoever is a member of eastadmins.

Let's say I were to run sudo useradd mbishop. And maybe I'll run sudo usermod mbishop -g eastadmins to add them to that group. Now mbishop would have read and write to the budget1.txt file. Now we can also change user ownership.

[Video description begins] The command reads: sudo useradd mbishop. [Video description ends]

[Video description begins] The command reads: sudo usermod mbishop -g eastadmins. [Video description ends] 

Let's add an additional user here, sudo useradd lbrenner. I could then use the sudo change owner, chown lbrenner for the file, let's say budget1.txt. 

[Video description begins] The command reads: sudo useradd lbrenner. [Video description ends]

[Video description begins] The command reads: sudo chown lbrenner budget1.txt. [Video description ends]

If I do a long listing, notice that lbrenner is now the owner of budget1.txt. And so of course, user lbrenner will now enjoy the permissions assigned for whoever the owner is, which in this case works out to be read and write.

4. Video: Extended ACL File System Permissions (it_oslsys_03_enus_04)

Upon completion of this video, you will be able to recall how extended access control list (ACL) file system permissions work in Linux.
recall how extended access control list (ACL) file system permissions work in Linux
[Video description begins] Topic title: Extended ACL File System Permissions. Your host for this session is Dan Lachance. [Video description ends]
Besides standard Linux filesystem permissions, we can also choose to work with extended access control lists for filesystem permissions. What does this do? Well, it allows filesystem permissions for the owning user, the owning group, and other. Well, OK, but we can already do that with standard filesystem permissions. Well, ACLs are interesting because you can also then set permissions for different individual users and groups.

Standard Linux filesystem permissions allow you to specify one user, one group, and everybody else, that's it. But that's not the limitation when we work with ACLs. So, that's where it can be useful to assign different permission sets to different groups and different users for the same files and directories.

So, this allows you to have more flexibility, you have to plan out your filesystem permissions. Which users and groups will need permissions and what permissions will they need to given files and directories such as read and write to execute scripts in a specific subdirectory where some group members can execute the scripts, but perhaps other group members cannot and everybody else has no access at all, perhaps to the scripts directory. That's the kind of thing you can do with ACLs.

But working with ACLs is great, but it may not automatically be available in a given Linux distributions, for example Ubuntu Linux doesn't automatically include the tools for this, so you can install the package using sudo apt install acl.

And when you do that, you will get a number of commands available to manage ACLs, which includes the setfacl command. Set file ACL which as it implies lets you configure the permissions for different users, different groups for files and directories. And we'll take a look at some specific syntax examples of how that actually works. The other command you get when you install the ACL package is the getfacl command. You can retrieve or show the permissions that were assigned to various users and groups for given files and directories. And again, we'll look at some examples of how that syntax works of course as well.

Let's look at that syntax right now. The first example we have is getfacl for a file called file1.txt Well, that would return the standard Linux filesystem permissions, the owning user, the owning group, but also potentially any other users or groups that also have different sets of permissions. setfacl can be used to modify permissions, which is where the -m comes from. Here we are modifying the ACL. The user we are modifying is mbishop, and we are granting read, write, execute.

Notice that u is separated from mbishop, which is separated from the permissions by a : for that single entry. So, we're setting the permissions for mbishop for a file called file1.txt. We are not setting mbishop as the file owner. That account might happen to be the owner, but if not, we're adding an additional user with their own permissions to file1.txt that's a user.

We can also use setfacl with -m for modify to add multiple groups. Here we're adding a group called eastadmins and we're granting read and write to file1.txt. You can have multiple groups, each with different permission sets to the same file or directory. We can also use setfacl with the -R syntax, which means recursive -m for modify. We can set let's say other to read or r and we can specify then the directory, in this case, /dir1 that saves us from having to set the same permissions on multiple files in the same directory structure.

You can also use getfacl with the -R to recursively go through let's say a directory called dir1. And because we don't have a leading slash in front of dir1, it would have to be in the current path, we can use the output redirection symbol, the greater than sign to write out to a file, let's say called aclpermissionsbackup.txt. You could apply that in the future, or you could restore it using the setfacl command with the restore parameter and specify the name of that file.

Pictured on the screen, we have an example of using sudo setfacl -m to modify where we're adding user mbishop with read and write to a file called budget1.txt. If we do a long listing in ll, notice for budget1.txt, we have the standard permission set shown in the leftmost or first column, but there's a + there. + means an ACL has been set for that file.

In our next screenshot, we are using getfacl for budget1.txt So, the filename is shown, the owner, the group. So, the user permissions for the owner shown as lbrenner are shown. But then we have another user entry for a different user mbishop and we have a group entry here for a group called westadmins which only has read permissions. There's also an item here. When we run getfacl returned, that's labeled as mask, and it's shown here with rw. The mask is like a filter that sets the maximum permissions. It overrides any assigned permissions. So, it's yet another option when you're working with ACLs in the filesystem.

5. Video: Managing Extended ACL Linux File System Permissions (it_oslsys_03_enus_05)

During this video, discover how to manage Linux extended ACL file system permissions using getfacl and setfacl.
manage Linux extended ACL file system permissions using getfacl and setfacl
[Video description begins] Topic title: Managing Extended ACL Linux File System Permissions. Your host for this session is Dan Lachance. [Video description ends]
Let's take a few minutes and let's experiment with extended ACL Linux file system permissions. Here on my Ubuntu server, if I were to type ls, I've got a budgets folder in my home directory. Let's go into it because in here I have a file called budget1.txt.

[Video description begins] A terminal window appears with the heading: cblackwell@ubuntuserver1:~/budgets. The following command is added: cd budgets. [Video description ends]

If I type ll for long listing, we get a listing of the budget1 file as well as the parent directory and the current directory.

[Video description begins] The following commands are added. Line 1 reads: ls. Line 2 reads: ll. [Video description ends] 

But the budget1.txt file shows the owning user here, lbrenner, the owning group here eastadmins. So, lbrenner would get the read and write permissions set for the owner. The members of the eastadmins group would get read and write set for the owning group, and anybody else would have read. Now that's fine, but there are a couple of glaring problems with this. One of which is how do I sign different specific permission sets for different users and different groups?

Well, with standard Linux permissions, otherwise called POSIX-compliant permissions. This is a limitation, and it stems way back many decades ago. However, if you need some more advanced features, such as the ability to assign different permission sets for different users and groups, that's where extended ACLs come in as being useful.

If I were to run getacl, actually I'll just run that by itself and press Enter because it comes back and says first of all, did you mean getfacl, get the file ACL? Well, yes, I actually did mean to type that in. 

[Video description begins] The command reads: getacl. [Video description ends]

Well, let's see what it says, getfacl. It says it can't be found.

[Video description begins] The command reads: getfacl. [Video description ends]

But you can install it with: sudo apt install acl. So, the getfacl and the setfacl commands are unavailable. So, if I type setfacl we get the same message.

[Video description begins] The command reads: setfacl. [Video description ends]

So, let's go ahead and install that sudo apt install acl.

Some Linux distros will have these commands built in automatically.

[Video description begins] The command reads: sudo apt install acl. [Video description ends]

Obviously, this version of Ubuntu server did not. If I were now let's just run getfacl against budget1.txt, it'll return what we can already see with the long listing command up above. The owner being lbrenner, the group being eastadmins, and then the permissions for the owning user and group and other.

OK, so there's nothing new there yet, but we haven't yet manipulated the ACL for that file, the access control list. Let's clear the screen. I'm going to run setfacl and I'm going to use -m because I want to modify the file ACL, u for user : I know I have a user on this server by the name of mbishop. I'm going to specify that name and I'm going to set : rw read and write.

I could specify x for execute if I wanted to and then I'll specify after a space the name of the subject to which that should be applied, in this case, budget1.txt, Enter.

[Video description begins] The following command is now added: setfacl -m u:mbishop:rw budget1.txt. [Video description ends]

Now I get an operation not permitted because when you start modifying some of these things, you should make sure that you are using the sudo prefix to run it with elevated privileges and of course, it works fine after that.

If I type ll for long listing, notice that with the traditional long listing and the standard Linux permissions, we do not have a reference to mbishop, but do you notice this little + here? 

[Video description begins] The following command reads: sudo setfacl -m u:mbishop:rw budget1.txt. [Video description ends]

There's some additional stuff that's been set here, which means an ACL. If I run getfacl against budget1.txt, well this is interesting now, besides the standard items that we saw previously, what's new of course, is user mbishop is listed as a separate entry in the ACL for that file having read and write permissions.

[Video description begins] The command reads: getfacl budget1.txt. [Video description ends] 

And they don't have to have the same permissions as the owning user which happens to be read and write also in this case. So, if I were to run sudo setfacl u : I have another user on this system by the name of lbrenner: let's say just read for budget1.txt. So, let's say I were to run sudo setfacl -m for modify, u for user.

[Video description begins] The following command reads: sudo setfacl u:lbrenner:r budget1.txt. [Video description ends]

I know I've got another user on this system called lbrenner: r let's say just read permissions for budget1.txt. Enter.

[Video description begins] The command reads: sudo setfacl -m u:lbrenner:r budget1.txt. [Video description ends]

Now we run getfacl against budget1.txt. Now we have an additional user added to that same file as ACL with totally different permissions. That's one of the benefits of using these ACLs. But you can do the same thing for groups. Here we've got an entry for group read and write that maps to if I type ll the owning group eastadmins.

[Video description begins] The command reads: getfacl budget1.txt. [Video description ends] 

OK, but what if I have a different group that needs different permissions to that file? By the way, this could also be done for a subdirectory, we're just doing it on a file in this example. First thing I'll do here is add a new group, sudo groupadd westadmins. OK, now what I want to do is setfacl -m modify, g this time for group of course, not u for user: westadmins : r for read let's say for budget1.txt. 

[Video description begins] The command reads: sudo groupadd westadmins. [Video description ends]

[Video description begins] The command reads: setfacl -m g:westadmins:r budget1.txt. [Video description ends]

Now we know we're going to have to prefix that with sudo to run it with elevated permissions and then Enter.

[Video description begins] The command now reads: sudo setfacl -m g:westadmins:r budget1.txt. [Video description ends]

If we now once again run getfacl against budget1.txt, it should be no surprise, we now have an additional group here with different permissions added to the ACL budget1.txt westadmins with permissions of read.

[Video description begins] The command reads: getfacl budget1.txt. [Video description ends]

6. Video: Linux File Compression and Archiving Tools (it_oslsys_03_enus_06)

After completing this video, you will be able to recognize Linux file system compression and archiving commands such as tar, gzip, bzip, zip, xz, cipi, and dd.
recognize Linux file system compression and archiving commands such as tar, gzip, bzip, zip, xz, cipi, and dd
[Video description begins] Topic title: Linux File Compression and Archiving Tools. Your host for this session is Dan Lachance. [Video description ends]
An important part of managing a Linux environment is knowing how to work with Linux file compression and archiving tools. Let's talk about Linux file compression first. So, what we're talking about, of course, is saving disk space. Often most algorithms in a simple sense will look for repetitive patterns in files and use a placeholder that takes less storage space to represent those.

But in truth, the algorithms get much more complex than that. So, it's all about efficient disk space utilization. Now this might be something, for example, we do for files that reside on storage that sits in the Linux host. But we can also do this before we back up or archive data. We might choose to compress it so that we have a smaller backup or archive that in turn would have to be stored whether it's on-premises or whether it's in the cloud. So, that's file compression.

But what about archiving? With Linux archiving, we're talking about making sure we have a backup or an archive of data. We can have copies of it even for downloaded files that might otherwise take a lot of space. So, with archiving, it really goes hand in hand with compression to reduce the size of the archive. So, often we'll see these things together. So, which tools in Linux then can we use to manage this type of thing?

Well, the first tool is called dd. The dd tool allows us to specify what we want to add as input to the command and then what we want to output as a result, and this is often used for copying and converting files. You could even use the dd command to copy an entire disk partition to an image file. As an example, take a look here, we've got dd if = that means input file equals, except what we're specifying here is an entire partition

in the form of /dev/sdb1. Then the of parameter or output file parameter is being used. So, of = and here we're creating a file that we are calling datapartition1backup.img because that's really what it is. The next command is called xz. This is a data compression type of tool. It results in smaller archive files than other tools that we haven't yet talked about, but we will in a moment, such as gzip.

Examples of the syntax would include xz -v for verbose, T0 which means we want to use one CPU thread for every available core to perform the data compression because data compression can become very computationally expensive, there's a lot of math involved when you're doing a lot of compression. And of course, we would tell it what we want to compress, which in this case is a file called databasefile1. To decompress, you would use the -d command line parameter and specify the compressed file.

Normally xc compressed files have an extension of .xc, but of course file extensions in Linux do not have the same meaning or relevance that they do in a Windows environment. Let's get into Linux file zipping. We've got a couple of utilities that we can use to do this, for example gzip and bzip2. Their relative file extensions would be .gz for gzip or .bz2 for bzip2.

When you use these utilities, the file that you specify that you want to zip up actually gets replaced with the compressed file and you would decompress the zipped-up files using gunzip or bzip2 with the -d parameter. Then we've got the zip command line tool. Now this is standard for creating zip or archive files across multiple platforms beyond just Linux. And you would decompress using the unzip command.

So, these are just various ways to zip up or archive and compress numerous files. What really makes these differ is the compression algorithms that they use internally. And then we've got the Linux tar command. This is for tape archiving. That's where the name of the command originally came from. So, this is a tool that's used for archiving and optionally you can choose to compress the archive. Terminology wise tarred files are called 'tarballs'. You can create a compressed archive when you use the tar command

when you specify the -z command line, parameter that means use gzip compression. So, in our command example we have tar -c we want to create, z, a compressed archive, v means verbose, and f we give it the source file. And f means the file we want to result in, in this case, backup1.tar and then a space and then the source, in this case, /data.

If we have a tarball file and we want to view the contents of it, we can list it using the tar command with -t and then f and then specify the file, in this case, the file is called file.gz, which implies that it's a compressed archive. To extract the archive, you would use tar -z that would be if it's compressed and that would decompress it, x to extract, v for verbose, f to specify the path, and the filename. And lastly, we have the Linux cpio command. cpio stands for 'copy in, and copy out'.

So, this is an archiving type of command in Linux. So, working with an archive might look like this, ls so a standard listing in the file system. But we would pipe the output of the ls command with our vertical pipe symbol to the cpio command using -ov. o means to create an archive and v means verbose output. And we would redirect that to a cpio file using the > or the redirection symbol for output. You would extract from that archive using the cpio command -idv.

And then you would use the input redirection symbol, which is a <, and then specify the name of the cpio file. So, what we've done here is we've taken a look at some common Linux commands that you would use for compressing perhaps numerous files into a single archive file, and there are many tools to use to do this.

Now of course, if you already have for example, a tarball file, well, you'll have to use the appropriate tools to decompress it and archive it. It's also important to note too that you can automate the use of some of these in a shell script and you might periodically run that shell script, maybe for backup purposes through scheduled cron jobs.

7. Video: Managing Linux Compression and Archiving (it_oslsys_03_enus_07)

In this video, you will learn how to manage Linux file system compression and archiving.
manage Linux file system compression and archiving
[Video description begins] Topic title: Managing Linux Compression and Archiving. Your host for this session is Dan Lachance. [Video description ends]
In this demo, we're going to experiment with various methods of working with Linux compression and archiving through the use of different command line tools. The first thing we'll do here is just type pwd.

[Video description begins] A terminal window appears with the heading: cblackwell@ubuntuserver1:~/projects. The following command is added: pwd. [Video description ends]

I'm in my home directory and in a projects subdirectory that I've created where I have a number of project files. They're just sample files. If I were to run cat * to see the contents of all of them.

[Video description begins] The following command is added: cat *. [Video description ends]

They all contain the same thing. It just says, This is a sample project file. And if I were to do an ll a long listing, the files of course are very tiny, but that's going to be what we're going to work with when it comes to some of these commands.

Let's start by working with the tar command to create a compressed archive. To do that, I'll run sudo tar -c for create. I want to create an archive. Now if I want to compress it with gzip, I would then specify z as a parameter, v for verbose if I want to see output of what it's doing, and then f for the file. I want to call this projects_backup.tar.gz. That's the convention when something is archived and compressed with gzip, although you don't have to use those extensions, but it is normal.

Then we have to tell it the source. In this case, I'll put ./ current directory * and I'll press Enter. Because we use the -v the verbose parameter, it spit back out on the screen here all of the project files that it added to the compressed archive. So, if we were to do an ls in the current directory, notice we've got a file shown here with red lettering in Ubuntu Linux because it's a compressed archive. It's our projects_backup.tar.gz.

[Video description begins] The command now reads: sudo tar -czvf projects_backup.tar.gz ./*. [Video description ends]

Now we have a way that we can list what's in the archive without even extracting it. We can do that with sudo tar -t for listing, then f for the file and I give it the file name. So, I'll put in the file name here and Enter.

[Video description begins] The command now reads: sudo tar -tf projects_backup.tar.gz. [Video description ends]

What it does is it shows me what's inside that archive and what it's showing me of course, are my five sample project text files. Let's go ahead and just remove all of the text files in the current directory, rm * .txt.

[Video description begins] The command reads: rm * .txt. [Video description ends]

We'll clear the screen.

We'll do an ls so those files are gone. We're going to extract our archived gzip file to get those files back. We can do that with sudo tar. Now depending on where you're doing this in the file system will determine whether or not you really need to use sudo. We'll just use it anyhow. In this case, z it's compressed, x for extract, v verbose, and f for file. We just give it the name of the file. Enter.

[Video description begins] The command now reads: sudo tar -zxvf projects_backup.tar.gz. [Video description ends]

So, there's the verbose output. But if I clear the screen, do an ls, the project files are back.

Now the tar command has many command line parameters. We could view that with man tar to view the manpage where you might choose to append to an existing archive, or you might extract it to a directory other than the current directory and many more possibilities. I'll press Q to quit out of that. If I were to type sudo mount and pipe that to grep and look for device sdb. We've got a mount point called data1 and it's pointing to /dev/sdb1. 

[Video description begins] The command adds: man tar. [Video description ends]

[Video description begins] The following command is added: sudo mount | grep sdb. [Video description ends]

So, what I can do is I can take a backup image of an entire disk partition using the dd command. So, for example, sudo dd if for input file, = /dev/sdb1 and then of for output file equals and let's put that on the root of the file system. Let's call it sdb1.img. Enter. Depending on how big that partition is and how full it is will determine how long this operation will take. OK, so it looks like it's created our image file for our partition. If we go to the root of the file system and do an ls. Here we'll have our sdb1.img.

[Video description begins] The following command is now inserted: sudo dd if=/dev/sdb1 of=/sdb1 . img. [Video description ends] 

If I do an ll against that file, notice it's a rather large file because it's a copy of an entire disk partition.

[Video description begins] The following command is added: ll sdb1 . img. [Video description ends]

Not only can you use dd to create an image, but you can also apply it to a partition if you need to. So, normally you would store these files on some kind of backup media, whether it's removable USB drives or actual tape drives.

Let's clear the screen and let's go back to the home directory by typing cd and pressing Enter. And if we do an ls, we see that we've got our projects directory. Let's go back into projects again and do an ls in there. Let's take a look at how we would compress using the xz command line tool. If I just type sudo xz, it knows what I'm talking about.

[Video description begins] The command reads: sudo xz. [Video description ends]

With some Linux distributions if it doesn't, you'll have to install the package. So, in this case, sudo xz, I'll use -v for verbose and I'm simply going to tell it * .txt.

[Video description begins] The command reads: sudo xz -v *.txt. [Video description ends]

Of course, it will assume the current subdirectory. OK, so it's listed for each of the five sample project files the compression status, so 100%. If we clear the screen and do an ll, the files are shown here but with a .xz file extension, so it actually replaced the source text files.

Now if I want to decompress one, I could use xz -d and then specify the file. Why don't we do Project _A here?

[Video description begins] The command reads:xz -d Project_A.txt.xz. [Video description ends]

And now if we do an ll, long listing, notice we have Project_A.txt. Now when you're dealing with very tiny files, such as we are, you might not realize a benefit to using xz to perform compression. So, it really shines when you're using much larger files.

8. Video: Course Summary (it_oslsys_03_enus_08)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary [Video description ends]
So in this course, we've examined how to manage Linux file system permissions, compression, and archiving. We did this by exploring standard Linux file system permissions management as well as extended ACL permissions management. We covered Linux file compression and archiving tools, and then we used them to manage the Linux file system for compressing and archiving data.

In our next course, we'll move on to explore how to implement and manage IP addressing and routing in Linux, and also how to capture and analyze network traffic.

© 2024 Skillsoft Ireland Limited - All rights reserved.