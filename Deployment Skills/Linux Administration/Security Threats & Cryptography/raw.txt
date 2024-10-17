CompTIA Linux+: Security Threats & Cryptography
Managing Linux security properly lessens the impact of security incidents. Cryptography can play a role in securing Linux environments. In this course, I will start by discussing common Linux threats and their mitigations followed by going over the CIA security triad. I will then discuss how cryptography can secure data and how to manage Linux file system encryption. Next, I will discuss integrity and use Linux file system hashing to determine if files have been modified. Lastly, I will discuss the public key infrastructure (PKI) hierarchy, create a private certificate authority (CA) and certificate, discuss Secure Sockets Layer (SSL) and Transport Layer Security (TLS), and enable a Hypertext Transfer Protocol Secure (HTTPS) binding. This course can be used to prepare for the Linux+ XK0-005 certification exam.

Table of Contents
    1. Video: Course Overview (it_oslsec_01_enus_01)

    2. Video: Common Linux Security Threats (it_oslsec_01_enus_02)

    3. Video: The CIA Security Triad (it_oslsec_01_enus_03)

    4. Video: Cryptography (it_oslsec_01_enus_04)

    5. Video: Managing Linux File System Encryption (it_oslsec_01_enus_05)

    6. Video: Integrity (it_oslsec_01_enus_06)

    7. Video: Generating File System Hashes Using Linux (it_oslsec_01_enus_07)

    8. Video: Public Key Infrastructure (PKI) (it_oslsec_01_enus_08)

    9. Video: The PKI Certificate Lifecycle (it_oslsec_01_enus_09)

    10. Video: Deploying a Private Certificate Authority (CA) (it_oslsec_01_enus_10)

    11. Video: Acquiring PKI Certificates (it_oslsec_01_enus_11)

    12. Video: SSL and TLS (it_oslsec_01_enus_12)

    13. Video: Enabling an HTTPS Binding (it_oslsec_01_enus_13)

    14. Video: Course Summary (it_oslsec_01_enus_14)

1. Video: Course Overview (it_oslsec_01_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance. [Video description ends]
Hi, I’m Dan Lachance. Managing Linux security properly lessens the impact of security incidents when they occur.

Cryptography can play a role in securing Linux environments.

In this course, I'll start by discussing common Linux threats and their mitigations, followed by going over the CIA security triad.

I will then discuss how cryptography can secure data followed by managing Linux file system encryption.

Next, I will discuss integrity and use Linux file system hashing to determine if files have been modified.

Lastly, I will discuss the PKI hierarchy, create a private CA and certificate, discuss SSL and TLS, and I will enable an HTTPS binding.

This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: Common Linux Security Threats (it_oslsec_01_enus_02)

After completing this video, you will be able to list common Linux threats including social engineering, malware, flawed software, and security misconfigurations.
list common Linux threats including social engineering, malware, flawed software, and security misconfigurations
[Video description begins] Topic title: Common Linux Security Threats. Your host for this session is Dan Lachance. [Video description ends]
Linux technicians need to be aware of the most common Linux threats so that they can prepare defenses to mitigate the impact of those threats or even to prevent them from occurring in the first place.

One of the biggest threats is social engineering. This means tricking people, trying to deceive people in some way so that the victims will disclose some kind of sensitive information or allow access to secured resources like internal servers, databases or provide credit card info, that type of thing. So it's basically fooling people into doing this type of thing. And there are many ways that that's done.

Social engineering techniques include malicious actors impersonating people of authority, someone in control, like a government official.

Impersonating law enforcement. This definitely helps nudge some people that might be fooled easily into compliance with whatever the attacker is trying to do or get.

But of course, on the modern technology side, phishing, with ph, via email messages, social media, SMS text messages, phone calls. Basically, sending a message that looks like in some way it would benefit the victim, such as: Click here to collect your free rebate, or Contact law enforcement as there is a warrant out for your arrest. People get scared by these things and are easily fooled. And so there are many ways that those types of things can be perpetrated.

Of course, social engineering can also include extortion or blackmail. One common example of this is receiving an email message or a social media message stating that your webcam has been recorded for the past period of time and unless you want that webcam video made public, pay a certain ransom amount.

So there are plenty of ways that these nefarious actors will in some way try to achieve their goals.

So social engineering is possible without infecting computers and without malware.

So the attacker might impersonate a communications provider technician over the phone and ask for account details. Or an attacker could show up to a physical location dressed convincingly, such as the local communications provider, thus, perhaps illegitimately gaining access to a wiring closet or a server room. So the victim would allow them into it, thinking that they looked the part, they sound the part.

And we know that when attackers have physical access to equipment, a lot of technical safeguards are no longer applicable. Some are like local disk encryption and the locking of server room racks, and so on.

As an example of social engineering via phishing, with a ph, let’s say that a user, a victim, receives a legitimate-looking email. Now, that legitimate-looking email might have the correct grammar, it might have the logo of a corporation or a government agency and look real.

However, the email would contain something about clicking a link or downloading a file attachment maybe to read the warrant for their arrest or read their tax bill due or something like that. Something that would make someone want to click on a link or download a file that’s attached to the message. So the victim would click the link, in this example, thinking it’s legitimate, but the link then, in turn, in the background would download and install malware.

Or it could be a link that asks the user to sign in to some kind of an account on a website. Of course, the website would be fraudulent. So the user then will have unwittingly provided those credentials to malicious actors. It happens all the time.

The same type of thing is possible with ransomware. And we’ve all heard about the explosion of ransomware incidents around the globe for corporations, municipalities, different types of government agencies. But the example would play out quite similarly to the previous one we just talked about.

So the victim would receive a legitimate-looking email that might contain a malicious file attachment or a link. In this case, the victim would be tricked somehow into opening a file attachment. Then the ransomware would execute on the user device or there might be instructions to go and download it from an alternate location. Once the ransomware is on that machine, that machine is under malicious user control. It’s called a zombie or a bot. A collection of those is called a botnet.

So the ransomware then would talk to the command and control or the C&C server may be to generate a key pair for encrypting data files because ransomware in its most common form encrypts data files and demands a ransom in order for the decryption key to potentially be provided. There are never any guarantees.

So it’s really the same kind of mechanism, isn’t it, as our previous example. The same mechanism trying to trick someone through an email or through other means can be used for a variety of different types of illegal activities.

Here we’ve got a screenshot of a real phishing email message. Here it’s trying to fool someone into saying they’ve got some kind of an inheritance of $7.5 million. All that they have to do is provide some details to make sure we get our money, including the first $5,000 installment. We have to provide our full name, address, mobile number, age, country, occupation. And, you know, there’s going to be more after that. [Video description begins] A screenshot of a phishing email message is displayed. The email header reads: Your first payment of $5000 release. The sender shares the contact information of a person for the receiver to connect with to get the total funds. [Video description ends]

The key is not to be tricked by greed or fear or any other type of emotion when reading emails. And always question everything you receive if you didn’t ask for it, whether it’s through SMS text, email, or whatever the mechanism.

So the general malware infection process goes like this, whether it’s on the macOS, Windows, or Linux.

There are many people that believe that the macOS and Linux are immune to malware and these types of attacks, which in fact is not true at all.

So in step one, malicious actors will perform some kind of reconnaissance to determine who they want to target. Then they target a user such as through a phishing email message. The user is tricked in one way or another to click on something or to download something or provide some details about something.

If it's malware, then the malware would then infect the device, especially, if the user initiated some kind of an action that went out and got something from some URL on the Internet.

And in step four, a lot of bad things can happen. The user gets blackmailed, sensitive data is exfiltrated out of the organization or agency, or sensitive data is encrypted and a ransom is demanded, sensitive data is deleted, or the botnet might be instructed to run a DDoS attack against other victims. And that's just a tiny beginner list of problems.

So on the Linux side for security threats, besides social engineering and malware and phishing, leaving default settings is always a problem.

Default usernames and passwords. This is especially a problem when you deploy a Linux host via a template on a cloud computing platform where the known username is never changed. Of course, if a password is not chosen that is strong or if public key authentication is not used, that's also a problem.

Having Linux hosts directly exposed to the Internet unless absolutely necessary is a bad idea since they are that much more visible to potential attackers for reconnaissance and ultimately attacks. Use a jump box instead. What’s a jump box? A jump box is a host that you connect to and use as a launching pad to connect to servers internally, using private IPs to manage them.

Jump boxes can be manually configured with two network interfaces, one on a private network, one on a public. But cloud providers also have built-in solutions such as Microsoft Azure’s Bastion Solution.

The lack of encryption at the network and storage level is always a problem, regardless of the platform.

Using short passwords, violating the principle of least privileges, such as assigning too many file system permissions to regular Linux users when they don’t need those permissions.

The lack of applying updates, such as on a Debian-based distro, updating your repository list, and then running an upgrade on installed packages.

3. Video: The CIA Security Triad (it_oslsec_01_enus_03)

Upon completion of this video, you will be able to outline how the CIA triad enhances IT security.
outline how the CIA triad enhances IT security
[Video description begins] Topic title: The CIA Security Triad. Your host for this session is Dan Lachance. [Video description ends]
Properly managing the security of Linux hosts means having a solid understanding of the CIA security triad.

The C in the CIA security triad stands for confidentiality, the I stands for integrity, and the A stands for availability. How does this apply to Linux?

Well, let’s start with confidentiality. What we’re talking about here is making sure that data, that is sensitive, is only available to those authorized parties that should be able to access it, and that might be in line with contractual or regulatory requirements that stipulate those types of details.

It means preventing unauthorized access to sensitive data. Nine times out of ten, the way that that is implemented is through encryption. The encryption of data at rest or storage encryption, whether we're talking about Linux hosts and locally attached mass storage devices that are using some kind of encryption work. Or if those Linux hosts are in the cloud, maybe virtual machines, maybe those virtual machine disks are encrypted.

But not only that, making sure that we have encryption over the network. For example, using SSH for remote management instead of Telnet. And of course, always using HTTPS as opposed to HTTP. That would apply to confidentiality.

For web applications, we know that we want to encrypt data at rest. In some cases, Linux technicians might allocate an entire disk partition to host the content of a website. And depending on the nature of that content, might determine that it should or should not be encrypted.

We should assign only the permissions that are required for resource access. That’s a principle of least privilege that also would apply to the Linux user account that Daemons are running under. So the Apache web server, for example, uses a specific user account, and that user account requires permission to be able to serve up files, for example, from the web server root directory. But you want to make sure you only grant the permissions that are required. That is more work usually than just granting full permissions. But it's absolutely crucial from a security perspective, and that often means referring to documentation.

On the web developer side, the use of claims can be very handy. A claim is an assertion about a user or device when they authenticate, such as a user signing in and their date of birth being a part of the claim, or whether they're a full-time or a contract employee, that type of thing. Of course, that’s configured on the authentication server side and then consumed on the web application side.

Web application developers have to build their app to look for those types of claim details and then determine what access to an app that users or devices would have.

We know we should always use HTTPS instead of HTTP. That means having a PKI certificate and creating an HTTPS binding for the web app, normally which listens on port 443. But you can also disable HTTP, not just blocking port 80, but disable HTTP access to a web server. Whether you’re using the Apache web server, or NGINX, or whatever solution you’re using.

And of course, we want to make sure that we always keep our Linux host and web server stacks and all related modules patched. Keep them up-to-date as those updates are made available.

Now in the CIA security triad, we also have integrity. This means that we have an assurance of the trustworthiness of certain types of data. Integrity solutions at the file system level can be used to detect data tampering, whether it’s a database or an office productivity document.

But of course, at the network level, network integrity comes in the form of things like digital signatures. A digital signature of a network message is created by the sender’s private key. So you need a public and a private key pair.

On the receiving end, the digital signature is verified by the recipient using the related public key.

When we are talking about file system integrity for files or databases, this is done using hashes. When you generate a unique hash of a file or a database, what you’re doing is feeding that data at the binary level into a one-way hashing algorithm, which results in a fixed-length hash or message digest, whatever you want to call that resultant value.

When you run the hashing against that file in the future, if you get the exact same result, it means nothing has been modified in the file. If the hash is different, something has changed.

And of course, integrity means auditing. Auditing system, data access logs where appropriate. Meaning you don’t want to audit all activities for everybody. That's just way too much information to sift through.

The A part of the CIA triad is availability. Here we’re talking about things like the Recovery Time Objective, the RTO. The RTO, of course, is used in disaster recovery scenarios. It really stipulates in time the maximum tolerable amount of downtime. Whereas the Recovery Point Objective or the RPO stipulates the maximum tolerable amount of data loss in the event of some kind of a disruption. The RPO often dictates how often data backups need to be taken.

It means making sure IT services are up and running and always available, as well as data. And that might be achieved in a variety of ways, such as through replicating data to alternate locations.

And for application availability, we might use load balancing. In our diagram, we’ve got a client device connecting to www.quick24x7.com, which in this example would resolve to the public IP address of a load balancer configuration. Whether that load balancer is configured on-premises or in the cloud.

And behind the load balancer, we would have back-end VMs running the application. [Video description begins] In the diagram, a client's cellphone is shown connected to the site: www.quick24x7.com, which is a public IP address load balancer. The load balancer is further connected with three back-end VMs to run the application. [Video description ends] And perhaps enabled for autoscaling, meaning when we get to a certain point of busyness for this web app, it’ll start launching or deploying new VMs in the back-end to accommodate the increased workload.

So that gives us a sense then of the CIA security triad, and some examples of how that might be implemented.

4. Video: Cryptography (it_oslsec_01_enus_04)

After completing this video, you will be able to recognize how cryptography protects data.
recognize how cryptography protects data
[Video description begins] Topic title: Cryptography. Your host for this session is Dan Lachance. [Video description ends]
Let's have a chat about cryptography. So cryptography really lends itself to the confidentiality part of the CIA security triad. What it means is that we need to provide data security.

But in what form? Well, confidentiality, integrity, and authentication. So cryptography is involved with all three of those items.

Confidentiality can be applied to things like network communication channels to make sure that we are encrypting network traffic, whether it's through a VPN tunnel, whether it's just on a local area network with IPsec, whether it's using SSH instead of Telnet for remote management, whether it’s using HTTPS over HTTP, many forms that will come in.

File system encryption, whether that’s done at the drive level, you get self-encrypting drives that will handle that or you might do it at the Linux host level using software solutions, which might work in conjunction with the trusted platform module or the TPM chip in the machine, which stores decryption keys.

So we've got file system and full disk encryption options. These are important as even if disks are physically stolen and acquired by malicious parties, if encryption was enabled correctly, those malicious parties will still not be able to get into that encrypted data. Now they’d be able to wipe the storage media and use it for something else of course, but they wouldn’t be able to get to that sensitive data. But in order to work with confidentiality, specifically with encryption, we need keys.

So where do the encryption keys come from? Well, one way is through public key infrastructure or PKI certificates, where you generate a public and a private key pair. This is called asymmetric encryption because the keys are different. They are asymmetric! One is used to encrypt, one decrypts.

For example, to encrypt a message to a recipient, you encrypt with their public key. They decrypt it with their related private key. But you don't need a PKI certificate for keys.

Keys can also be generated using different tools, like OpenSSL or PuTTYgen, where you result in key pairs, public and private key pairs.

Or you can work with individual single keys. Not public and private keys, but one single symmetric or secret key which is used for both encrypting and decrypting. The problem with that is if you have a large-scale environment where everyone needs to be able to encrypt and decrypt, first of all, everyone’s got the same keys. There's not a lot of security in that sense.

Secondly, how do you safely distribute the secret key? There’s only one to all involved parties. At least with public and private key cryptography, the public key is designed to be shared publicly. There's no security risk with that.

So with encryption, what happens is the plaintext shown here as the quick brown fox jumps over the lazy dog, is fed into an encryption algorithm along with a key, which results in the scrambled or encrypted data, which you can’t make sense of. That’s called the ciphertext. [Video description begins] In the diagram, two containers are shown with the headers: Plaintext and Ciphertext. The Plaintext reads: The quick brown fox jumps over the lazy dog. The Ciphertext reads: DHD$^&00gaibxrdHAAHV. The Plaintext container is sending the key + algorithm to the Ciphertext container. [Video description ends]

So the process is done in reverse for decryption. And depending on the type of encryption, whether it’s asymmetric or symmetric, will determine which key is used for the decryption.

If malicious actors can somehow gain access to decryption keys, then, of course, they would be able to return the ciphertext to its original plaintext, and thus, gain access to that sensitive data. It's crucial that keys be kept safe.

So with symmetric encryption, it’s one key, that one key needs to be kept secure. Only the authorized parties that need it should have it. With public and private key pairs, the private key, which is used for decryption, must be kept secured, usually password-protected file. Or maybe the private key is burned onto a smart card, or whatever the case is. It needs to be protected! Otherwise, what’s the point in encryption?

But cryptography also is related to integrity, where integrity is used to assure the authenticity of some kind of data or message over the network through various techniques, such as hashing. However, while a hashing algorithm is used in cryptographic function, there's no key used with hashing.

So this means then that integrity can apply to the legal system in terms of admissibility of evidence, where we can use it to generate a unique hash of a captured disk image so we can detect any changes to the original evidence.

You can use integrity along with encryption or without it. For example, you might use digital signatures for authentication and integrity of sent email messages while also encrypting them to scramble the data to prevent unauthorized viewing of sensitive email messages.

So there are different types of cryptographic algorithms such as for encryption like the Advanced Encryption Standard, AES, and there are also different cryptographic functions for hashing, such as the Secure Hash Algorithm or SHA.

5. Video: Managing Linux File System Encryption (it_oslsec_01_enus_05)

In this video, find out how to configure Linux file system encryption to protect data at rest.
configure Linux file system encryption to protect data at rest
[Video description begins] Topic title: Managing Linux File System Encryption. Your host for this session is Dan Lachance. [Video description ends]
In this demo, we’re going to take a look at how to work with file system encryption on a Linux host. We'll start by encrypting an individual file and then we’ll talk about how you would go about encrypting an entire disk partition. [Video description begins] A blank Linux host page is open. The header reads: cblackwell@ubuntu1 :~ [Video description ends]

Let's start with individual file or directory encryption. The first thing I’ll need to do is run sudo apt install, and I’m going to choose to use the gnupg2 package to work with file encryption. Although there are many other choices you could potentially choose from. [Video description begins] A list of outputs appears on the screen. The presenter clears the screen to run the new command. [Video description ends]

After that, I’m going to run gpg2 --version just to make sure it’s installed and it knows what I’m talking about. And it looks like it’s returning back some information about public key support and different cipher or encryption algorithms support, hashing support, and so on. [Video description begins] Under the Supported algorithms, there are four support options displayed. It reads: Pubkey, Cipher, Hash, and Compression. Each option has further items. [Video description ends] So it knows that we've got GPG installed.

If I were to take a look at the man page for GPG, so man gpg, and Enter, [Video description begins] The presenter clears the screen to run the new command. [Video description ends] [Video description begins] A new page opens with the title: GPG (1) GNU Privacy Guard 2.2. It has five categories: Name, Synopsis, Description, Return Value, and Commands. Each category has further details. [Video description ends] there are plenty of things that we can do with this. gpg, by the way, as we see here, stands for GNU Privacy Guard. And as we go down through the man page, there's quite the description and there are many command line options and their behaviors are discussed here.

Now we're not going to read through the man page, but this is one of those types of tools where because it’s got so many options, it’s impossible to memorize all of them. So the man page becomes very useful. So I’m going to type Q to quit, get out of there, and there we have it.

So if I type ls here in my current working directory, I’ve got a file called Project_A.txt and if I cat that file, it simply contains some text that says, this is sample text for Project A. The point is that we can read it because the file’s not yet been encrypted.

So to encrypt it, I can do the following. I can run gpg --symmetric which means the same key to encrypt will also be used to decrypt. It’s in the current directory, so ./ and it’s called Project_A.txt

When I press Enter, it asks me for a passphrase. [Video description begins] A new page opens with a box in the middle of it. Inside the box, the message reads: Enter passphrase. A blank field is provided. There are two buttons below it: Ok and Cancel. [Video description ends] This passphrase is used to encrypt and it must also be provided for decryption to occur. So I’ll enter the passphrase and it asks me to re-enter it or to confirm it, after which point it has encrypted the file. If we clear the screen and do an ls again, what we have as a result is a file called Project_A.txt so that’s the original file name, but it’s also got a .gpg extension.

Notice the original file Project_A.txt remains. Normally what you would do is remove that original file and keep only the encrypted file. [Video description begins] The presenter runs the command: cblackwell@ubuntu1 :~$ rm Project_A.txt. The output appears on screen: rm: remove write-protected regular file 'Project_A.txt'? He clicks Y for yes. [Video description ends] So I’ll go ahead and remove that. [Video description begins] The presenter clears the screen to run the new command. [Video description ends] So now all we’re left with is the GPG file. If I try to cat that file, by the way, notice we get a bunch of scrambled looking characters because the file has been encrypted.

Okay! So let’s say I want to decrypt that file. So I would run gpg --output and I would specify what I want the output file to be called. Let’s say I want to call it the same name Project_A.txt but it doesn't have to be called the same thing. And then, I’ll specify the --decrypt parameter and I’ll specify the name of the encrypted file. So Project_A.txt.gpg, and I’ll press Enter. And if I type ls, we’ve now got our Project_A.txt file. So let’s cat it, Project_A.txt We’re back to having the original file which could have been called anything with the plaintext within it. [Video description begins] The plaintext reads: This is sample text for Project A. [Video description ends]

Now our password information has been cached in memory in this session, which is why we were not prompted again. All right! So that’s how we might work with individual file encryption.

We can also encrypt an entire disk partition, so I’m going to run sudo lsblk --scsi. [Video description begins] The presenter clears the screen to run the new command. [Video description ends] What do we have for devices? [Video description begins] A table appears as the output. It has five columns with headers, such as: NAME, TYPE, VENDOR, and more. It shows a list of device names, such as: sda, sdb, and so on. [Video description ends] I’ve got device sde here. So let’s run sudo fdisk /dev/sde to create a new partition. So I’ll press N for new, P for primary. And I’ll press Enter to accept all of the defaults and then Q for quit to get out of fdisk, and I’ll clear the screen.

Next I’m going to run sudo apt install, and I’m going to choose to install the cryptsetup tool. Now, there are many tools just like there is for individual file encryption for entire disk partition encryption in Linux. I’m going to use this tool. [Video description begins] A list of outputs appears on the screen. The presenter clears the screen to run the new command. [Video description ends]

So I’ll run sudo cryptsetup luksFormat, luks is spelled LUKS and that stands for Linux Unified Key System. And the word format has a F. So luksFormat, one word, and I’ll point to our new device /dev/sde Okay! I’m then given a warning. This will overwrite all of the data on that device. Are you sure? If you are, type yes in capital letters, that’s what I’ll do, and I’ll press Enter.

So we’re then prompted for a passphrase for /dev/sde, we are creating the passphrase here. I’ll go ahead and enter that, and then I’ll verify it. Okay, then that part is done! So now what I’ll do is unlock that partition. So sudo cryptsetup luksOpen this time, open with the O, I’ll point to my device /dev/sde and I’ll specify cryptpart for the partition. I’ll press Enter.

So we're asked for the passphrase that we specified. [Video description begins] The output reads: Enter passphrase for /dev/sde [Video description ends] So now that we've unlocked that partition, we can go ahead and do things like sudo mkfs -t let’s say, ext4 file system. But what we’re going to point to here is /dev/mapper/ and we call it cryptpart from our command up above. Enter, and it’s done! [Video description begins] The output on the screen reads: mke2fs 1.47.0. The following four items appear as done: Allocating group tables, Writing inode tables, Creating journal, and Writing superblocks and filesystem accounting information. [Video description ends]

Let's go ahead and make a directory here on the root of the file system. Let’s call it vault, that’s going to be our one-point directory. [Video description begins] The presenter runs the command: cblackwell@ubuntu1 :~$sudo mkdir /vault [Video description ends] Now let’s run sudo mount /dev/mapper/cryptpart and we’ll specify /vault to mount it into. So with this point, if we run an sudo mount and grep it, let's say just for the word vault, our encrypted file system is now up and mounted. [Video description begins] The output reads: /dev/mapper/cryptpart on /vault type ext4 (rw, relatime) [Video description ends]

Now, while individual file encryption will protect encrypted files until they’re decrypted within this session, the purpose of encrypting an entire disk partition is for the protection of data at rest before it’s mounted. Once it’s mounted, then within that session, you can access all of the files in it.

But the great thing about it is that files created within that partition will be automatically encrypted.

So that gives us a general idea then of how to work with individual file encryption in Linux and disk partition encryption.

6. Video: Integrity (it_oslsec_01_enus_06)

Upon completion of this video, you will be able to recognize network and file integrity solutions such as digital signatures, hashes, and checksums.
recognize network and file integrity solutions such as digital signatures, hashes, and checksums
[Video description begins] Topic title: Integrity. Your host for this session is Dan Lachance. [Video description ends]
We’ve talked about the fact that the I part of the CIA security triad stands for integrity.

So we’re going to talk about integrity and authentication. This really means that we need to be able to trust that data we are dealing with, whether transmitted over the network, whether it's a file on the file system, is to be trusted to make sure it has not been tampered with by unauthorized parties. That’s what this is really about!

Now we can do this in a number of ways, the first of which in the file system is through file hashing. Now, in order to generate a file hash, you need a tool that utilizes a hashing algorithm. Hashing algorithms, you can think of as kind of being like a lobster trap in the ocean, where it’s very easy to go in one way but pretty much impossible to reverse it.

So with file hashing, you feed data into a one-way algorithm which results in a unique hash value or message digest. There’s no way to reverse engineer that. And there’s no keys involved like there is with encryption. You might have two keys, public and private keys, where the public key encrypts and the related private key decrypts. There's no keys involved here to reverse the process of hashing. So file hashing is one form of this.

Also, it comes in the form of an email digital signature. And when we send an email message, if our environment is configured for it, we can digitally sign messages that we send to others. What does that mean? What it means is the sender’s private key is used against that message for security assurances. That means that the recipient would need the related public key of the sender to verify that the signature is valid and that the message is authentic. It came from that party because only that party has access to that private key, and also to make sure that the message was not tampered with along the way over the network.

Of course, in order for this system to work reliably, private keys must be secured. If they’re stored as files on device storage media, then those files should at least be password protected with strong passwords.

Integrity and authentication can also come in the form of using a virtual private network or a VPN. Not an end-user VPN for anonymizing which country they’re coming from so they can stream videos from different services, not that type of VPN. We’re talking about a corporate VPN that might link branch offices together over the internet through an encrypted tunnel that is authenticated, or maybe allowing remote workers to work from different locations, including home, through a secured tunnel into a remote network elsewhere.

Another form of integrity and authentication would be using cryptocurrency solutions of any type, which are based on blockchain technology. Blockchain technology uses hashing to ensure the validity of transactions in the blockchain.

So let’s focus on file hashing for a moment. This provides file integrity so that we can trust that files haven’t been tampered with. So we can detect unauthorized file modifications. How so? Well, if we’ve generated a file hash, let’s say, one week ago, of a sensitive document. And we’ve stored that file hash somewhere, perhaps in a file, and then we run that hash again today, in other words, we feed that same file through the same hashing algorithm but will result in a different hash value, we know something has changed.

Now, we don't necessarily know that change was unauthorized. That might be used in conjunction with audit records to determine who made changes. And some tools will combine those features and do that for you.

File hashing is also important from a legal standpoint for digital forensic analysis. In the case where, for example, storage media is seized from a suspect, digital forensic analysts could then generate a unique hash of that entire storage media, that entire disk, USB drive, whatever it is. Then take a copy of it and analyze the copy.

But the point is that from a legal admissibility standpoint in a court of law, we need to be able to demonstrate that the original data, the evidence is intact and it hasn't been tampered with. And that can be proven legally through hashing. There are other things at play too, like the chain of custody, to make sure that evidence was tracked and stored securely at all times.

Now there are many different ways or algorithms, specifically, that you can use for file hashing. One example would be the Secure Hash Algorithm, SHA, and a number of bits like SHA-256 for 256-bit hashing. But there are many others as well, including older deprecated solutions like MD5, Message Digest 5, as a hashing algorithm.

So the hashing process works like this. The raw data bits are fed into a one-way hashing algorithm, whatever it happens to be. The result of that is a unique "hash" or a "message digest". Future hashes will differ. It'll be a different hash value. It'll be a different message digest if the source data has been modified.

Now one way to provide assurances for things like PowerShell scripts, which are not limited to running on Windows, they’ll also run in Linux too, is by having digitally signed PowerShell scripts. Here we have a screenshot of the digital signature block at the bottom of a PowerShell script. [Video description begins] The title of the page reads: PowerShell Script - Digital Signature Block. A screenshot of a PowerShell script is displayed. A list of scripts is shown on it. [Video description ends] So PowerShell devices or machines that support PowerShell can be configured to only trust certain digital signers, which limits which scripts are allowed to execute on those devices.

In our next screenshot, we've got file hashing within the Linux environment. What’s been done here is the sha256sum command has been issued followed by the name of a file, in this case, hello.sh

What results below that is a fixed length hash value. Fixed length meaning it doesn't matter how much data you feed into it, the resultant hash value is the same length. Here we've only highlighted the first couple of characters within the hash values to point out that if we make a change to the file, the way we’re doing that in this screenshot is we are echoing the text new data and appending it to hello.sh

So we’re adding data to that same file. Then we are once again running sha256sum against that same file name. [Video description begins] The title of the page reads: File Hashing Using Linux. A screenshot is displayed below it. The initial characters of two hash values are highlighted on it. The first value reads: c22b897633c1b64. The second value reads: 4aba0cccde890a7. [Video description ends] Notice the hash value is different because the file has changed.

So using this type of a solution is important because file changes can be hard to spot manually.

You can store file hashes in a file in Linux using output redirection. Whether you want to use a > sign or >> sign for appending. And this type of thing can be used in many ways. One example is for web site technicians to do this to track changes to any files within the web site.

So that gives us an idea then of how integrity and hashing serves as being very important to assure that data is valid and hasn’t been tampered with.

7. Video: Generating File System Hashes Using Linux (it_oslsec_01_enus_07)

In this video, you will learn how to generate Linux file system hashes.
generate Linux file system hashes
[Video description begins] Topic title: Generating File System Hashes Using Linux. Your host for this session is Dan Lachance. [Video description ends]
Detecting changes to files can be important for a number of reasons. One of those reasons might be to make sure that a file is not corrupt. That a file that you copied or downloaded is the same as the original at the bit binary level.

Or you might want to be able to detect changes perhaps made by unauthorized users. Either way, we’re going to take a look at how to generate file system hashes in a Linux environment.

The first thing I’m going to do here on my Linux host is type ls, [Video description begins] A blank Linux host page is open. The header reads: cblackwell@ubuntu1 :~ [Video description ends] in my current directory, I’ve got a file called Project_A.txt If I cat the Project_A.txt file, it’s got some text that says- This is sample text for project A.

Now there are a number of different types of hashing algorithms out there. [Video description begins] The presenter clears the screen to run the new command. [Video description ends] The purpose of hashing algorithms is to bring in original data, feed it into the hashing algorithm, which is called a one-way algorithm because it can’t be reversed. And there are no keys required like there would be with encryption, whether they be symmetric or asymmetric public and private key pairs. With hashing, you feed the data through the algorithm and the result is a fixed length hash or message digest.

So regardless of the size of the data you input, the size of the hash or the message digest is always the same. Now, of course, different hashing algorithms result in a different-sized message digest.

So as an example, if I were to do sudo md5sum and let’s run that against Project_A.txt, we get a unique hash value shown here based on the old message digest or md5sum command. [Video description begins] The hash value reads: 14a5363d4bd8f4aaed712ecc75e84c6d [Video description ends]

However, MD5 hashes are not used as frequently as the secure hash algorithm or sha, SHA.

Notice if I run sudo sha256sum against our Project_A.txt file, it’s the same file, but we get a different returned hash value just as we would if we used sha512sum. But let’s clear the screen.

Let’s go back to our sha256sum. Notice the value here, it begins with e9aa. Let’s make a quick change to the Project_A.txt file, run a sha256sum against it and see what we get.

So sudo nano, let’s open up that Project_A.txt file. [Video description begins] A new page opens with the header: GNU nano 7.2 Project_A.txt. The first line reads: This is a sample text for Project A. [Video description ends] I’m going to add some new text here and I’m going to save that out to the file. And I’ll use the up-arrow key to go back to where we can run our sha256sum of the Project_A.txt file. Notice that we get a different hash value. [Video description begins] The presenter highlights the first few characters of the hash value. It reads: 5cdf3 [Video description ends] That, of course, is because the file has changed, that’s the purpose here. Whether you want to detect corruption in terms of changes or you just want to know that a modification has been made to a file.

Now the other thing that's interesting here is user passwords for local Linux user accounts because they are hashed. For example, if I were to run sudo tail /etc/passwd, [Video description begins] The presenter clears the screen to run the new command. [Video description ends] now it doesn’t contain passwords these days, but it’s just a user account file. Notice we’ve got a user here, mbishop. But the password is not here. Instead, if we do an sudo tail of /etc/shadow Then here for user mbishop, the second field and each field here is denoted with a full colon delimiter. But the second field here contains a hash of the password for mbishop. [Video description begins] The presenter highlights the hash for mbishop. The initial characters read: $y$j9T$4Z3ywQS.ubp/yN1/ [Video description ends]

Now remember, hashing algorithms are used as one-way functions, in other words, you can’t reverse it. We can’t take that hash and somehow reverse engineer it to the original source data. Where with encryption, you can decrypt the ciphertext to reveal the plaintext given that you have the correct key. Can’t do that with hashing!

But from a security aspect, there is this notion of rainbow tables which are enormous lists of resultant hash values from known plaintexts that can be compared. For example, if we know the password for mbishop is apple and it results in this hash value when fed into a particular hashing algorithm, then that would be one possible way from a cybersecurity standpoint that hashes can be cracked.

These days, though, most algorithms that hash a value to result in that message digest will use a feature called salting, which means it uses some kind of random data that gets generated when you set things like a password. And in this way, it makes it very difficult, if not impossible, to try to crack password hashes using rainbow tables.

And remember, because there's no keys involved, you don't have to worry about keys being compromised or anything like that to result in letting malicious actors into a system because they've somehow determined what a password hash value is.

The last thing we'll do here is just take a quick look at [Video description begins] The presenter clears the screen and runs the command: cblackwell@ubuntu1 :~$ ls [Video description ends] a sample script I’ve got here called hashscript.sh

If we were to run, let’s say sudo nano against that, just to open up that file, [Video description begins] A new page opens with the header: GNU nano 7.2 hashscript.sh. Three lines of variables are shown: day, year, and month. Each has further details that the presenter reads out. [Video description ends] this is a simple shell script where we're creating a couple of variables. One for the day of the month, one for the year, one for the month itself. For example, the day variable equals, and this is all within backticks, not single quotes. We’re running the date command and we’re asking just for the date portion storing the day variable respectively.

The same type of thing is happening to gather the year and storing it in the year variable and the month and storing it in the month variable.

Then we’re echoing some text and then we are putting together our month, day, and year variables. Basically, so we have a date stamp, and we are appending with the >> signs to a file called file_hash_history.txt

And what we’re doing in this file is we’re running sha512sum of a file, a sample file I have in the current directory called file1.txt, we keep appending it to our file_hash_history file.

And then we echo a new line character for spacing. What we're doing here in this script is essentially hashing a file and formatting the output a little bit and writing it to a file. So we have a running list of hashes of a file over time so we can detect changes. Let's see this in action.

So if I were to cat file1.txt, it has the word Testing in it. Let's run our local script here. So ./current directory hashscript.sh, that should result in a file called file_hash_history.txt so if we take a look at that. Okay, it says sha512 Hash value. [Video description begins] The presenter runs the command: cblackwell@ubuntu1 :~$ cat file_hash_history.txt [Video description ends] Here’s the date stamp, and we’ve got a hash here for file1.txt [Video description begins] The date stamp reads: 07-11-2023 [Video description ends]

You might schedule this as a cron job perhaps, and have it run once or more daily or whatever the case might be. But let’s go in and make a change to file1 So sudo nano file1.txt [Video description begins] A new page opens with the header: GNU nano 7.2 file1.txt. The first line reads: Testing [Video description ends] I’ll just add a New line here, save that to the file. [Video description begins] The presenter clears the screen to run the new command. [Video description ends] And let’s just go ahead and run our script again ./hashscript.sh And let’s go back in our command history and cat our file_hash_history file. Now we have a new hash value, same date, but the hash value is different, of course, because the file contents have changed.

So this just gives us a little idea of how we might use hashing along with the script to track file changes over time.

8. Video: Public Key Infrastructure (PKI) (it_oslsec_01_enus_08)

After completing this video, you will be able to recognize how public key infrastructure (PKI) certificates are issued and used.
recognize how public key infrastructure (PKI) certificates are issued and used
[Video description begins] Topic title: Public Key Infrastructure (PKI). Your host for this session is Dan Lachance. [Video description ends]
The public key infrastructure, otherwise just called PKI, is really just a hierarchy of digital security certificates. But an important part of this is the chain of trust.

In other words, if a device trusts a high part of the hierarchy, if they trust a certificate authority, then any subordinate certificates in the hierarchy issued by that certificate authority will also be trusted. That's in essence what the chain of trust is about when it comes to PKI.

So certificates then, of course, are issued by what's called a certificate authority or a CA.

You can have public trusted CAs, of which there are many that are used to issue certificates. If you get a certificate issued by a public trusted CA, it means that devices in the enterprise, whether they’re servers, desktops, laptops, smartphones, tablets, whatever they are, they will automatically trust that certificate such as making a connection to an HTTPS website that uses that certificate because public CAs are automatically trusted by modern operating systems.

However, you can also create your own public key infrastructure, which means that you would create your own private internal untrusted CAs or certificate authorities. Notice it’s plural. You might have more than one. So with a large organization that wants its own control of PKI certificates internally, there might be a CA for each region where the company does business, each country, each department or business unit, each project, there are no rules on how it’s done.

However, if you use private internal untrusted CAs, device operating systems will not trust the signer of that certificate, the issuer of the certificate. And so, you would have to install the public key trusted root certificate of your private internal CA on all devices so that the devices would trust issued certificates from that private internal CA.

And you could use a lot of centralized configuration management tools, perhaps to do that, like Ansible or Puppet, and so on.

So we know then a certificate authority, a CA, can be public. We know that it will be trusted by devices, and we know that we can have private CAs, where we control every aspect of PKI certificates. But they would not be trusted, so we’d have to make some configuration changes for that to work.

Because if you have a web server internally, let’s say for an internal web app, using a privately issued PKI certificate, when client devices connect to that website, let's say with a web browser, they’re going to get warning messages. Or the browser, depending on the version of the browser, the type of browser, how it’s configured, might not let them proceed to that site because the certificate isn’t trusted.

In other words, anybody could have issued a certificate called anything. And if it's not from a trusted authority, why should it be trusted?

Pictured on the screen, we’ve got a screenshot of configuring a private CA. In this case, it’s being done on a Microsoft Windows server. What does that have to do with Linux? Well, the private CA might issue PKI certificates to any type of device, including Linux-based devices. It doesn't matter what platform the CA is configured on. [Video description begins] The title of the page reads: Private CA - Microsoft Windows Server. A screenshot of a Microsoft Windows server is displayed below it. The header of the page reads: Select role services. Under the category: Role services, the Certification Authority option is selected. [Video description ends]

In our next screenshot, to follow along with that, we can also deploy a private CA in the public cloud. We’ve got a screenshot of doing just that in Amazon Web Services, in AWS, where we can select the CA type. Notice in the screenshot, what’s selected is a root CA. So when you define your own public key infrastructure, you must begin at the very utmost top of the hierarchy. You have to define a root CA.

After you’ve done that, if you choose, you can configure one or more subordinate CAs. That goes back to what I was describing, where you might have a different certificate authority for different admin teams, different projects, different regions, that would be responsible for issuing their own subset of certificates from their own CA.

But you can’t have subordinate CAs until you first have a root CA. That just makes sense in the hierarchy. [Video description begins] The title of the page reads: Private CA - Amazon Web Services. A screenshot is displayed below it. The header reads: Create CA. The page is divided into two sections. On the left pane, the steps to create CA are given. On the middle pane, Select the certificate authority (CA) type option is displayed. There are two categories under it: Root CA and Subordinate CA. [Video description ends]

So if we were to visualize the PKI hierarchy, which we’ve done here on the screen, at the top you’ve got the root CA, below which we would have one or more subordinate CAs, and each of those subordinate CAs would then issue their own certificates.

Technically, the root CA can still also issue certificates. But in a larger enterprise where this might be done, often the root CA is taken offline for security reasons; unless it’s needed maybe to generate a new subordinate CA, but then it would only temporarily be brought online.

The idea is that if the root CA is compromised, then so is everything under it, which means the entire hierarchy. Whereas if only one of the subordinate CAs happens to get compromised, only the certificates under it would be treated as untrusted.

Then we have the notion of certificate templates. Of course, a template is a blueprint. This would be used when issuing certificates. It would specify which type of encryption and signing algorithms can be used when that certificate is used for security operations. And also, some certificate usage constraints such as this PKI certificate is designed to only be used for email encryption or file system encryption or email digital signatures.

And within a PKI certificate, you’ll have a number of details like the name of the subject, whether that’s the FQDN of a website or a user email address. Certificate usage details, the issuing CA name, and the issuing CA digital signature. The date and time that the certificate was issued and when it expires. These certificates have a limited lifetime, they expire eventually. Kind of like a passport does or a driver’s license does.

A PKI certificate utilizes public and private key pairs that are related to one another. So the public key is actually a part of the PKI certificate, but the private key is not stored within it. It’s usually stored in the OS secret secure storage location, which varies from platform to platform. You might also have other attributes stored within the PKI certificate.

9. Video: The PKI Certificate Lifecycle (it_oslsec_01_enus_09)

Upon completion of this video, you will be able to recognize the various stages of the PKI certificate lifecycle.
recognize the various stages of the PKI certificate lifecycle
[Video description begins] Topic title: The PKI Certificate Lifecycle. Your host for this session is Dan Lachance. [Video description ends]
At this point, we’ve discussed the PKI hierarchy, and we've briefly discussed PKI certificates. So now it makes sense then for us to have a discussion about the PKI certificate lifecycle.

When a PKI certificate is issued, it doesn’t last forever. So kind of like a driver’s license or a passport, at some point, it will expire. Prior to the expiry, you might choose to renew it or just let it expire so it no longer really exists. It certainly cannot be used.

So the PKI certificate lifecycle begins with the creation of a certificate signing request, otherwise just called as CSR for short. This means that we have to generate a public and a private key pair and generate a certificate signing request that will then be submitted to a certificate authority or a CA, which will then ultimately, hopefully, issue the certificate.

[Video description begins] The title of the page reads: PKI Certificate Lifecycle. A diagram is shown below. A circle with five boxes representing the PKI Certificate process is displayed. The items inside the boxes read: Certificate signing request (CSR), Issuance, Use, Revocation, and Renewal/Expiry. [Video description ends] Before certificates are issued, depending on the type of certificate authority, depending on the type of certificate you are requesting will determine what kind of due diligence the CA will perform to make sure everything looks legitimate before actually issuing the certificate.

Now the certificate signing request or the CSR, and the key generation, all of that can be automated. It might be part of something that you generate locally on your machine and then paste it into a web form field for a public certificate authority. It might be automated if you’re in, for example, a Microsoft Active Directory environment. And it may be partially or fully automated if you’re using a cloud private CA.

But after the certificate is issued, of course, the certificate can be used. What does that mean? Well, let’s think about the form that the certificate can exist in. It could be a file on a device. So you copy the file to a device. You install it in the local certificate store, which varies from platform to platform. And then it could be used for things like disk encryption if that’s what the certificate is for. Or for email encryption or digital signatures or authenticating a device to a VPN. The possibilities are many!

Remember that certificates can also exist in various forms other than files. They could also be burned into a smartcard. So if you have devices with smartcard readers, you could insert your smartcard, it’ll read your certificate and then allow you to do whatever it is it's configured to allow you to do maybe to send confidential types of emails, where otherwise you wouldn’t be able to send them.

Certificates potentially could then be revoked, such as if a device is lost or stolen. When a PKI technician revokes a certificate, the revoking it based on the certificate’s unique serial number.

It means that all of the players in the PKI hierarchy, and when I say players, what I’m talking about are all of the servers, all the VPN devices that partake in using certificates to allow authentication and encryption and whatnot, they must be configured to periodically pull down an updated certificate revocation list to CRL, or a crl, from the CA so they know which certificates are revoked and are not allowed to be used. So while revocation is listed here, it may not apply in many cases. Certificates might not need to be revoked.

Before the certificate expires, you can choose to renew the certificate and then keep on using it. Kind of like renewing a driver’s license or a passport before it expires. Otherwise, if you let it expire, it can no longer be used, and you have to start the entire process again from the CSR portion.

So the certificate signing request, the CSR. This is the first step when you are manually requesting a new PKI certificate. And the word manual is the operative term here because if you have an automated solution of some kind, this might be completely hidden from you as the end-user requesting a certificate.

You also, of course, need a unique public and private key pair. The private key is stored in a separate file. It’s not actually stored with the certificate like the public key is.

When you create a certificate signing request, you might specify details, including the common name that might be an email address, or it could be the FQDN of the web server that the certificate will be used for. You would also specify details like the organization name, the country, the email address of the admin that’s requesting the certificate, and potentially many other details as well.

PKI certificates can then be issued to individual users for their use, such as with securing email messages.

Or the certificate might be issued to be used on a specific device like a user’s smartphone to allow authentication to a work-based VPN.

Or it might be assigned to a software such as a particular service that’s running on a Linux host. Maybe it needs a certificate so that it can authenticate with another component running elsewhere. A good example of this is using Puppet for configuration management, where the client authenticates to the server using PKI.

Now, when certificates are requested and ultimately issued, they could be wildcard certificates. Imagine that you have a number of web servers that you want to secure with HTTPS. So normally, you would need a PKI certificate for each FQDN for each of those servers, and that’s fine!

However, if all of those servers have the same DNS domain suffix, let’s say they all end in .mydomain.com Well, you could request a wildcard certificate that you could then install on all of those servers without having to manage individual certificates.

Then there's the notion of extended domain validation. Depending on how the certificate will be used, such as for e-commerce sites, there might be enhanced certificate authority due diligence against the certificate requester to make sure everything looks legitimate, that they have a registered corporation, and so on.

Then we have code signing certificates used by software developers. This, of course, is important in this day and age in mobile app stores. In order to get a mobile app into an App Store, you have to have a certificate that will allow you to digitally sign your code so it’s trusted by the App Store. And then by extension, ultimately trusted by users installing apps from that App Store.

Now, we’ve mentioned the PKI chain of trust, which is based on the PKI hierarchy. What we have on the screen here is a screenshot of the certificates on a Windows machine, specifically the Trusted Root Certification Authorities tab has been selected here. This is a list of trusted root CAs out on the Internet, which means that any certificates issued by the CAs at any subordinate hierarchical level will be trusted by this device.

But notice that there is an import button here. [Video description begins] The title of the page reads: PKI Chain of Trust. A screenshot is displayed below it. The header inside reads: Certificates. The Trusted Root Certification Authority tab is selected. A list of user names is shown. The Import button is located below the list. [Video description ends] If you’ve got a private internal CA you’ve set up yourself, you know that it won’t be trusted by the device, so you could choose to import the trusted root certificate for that private CA. So it would trust issued certificates from it. Of course, there are centralized automated ways to do this on a larger scale.

We've mentioned, of course, revoked certificates as being a potential part of the PKI certificate lifecycle. There are two common variations of how that's dealt with. We’ve mentioned the CRL, the certificate revocation list, which is a list of revoked certificates' serial numbers where various services like websites, VPN, appliances, anything that would use PKI certificates and trust them can download the CA. So it has a list of certificates that are revoked and should not be allowed to be used.

However, we also have the Online Certificate Status Protocol, otherwise called OCSP. This one’s a little bit different because instead of downloading the entire CRL, only the individual certificate validity is checked as it is attempted to be used. So in this way, OCSP is considered a little bit more efficient than the older CRL standard.

10. Video: Deploying a Private Certificate Authority (CA) (it_oslsec_01_enus_10)

Discover how to create a Linux-based private certificate authority (CA).
create a Linux-based private certificate authority (CA)
[Video description begins] Topic title: Deploying a Private Certificate Authority (CA). Your host for this session is Dan Lachance. [Video description ends]
In this demo, I will be deploying a private CA. So we know then that a CA or a certificate authority is the topmost part of the PKI hierarchy. At least if it’s a root CA, it is.

Under which we can create subordinate CAs and then have them issue certificates. Or the root CA itself could also issue PKI certificates, whether for users, for devices, whatever the case might be. [Video description begins] A blank Linux host page is open. The header reads: cblackwell@ubuntu1 :~ [Video description ends]

Now setting up a private CA is sometimes advisable when you need full ultimate control and flexibility in how PKI is used and how it’s set up.

So to get started here, I'm going to run sudo apt install and I’m going to be installing the easy-rsa product. There are plenty of crypto solutions out there for PKI hierarchies that you can run. In this case, we’re installing easy-rsa. It asks- Do you want to continue? I will type in the letter Y for Yes.

Here in my home directory, I’m going to make a directory called easy-rsa If I do an ls, there it is easy-rsa. So what I'm doing here is I want to create a link. I’m going to run sudo ln -s /usr/share/easy-rsa/* and I want that to be put into my ./easy-rsa/ folder. Enter!

So now in my home directory here, [Video description begins] The presenter runs the command: cblackwell@ubuntu1 :~$ ls [Video description ends] if I change directory to easy-rsa and do an ls, we’ve got a bunch of symbolic links to the files that really live in /usr share/easy-rsa [Video description begins] The output reads: easyrsa openssl-easyrsa.cnf vars.example x509-types [Video description ends]

You don't have to do it this way, but this is a benefit in that if software updates are applied to easy-rsa on this host, then our references in our home directory will reflect those software updates. If any changes happen to apply to these files.

I’m going to run sudo chmod 700 to give all permissions read, write, and execute to the file owners. If I do a long listing, or LL, my symbolic links are shown here with the owner of root.

Then, of course, we can run sudo chown -R, for recursive to, cblackwell for the PKI directory. Okay! So in my easy-rsa folder, I’m going to run ./easy-rsa [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

If I do an ls in here, notice that we’ve got an easyrsa file. If I cat is easyrsa, it is a script. Okay! [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

It gives me a warning here that we are about to initialize a fresh PKI, a public key infrastructure. [Video description begins] The warning outcome reads: You are about to remove the EASYRSA_PKI at: * /home/cblackwell/easy-rsa/pki and initialize a fresh PKI here. [Video description ends] Type the word yes to continue. Okay, I’ll type in Yes and press Enter. Okay! At this point, it says you may now create a CA or requests. And you’ve got a new PKI directory in /pki underneath easy-rsa. And it also says that the vars file has been moved to PKI. Okay!

So if I change directory into pki and do an ls, notice, indeed, we do have a vars file here.

What we want to do is run sudo nano against the vars file. [Video description begins] A new page opens with the header: GNU nano 7.2 vars. The first line reads: Easy-RSA 3 parameter settings. Some configuration details are given below it. [Video description ends] And as I scroll down in this file, I've got a bunch of lines commented out for things like the country. So I’m going to set that to the two-character code for Canada, CA. And I’ll set all of these other variable values accordingly for the province, for the city, the organization, the admin email, and the OU. [Video description begins] The presenter changes the first command line: set_var EASYRSA_REQ_COUNTRY "CA". The rest of the command lines changes into: EASYRSA_REQ_PROVINCE "Ontario", EASYRSA_REQ_CITY "Toronto", EASYRSA_REQ_ORG "Quick24x7", EASYRSA_REQ_EMAIL "cblackwell@quick24x7.com", and EASYRSA_REQ_OU "HQ" [Video description ends] I'll press Ctrl X, I'll save this file.

So back here in the easy-rsa directory, I’ll run ./easyrsa build-ca which we’ll look at the vars file to build our certificate authority. It wants us to enter a new CA key passphrase. And then it wants me to re-enter it. And for the private key we'll enter in a passphrase and verify that passphrase.

I’m then asked for the common name of this CA host. I’m going to put in ubuntuca, and I’ll press Enter. Okay, and that’s it! So if I change directory to pki once again, if we do an ls, [Video description begins] The presenter clears the screen to run the new command. [Video description ends] we’ve now got our CA certificate file. And if I change directory into private, we’ve also got our ca.key file.

Just like with the regular certificate created from the CA, the CA itself also has a public and a private key pair. Private key is used to digitally sign issued certificates. So it is crucial to safeguard the ca.key file, that’s a private key file.

Whereas the ca.crt file, is the public key certificate. That's what you can distribute to clients to establish a chain of trust. So that trust certificates are issued by the CA.

We'll see how to generate certificate requests from a CA in another demo. But at this point, we have successfully configured our own private CA on our Linux host.

11. Video: Acquiring PKI Certificates (it_oslsec_01_enus_11)

Find out how to acquire a PKI certificate.
acquire a PKI certificate
[Video description begins] Topic title: Acquiring PKI Certificates. Your host for this session is Dan Lachance. [Video description ends]
In this demo, I’m going to go about acquiring a PKI certificate for our Linux host.

In our example, let’s assume that we need a PKI certificate for a web server stack. [Video description begins] A blank Linux host page is open. The header reads: cblackwell@ubuntu1 :~ [Video description ends] So we want to enable an HTTPS binding, so, therefore, we need a PKI certificate. You can acquire PKI certificates from public certificate authorities, public CAs, or private CAs.

I’ve already got a private CA established, and it happens to be on this same server. But it certainly doesn’t have to be on the same server where you will be requesting a certificate, but that's how it is in this particular configuration.

So here in my server, for example, if I change directory into easy-rsa and then change the directory into pki and do an ls, I’ve got a CA certificate file here, ca.crt which if I cat is the public key certificate for my CA. [Video description begins] The page gets populated with certificate output. The header of the output reads: BEGIN CERTIFICATE. The footer of the output reads: END CERTIFICATE. [Video description ends]

[Video description begins] The presenter clears the screen to run the new command. [Video description ends] If I were to go into the private directory under PKI and do an ls, here we’ve got the ca.key, the private key file which is passphrase protected for my certificate authority. Now that doesn't have to be on the same server once again, but it happens to be here. [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

From a client perspective that’s going to request a certificate, we can do that using the openssl utility. So sudo apt install openssl. Now if it’s already there, that’s great, otherwise, we would have to install it. [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

Here in my home directory, I’m going to run mkdir csr, for certificate signing request, and I’ll change directory into that location. You don’t have to create a subdirectory for this, but I’m just trying to be a little bit organized here. So I’m going to run openssl genrsa, to generate an RSA public and private key pair, -out I’m going to call it ubuntu1server.key Then I’ll run openssl. Then I’ll run openssl req, for request, -new -key We know our file is called ubuntu1server.key -out and then I’m going to call the request file ubuntu1server.req

Then I'm prompted with the fact that I'm going to be asked for information that will be incorporated into my certificate request. So the country name, two-character code, for my certificate request. And this is the same type of thing that was done at the CA level to establish the CA. We aren’t establishing a CA here, we’re trying to request a certificate from a CA.

For the common name, I’ll put in www.quick24x7.com Presumably that’s what we’ll be using this for is for a website under that name, and I’ll enter the admin’s email address. I’ll enter a challenge password, and I’ll fill in the company name. Okay! [Video description begins] The presenter makes the following changes: Country Name: CA, State or Province Name: Ontario, Locality Name: Toronto, Company Name: Quick24x7, and Email address: cblackwell@quick24x7.com. He clears the screen to run the new command. [Video description ends]

If I do an ls, we’ve now got the Ubuntu1server.req So if we cat the ubuntu1server.key file, this contains the private key. Remember, we generated an RSA key pair which consists of a public and a private key that are both related to each other, mathematically. [Video description begins] The page gets populated with output. The header of the output reads: BEGIN PRIVATE KEY. The footer of the output reads: END PRIVATE KEY. The presenter clears the screen to run the new command. [Video description ends] If we were to cat the ubuntu1server.req file, request file, this is actually the certificate request.

So what you would then do is make sure that you get this request file to the CA server. That might be done through email by submitting it in a web form, by copying it over the network using secure copy, whatever the case is, the CA needs this certificate signing request file. [Video description begins] The page is populated with output. The header of the output reads: BEGIN CERTIFICATE REQUEST. The footer of the output reads: END CERTIFICATE REQUEST. The presenter clears the screen to run the new command. [Video description ends]

Now because the server is also this same machine, it’s already available here. So I’m going to go into my easy-rsa directory, which is where I'm running my CA stuff from. From there I’ll run ./easyrsa, which is a script, import-req, of course, that means import request, and that’s back in my csr directory. And I’m going to refer to my Ubuntu1server.req file. And I want the output to be called ubuntu1server. Okay! I then get a message stating that the request has been successfully imported with the short name of ubuntu1server, that’s the last parameter I specified on the command line.

The next thing that the CA must do is using its private key, it must digitally sign the certificate. So I’ll run, within my easy-rsa directory, ./easyrsa, again that’s the script that’s part of the CA software I’m using. sign-req, to sign the request, and the server is Ubuntu1server

Now notice it says you're about to sign the following certificate. And here down below we have the original certificate signing request details. The country name, the state or province, the locality, and so on. [Video description begins] The presenter indicates to the following subject lines: countryName = CA, stateOrProvinceName = Ontario, localityName = Toronto, organizationName = Quick24x7, organizationalUnitName = HQ, commonName = www.quick24x7.com, and emailAddress =cblackwell@quick24x7.com [Video description ends] It says type the word Yes to continue. Okay! I’ll type the word Yes to continue. It wants me to enter that passphrase for the CA key. This would have been specify one I originally established the CA. Now this is important because that's the private key of the CA, which is used to create the digital signature to validate the certificate it is issuing. Okay!

Then it says the certificate is to be certified until and we’ve got date and timestamp by which time it will expire. So it’s good for a little over two years. [Video description begins] The message reads: Certificate is to be certified until Oct 13 12:31:48 2025 GMT (825 days) [Video description ends] And it says our certificate was created at, and we’ve got a path and name of a file.

So if I change directory to pki, change directory to issued because it's an issued certificate, [Video description begins] The presenter clears the screen to run the new command. He runs the new command: cblackwell@ubuntu1 :~ /easy-rsa/pki/issued$ ls [Video description ends] there is the Ubuntu1server.crt file.

So that’s an example at the command line on a Linux host of how you might acquire a PKI certificate from a private CA.

12. Video: SSL and TLS (it_oslsec_01_enus_12)

After completing this video, you will be able to recognize how transport layer security (TLS) supersedes secure sockets layer (SSL) for network security.
recognize how transport layer security (TLS) supersedes secure sockets layer (SSL) for network security
[Video description begins] Topic title: SSL and TLS. Your host for this session is Dan Lachance. [Video description ends]
HTTP network encryption is possible using two common protocol suites, one of which is deprecated. We’re talking about the Secure Sockets Layer or SSL Network Security Protocol Suite.

Now, this is deprecated because it’s older. It was started by Netscape in the early 1990s, but has since had various versions and has since been known to be vulnerable to many types of attacks perpetrated with freely available tools. So, in other words, you should never be using SSL. And this can be disabled both server’s side and on client’s.

Instead, we should be using Transport Layer Security or TLS. TLS was designed to supersede SSL, and it’s had variations as well over the years.

So with Transport Layer Security, we should be using at least version 1.2, ideally, the most current version 1.3. It’s important for security technicians to keep up with the latest versions of these things.

So TLS then, just like SSL, is enabled on HTTPS web servers. So you need a PKI certificate to enable an HTTPS binding which normally uses TCP port 443. But you can also determine if SSL or TLS is being used client side in the web browser settings or in some particular app settings. So TLS is always preferred then over SSL.

What's interesting is even today, many references in literature, even in GUI interfaces, will still refer to certificates as SSL certificates, when really that's a misnomer. It's not an SSL certificate, it's a PKI certificate.

And you can choose to use any number of network security protocol suites like SSL, TLS, IPsec, all of that stuff can use certificates. So don’t worry about it if an interface still shows you an SSL certificate, as long as you know it’s not being used on the server's side nor on the client's side.

So TLS communication. How does it work? In step one, a client would contact the server on the default HTTPS port, port 443, and present its supported ciphers. [Video description begins] The title of the page reads: TLS Communication. There are five steps given that the presenter elaborates on. [Video description ends] What does that mean? It means it tells the server, here are the encryption algorithms that I understand and support. Do we have something in common?

In step two, the server and the client will agree on a cipher suite to use.

In step three, the server will then send the client its PKI certificate information, which includes the public key of the server, not the private.

The client then confirms that the certificate is valid and trusted as per the PKI chain of trust and that it hasn’t expired and it will then generate a unique session key that happens client's side. It'll encrypt that session key with the server public key, which it now has, and send it over the network back to the server.

So the server, in step five, will decrypt that unique session key with its related private key. From then on in, that unique session key is used to secure the communication between the client and the server.

When you capture TLS network traffic, it's designed to look scrambled. Here we’ve got a packet capture being displayed within the Wireshark tool, where a packet has been selected in the top frame. Notice in the middle frame Transport Layer Security, or the TLS header, has been opened up where the version is shown in the field as being TLS 1.0. Ideally, we’ll be using 1.2 or even 1.3.

Down in the bottom frame on the left, we have the hexadecimal representation of the data in the payload of the packet. And on the right, we have the ASCII representation, which just looks like a bunch of symbols and letters and numbers. We can't make any sense of it. [Video description begins] The title of the page reads: Captured TLS Network Traffic. A screenshot is displayed below. It is divided into three sections. The first section shows a table with six columns, with headers such as: Time, Source, and so on. The middle section displays the TLS header with further details. The bottom section is populated with numbers and symbols. [Video description ends] If the text was sent in the clear, then we would be able to read back what was in the payload of that transmission. But that's not possible here because TLS is in use.

In the cloud, specifically in the Microsoft Azure Cloud, you can create a key vault resource within which you can then create or generate brand new PKI certificates. [Video description begins] A new page opens with the title: Microsoft Azure Key Vault PKI Certificate Creation. A screenshot is displayed below. The header inside reads: Create a certificate. A list of configurations is shown with their name fields, such as: Certificate Name, Type of Certificate Authority (CA), Subject, and so on. [Video description ends] Those certificates can be used not only by cloud services in the Azure cloud but by any service needing a certificate. Even an on-premises web server.

So the type of authority field, the third field down is set here to self-signed certificate. But of course, it can be specified that we are having the certificate issued from a public trusted CA.

The validity period is shown as being 12 months, so that's when it will expire. But that can be controlled as well.

We could then use that certificate to create an HTTPS web application binding.

Now, in this case, it's a web app hosted in the Microsoft Azure Cloud. What does that have to do with Linux? A lot! [Video description begins] A new page opens with the title: Microsoft Azure Web App HTTPS Binding. A screenshot of the Web App is displayed below. The header reads: quick24x7testing. It is divided into two sections. On the left pane, the Overview tab is selected. On the middle pane, Essentials and Properties are shown. The https prefix is highlighted on the URL. [Video description ends]

When you define a web application in the cloud, you can determine the platform on which it runs. There’s a virtual machine running somewhere to host your web app. And so, you can elect to have that running on the Linux platform, either as a Docker container for your web app or just a standard full HTTP web server stack running the code that you write for your web app.

Well, here in the properties of the web app in the cloud on the left, Overview has been selected. Over on the right, notice that the URL is being highlighted here showing that we have an HTTPS prefix. For that to work, you need to be using a PKI certificate. So you might not necessarily be configuring HTTPS type of security for a web app running on a pure Linux host to which you have full access, might be a managed cloud service.

So indirectly, you are managing Linux because Linux is running under the hood, but you don't have direct access to that host OS.

13. Video: Enabling an HTTPS Binding (it_oslsec_01_enus_13)

Learn how to configure a hypertext transfer protocol secure (HTTPS) binding for a web application.
configure a hypertext transfer protocol secure (HTTPS) binding for a web application
[Video description begins] Topic title: Enabling an HTTPS Binding. Your host for this session is Dan Lachance. [Video description ends]
In this demo, I will be configuring an HTTPS binding for a web server. Specifically, here on Ubuntu in Linux, I’ll be using the Apache 2 web server and I’ve already acquired a PKI certificate for use with the server from a private CA. [Video description begins] A blank Linux host page is open. The header reads: cblackwell@ubuntu1:~ [Video description ends]

Let's examine some of the prerequisites here first. First thing I want to do is run sudo apt install apache2 Now this means that the Apache web server is already installed [Video description begins] The presenter indicates the list of outputs that appears on the screen. He clears the screen to run the new command. [Video description ends] so we can verify this with sudo service apache2 status and notice that the Apache HTTP web server is showing as active and running. [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

If I do an ip a I know my private IP address here in this web server is 10.0.0.4 So if I were to run the curl command and specify http :// here I’ve just got the IP address of the server and I know it’s configured currently to listen on TCP port 82. [Video description begins] The presenter runs the command: cblackwell@ubuntu1:~$curl http://10.0.0.4:82 [Video description ends]

Okay! So we got the returned HTML so we know then that the server is up and running. What we want to do is have it listening on port 443 for HTTPS connections. [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

So on this server, if I were to change directory to easy-rsa/pki/issued/ and do an ls here we’ve got a certificate called ubuntu1server.crt

If we were to cat that file, then up at the top, we have the issuer here showing us CN, or common name, =ubuntuca. We’ve got the certificate validity of when it is valid and when it expires. [Video description begins] The validity period reads: Not Before: Jul 11 12:31:48 2023 GMT and Not After: Oct 13 12:31:48 2023 GMT [Video description ends] And we’ve got the subject details here, including the common name of the server which is set here in the certificate to www.quick24x7.com

So your server has to be configured to use that and DNSA or Quad A records must resolve to the IP of this server. Basically, when people connect to the website, the name and the certificate has to match what they're connecting to.

Notice as I go down further and look at the Extended Key Usage for this certificate, it says TLS Web Server Authentication, among other things. And again, the DNS Subject Alternative Name is showing as www.quick24x7.com

Okay! And then we’ve got the certificate details here. [Video description begins] The presenter points to the certificate output details. The header of the output reads: BEGIN CERTIFICATE. The footer of the output reads: END CERTIFICATE. A bunch of symbols, numbers, and letters are shown in the middle. [Video description ends] So what we should now do is run sudo nano /etc/hosts If you’re using DNS, modify DNS, [Video description begins] A new page opens with the header: GNU nano 7.2 /etc/hosts. A list of hosts' names is displayed, such as: ip6-localnet, ip6-allnodes, and so on. [Video description ends] but I’m just going to go ahead and pop in here the private IPv4 address followed by www.quick24x7.com and I’ll save that out. [Video description begins] The presenter types the private IPv4 address: 10.0.0.4 [Video description ends]

So therefore, if I were to go back in my command history, [Video description begins] The presenter clears the screen to run the new command. [Video description ends] I should be able to go back to my curl command and replace the IP address with www.quick24x7.com again still on port 82 currently and it’s still working. Okay!

Well, we know the name has to match what’s in the certificate when we enable our HTTPS binding. So that’s been done now. [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

So now I’m going to run sudo mkdir /etc/ let’s say we’re going to make a directory here called certificate, and I’m going to run sudo cp, to copy, my Ubuntu server certificate to /etc/certificate/

And I’m going to change directory to where I know I’ve got the certificate signing request, or CSR, for my Ubuntu server here. I've got the private key for the server. If I cat my ubuntu1server.key file, it’s the private key. Well, that also has to be present with the certificate on the web server. [Video description begins] The presenter clears the screen to run the new command. [Video description ends]

So I'm going to run sudo cp and I’m going to copy my ubuntu1server.key file. That’s the private key file to /etc/certificate/ Now if we do an ls of /etc/certificate/ we’ve got the server certificate and we’ve got the server’s private key. Perfect! [Video description begins] The server certificate name reads: ubuntu1server.crt. The server's private key name reads: ubuntu1server.key [Video description ends]

So now what we need to do is make sure the SSL module is enabled for the Apache web server. We can do that by running sudo a2enmod, enable module, and ssl If it’s already enabled, it will tell us down below, otherwise, it will enable it.

At the same time, we should also run sudo a2enmod, enable module, rewrite, to rewrite connections, let’s say from port 80 to port 443 if we want to do that.

After which we should restart the Apache web server, we can do that in a couple of ways, one of which is sudo service apache2 restart Okay, no errors and we'll just check the status here. [Video description begins] The presenter clears the screen to run the new command. He runs the command: cblackwell@ubuntu1:~$sudo service apache2 status [Video description ends] Looks like it's active and running.

However, we should also modify our web server conf file so it knows to listen on port 443. It knows to use SSL, it knows where the certificate is and the server’s private key.

So for that, I'm going to run sudo nano and I want to connect to /etc/apache2/sites-enabled/ and I want to get into the file called 000-default.conf or whatever the main config file is for your website. [Video description begins] A new page opens with the header: GNU nano 7.2 /etc/apache2/sites-enabled/000-default.conf. The first line reads: <VirtualHost *:443>. There are further details given below. [Video description ends]

In the Virtual Host block on the top, I want to make sure I’ve got :443 which is the standard HTTPS listening port. And I want to make sure down below I’ve got the SSLEngine directive. There’s no spaces between those two words and I want to make sure it’s set to on.

I want to then make sure I’ve got the SSLCertificateFile directive. Again, no spaces between those three words. And I want to make sure it points to the correct location of my server's certificate file, which normally ends with the .crt file extension.

And then, I want to make sure I have the SSLCertificateKeyFile directive. No spaces between those words, and make sure it’s pointing to the correct path and name of my web server private key file.

Let’s just get out of that file. Whenever you make changes to config files for Apache, you might want to run sudo apache2ctl configtest. Okay! The syntax is ok. That’s great news! Otherwise, we would have to correct any syntax errors before moving on.

Now, when you make changes to config files, you should, of course, always restart the appropriate service, in this case for Apache 2. So what we need to do is copy the CA certificate on this machine so that this machine trusts the certificates that that private CA has issued.

Now this server, which is our Apache web server, also is the server where I created the CA. So it’s very easy for us to copy the file.

I’m going to run sudo cp to copy. I'm going to specify the path and file name of that file and I’m going to copy it into the current directory. [Video description begins] The presenter indicates the file: /home/cblackwell/easy-rsa/pki/ca.crt [Video description ends] I’ve changed directory to /usr/local/share/ca-certificates on Ubuntu Linux, that’s where your trusted CA certificates have to go.

After that though, I have to do something else. I need to run the sudo update-ca-certificates command so it will read that location, see any new certificates that we've added, configure it so that this machine then trusts certificates from that CA.

And so if we go back to our curl command [Video description begins] The presenter clears the screen to run the new command. [Video description ends] where we’re connecting over HTTPS to our DNS name, now it returns the HTML for that web page instead of returning the error about not trusting the issuer of the certificate. So there you have it! We’ve successfully enabled an HTTPS binding for the Apache web server.

14. Video: Course Summary (it_oslsec_01_enus_14)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary. Your host for this session is Dan Lachance. [Video description ends]
So in this course, we’ve examined how to manage common Linux security threats and how cryptography can be used to secure Linux.

We did this by exploring common Linux security threats. We covered the CIA security triad and cryptography, and also, how to manage Linux file system encryption as well as network encryption. And we covered file integrity solutions.

Next, we generated file system hashes using common Linux commands. Then we covered PKI and the PKI certificate lifecycle.

Lastly, we deployed a Linux-based private CA, acquired PKI certificates from it. We covered SSL and TLS, and we enabled an HTTPS binding.

In our next course, we’ll move on to configure Linux authentication and authorization.

© 2023 Skillsoft Ireland Limited - All rights reserved.