CompTIA Linux+: Network Services
Using the Linux OS in the enterprise necessitates the use of network services to meet a variety of needs, including the Dynamic Host Configuration Protocol (DHCP), the Domain Name System (DNS), and the Network Time Protocol (NTP). Remote management and file transfers are common tasks performed by Linux technicians. In this course, you will begin by learning how and when DHCP should be used. Next, you will find out how to deploy a Linux-based DHCP server and configure a Linux DHCP client. Then, you will explore how DNS is used, deploy a Linux-based DNS server, and configure a Linux DNS client. Finally, you will configure network time synchronization with NTP, and remotely manage Linux through Secure Shell (SSH) and transfer files using secure copy protocol (SCP) and Secure File Transfer Protocol (SFTP). This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_06_enus_01)

    2. Video: Dynamic Host Configuration Protocol (DHCP) (it_oslsys_06_enus_02)

    3. Video: Deploying a Linux DHCP Server (it_oslsys_06_enus_03)

    4. Video: Managing DHCP Client Settings in Linux (it_oslsys_06_enus_04)

    5. Video: Domain Name System (DNS) (it_oslsys_06_enus_05)

    6. Video: Deploying a Linux DNS server (it_oslsys_06_enus_06)

    7. Video: Configuring DNS in Linux (it_oslsys_06_enus_07)

    8. Video: Network Time Protocol (NTP) (it_oslsys_06_enus_08)

    9. Video: Configuring Network Time Synchronization in Linux (it_oslsys_06_enus_09)

    10. Video: Configuring Secure Shell (SSH) in Linux (it_oslsys_06_enus_10)

    11. Video: Transferring Files Using SCP and SFTP (it_oslsys_06_enus_11)

    12. Video: Deploying an Apache Web Server (it_oslsys_06_enus_12)

    13. Video: Course Summary (it_oslsys_06_enus_13)

1. Video: Course Overview (it_oslsys_06_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance. [Video description ends]
Hi, I’m Dan Lachance.

Using the Linux OS in the enterprise necessitates the use of network services that serve a variety of needs, including DHCP, DNS and NTP.

Remote management and file transfers are common tasks that get performed by Linux technicians. So, in this course, I’ll begin by discussing how and when DHCP should be used, followed by deploying a Linux-based DHCP server, and configuring a Linux DHCP client.

Next, I will discuss how DNS is used, followed by deploying a Linux-based DNS server, and configuring a Linux DNS client.

Lastly, I will configure network time synchronization using NTP and I will remotely manage Linux through SSH, and transfer files using SCP and SFTP.

This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: Dynamic Host Configuration Protocol (DHCP) (it_oslsys_06_enus_02)

Upon completion of this video, you will be able to describe DHCP centralized IP configurations.
describe DHCP centralized IP configurations
[Video description begins] Topic title: Dynamic Host Configuration Protocol (DHCP). Your host for this session is Dan Lachance. [Video description ends]
The Dynamic Host Configuration Protocol or DHCP became very common in the early and mid-1990s. Prior to that, configuring TCP IP settings on a large scale for devices was either done manually on each device or by using a script.

So, DHCP then, is the centralized IP configuration that gets delivered to client devices over the network without administrative intervention.

So, the idea is that we can have a DHCP server in the form of a hardware appliance and in many cases DHCP is built into standard routers including Wi-Fi routers or a DHCP server could simply be a software that you install and configure within the operating system.

Let’s take a minute to look at the packet flow with dynamic host configuration protocol. In step number one, our client, depicted in the right-hand part of our diagram here, will transmit a broadcast on the local area network to discover DHCP servers. [Video description begins] A diagram representing Client device on the right connected to the DHCP server on the left through the LAN router is depicted on the screen. [Video description ends] Network broadcasts never cross routers, and, so, if there is no DHCP server available anywhere on that local area network, the client will not be able to properly partake in DHCP to acquire an IP configuration.

You can configure servers or routers on the LAN to forward DHCP discovery broadcast packets in terms of directing it to a DHCP server elsewhere on a different network. One way or another, in step one, clients discover a DHCP server.

Now, existing DHCP clients on the network when they have to renew their IP config, already know the server’s address.

Step two, the DHCP server will then respond to the client with an IP configuration offer. If you’ve got a DHCP server that services many subnets with different IP address ranges, it will know where the request originated and send the appropriate IP configuration information to the client.

Step three, the client will accept the offer and depending on how DHCP has been set up by the technicians, maybe there's a lease expiration date and time, which means that at a certain percentage of that time having been depleted, the client has to renew the lease with the server. Otherwise, it gets released back to the pool of IP addresses on the DHCP server, to then be reassigned to other DHCP clients.

Assuming everything works correctly in step four, the server will then acknowledge that the client has accepted the IP configuration that it put forth to the client, and then, the client is actively talking on the IP network.

Pictured on the screen, we have an example of how you would enable DHCP for IPv4, using the Ubuntu desktop. So, when you’re configuring network settings, [Video description begins] The Ubuntu desktop is displayed on the screen. It has the Wired tab open in Network settings. The Wired tab displays five options, namely: Details, Identity, IPv4 , IPv6 , and Security. The IPv4 Method shows three radio options: Automatic (DHCP), which is currently selected, Manual and Shared to other computers. The tab also has DNS and Routes options already set to Automatic. [Video description ends] you either manually enter IP configuration info or you set it to automatic through DHCP.

Then there’s the DHCP client side of things. Depending on which specific Linux distribution and which version of that distribution you’re using will determine exactly, what the file names and locations are of things like configuration files for DHCP clients and binaries that you can use commands to manage that DHCP client.

On Debian-based Linux distributions, Ubuntu Linux is a good example of that, you can set the dhcp4 option, to true, within /etc/netplan and within that netplan directory there'll be a network configuration file. So, open it up and then after you put that dhcp directive in it, apply it by running: sudo netplan apply. That way you don't have to reboot the Linux client. Of course, it behaves differently if the client happens to be using the MAC OS or if it’s Windows based.

If you want to set up a DHCP server on Linux, the first thing to consider is which package you want to use. There are many different options for selecting a DHCP server to run on Linux. One example, is a DHCP service called kea, spelled k, e, a. So, you would configure it in: /etc/kea/kea-dhcp4.conf [Video description begins] A command that reads: sudo apt install kea, appears on screen. [Video description ends] Within that conf file you'll have an open curly brace. And I’ve removed a lot of directives here to save on space, because the file can get quite long. But one of the things you’ll see inside that DHCP server config file is an interfaces statement, which means, which interfaces should DHCP bind to and listen for client requests on. [Video description begins] The interfaces statement within the dhcp4 conf reads: "interfaces": [ "eth1" } , [Video description ends] Then you can give it a subnet information.

Now, remember a DHCP server could accept client requests from many different subnets. So, in this case, we’re saying if it comes from subnet 192.168.4.0/24 then we’ve got a pool of IP addresses that we want to use, to hand out unique IPS to clients on that subnet. [Video description begins] The screen displays example subnet and pool statements. [Video description ends]

Now, of course, there’s a lot more you would configure for DHCP, including perhaps, a lease duration, the IP addresses of DNS name servers, the IP address of the default gateway and many other possible options. But this just gives us a sense of what that config file might look like.

On the security side of DHCP one consideration in highly secured environments is to ask yourself, do we even need to use DHCP? Because DHCP makes it easy for anyone that can get access to the network, to all of a sudden be active on the network and start communicating.

From a security perspective, it would be better not to use DHCP because anyone wanting to connect to the network, whether it’s a wired or a wireless client would need to know the subnet in use and so on. Now, there are ways to find that out with freely available tools. It's just more of a hassle. But, on busy networks with different client devices coming online, it might make more sense to use DHCP as opposed to having manual configurations, of course. So, it’s a give-and-take situation and usually, most things are when it comes to cyber security. Also, bear in mind, DHCP by itself provides no authentication of any devices connecting. In other words, if a device can get on the network and send out a DHCP broadcast, DHCP server will gladly make an offer to it.

The other thing to think about is that if a DHCP server itself gets compromised, then an attacker could alter client IP settings, essentially to prevent network connectivity from working correctly for DHCP clients, and that would be considered a form of a denial-of-services attack, if we’re preventing clients from connecting to the services that they need. So, bear that in mind when it comes to thinking about DHCP security.

3. Video: Deploying a Linux DHCP Server (it_oslsys_06_enus_03)

In this video, you will learn how to configure a Linux-based DHCP server.
configure a Linux-based DHCP server
[Video description begins] Topic title: Deploying a Linux DHCP Server. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I will be installing and configuring a DHCP server on Ubuntu Linux.

So, of course, we would use DHCP, because we want to have a centralized IP configuration that gets delivered to clients on the network that are configured to obtain their IP settings automatically through DHCP.

So, it saves us from going to each device to manually configure IP settings things like unique IP addresses, subnet masks, and so on.

So, the first thing I’ll do here on my server is run: sudo apt install. I’ll be installing the kea, spelt; k, e, a, dhcp server stack. So, it asks, do you want to continue? I will type in the letter y for yes, and I’ll press enter. Okay.

So, it’s pulling down the package from repositories over the internet and installing it locally.

So, the next thing I want to do is change the directory into /etc then into kea, k e a. If I do the ls here, we’ve got a file here called, kea-dhcp4.conf

Notice, we also have the option of configuring dhcp for IPv6 clients. [Video description begins] He highlights the command: kea-dhcp6.conf which is below the command: kea-dhcp4.conf [Video description ends] We’re going to stick with IPv4.

So, I’ll run sudo nano kea-dhcp4.conf and enter. So, we have a number of comments at the top here. The comments are notated here with two slashes at the beginning of the line. As I go further down in that conf file, I’ll come across a subnet listing for my subnet, and then down below I’ve got the pools where I can specify the range of IP's that I'm willing to hand out to dhcp clients.

Now, I can accept the default settings here that it determined, [Video description begins] He points at the subnet information and the pool ips, appearing on the screen. [Video description ends] or I can change them. Then down under the option-data section, I've got the IP address of a default gateway or a router. [Video description begins] The IP address, that he points to, reads: "data" : "192 . 0. 2.1" [Video description ends]

We can also configure dhcp "reservations" Reservations are useful if you know you want the same IP tied to a machine with a specific hardware or MAC address.

Think of things like network printers or other servers whose IP address really should not change. You just want to use DHCP to deliver it to them in a convenient fashion. But, back up here under the option "data" where we had our router or default gateway after the closing bracket for that section, we can put in a comma and then on the next line we can start a new open curly bracket.

We could specify "name" colon space Of course, the name is in double quotes "domain-name-servers", that goes in quotes, comma And, then "data" in quotes, colon space We could specify the IP addresses of one or more DNS servers. Then we’ll close off that section with the closing curly bracket and, so, we can make changes as we see fit to how we want DHCP configured in our environment.

But just realize that it should be "domain-name-servers", in plural. The dhcp server won’t load correctly if any of these things are entered incorrectly. Okay. Now, that that’s been caught, let’s control S to save that. Yes. We'll write it out to the conf file and enter.

Now, the next thing we need to do is, we need to make sure that the dhcp server for kea, reads those new settings.

So, I’m going to enter the sudo service kea-dhcp4-server status command. Let’s check to see what the status is. Okay, it's inactive, it's dead.

Fine, Let's bring it up and let's get it running. [Video description begins] The screen shows various comments including the Active status as inactive (dead) since Mon 2023-06-26 14:49:06 UTC; 14 min ago. [Video description ends] So, we’re going to run that same command, except we will change the status to the word start. And, let’s check the status now to make sure it was able to get up and running. And, it was, it says it’s active and running, so I’ll press Q for quit.

Now let's take a moment here to talk about the fact that you can use commands, such as, sudo journalctl, for log reading, you can specify, -u kea-dhcp4-server to view related messages for dhcp v4 and this is going to be important if you're having some kind of error condition and you're not sure what the problem is.

You could also run, sudo cat/var/log/syslog and grep that, | grep -i for case insensitive, perhaps, look for k e a, kea. And that would give you another way to view messages specifically related to your dhcp server daemon.

Okay, so, at this point, we’ve got an active dhcp server running that is configured with some IP configuration settings that can be handed out to DHCP clients.

4. Video: Managing DHCP Client Settings in Linux (it_oslsys_06_enus_04)

Find out how to configure DHCP client settings in Linux.
configure DHCP client settings in Linux
[Video description begins] Topic title: Managing DHCP Client Settings in Linux. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, we’re going to take a peek at how to work with the DHCP client side of things in Linux.

The first thing I’ve done here is, I’ve gone to my Ubuntu desktop machine where I’ve got the GUI installed.

However, the first thing, I think that we will do is check out some command line stuff. So, I’ll open up a terminal window here in the Ubuntu desktop.

The first thing we should consider is, whether or not, the network manager service is up and running. The network manager service is what actually controls the network configuration on Ubuntu Linux.

Now that’s not going to be the same for every Linux distribution out there. They do vary slightly when it comes to some of these configuration details.

So, here at the command line I’ll run, sudo service NetworkManager. Notice, that it’s capital N for network and capital M for manager. That's important. If we check the status of it, the first thing we want to do is make sure that it's active and running. But you’re also going to have some very important messages, basically logged items down before shown. [Video description begins] Various commands and statements appear on the screen. The host points on the Active status which shows, active and running. Furthermore, he points at the list of statements on the screen. [Video description ends]

So, if you have any error messages or warnings, you're going to see them shown down here. And that can be absolutely invaluable when you have to troubleshoot, why is this DHCP client not getting the correct IP settings from a DHCP server?

You could also, of course, run sudo cat /var/log/syslog and you could pipe that to grep and look for DHCP entries within there. So, you’ll see a number of DHCP transactions. And again, you might be looking here for any error messages.

One of the more recent DHCP messages in the system log that I see here, is some new lease information, it's date and time stamped, and the IP address assigned to this client. [Video description begins] Many lines of DHCP transaction statements appear on the screen. He points to the last line of DHCP transaction comment and explains it. [Video description ends] In this case, it shows the address of 192.168.2.40 Let’s check it out if I type: ip a, for the IP address, indeed, that is the IP address assigned to this host. And, of course, DHCP is really neat, because we don’t have to configure IP settings on all of the devices on the network. They just get it centrally from our configuration on the DHCP server. That DHCP server could be DHCP software installed on a host, it could be built into a router, including a wireless router, it could be built into a VPN appliance.

There are many forms of DHCP servers, but when it comes to configuring DHCP clients, we don’t really care what it is, we just care that we know it's there and that it's working. Now, if I have a desktop GUI, as I do, I can also check whether I'm using DHCP or manual IP configurations in the GUI.

So, here on Ubuntu desktop, I’ll just click to open up my menu of options here and I’ll search for the word network, and I’ll choose the advanced networking options. [Video description begins] The Network Connections window is now displayed. [Video description ends]

Okay, So here I’ve got an ethernet wired connection called, Wired connection 1 If I double-click on it, it pops up the details for it where I can click on IPv4 settings, it’s kind of over to the right a bit. Notice, it’s set for: Automatic (DHCP) as opposed to a manual configuration, where I would click the details, like the IP address, the Netmask, the Gateway, and so on and so forth. [Video description begins] On the Editing Wired connection 1 window, he clicks on IPv4 and points at the Method tab which is set to Automatic (DHCP). On changing the method from Automatic to Manual, a box named Address, with buttons Add and Delete appear. [Video description ends] But, even if I’m using DHCP, notice, I can specify additional DNS servers beyond what might have been delivered via DHCP. I can go to the command line again, and I enter: cat/etc/resolv.conf to see any name servers that might be configured in here locally on this device.

At the command line, I could also issue commands like sudo nslookup, name server lookup, where, if I type server, it’ll show me the default DNS server that we’re connected to for query purposes.

If I were to type www.skillsoft.com it’ll go out and try to resolve that name. Now of course, if the DNS server I'm pointing to doesn't know how to resolve www.skillsoft.com to an IP address, it should recursively by itself go out and talk to other DNS servers until it comes up with answers and here it’s come up with a couple of different IPv4 addresses for the skillsoft.com website, as well as, some IPv6 addresses. [Video description begins] He highlights the IP addresses for www.skillsoft.com that appear on the screen. [Video description ends] So, we know that DNS is working.

You want to be careful, because if I type exit to get out of that, if I rely on: ping www.skillsoft.com I’m not getting replies. But, what’s important to note is that it is resolving the DNS name here to an IP. [Video description begins] He points at the DNS name which is, www.skillsoft.com followed by the IP (18.191.63.135) [Video description ends] So, we’re not getting a reply.

We're going to assume that ICMP ping traffic is blocked at some firewall between us and skillsoft.com. I’ll press ctrl C to stop pinging. Let’s flip over to an Ubuntu Linux server where again we could issue sudo service NetworkManager status. However, notice, it returns: NetworkManager.service could not be found. And, it’s spelt correctly, I’ve got the capital N and M.

So, even within the Ubuntu desktop versus the Ubuntu server, there is a difference on how network configurations are handled. So, here on the server side, if I were to change directory to /etc/netplan and do an LS, I've got a configuration yaml file for my network configuration on this Ubuntu Linux server.

If I were to cat that file and pipe it to more, well, there’s not very much in there anyway, because we’re using DHCP. [Video description begins] He enters the command: cat 00-installer-config.yaml | more [Video description ends] Notice, that under network: ethernets: and here’s our interface. It’s called, ens 33, we’ve got dhcp4 set to a value of true. Of course, if I type ip space a to show IP information on this host, notice, for interface ens 33 we do have a valid IPv4 address that was acquired through DHCP. [Video description begins] He highlights the IP address for ens33 interphase that reads: 192.168.2.42/24 [Video description ends]

If you happen to be in a situation where you’re troubleshooting DHCP, you should also be aware you can run: sudo dhclient to manually force the DHCP client to do what it does to send out a broadcast, talk on the network and acquire an IP configuration. You could also pass it: -r for renew and give it the interface name just to perform a renewal if you just want to refresh it. [Video description begins] The refresh command on the second line, for dh client with the interphase name reads: sudo dhclient -r ens33 [Video description ends]

5. Video: Domain Name System (DNS) (it_oslsys_06_enus_05)

After completing this video, you will be able to outline how DNS is commonly used for name resolution.
outline how DNS is commonly used for name resolution
[Video description begins] Topic title: Domain Name System (DNS). Your host for this session is Dan Lachance. [Video description ends]
The Domain Name System or DNS, is a crucial component for enterprise networks and, of course, for accessing internet resources.

Normally, DNS is used to resolve friendly DNS names that are easy to remember, to IP addresses, which are more difficult to remember. Now, we say commonly because you can also do the opposite. Maybe you already know an IP address, because you were looking through firewall logs perhaps, and you'd now like to associate that with a DNS name so you can do reverse lookups as well.

But, by far forward lookups are the most common. So, if we can do forward and reverse lookups, that means in the DNS server side, there is support for forward and reverse lookup zones.

Now, there seems to be a lot of confusion all the time between a DNS domain name and a zone. The DNS domain name is just a text string like skillsoft.com. It’s just a name. The zone really refers to the underlying configuration supporting that name.

For example, a DNS zone file is a file for a zone like skillsoft.com that contains all of the DNS record information, that might even be replicated to secondary DNS servers as well. So, that’s a relationship then between a DNS domain name and a zone.

Let's take a look at a diagram related to forward name resolution. So, what we have in our diagram is a DNS client on the left that is querying, let’s say, for www.skillsoft.com. Perhaps, the user is simply entering that into the address bar of their web browser. So, the client will query that DNS name. It will look specifically for an “A” record. We’ll talk about DNS record types shortly and we’ll do that over (UDP) port 53 That's the standard port that DNS clients use to talk to DNS servers.

Now, in a perfect, simple world, the local DNS server your client is configured to point to for name, resolution would have the answer and would respond with the IP address for www.skillsoft.com directly back to the client. The reality is that if the local server is not authoritative over the skillsoft.com zone, it will forward off that query to servers that are including DNS root servers on the Internet that handle the top-level domains from which we can then, for example, find skillsoft.com and the record is sent back to the client. DNS servers can also cache the answer to DNS client queries depending on their configuration for a period of time.

Just like DNS clients can cache it in memory as well. This all happens very quickly. All the user knows is they're typing in the DNS name in a browser, for instance, and then they're connected. So, we said, we would talk about DNS zone record types.

So, we’ve mentioned already an A record. An A record is used to resolve a fully qualified domain name or an FQDN like www.skillsoft.com to its IPv4 address. So, the A record lives within the DNS zone for skillsoft.com in that example.

But nowadays we have IPv6 support. It’s become more and more popular. So, the equivalent for an IPv6 DNS record, IPv6 addresses are four times as long as IPv4. And, I suppose that’s why the record type is called a quad A record, AAAA. We also mentioned the notion of reverse lookup zones, meaning that you already know the IP, but what you're looking for is the DNS name. Well, for that you need PTR or reverse lookup records in a reverse lookup zone.

MX stands for mail exchanger, this is for SMTP mail transfer between servers. TXT records are rarely used, it's just a place to store some arbitrary information in DNS. It's not functional in any real way. [Video description begins] The screen shows various record types with their descriptions in a tabular format, while the host explains each of them. [Video description ends]

CNAME records are alias records that can point to other records like an A record. NS is the name server record, this specifies what’s called the authoritative server over a zone, the one that can write to the records.

We also have another special record type here called, SOA or Start of authority, and this contains some metadata about the DNS zone like the last update or who it's supposed to replicate to in terms of secondary DNS servers. So, these are some common DNS zone record types.

Pictured on the screen, we’ve got a screenshot of the Ubuntu desktop in the GUI, where the user has gone into their network settings and clicked on the IPv4 tab where notice the IPv4 method is showing us automatic DHCP, and the DNS server entry is also set to automatic, which means that this client will get its DNS server IP address or addresses who it sends queries to through DHCP. But, it is possible to have a client that gets everything else about IP through DHCP, but you configure DNS server entries manually. That's not been done here, but certainly, it's possible and it does happen. [Video description begins] The wired tab shows the IPv4 Method set to Automatic, DNS set to automatic and Routes, also set to automatic. [Video description ends]

Depending on the distribution of Linux you're running and the version will determine exactly where you go to configure network settings.

In Ubuntu Linux for example, you can configure DNS server entries manually at the command line if you want to do it at the file level by modifying the network configuration file in /etc/netplan [Video description begins] The pointer reads, DNS server entries can be manually set in, /etc/netplan/ <network configuration file> [Video description ends]

What you would do is, modify the nameservers address section or add it and add DNS server IP addresses and then to put that change into effect without restarting the Linux machine, you would then run sudo netplan apply.

On the security side of things with DNS, it’s important to always harden DNS hosts. Hardening means you’re reducing the attack surface, tightening up the security by applying updates and disabling unnecessary services and using complex passwords and that type of thing. We don’t want a DNS host to be compromised because an attacker could poison it, put in fake DNS records to redirect something like www.mybank.com to a fraudulent website that simply gathers user credentials. We don’t want that.

If you've got secondary DNS servers, especially across regions, to allow local DNS queries for clients, make sure that you limit or configure DNS zone transfers to those specific secondary servers and don't leave it wide open to replicate with any servers. Remember, we talked about the TXT record type? It’s rarely used, but what has popped up, over the years is that DNS TXT records will often contain malicious details such as addresses of command and control, or C2 type of servers, or even instructions that infected computers will reach out to. So, they’ll reach out to DNS to a query for the TXT record, maybe get some kind of malicious commands or the address of a command and control server, and then the client can do whatever it needs to do at the malicious level.

So, in other words, part of monitoring for security issues would be to detect potential security problems like this. DNS TXT queries are just rare. So, the fact, that it might be happening on your network should raise alarms. Another thing to think about is some DNS servers will support DNS security extensions or DNSSEC. Same goes with the clients. Some clients support this, some do not.

The idea is that you can digitally sign a DNS zone. Each record gets its own digitally signed record, which gets verified by clients to make sure it's authentic from that DNS server and has not been tampered with.

[Video description begins] Topic title: Domain Name System (DNS). Your host for this session is Dan Lachance. [Video description ends]
The Domain Name System or DNS, is a crucial component for enterprise networks and, of course, for accessing Internet resources.

Normally, DNS is used to resolve friendly DNS names that are easy to remember, to IP addresses, which are more difficult to remember. Now, we say commonly because you can also do the opposite. Maybe you already know an IP address, because you were looking through firewall logs perhaps, and you'd now like to associate that with a DNS name so you can do reverse lookups as well.

But, by far forward lookups are the most common. So, if we can do forward and reverse lookups, that means in the DNS server side, there is support for forward and reverse lookup zones.

Now, there seems to be a lot of confusion all the time between a DNS domain name and a zone. The DNS domain name is just a text string like skillsoft.com. It’s just a name. The zone really refers to the underlying configuration supporting that name.

For example, a DNS zone file is a file for a zone like skillsoft.com that contains all of the DNS record information, that might even be replicated to secondary DNS servers as well. So, that’s a relationship then between a DNS domain name and a zone.

Let's take a look at a diagram related to forward name resolution. So, what we have in our diagram is a DNS client on the left that is querying, let’s say, for www.skillsoft.com. Perhaps, the user is simply entering that into the address bar of their web browser. So, the client will query that DNS name. It will look specifically for an “A” record. We’ll talk about DNS record types shortly and we’ll do that over (UDP) port 53 That's the standard port that DNS clients use to talk to DNS servers.

Now, in a perfect, simple world, the local DNS server your client is configured to point to for name, resolution would have the answer and would respond with the IP address for www.skillsoft.com directly back to the client. The reality is that if the local server is not authoritative over the skillsoft.com zone, it will forward off that query to servers that are including DNS root servers on the internet that handle the top-level domains from which we can then, for example, find skillsoft.com and the record is sent back to the client. DNS servers can also cache the answer to DNS client queries depending on their configuration for a period of time.

Just like DNS clients can cache it in memory as well. This all happens very quickly. All the user knows is they're typing in the DNS name in a browser, for instance, and then they're connected. So, we said, we would talk about DNS zone record types.

So, we’ve mentioned already an A record. An A record is used to resolve a fully qualified domain name or an FQDN like www.skillsoft.com to its IPv4 address. So, the A record lives within the DNS zone for skillsoft.com in that example.

But nowadays we have IPv6 support. It’s become more and more popular. So, the equivalent for an IPv6 DNS record, IPv6 addresses are four times as long as IPv4. And, I suppose that’s why the record type is called a quad A record, AAAA. We also mentioned the notion of reverse lookup zones, meaning that you already know the IP, but what you're looking for is the DNS name. Well, for that you need PTR or reverse lookup records in a reverse lookup zone.

MX stands for mail exchanger, this is for SMTP mail transfer between servers. TXT records are rarely used, it's just a place to store some arbitrary information in DNS. It's not functional in any real way. [Video description begins] The screen shows various record types with their descriptions in a tabular format, while the host explains each of them. [Video description ends]

CNAME records are alias records that can point to other records like an A record. NS is the name server record, this specifies what’s called the authoritative server over a zone, the one that can write to the records.

We also have another special record type here called, SOA or Start of authority, and this contains some metadata about the DNS zone like the last update or who it's supposed to replicate to in terms of secondary DNS servers. So, these are some common DNS zone record types.

Pictured on the screen, we’ve got a screenshot of the Ubuntu desktop in the GUI, where the user has gone into their network settings and clicked on the IPv4 tab where notice the IPv4 method is showing us automatic DHCP, and the DNS server entry is also set to automatic, which means that this client will get its DNS server IP address or addresses who it sends queries to through DHCP. But, it is possible to have a client that gets everything else about IP through DHCP, but you configure DNS server entries manually. That's not been done here, but certainly, it's possible and it does happen. [Video description begins] The wired tab shows the IPv4 Method set to Automatic, DNS set to automatic and Routes, also set to automatic. [Video description ends]

Depending on the distribution of Linux you're running and the version will determine exactly where you go to configure network settings.

In Ubuntu Linux for example, you can configure DNS server entries manually at the command line if you want to do it at the file level by modifying the network configuration file in /etc/netplan [Video description begins] The pointer reads, DNS server entries can be manually set in, /etc/netplan/ <network configuration file> [Video description ends]

What you would do is, modify the nameservers address section or add it and add DNS server IP addresses and then to put that change into effect without restarting the Linux machine, you would then run sudo netplan apply.

On the security side of things with DNS, it’s important to always harden DNS hosts. Hardening means you’re reducing the attack surface, tightening up the security by applying updates and disabling unnecessary services and using complex passwords and that type of thing. We don’t want a DNS host to be compromised because an attacker could poison it, put in fake DNS records to redirect something like www.mybank.com to a fraudulent website that simply gathers user credentials. We don’t want that.

If you've got secondary DNS servers, especially across regions, to allow local DNS queries for clients, make sure that you limit or configure DNS zone transfers to those specific secondary servers and don't leave it wide open to replicate with any servers. Remember, we talked about the TXT record type? It’s rarely used, but what has popped up, over the years is that DNS TXT records will often contain malicious details such as addresses of command and control, or C2 type of servers, or even instructions that infected computers will reach out to. So, they’ll reach out to DNS to a query for the TXT record, maybe get some kind of malicious commands or the address of a command and control server, and then the client can do whatever it needs to do at the malicious level.

So, in other words, part of monitoring for security issues would be to detect potential security problems like this. DNS TXT queries are just rare. So, the fact, that it might be happening on your network should raise alarms. Another thing to think about is some DNS servers will support DNS security extensions or DNSSEC. Same goes with the clients. Some clients support this, some do not.

The idea is that you can digitally sign a DNS zone. Each record gets its own digitally signed record, which gets verified by clients to make sure it's authentic from that DNS server and has not been tampered with. [Video description begins] Topic title: Domain Name System (DNS). Your host for this session is Dan Lachance. [Video description ends]

The Domain Name System or DNS, is a crucial component for enterprise networks and, of course, for accessing Internet resources.

Normally, DNS is used to resolve friendly DNS names that are easy to remember, to IP addresses, which are more difficult to remember. Now, we say commonly because you can also do the opposite. Maybe you already know an IP address, because you were looking through firewall logs perhaps, and you'd now like to associate that with a DNS name so you can do reverse lookups as well.

But, by far forward lookups are the most common. So, if we can do forward and reverse lookups, that means in the DNS server side, there is support for forward and reverse lookup zones.

Now, there seems to be a lot of confusion all the time between a DNS domain name and a zone. The DNS domain name is just a text string like skillsoft.com. It’s just a name. The zone really refers to the underlying configuration supporting that name.

For example, a DNS zone file is a file for a zone like skillsoft.com that contains all of the DNS record information, that might even be replicated to secondary DNS servers as well. So, that’s a relationship then between a DNS domain name and a zone.

Let's take a look at a diagram related to forward name resolution. So, what we have in our diagram is a DNS client on the left that is querying, let’s say, for www.skillsoft.com. Perhaps, the user is simply entering that into the address bar of their web browser. So, the client will query that DNS name. It will look specifically for an “A” record. We’ll talk about DNS record types shortly and we’ll do that over (UDP) port 53 That's the standard port that DNS clients use to talk to DNS servers.

Now, in a perfect, simple world, the local DNS server your client is configured to point to for name, resolution would have the answer and would respond with the IP address for www.skillsoft.com directly back to the client. The reality is that if the local server is not authoritative over the skillsoft.com zone, it will forward off that query to servers that are including DNS root servers on the Internet that handle the top-level domains from which we can then, for example, find skillsoft.com and the record is sent back to the client. DNS servers can also cache the answer to DNS client queries depending on their configuration for a period of time.

Just like DNS clients can cache it in memory as well. This all happens very quickly. All the user knows is they're typing in the DNS name in a browser, for instance, and then they're connected. So, we said, we would talk about DNS zone record types.

So, we’ve mentioned already an A record. An A record is used to resolve a fully qualified domain name or an FQDN like www.skillsoft.com to its IPv4 address. So, the A record lives within the DNS zone for skillsoft.com in that example.

But nowadays we have IPv6 support. It’s become more and more popular. So, the equivalent for an IPv6 DNS record, IPv6 addresses are four times as long as IPv4. And, I suppose that’s why the record type is called a quad A record, AAAA. We also mentioned the notion of reverse lookup zones, meaning that you already know the IP, but what you're looking for is the DNS name. Well, for that you need PTR or reverse lookup records in a reverse lookup zone.

MX stands for mail exchanger, this is for SMTP mail transfer between servers. TXT records are rarely used, it's just a place to store some arbitrary information in DNS. It's not functional in any real way. [Video description begins] The screen shows various record types with their descriptions in a tabular format, while the host explains each of them. [Video description ends]

CNAME records are alias records that can point to other records like an A record. NS is the name server record, this specifies what’s called the authoritative server over a zone, the one that can write to the records.

We also have another special record type here called, SOA or Start of authority, and this contains some metadata about the DNS zone like the last update or who it's supposed to replicate to in terms of secondary DNS servers. So, these are some common DNS zone record types.

Pictured on the screen, we’ve got a screenshot of the Ubuntu desktop in the GUI, where the user has gone into their network settings and clicked on the IPv4 tab where notice the IPv4 method is showing us automatic DHCP, and the DNS server entry is also set to automatic, [Video description begins] The wired tab shows the IPv4 Method set to Automatic, DNS set to automatic and Routes, also set to automatic. [Video description ends] which means that this client will get its DNS server IP address or addresses who it sends queries to through DHCP. But, it is possible to have a client that gets everything else about IP through DHCP, but you configure DNS server entries manually. That's not been done here, but certainly, it's possible and it does happen.

Depending on the distribution of Linux you're running and the version will determine exactly where you go to configure network settings.

In Ubuntu Linux for example, you can configure DNS server entries manually at the command line if you want to do it at the file level by modifying the network configuration file in /etc/netplan [Video description begins] The pointer reads, DNS server entries can be manually set in, /etc/netplan/ <network configuration file> [Video description ends]

What you would do is, modify the nameservers address section or add it and add DNS server IP addresses and then to put that change into effect without restarting the Linux machine, you would then run sudo netplan apply.

On the security side of things with DNS, it’s important to always harden DNS hosts. Hardening means you’re reducing the attack surface, tightening up the security by applying updates and disabling unnecessary services and using complex passwords and that type of thing. We don’t want a DNS host to be compromised because an attacker could poison it, put in fake DNS records to redirect something like www.mybank.com to a fraudulent website that simply gathers user credentials. We don’t want that.

If you've got secondary DNS servers, especially across regions, to allow local DNS queries for clients, make sure that you limit or configure DNS zone transfers to those specific secondary servers and don't leave it wide open to replicate with any servers. Remember, we talked about the TXT record type? It’s rarely used, but what has popped up, over the years is that DNS TXT records will often contain malicious details such as addresses of command and control, or C2 type of servers, or even instructions that infected computers will reach out to. So, they’ll reach out to DNS to a query for the TXT record, maybe get some kind of malicious commands or the address of a command and control server, and then the client can do whatever it needs to do at the malicious level.

So, in other words, part of monitoring for security issues would be to detect potential security problems like this. DNS TXT queries are just rare. So, the fact, that it might be happening on your network should raise alarms. Another thing to think about is some DNS servers will support DNS security extensions or DNSSEC. Same goes with the clients. Some clients support this, some do not.

The idea is that you can digitally sign a DNS zone. Each record gets its own digitally signed record, which gets verified by clients to make sure it's authentic from that DNS server and has not been tampered with.

6. Video: Deploying a Linux DNS server (it_oslsys_06_enus_06)

During this video, discover how to configure a Linux-based DNS server.
configure a Linux-based DNS server
[Video description begins] Topic title: Deploying a Linux DNS server. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I will be installing a DNS server on Ubuntu Linux. There are plenty of DNS servers you can choose from and the same thing would be true when it comes to http web server stacks or DHCP servers and whatnot.

But they all share a lot of commonalities in terms of how they're configured. The fact that there would be a daemon running in the background and for DNS, of course, the standard is to listen for client queries on UDP port number 53.

Let’s get started here. I’m going to run sudo apt update because, I want to make sure my list of repositories from which, I can pull down software packages is up to date. So, that’s not updating my installed software, it's only updating my package repositories. Excellent. Okay.

The next thing I want to do is run sudo apt install. I want to install the bind9 standard DNS server, as well as the bind9utils package, with some command line utilities included and, also, bind9-doc. So, some documentation. So, each of these separate packages, I’m specifying in the command line separated with simply a space. I’ll press Enter. Okay, [Video description begins] The host runs the command that reads: sudo apt install bind9 bind9utils bind9 - doc [Video description ends] it asks, if I want to continue, I’ll type in y for yes and enter. Okay. So, it’s downloading and installing those packages for me. And, just like that it’s done.

If I issue the sudo service bind9 status command, it shows that in fact, our bind DNS server is up and running. Okay. So, that’s great. If I change the directory to /etc/bind [Video description begins] He points to the Active status for Bind DNS server that shows: active (running) with the date and time specifications. [Video description ends] we’ve got some config files here such as our named that stands for name daemon, by the way, .conf So, if we were to run sudo nano named.conf this is a parent file you could say that includes the configuration settings in the other files here, such as named.conf.options; named.conf.local, and so on.

So, I’m going to get out of here and let’s run sudo nano for named.conf.options The first thing is the directory where some of the files will go. The default is "/var/cache/bind"; You can also add additional options which I've done. I’ve added a keyword recursion and set it to, yes, to allow DNS client query recursion from this server to others. I’ve added the allow-transfer directive, and then within curly braces, I’ve specified { none; }; each of these lines. Of course, each end with a semicolon as well.

This means I will not allow zone transfers. I will not copy DNS records to secondary DNS servers, which is a good security setting. You might have an ACL section in here where you list trusted servers you want to allow the transfer to, but this is still a good security setting to have down below.

I can also specify a specific DNS servers I want to forward client requests to, if this server doesn’t have an answer. [Video description begins] He points to the command at the bottom that reads: forwarders { , 8.8.8.8; [Video description ends] Here, I’ve specified, for instance, 8.8.8.8; That’s followed by a semicolon. That's one of Google's DNS servers. So if I’m happy with this, I can go ahead and Ctrl S to save that out.

What I'm going to need to do is I'm going to need to restart the bind9 DNS server daemon. So, sudo service bind9 restart No news is good news, but let’s just check on the status anyhow. Okay, the DNS server is active and running. If you have a configuration file error like a syntax error, missing a semicolon or what have you, it'll normally prevent the bind DNS server from starting up. So, if you can’t start it up and you get errors, check the syntax in the conf files. Okay. So I'll type q.

Now, in the /etc/bind directory, if I do ls, there’s also a named.conf.local file. Let's run sudo nano against that file. [Video description begins] He runs the command as follows: sudo nano named.conf.local [Video description ends] Now, there's not really a whole lot in here, so, the way to create a forward lookup zone is, first of all, to begin by adding to this named.conf.local file, add the zone keyword and then in double quotes specify your zone, maybe, “sales.quick24x7.com”

Then, I would add a space and { and I'll move down to the next line where I'm going to specify that the type of zone is primary followed by a semicolon.

Then I will refer using the file directive to my zone file. So, in quotes, I’ll put "/etc/bind/zones/db.sales.quick24x7.com”; db for database. Files not there yet. Doesn’t exist, but it will. And, I’ll add } ;

So, I’ll press ctrl S and I will save that file. Now, we have to create our bind zone file. Now, if I do a ls here and, /etc/bind, there is no zones sub directory. So, I’ll go ahead and make one sudo mkdir zones Let’s change the directory to zones. I’m going to sudo cp, one level back, there is a file up here, you notice we’ve got a file called db.local? I can use that as a starting point, sort of a template, if you will, and copy that file into the current directory as sales.quick24x7.com.

So, this name has to match what we specified. Actually, I think we specified db.sales.quick24x7.com. Enter. And, if we do a ls, okay, in etc bind zones we’ve got our database file. Now we can edit it. So, I’ll use my nano editor to open that up.

So, like I said, this is kind of a little template, but I've gone ahead here and I've made a bunch of changes. So, for my start of authority, my SOA record, I’ve put in the name of my host. So, ubuntu2.sales.quick24x7.com You should set your hostname to be the same. Notice the trailing period at the end of that. I could change the admin details here, but I’ll just leave it at, root.localhost. that’s fine.

When you make a change to your zone file, you need to increment the serial number so that when you reload the bind9 DNS server daemon, it picks up changes. Down below, I’ve got a name server or [Video description begins] He changed the serial number from 3 to 4. [Video description ends] an NS record that identifies servers that are authoritative for this zone that can write to it. And, in this case, it’s the same thing as above.

It’s ubuntu2.sales.quick24x7.com, and I need an A record for that. Remember an A record is used to resolve FQDNs to IPv4 addresses. So, I’ve got my A record here for ubuntu2.sales.quick24x7.com. It’s an internet A record and I’ve got the IP address of that host. And, just for fun, I’ve added another A record for www.sales.quick24x7.com It happens to be pointing to the same IP address. It certainly does not. It should point to wherever that web server is. It's just an example.

Notice again, at the end of each of these FQDNs for the A record definitions, we have a trailing period. That's important. [Video description begins] He points at the period at the end of each of the A record FQDNs, that is www.sales.quick24x7.com. and ubuntu2.sales.quick24x7.com. [Video description ends] Okay, So I'm going to go ahead and save that out. Now, we've got some great utilities that will let us check our work both on the config files to make sure there are no syntax errors and on our zone files for the same thing, make sure there are no syntax errors.

For example, if I run sudo named-checkconf if you don’t get any errors output back it means that the syntax, at least, for the conf files for your DNS server are fine, but I can also use another bind utility. So, sudo named-check zone where I give it the name sales.quick24x7.com, followed by another parameter which is the path and name of our zone database file. Enter. If there are syntax errors, trust me, you’ll know. It’ll tell you on the screen. Here it says, it loaded serial 4

Remember, we made that change and it says, okay. Thank goodness, we don’t have any syntax errors in the config files or in our DNS zone file. So, the next thing to do, of course, is to restart our DNS server, sudo service bind9 restart No errors, we’re just going to verify the status. You just never know sometimes. Looks great. Active and running. [Video description begins] He enters sudo service bind9 status to verify the status and the command pulls the status values on the next screen. [Video description ends]

Now, if you've got a firewall running on this host, you want to make sure that client query traffic to UDP 53 is allowed. So, for example, I might run sudo ufw if you happen to be using the uncomplicated firewall product and I would say, allow Bind9 traffic. You could specify port numbers if you really wanted to, but that’s a built-in keyword that you can allow. And there you go. We've now got a DNS server up and running on our Linux server.

In another demo, we'll take a look at how to configure a Linux client with DNS settings.

7. Video: Configuring DNS in Linux (it_oslsys_06_enus_07)

Learn how to configure DNS client settings in Linux.
configure DNS client settings in Linux
[Video description begins] Topic title: Configuring DNS in Linux. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I’ll be configuring some DNS client settings on Linux hosts.

The first thing we’ll do is we’ll take a look at how to manually configure DNS servers on a client using Ubuntu Linux, specifically the server edition of Ubuntu Linux. What I’m going to do, to start is, do an ls of /etc resolv.conf. So, we have a file here, but notice it shows up as a symbolic link.

This can be verified by changing ls to ll for a long listing. [Video description begins] He points to the command: ll/etc/resolv . conf [Video description ends] Indeed, it is a symlink that points to resolv.conf under /run/systemd/resolv Either way, if we use sudo to take a look at with the cat command /etc resolv.conf there’s a note, up at the top that says you shouldn’t be editing this file.

However, notice that for the name server that's the DNS server listing. It’s got a stub IP for 127.0.0.53 In the past the resolv.conf file is where you would actually add your DNS name servers if you weren’t using DHCP that this host should connect to, to resolve names to IP addresses and it will vary between different Linux distributions and versions in terms of exactly where you go to configure this.

So, what I’m going to do then is run sudo nano I’m going to run my editor /etc/netplan and I’m going to open up my yaml configuration file here. Here I've already configured static IP addressing.

So, down under network, ethernets, and the name of my interface which is ens33: I’ve got dhcp4 set to a value of no. If you're using dhcp that will say yes or true. So I've got it set to no. And for the addresses item, I've specified a static IP address for this particular host using Cidr notation.

So, with the slash and the number of bits in the subnet mask down under routes, [Video description begins] The IP address that he points to reads : [ 192.168.2.156/24 ] [Video description ends] I've added a default route entry via my default gateway. And, what we’re really interested in here, nameservers, down under nameservers:

I've got a couple of addresses within square brackets, comma separated because I've got two DNS servers I'm pointing to. I'm pointing first to my own IP address because this server I am doing this on is actually a DNS server. [Video description begins] The host's IP address reads: [ 192.168.2.156 , [Video description ends] And then the second one, I'm just pointing to one of Google's DNS servers out on the internet at 8.8.8.8

Now, remember when you’re working with netplan yaml files, don’t use tabs to space these things, use spaces and the spacing is very important here. The indentation isn't only for making it readable, it actually has an influence on how this file is parsed. So, it’s very unforgiving.

At any rate, once you've made a change there, I already had the change there. You can run sudo netplan apply, to apply those changes, such as configuring DNS server entries. But what's interesting is even after you've done that and applied, your netplan changes, if you do a cat of, let’s say, /etc it will not reflect your new DNS server entries. [Video description begins] A page of information is now displayed with the things like, Run "resolvectlstatus" to see details about the uplink DNS servers currently in use. [Video description ends] For that, you can run sudo resolvectl status and, here, it will list the DNS servers as per your netplan configuration.

Now, this is important because it allows you to resolve names. [Video description begins] He highlights the Current DNS server IP that reads: 8 . 8. 8. 8 [Video description ends] For example, if I were to use ping www.google.com, we’re getting a reply. Okay, well, that’s good. We pinged it by name, it resolved it to the IP. We’re getting a reply.

If we were to ping another name like www.skillsoft.com well, it’s resolving the name to an IP, but we're not getting a reply and that's usually because it's firewalled.

Ping uses ICMP, the internet control message protocol, which is often blocked at firewalls, but we know it's working. We could also verify that it’s working using commands like nameserver lookup, nslookup.

If I were to just type in the word server and press enter, notice that for the default server it's showing the local DNS server stub that we saw on resolv.conf. 127.0.0.53 If you really wanted to, you could use the server keyword here and you could change it to any DNS server that you like.

Notice it's making a connection on Port 53, that's UDP port 53. However, when I change the DNS server in here, if I exit out and come back in to nslookup and type server, notice we're back to the initial config.

Either way, here in nslookup, we can simply type in what we want to look up. [Video description begins] After the exit prompt, the screen fills the previous Default server and address, which is: 127. 0. 0. 53 [Video description ends] For example, a DNS name www.skillsoft.com. And we have a number of non-authoritative answers back for IPv4 and IPv6 for the skillsoft.com name.

Non-authoritative simply means the DNS server we’re connected to doesn’t actually have the zone file for skillsoft.com but it went out and talked to other DNS servers to find the answer. You could also run set type=ptr if you wanted to search up reverse lookup or pointer records where you would specify the IP and if there is a reverse lookup zone available with the record for that IP, it would return back the name.

Notice what it does is reverses the IP address and tacks on the reverse lookup zone name of in-addr.arpa and returns back a name which in this case appears to be an ec2 instance or virtual machine running in Amazon Web Services. So, the nslookup tool then can be very useful. I’ll type exit.

You can also use the dig command, but it’s not interactive like nslookup for example, dig www.skillsoft.com and this is just another tool that will give us details about what we asked for, in this case, the skillsoft.com DNS name.

So, we’ve got the A records returned for IPv4 here as a result of running that command. Now here on a Linux desktop GUI machine, this happens to be running Ubuntu desktop.

We can also issue a lot of the same commands we did on Ubuntu server like sudo resolvectl status which turns back the DNS servers that we are pointing to. Of course, we can also open up some GUI tools to look at that as well. If I search my GUI tools here, let’s say for net,

I can choose my advanced network icon and if I go into my Wired Ethernet connection and go under IPv4 settings, even if we’re using DHCP, we can go ahead and add additional DNS servers here. So, depending on exactly which desktop GUI environment you’re using on top of your Linux OS will determine exactly where you click and what it looks like when you set DNS. But the underlying mechanisms remain the same.

8. Video: Network Time Protocol (NTP) (it_oslsys_06_enus_08)

Upon completion of this video, you will be able to recall how the network time protocol is used to synchronize network time.
recall how the network time protocol is used to synchronize network time
[Video description begins] Topic title: Network Time Protocol (NTP). Your host for this session is Dan Lachance. [Video description ends]
The Network Time Protocol or NTP, this is a very important concept as it’s important for time to be synchronized between devices over the network.

So, with NTP, we can have time synchronization between servers, but also, clients or any type of device really over UDP port 123. The specific details on how to configure NTP servers and clients will vary across Linux distributions and versions. The reason for this is because one distribution of Linux might use a particular NTP software package where a different distribution would use a different one.

And so, the syntax at the command line, the config files and so on, will vary, but the concept remains exactly the same. So, we know then, that we can have not only NTP servers that are time providers, which, by the way, can also get their time from higher level NTP servers that are considered reliable because NTP uses a time source hierarchy.

But, we know we can have NTP clients in the form of Linux stations, Windows stations, MAC OS, smartphones, network appliances. Anything that supports NTP is used to synchronize time over the network. Now there are a lot of packages or software solutions for NTP and Linux as we’ve mentioned, one of which is chronyd.

Now that's the daemon side for the server. It supersedes older NTP packages that were used previously in Linux.

So, why do we want to use this Network Time protocol? Everyone must agree on the time over a network, certainly, within an organization and of course, beyond really, as well. We need to have accurate, trustworthy date and time stamps for pretty much everything that's done on computers these days in the enterprise.

For things like Microsoft Active Directory, even for things like log-in, time stamps for users, we want to make sure that any log files, any audit files have the correct date and time in them.

Network services like DHCP rely on correct network time to determine, for instance, when a lease of an IP address given out to a client will expire. On the cybersecurity side, threat hunting tools will have a heavy reliance on correct date and time stamps to determine when something happened or to correlate suspicious events, perhaps even across platforms or networks.

If you are capturing network traffic, you want to make sure the packet captures have accurate date and time stamps. Otherwise, you don’t know exactly when, what you’re looking at occurred. And, of course, at the end user productivity level for document time stamping, creating documents, spreadsheets, invoices, all of this needs to be date and time stamped correctly.

One command we can issue in Linux is the timedatectl command. This command can be used to set the local system date and time and the time zone information. But by itself, as we have in our screenshot with no parameters, it returns back the local time of the device, which ideally will be exactly the same as universal time.

From time sources, the time zone will be shown and whether or not the system clock is synchronized and whether or not NTP is active. In this case, the clock is synchronized, NTP is active, everything looks good. It looks like time is in sync on this device with NTP time sources. Now, speaking of network time sources, these can be specified on an Ubuntu Linux host in /etc/system/timesyncd.conf Not only can you specify from where an NTP client should acquire the time, but you can also specify how often it should check that it’s in sync with the time source, so you can set a time polling interval.

Here we've got a screenshot where the technician has issued the systemctl status systemd-timesyncd command. This is the time sync or NTP daemon, which is showing here as being active and running and notice about halfway down in the screen output, for the status entry it says initial synchronization to time server and there’s an IP address here followed by : 123 because, we know, NTP uses UDP 123 for communication. So, initially went out and synchronized with an internet NTP server. [Video description begins] The host explains the Status, that reads, "Initial synchronization to time server 91. 189 . 94 . 4 :123 [Video description ends] Most NTP packages for time sync that you install will do this automatically. They will point to publicly available NTP time sources. You don't have to go and configure them unless you want to.

You might, for example, point only to internal NTP servers, especially if you have something like an air gapped network where you're not connected to the internet at all, which you might see in high security environments. At the NTP server level, we’ve mentioned that we have the chrony option, but there are some other options as well. You might choose to install the NTP daemon, which again is superseded by chrony, or you might install open-NTP.

If you are working with chrony to install it because you want to set up your own NTP servers, you could run: sudo apt install chrony; sudo nano/etc/chrony/chrony.conf to configure the config file; and then you would run sudo systemctl restart chrony.service

We’ll be taking a look at how to set up an NTP server in another demonstration.

9. Video: Configuring Network Time Synchronization in Linux (it_oslsys_06_enus_09)

In this video, find out how to configure NTP in Linux.
configure NTP in Linux
[Video description begins] Topic title: Configuring Network Time Synchronization in Linux. Your host for this session is Dan Lachance. [Video description ends]
In this demo, we’re going to take a few minutes to examine how NTP works in Linux.

Let's start here on a Linux server by simply issuing the date command. Of course, the date command returns, the date, the time, as well as some timezone information. Now what's critical here, of course, with network time protocol or NTP is that all of the devices on the network agree on the time.

Of course, we need that time to be correct, as different log files will be timestamped or end user productivity documents like generating invoices. A lot of these things will be time stamped and so it needs to be correct.

Another command we can issue here in Linux is timedatectl Here we've got a listing of the local date and time. That's for our specific time zone. Then we've got universal time and of course, our time zone is actually shown down below. We also have a reference as to whether our system clock is synchronized and whether we’re using NTP or not.

Notice that for NTP service it says, active. Now, this is not something I've configured. It's actually a default setting.

So, if I were to run sudo service systemd-timesyncd status so, this is a background daemon that’s running automatically. We get a listing here that says NTP is active. We get a listing here showing that the daemon is active and running. [Video description begins] A page of code is displayed which is headed: System clock synchronized : yes [Video description ends]

We have a date and time since that was true. And down below, next to status, the initial synchronization to a time server.

So, there’s a source out on the Internet. This is automatically done by default. It's pointing to an IP of that host. Interesting. So, in other words, Linux is set up as an NTP client out of the box and is synchronizing time, assuming it can talk to the internet. And the answer is, that’s true with the most distributions.

Yes, it will automatically be synchronizing time over the network. Of course, you have control over how that’s configured. One of the things that’s going to be important here is using sudo timedatectl list-timezones

Now, what we can also do actually is we can filter that by piping it to grep, let’s say, -i for a case insensitive match for the word Canada. So, here are the time zones that we can set. This is the notation that we would have to use within Canada so I could run sudo timedatectl set-timezone, for example, Canada/Atlantic This is how you would actually set that at the command line, because not only is it important that the date and time be correct, but of course, in order for that to work properly, to have the proper date and time stamps on our Linux host, we've got to be configured in the correct time zone.

Now not only can we act as an NTP client here in Linux, but we can also install and configure an NTP server. Why would we do this? We might do this because, within our enterprise network we want to control the time. Or maybe, we’re on an air gapped network that can’t talk to the internet. And so, we need our own reliable time source.

There are even external, precise time devices like atomic clocks, that can be connected to servers that serve as time servers so that they have their time from a reliable source. So, let’s say for example, we would run sudo apt install chrony Chrony is an example of an NTP time server package that we can choose to run. It’s not the only one out there though. Do you want to continue? Yes. And after a moment that part is done.

So, if I run sudo service chronyd for daemon status notice, it’s automatically up and running. And even though this isn’t an actual log file, [Video description begins] A page of code is now shown. The first line reads: chrony . service - chrony, an NTP client/server [Video description ends] of course, it can still be handy to take a look at some of the startup messages here, such as selecting a time source. Here we’ve got an IP address out on the internet that this server is talking to. NTP servers themselves can get their time from other reliable NTP time sources NTP servers, in other words. I’ll press Q to quit out of that and clear the screen.

I can also run sudo nano and open up /etc/chrony/chrony.conf What it’s doing down here is making references to NTP pools of publicly available NTP time sources. However, if you really wanted to, you could specify your own individual time sources here, such as within an enterprise network where you don't want to rely on time servers available out on the internet. However, I'll just control X out of that, clear the screen.

We can also issue commands like chronyc activity to make sure that our time sources are available, and it returns back, 200 OK 8 sources online. That’s great. That means that we can talk to those time sources. And if we are configured to get time from them, which is the default behavior for the chronydaemon, that’s good. We can also issue commands like chronyc clients to see if there are any client devices that are relying on us for time that are connected.

We could also type, chronyc sources to see where we are connecting to, to get our time. [Video description begins] A list of MS Name or IP addresses appear on the screen. [Video description ends] And these are some of the NTP servers available publicly out on the internet.

10. Video: Configuring Secure Shell (SSH) in Linux (it_oslsys_06_enus_10)

Discover how to enable SSH public key authentication in Linux.
enable SSH public key authentication in Linux
[Video description begins] Topic title: Configuring Secure Shell (SSH) in Linux. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I'm going to be configuring SSH. What I want to be able to do is from one Linux host, I want to be able to use SSH to have a secured command line connection to a remote Linux server.

Now, there are a number of ways to do this, one of which is through public key authentication. So, what I’m going to do is generate a public and private key pair here on my client, which is unique to this client. The private key will be passphrase protected and no one should have access to it except for the owning user on that station.

However, the public key can be shared with anybody, but, what needs to be done with the public key is it needs to be copied to the server so that the user is authorized to SSH, into that server because the private key on the client machine and the related public key on the server are both required to allow a SSH public key authentication.

Let’s get started here. So, here are my client machine. Notice, if I type pwd, print working directory, I’m in my user home directory, /home/cblackwell If I do an ls -a for all items, including hidden items, notice we have a hidden .ssh directory. if I change directory into it, [Video description begins] The host points at the .ssh prompt on the screen and enters the command cd . ssh on cblackwell @ ubuntudesktop1 [Video description ends] there’s nothing here other than known_hosts and known_hosts.old but there are no key files.

We’re going to go ahead and run: ssh-keygen to generate the key pair, so it asks me for the path and the file name, in which to save the key. Well, the key here in this context is the private key. Notice it wants to go in my current user home directory. So, /home/cblackwell in the .SSH hidden directory and it wants to call the private key file id underscore RSA. I’m okay with the default, I will press, enter.

Then it says you need to protect that file to private key file with a passphrase. So, I will enter and confirm a passphrase for the private key file. This means that even if somebody were to steal my private key file, if they don't know the passphrase, they can't actually use it. So, it returns back a unique fingerprint, which is great.

Let’s see what happened here, ls Okay, we know that we’ve got the private key file here called id_rsa We’ve got a mathematically related public key in the name of id_rsa.pub But what we need to do, is keep our private key here on our client machine. Doesn’t need to be on the server. However, the public key needs to be on the server, specifically in the user home directory in the .ssh hidden directory server side. Well, we can use the ssh copy id command to do this. Such as, ssh-copy-id the user, I want to authenticate as on the remote server because I know I have a cblackwell account there is, cblackwell @ and I’ll put in the remote host's name or IP address and I’ll press, enter.

So, it asks me to trust the authenticity of the unique fingerprint for that server as I’ve never SSH to it before. Are you sure you want to continue connecting? I'll type in, yes. And it asks for the password for that account on the remote server. So, I’ll enter it and press, enter. All right, it says, Number of key(s) added: 1 Now try to log in with ssh, and so on.

Let’s take a look server side at what happened for just a moment. Here, on my Ubuntu server, I am in the cblackwell home directory. Here on, the Ubuntu Linux server where we’ve copied the ID file, I’m already in the cblackwell home directory. If I change directory into .ssh, the hidden SSH directory, notice, we’ve got a file called authorized_keys We will wait a minute, I thought the ssh copy id file, I thought the ssh copy id command was supposed to copy the public key here. It did, it put it in the authorized keys file. If I cat the authorized keys file, that is the public key that resulted from our ssh key gen command. [Video description begins] The full command now reads: ssh$ cat authorized_keys after . ssh. [Video description ends] Notice down at the bottom, it’s got a reference to the username, cblackwell and the host on which that was done, Ubuntu desktop1. [Video description begins] He highlights the ubuntudesktop1 line at the bottom. [Video description ends]

So, the public key needs to be server side in the authorized_keys file for that user. The private key should never be on the server. So, back here on the client desktop, yes, the private key is here on the client id_rsa, all that we have to do in the future on this machine for this user is simply sign in to the remote Linux server using ssh cblackwell@ whatever the name or IP of the host is.

When I do that, it’ll pop up and ask me for the password to unlock the private key file. That’s a good thing. So, I’m going to go ahead and enter that in, after which, I am now signed in remotely to that Linux host. Notice, that my prompt has changed, I’m now user cblackwell not at Ubuntu desktop1 but at Ubuntu2. If I type ip a; I’m at the server, I’ve got the server’s IP here, 192.168.2.156 [Video description begins] He highlights the ip address that reads: 192 .168 .2 .156 / 24 [Video description ends] Notice also, that it did not prompt me for a password with ssh public key authentication. As long as you have the username, you possess the private key and, in our case, know the passphrase for the private key, you’re signed in.

It’s something, you know, the username and something you have, the private key file. If I type exit, I’ve closed out of that SSH connection. [Video description begins] He types exit on the screen and the prompt appears as follows: logout Connection to 192 .168 .2 .156 closed followed by cblackwell @ ubuntudesktop1 that says, .ssh clear [Video description ends] So, now I’m back as being cblackwell on my local ubuntu desktop1.

11. Video: Transferring Files Using SCP and SFTP (it_oslsys_06_enus_11)

During this video, you will learn how to copy files over the network using secure copy protocol (SCP) and Secure File Transfer Protocol (SFTP).
copy files over the network using secure copy protocol (SCP) and Secure File Transfer Protocol (SFTP)
[Video description begins] Topic title: Transferring Files Using SCP and SFTP. Your host for this session is Dan Lachance. [Video description ends]
Now that we've discussed how to set up SSH public key authentication, it would make sense then to talk about how to transfer files using SCP and SFTP.

Let’s start first with the SCP, the Secure Shell Copy command. This of course, is based on SSH authentication.

So, first of all, here I’m on my Ubuntu Linux server, where if I type, pwd for print working directory, I’m in the home directory for a user on the server called cblackwell. If I do an ls, we’ve got a projects directory and if I ls that, we’ve got some sample project files.

So, we’ll use some of these as our example of transferring files [Video description begins] The command: ls projects pulls the project files named: Project _ A . txt Project _ B .txt, and so on. [Video description ends] from the Linux server to a Linux client machine.

So, let’s switch to the client machine for a moment. Okay, I’m signed in, as a user by the name of cblackwell here on my client machine, I can type, id to verify the username. Of course, pwd to print working directory looks like I’m in my ssh hidden directory, in my user home directory, here on the client. [Video description begins] On the Linux client machine, . ssh id prompt pulls the client id, . ssh pwd gives /home/cblackwell . ssh [Video description ends]

Okay, so what we’re going to do is start by using scp. Actually, why don’t we take a look at the man page for it really quickly. The manual or help page; man scp- OpenSSH secure file copy, indeed, that is what it’s for.

Now, as you might guess, because it’s pretty much the same thing with most Linux commands, there are quite a few command line parameters. That’s a good thing, because it means we’ve got power, we’ve got flexibility, lots of options and there’s no shame in going into the man page to look up what the specific parameter or syntax might be for something.

For example, this -i; where you can select the file from which the identity or the private key for public key authentication is read. Okay, well, that would be important if you're using public key authentication with public and private key pairs, where the public key is on the server and the private keys on the technician station.

Even, -R, where scp is actually used on the remote server, for the copy session as opposed to scp being used locally, where lowercase r means, you can recursively copy entire subdirectory structures so, subdirectories within them and files, so, a lot of helpful stuff there. So, Q to quit out of that.

So, as an example, let’s say I were to run, scp cblackwell that’s the remote username on the server, the server, I’ll specify here with its IP address then colon. And I know that there are files under /home/cblackwell/projects such as, Project_A there’s some capital letters in there, .txt . and I want to copy that, let’s say locally to my current directory, so, dot. when I press, enter, we get a message back stating that 100% completion has occurred. The file is there, let’s see, ls Yeah indeed, Project_A.txt was securely copied over the ssh connection from the remote Linux server locally, but, it didn’t prompt me for authentication.

Now I'm going to log out of that session and log back in as user Cody Blackwell on that Ubuntu desktop. And I'm going to go ahead and fire up a new terminal window now that we’ve signed in, where I’m going to once again issue an scp command for cblackwell against that host, but the difference here, is I’m going to tell it to copy down, Project_B.txt, enter. We didn’t get this last time. [Video description begins] The scp command on the screen reads: scp cblackwell @ 192 . 168 . 2 .156 : / home / cblackwell / projects / Project_B . txt [Video description ends] It's prompting me to enter the passphrase to unlock the private key file. It knows I’ve got a private key file on my local machine, and a related public key in the home directory on the server.

Specifically, in the .ssh hidden directory, in the home directory on the server. It didn't do this the first time because I had already authenticated previously, but the reality is the first time you enter this, in a session SCP, you will be prompted to authenticate.

Okay, let me enter in the passphrase to unlock the private key, and I’ll press, enter, now we have 100% completion and if I do an ls indeed, there's Project A, there's Project B, but remember in the man page, lowercase r was recursive. And this is a very common parameter that’s used with secure copy. There are times you'll want to copy entire subdirectory structures and everything in them. That’s precisely what we’re going to do here. So, let’s copy down an entire sub directory structure then with scp -r recursively, the username on the remote server is, cblackwell@ and I’ll specify the remote server’s IP address.

Now on that remote server, I have to tell it the directory I want to copy. So, :/home/cblackwell/projects/ I want to copy the entire project sub directory and everything within it. That’s going to happen because of the -r. Where would you like to put that locally? How about, ./current directory just in a folder called projects, enter. Okay, wow, it looks like it found all of those sample project files in the server in the projects directory. [Video description begins] There are several projects and information about their status now listed on the screen. This includes : Project _ D . txt 100% 17.2KB/s , Project _ A . txt 100% 87.6KB/s , and so on. [Video description ends] If I type ls, looks like we have a projects directory here on the local machine. And if I ls the local projects directory, that’s where those sample project files are.

So, SCP is very easy to use and the beauty of it, is that you’re transferring files over a secured connection, an encrypted connection.

Now alternatively, you might choose to use SFTP, Secure FTP as a secure way to transfer files where I would type sftp, my username on the server, cblackwell@ and then of course the server’s identity, in this case, we’re going to use the IP address.

Now what this will do, if that's all I provide on the command line, is it will give me an interactive sftp command prompt that says I’m connected to the server’s IP address. so that, within sftp, if I type pwd, print working directory, it returns the remote working directory, which is, home/cblackwell.

Therefore, if I type ls, we’re seeing what’s on the server that’s not local. To see what’s local, [Video description begins] When he runs ls on sftp, the return prompt shows: results including cblackwell _ files; filelist . txt and so on. [Video description ends] for example, I could say lpwd and when I do, it says, Local working directory. And of course, it’s got the path to my local working directory for my user. So, if I type, lpwd, local print working directory, it returns the local working directory as being, /home/cblackwell

However, if I still type ls, that's still happening in the server side. That's not the same contents of what we have in our local directory. For that, I could type in, lls, local list files, that looks different. So, the command set is a little bit different when you’re working with sftp. So, let’s say I want to copy one of my local files here. sample_local_file.txt that’s on my local machine, I want to upload that to the server. So, I can do that by using the put command, put sample now I can just use my tab completion here and if I don’t give it another parameter, it will call it the same thing and put it in the server’s current working directory.

Okay, so, it looks like it copied it up to home cblackwell And there’s the name of the file.

So, on the server, we can see the contents there just simply by typing, ls. That’s server side, remember, because lls, would be local. Sure enough, there's the sample local file. If I want to download files I can use get. Let's say I'm interested in file list txt. I can issue the command, get filelist.txt and if I don't specify any parameters, the file will be called the same thing and stored in the local working directory. So, if I type, lls, local list files, sure enough, there’s file.txt type exit to get out of my sftp session. So, that gives you an idea then of how you might use, secure methods of transferring files between Linux hosts using SCP and SFTP.

12. Video: Deploying an Apache Web Server (it_oslsys_06_enus_12)

Find out how to install the Apache web server on Linux.
install the Apache web server on Linux
[Video description begins] Topic title: Deploying an Apache Web Server. Your host for this session is Dan Lachance. [Video description ends]
In this demo, I’m going to be installing an Apache Web Server. So, the first thing we have to consider, of course, is the planning aspect of it. Why do you need a web server? Is it for a public facing web app? Is it for an internal line of business app? Is it for software developers for testing? And then of course, pick a host on which the web server will run.

So, I’m sitting at the Ubuntu Linux server where, I want my Apache2 web server stack up and running.

So, the first thing I’ll do then, is get it installed, sudo apt update. I'm going to update my list of package repositories. I do have a connection to the internet from this server.

Now, I don’t want to do an upgrade, because I’m not interested in upgrading anything already installed on this server. So, now I’m going to run, sudo apt install, and I know that [Video description begins] He types in, clear and moves to the next screen. [Video description ends] the Apache2 web server is simply called Apache2. Okay, it won’t take very long for that to happen. If I now run, sudo service apache2 status, the Apache web server is inactive or dead, so it's not up and running.

So, let’s go ahead and run, sudo service apache2 start Then we’ll check its status and now it shows as being up and active and running. Now, what we should really do here is make sure that we are allowing traffic to the web server.

So, we can run, sudo ufw, because I know the uncomplicated firewall is running on this host and I can put in, allow and let’s say 80/tcp

Now if we're going to be using Port 443 because we've got a PKI certificate for https, then we would allow that traffic, as well. If I do an ls of /etc/apache2; notice that we’ve got a number of config files in here.

So, if I were to run, sudo nano/ etc/apache2/apache 2.conf this is the main config file for the Apache web server. [Video description begins] The config file shows several lines of comments, each starting with # on the screen. [Video description ends] However, notice that there are some variables and items being referenced here that are used by other files. For example, the user and group references here need to be set in /etc/apache2/envvars; environment variables. [Video description begins] He points to the variables, User {APACHE_RUN_USER} and Group {APACHE_RUN_GROUP} under /etc/apache2/envvars [Video description ends]

Most more complex software packages will not have a single configuration file, but rather numerous config files where you might have a global or a parent config file that references others. Notice, there are also include statements, like, include the ports.conf file. There are subdirectory options for web server directories.

Notice that there’s a reference here for /var/www/> Okay, well, we’re not going to change anything here, so, let’s ctrl X out of it, from one of our previous commands, notice, for example, the ports.conf file in /etc/apache2 If we were to cat that file and pipe it to more, [Video description begins] The entered command reads: cat / etc/ apache2/ ports .conf | MORE [Video description ends] in case, there’s a lot of content.

Notice the default listening port for the web server is set to port 80. There's also an if module block here that states that if we do have the ssl module enabled for the server to Listen also on Port 443, ideally you won’t be using ssl, rather, tls ssl is deprecated and has known security issues. [Video description begins] The IfModule for tls reads: < IfModule mod_gnutls.c> [Video description ends]

If I were to do an ls of /var/www notice, we’ve got an html directory in which we’ve got an index.html. That's the default location for website files. Also, if I do an ls of /var/log/apache2/ it's got its own subdirectory for logs.

This is where we've got various logs for the Apache web server. I’m going to type ip a, so, the server’s IP here is 192.168.2.156 Let's just test a connection to it from a web browser to pop up the default web page. So, when I enter that IP address into my browser’s address bar, it pops up the Apache2 Default Page and it says Ubuntu. It works.

Now of course, it’s not a secured connection because we don’t have a PKI certificate and an https binding configured. [Video description begins] He points on the address bar where it says, not secure followed by the ip address. [Video description ends] Okay, so, we’ve got our basic Apache2 Default web server up and running. At this point, it would be up to software developers to develop the website appropriately and place the files in the web server directory.

13. Video: Course Summary (it_oslsys_06_enus_13)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary. Your host for this session is Dan Lachance. [Video description ends]
So, in this course, we’ve examined how to manage various network services such as DHCP, DNS, NTP, SSH, and we also looked at how to transfer files using SCP and SFTP.

We did this by exploring how to deploy a Linux DHCP server and managing DHCP client settings.

We also took a look at deploying and configuring Linux DNS servers. We also configured Linux NTP and SSH and we transferred files using SCP and SFTP. And lastly, we deployed a basic Apache web server.

In our next course, we’ll move on to manage Software repositories, packages and take a look at how to build Software packages from source code.

© 2024 Skillsoft Ireland Limited - All rights reserved.