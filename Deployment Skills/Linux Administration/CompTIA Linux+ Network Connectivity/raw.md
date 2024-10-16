CompTIA Linux+: Network Connectivity
Linux distributions support IPv4 and IPv6 addressing. Technicians must be familiar with standard commands that can be used to manage all aspects of Linux networking. Begin this course by focusing on how to plan for the use of IPv4 and IPv6 on a network. Then you will explore common Linux commands used to manage networking, such as ifconfig, arp, route, nslookup, and more. Next, you will learn how to manage Linux network interfaces and IP settings at the command line, and how to manage IP routing. Then you will use tcpdump and Wireshark to capture and analyze network traffic. Finally, you will examine the use of rsync to synchronize files between Linux hosts. This course can be used to prepare for the Linux+ XK0-005 certification exam.
Table of Contents
    1. Video: Course Overview (it_oslsys_04_enus_01)

    2. Video: IP Addressing (it_oslsys_04_enus_02)

    3. Video: Common Linux Networking Commands (it_oslsys_04_enus_03)

    4. Video: Managing Linux Network Interfaces and IP Addressing (it_oslsys_04_enus_04)

    5. Video: Network Routing (it_oslsys_04_enus_05)

    6. Video: Configuring Linux Routing in the Linux OS (it_oslsys_04_enus_06)

    7. Video: Configuring Linux Routing in the Cloud (it_oslsys_04_enus_07)

    8. Video: Capturing and Analyzing Network Traffic Using tcpdump (it_oslsys_04_enus_08)

    9. Video: Capturing and Analyzing Network Traffic Using Wireshark (it_oslsys_04_enus_09)

    10. Video: Sychronizing Files Between Hosts Using rsync (it_oslsys_04_enus_10)

    11. Video: Course Summary (it_oslsys_04_enus_11)

1. Video: Course Overview (it_oslsys_04_enus_01)

In this video, we will discover the key concepts covered in this course.
discover the key concepts covered in this course
[Video description begins] Topic title: Course Overview. Your host for this session is Dan Lachance. [Video description ends]
Linux distribution support IPv4 and IPv6 addressing and so, technicians need to be familiar with standard commands that can be used to manage all aspects of Linux networking. In this course, I'll begin with planning for the use of IPv4 and IPv6 on a network.

I will then discuss common Linux commands that get used to manage networking such as ifconfig, arp, route, nslookup, and more. Next I'll manage Linux network interfaces and IP settings at the command line, followed by managing IP routing. I will then use tcpdump and Wireshark to capture and then analyze network traffic. Lastly, I will use rsync to synchronize files on and between Linux hosts. This course can be used to prepare for the Linux+ XK0-005 certification exam.

2. Video: IP Addressing (it_oslsys_04_enus_02)

After completing this video, you will be able to plan for IPv4 and IPv6 addressing needs.
plan for IPv4 and IPv6 addressing needs
[Video description begins] Topic title: IP Addressing. Your host for this session is Dan Lachance. [Video description ends]
Managing the network components in the Linux environment means understanding IPv4 and IPv6 addressing. Let's start with IPv4. IPv4 uses 32-bit IP addresses. Bits, of course, are zeros, and ones, and various combinations of those up to 32 uniquely identify a host or a device on an IPv4 network. IPv4 uses a dotted decimal notation where we have a dot that separates each group of 8 bits, 8 bits is a byte. So, you have four components then to end up with 32 bits in an IPv4 address, and each of those four components are separated by a dot or a period. IPv4 has been around for a very long time, it's been an IP addressing standard since the 1970s. If we map IP addresses to the Open Systems Interconnect or the OSI model, we would find that IPv4 addressing would apply to layer 3 of the OSI model of the network layer.

You might recall that the network layer deals with things like routing such as IP routing, and also things like software network addressing like IP addressing, whether it's IPv4 or IPv6, it would still apply to layer 3, the network layer. So, we know then that we've got four components in an IPv4 address. Often they're just called octets, each of the four of them because they're collections of 8 bits, zeros and ones, so separated by periods. Now mathematically, IPv4 addresses are represented as decimal values, base 10 numbers. And so, given that, each octet when it comes to decimal notation would have a numeric value that would fall somewhere between 0 and 255. Although there are some special use addresses, 255 in some contexts will mean a broadcast address, a transmission sent to everybody, for instance, on a subnet, and depending on where it is in the IP address, such as at the very end on the right, a 0 can be used to notate a reference to the current network as a whole when it comes to addressing purposes.

An example of a valid IPv4 address would look like 192.126.128.190. Notice that if you had .300, for example, that's just impossible, it's not possible mathematically when you convert binary ones, 8 of them to decimal to get beyond 255. With IPv4, there are some reserved IP address ranges. What this means is that they are reserved for internal use in that routing equipment, both internally within the enterprise and out on the Internet, will not route packets within these ranges. There's the 10.0.0.0 through to the 10.255.255.255 range, then we've got the 172.16.0.0 through to 172.31.255.255 range. And finally, what we're probably all more familiar with since it's used a lot with home network equipment, would be 192.168.0.0 through to 192.168.255.255.

So, any addresses within those ranges do not get routed over the Internet. You might have an infrastructure internally in an enterprise network where the routers are configured to allow that. But generally speaking, they don't get routed. Then there's the notion of subnet masks. So, when you configure an IP address on a host, you also configure a subnet mask, and the mask defines which part of the IP address is the network versus the host address. It's kind of like a telephone number. A part of the telephone number has a country code, an area code, a local exchange, and then finally, last four digits of a telephone number uniquely identify a given handset. Well, the same is true here in the sense that we have one part of the IP identifying the network and the rest of it identifying a host or a device on that network.

You can represent a subnet mask depending on what you're using for a tool or a GUI interface in decimal notation base 10. So, for example, if you have a subnet mask of 255.255.255.0, 255 means all of the binary bits are turned on to a value of 1. So, it means that the first 3 octets, the first 3 bytes of the address identify the network and only the last octet, the last byte, or the last 8 bits would identify a host on that network. You could also reference that in a different way. So, instead of that decimal notation for the subnet mask, sometimes just called the network mask, you could also use the CIDR notation method. CIDR stands for Classless Inter-Domain Routing. But to get right to the point, instead, of all those 255s and the 0s, you could just say /24, which means you've got 24 bits set to a value of 1 starting from the left, which makes sense, we've got 3 octets here. 8 times 3 is 24, but that's IPv4. A lot of the same concepts would apply to IPv6.

But there are definitely differences. For example, IPv6 addresses are four times longer than IPv4. Instead of only being 32 bits long, IPv6 addresses are 128 bits long. Now, IPv6 has been around for a couple of decades now, but it's only really been widely adopted for less than that. We start seeing it being included automatically in consumer-grade and networking products and also built into operating systems and being enabled, such as with Linux and Windows, and macOS variants. Now, instead of using a dot or a period to separate each octet in an IPv4 address, in IPv6, it uses hexadecimal representation, so base 16, not base 10. Hexadecimal means that you start counting at 0 and then once you get up to 9, instead of using 10, because it's not base 10, it's hexadecimal, you would use the letter A, which means 10, the letter B means 11, and so on, all the way up to 15.

Now remember hexadecimal 16, you start counting at 0, all the way up to 15, that's 16 placeholders, you end up with F, which stands for 15, and it separates each portion not with the dot or a period, but with a full colon. So, instead of an octet, you could say you have a hextat, four of which are separated with colons. An example is shown here of an IPv6 address. It's a combination of hexadecimal characters such as fe80:: The two colons is simply shorthand for referencing 4 zeros there. Then we have 20c:29ff, and so on. And then the mask is represented here /64, the network mask. So, as you might imagine in this day and age being a Linux technician demands that we have an understanding of IPv4 and IPv6.

3. Video: Common Linux Networking Commands (it_oslsys_04_enus_03)

Upon completion of this video, you will be able to use common Linux networking commands such as ip, ifconfig, hostname, arp, route, dig, nslookup, traceroute, curl, wget, nc, and netstat.
use common Linux networking commands such as ip, ifconfig, hostname, arp, route, dig, nslookup, traceroute, curl, wget, nc, and netstat
[Video description begins] Topic title: Common Linux Networking Commands. Your host for this session is Dan Lachance. [Video description ends]
Let's take a few minutes to talk about common Linux networking commands. Being able to master network configurations and network statistic viewing from the command line is a crucial skill for Linux technicians. The first thing we have to go through is the fact that we could have one or more network interfaces on a given Linux host, whether it's a client desktop machine or whether it's a server, whether it's physical or virtual, it makes no difference. Now you can expect to see an interface called lo which is the local loopback interface. But then you might see interfaces such as eth0 for Ethernet0, eth1 for the second network interface card, or it might be called something different like ens33. And for wireless interfaces, you might see interfaces like wlan0, wlan1, and so on.

Now some Linux networking commands will require you to specify an interface. Now, while we are focusing on command line management of Linux network components, you can also do this using a graphical user interface or a desktop if you've got that installed on a given Linux host. Here's a screenshot of Ubuntu desktop where you can go into the network settings in the GUI and here

[Video description begins] A slide labeled Ubuntu Desktop Network Settings appears. It displays a Wired screenshot. It contains 2 tabs: Cancel and Apply. It further consists of the following sections: Details, Identity, IPv4, IPv6, and Security. The Details section contains the following options: Link speed, IPv4 Address, IPv6 Address, Hardware Address, Default Route, and DNS. [Video description ends]

the details of a network interface are being shown. It's a wired network interface. We've got an IPv4 address, an IPv6 address, the hardware or the MAC address of the network interface is shown, the DNS server, the Default Route, or the default gateway. So, all of this can be configured whether it's through DHCP and delivered to the client, or whether you configure it statically or manually. But let's get to the command line so Linux networking commands. The first thing we have is ifconfig, interface config.

This is an older command. You might have to install this package if it's not already present on your Linux distribution or you could opt to use newer equivalent types of commands that we will talk about. Well, let's start with this one. First thing we could do is issue ifconfig -a, in other words, list the active network configurations. You could pick on a specific interface to view its configuration, such as ifconfig eth0, if that interface is down, you can bring it back up using ifconfig eth0 up, of course, you can bring it down using the down suffix as well. Sometimes you might do this to have a new configuration put into place or for troubleshooting reasons. At the command line, you might even assign an IP address using ifconfig, in this case, the name of the interface eth0, and you could statically assign it an IPv4 address. We'll talk more about setting persistent network settings later because that's only at the command line for that current session.

But ifconfig, as we've mentioned, is a bit of an older Linux command. It still works and you might have to install it, but what you'll find is more prevalent now on modern Linux distributions is simply the IP command set. For example, ip -4 a, as you might guess, would show IPv4 addressing information on that Linux host, where ip -6 a would show, of course, the IPv6 addressing information on that host. You could also just issue ip a to view all IP addressing, whether it's IPv4 or IPv6 for all network interfaces. You could type in commands such as ip a show eth0. Of course, it only shows that network interface and its details. You could also, just like with ifconfig, add a manual IP address configuration at the command line for the current session with ip a add, give it an IP address, in this case, the network mask is shown with /24, and then dev for device, eth0. You've got to tie that IP address to a network interface, of course.

Other Linux networking commands would include things like hostname which returns the local machine name, also the arp command, ARP stands for Address Resolution Protocol. So, the arp command lets you view and manage the ARP cache in memory on that local Linux host, where the ARP cache contains information for IP addresses that are mapped to MAC addresses for local area network hosts and devices. The MAC address is irrelevant when you are talking to a machine or a device on a remote network. The only MAC address that's relevant in that context would be your default gateway's MAC address to get out of the local area network. And then we've got a whole bunch of other Linux networking commands, such as route which is used to view and manage the IP routing table on the Linux host, traceroute which shows all of the routers that your traffic goes through between your local machine and the specified target.

Then for DNS name resolution, we've got two tools, dig and nslookup. One of the differences is that nslookup has an interactive Command Prompt mode if you want to work in that context. We have curl, the Client Uniform Resource Locator command which is used to transfer data to the machine over protocols like FTP and HTTP. You've also got the get command which can be used to do that as well, the netstat command to monitor network connections and things like listening sockets which are combinations of IP addresses and port numbers.

You have the nc or netcat command to transfer data over any type of network connection, whether it's TCP or UDP-based. So, in our screenshot, we have examples of issuing commands like hostname which returns the hostname, ip -6 a which returns the IPv6 information. The netstat command where it's being piped to grep for ssh, and if it returns anything it means the SSH service is listening on a given port number. We've got some kind of connection. And the wget command where we could specify a URL and download files. So, these are going to be important when it comes to networking for the Linux technician.

4. Video: Managing Linux Network Interfaces and IP Addressing (it_oslsys_04_enus_04)

During this video, discover how to manage Linux network settings using ifconfig, ping, and ip.
manage Linux network settings using ifconfig, ping, and ip
[Video description begins] Topic title: Managing Linux Network Interfaces and IP Addressing. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, we're going to take a look at some Linux OS commands that we can use to manage network interfaces as well as IP addressing. Let's start with the ifconfig command. Now, in this case, I typed it in and it worked.

[Video description begins] A terminal window appears with the heading cblackwell@ubuntuserver1:/. The following command is inserted: ifconfig. [Video description ends]

If it's not installed, you might have to run, for example, here in Ubuntu Linux sudo apt install, and then specify the package such as ifconfig, or it might be a network utilities package to get it installed. However, we don't have to do that here.

[Video description begins] The following command is now added: sudo apt install ifconfig. [Video description ends]

When I type ifconfig, interface config, notice that it's returning back to network interfaces, in my particular case, one is called ens33, that's my local Ethernet interface, and I have one here called lo, that's my Local Loopback. It will always have a Local Loopback IPv4 address of 127.0.0.1 where the equivalence in IPv6 is ::1.

Loopback testing can be conducted just to verify that the TCP/IP stack is working on the local machine, or to test things like a local website you might be running on a local web server as a developer. However, notice for our Ethernet interface, we've got an IPv4 address shown here, and the decimal representation of the subnet mask, in this case, 255.255.255.0. And we've got the IPv6 address shown here as well. Notice the IPv6 address here starts with fe80. That's called a link-local address. It's used internally by IPv6 for communication and to discover other devices on the network so that if you actually assigned your own unique IPv6 address, that would show up here in addition to the link-local address that has a prefix of fe80. Notice here, it says, prefixlen, that would be the network. Prefix length is 64 bits, so /64.

ifconfig also shows the MAC address, the 48-bit hexadecimal address ifconfig also shows the 48-bit hexadecimal MAC address that uniquely identifies that network interface. And then we're going to have some statistics like the number of received versus transmitted packets and any errors related to that. So clearly, ifconfig is a valuable command. I could also run sudo if config, in our case, ens33 up if I wanted to bring the interface up, or down if I wanted to bring it down. Naturally, if you're connected through a remote network SSH connection and you bring the network interface down, that could be a problem because how would you get back to it if it doesn't have another network interface or if it's not a virtual machine whose host you have access to?

[Video description begins] The following command is highlighted: sudo ifconfig ens33 down. [Video description ends] 

Then we can also run the ip a command for IP address which gives us a listing showing us our Local Loopback address for that Local Loopback interface lo, our network interface of ens33 with our IPv4 information along with our MAC address, and also the IPv6 addressing information for that interface. Now we could use, for example, ifconfig or, in this case, ip a add, and we could give it an IP address, along with the slash CIDR subnet mask, let's say 24, specify a device, and we could assign a device to an interface in that manner, but it's not persistent.

[Video description begins] The following command is now added: ip a. [Video description ends] 

[Video description begins] The following command reads: ip a add 200.1.1.1/24 dev ens33. [Video description ends]

If you reboot that configuration is gone. So, where do we go to configure persistent network settings? And that will vary a little bit between different Linux distributions. Here in Ubuntu Linux, if I change directory to /etc/netplan, and then do an ls, I've got a config file here. I'm going to use sudo nano to open up that config file.

[Video description begins] The command reads: cd /etc/netplan. [Video description ends] 

Now, this network config file notice has a number of directives, and for readability a lot of the directives are indented where they should be and each directive has a colon after it. So, we've got network, ethernets, here's our interface ens33. Notice that it's set to use dhcpv4, it's been set with the value of true. If we wanted to configure a static IP and I've got this here shown in Wordpad, then we could set dhcp4 to a value of no or false. We could specify the IP address using the addresses: syntax and put it in square brackets insider notation.

We could configure the default gateway address and under the nameservers section, we could add the addresses for one or more DNS servers for name resolution. If you make a change to that, you would then run the sudo netplan apply command instead of rebooting to put those settings into effect. Now, of course, you have a number of other commands related to networking that you might run here in Linux, such as ping.

[Video description begins] The command reads: sudo nano 00-installer-config.yaml. [Video description ends]

[Video description begins] The command reads: sudo netplan apply. [Video description ends] 

So, if I ping a given IP address, it'll ping it using the ICMP network transport mechanism, and if it's there, and ICMP is not blocked by firewalls, I'll get a response. Now unlike Windows which only does this four times and then stops, you would have to press Ctrl+C to get this to stop pinging. 

[Video description begins] The command now reads: ping 8.8.8.8. [Video description ends]

All that pinging is telling you is that there's something out there listening at that IP, but in reality, a lot of ping-type of traffic is blocked by firewalls these days. You can also use traceroute where you could specify the path that you are taking from your local machine to get to the listed destination. Now again if the firewalls between you and the target are blocking ICMP traffic, you might not get information reported back. Here we have a few references here for Internet providers that are being specified all the way up to the target for 8.8.8.8 in my example which is just dns.google so Google DNS servers.

[Video description begins] The command reads: traceroute 8.8.8.8. [Video description ends] 

You might also find it useful to use commands like netstat. If I just press netstat with nothing, it returns all of the socket connections, whether it's incoming to this machine, if it's a server, maybe hosting a website, or if this machine is connected elsewhere. So, if I were to use netstat, let's say, I'll pipe that to grep, and look for ssh, it returns back that ssh indeed is shown here with an ESTABLISHED connection from this client 192.168.2.11. on the higher side, client port of 39806. Of course, the server itself is listening on TCP port 22. So, these are a handful of commands that can be very handy in managing networking in a Linux environment.

[Video description begins] The following command is added: netstat. [Video description ends]

[Video description begins] The command reads: netstat | grep ssh. [Video description ends] 

5. Video: Network Routing (it_oslsys_04_enus_05)

Upon completion of this video, you will be able to outline the importance of network traffic routing.
outline the importance of network traffic routing
[Video description begins] Topic title: Network Routing. Your host for this session is Dan Lachance. [Video description ends]
Network routing is all about getting traffic destined for a particular host, sent through the most efficient path, which could be across one or more routers. We're going to focus on IP routing. Now, network routing uses not only routers. A router is a device, a network infrastructure device, that has at least two network interfaces to route from one network to another, but it could have more than two network interfaces. It could either be an actual router hardware appliance designed to be a router, but it also could be a computer with two or more network interface cards installed, whether they're physical or virtual makes no difference. And IP routing enabled in the OS, and then the appropriate IP addresses assigned to the interfaces. And, of course, routing tables configured, or maybe routing protocols enabled. We'll talk about routing protocols a little bit later.

So, network routing uses router devices, but it also means that the in-memory routing table on every device, even every client endpoint device on the network also gets consulted. Pictured in our network routing diagram to the far left, we've got a client laptop, it's in memory routing table, let's say has a default route, and in IPv4 the default route, which means after checking the routing table and there's no other route for the target the client's trying to connect to, it'll consult the default route, which IPv4 notates as 0.0.0.0 and that would point to the default gateway on that local area network where the client resides, so 192.168.2.1. After the traffic gets to the local router, the default gateway, let's call it router1, it will consult its routing table and say do I know how to get to 192.168.2?

Let's say that's the network portion of the IP address. And after consulting the routing table, it might realize yes, in order to get to that target, I first have to send the traffic to another router interface whose address is 200.1.1.1. So, let's say that takes the traffic over to router2. It's a router, so it's got at least two network interfaces. It would consult its routing table to say do I know how to get to 192.168.2? Now if router2 has an interface connected directly to that network, it'll just send the traffic to the host on that network, on that local area network through the appropriate interface. Now in reality, in an enterprise network or the Internet, there could be dozens, hundreds, thousands, even tens of thousands of routers involved. Now within a given session trying to get a packet to a destination, even over the Internet, there's usually only a limited number of routers that traffic will go through.

An IP packet has a field called Time to Live or TTL which gets decremented by at least a value of 1 every time the packet traverses a router. So, if we have an operating system that sets an IP TTL of 255, that's the maximum number of routers it will go through. At any rate, let's take a look at the Linux route command shown here in the screenshot. When the route command is issued with no parameters, it simply displays that device's local routing table. Now, you can use the route command to add static or manual route entries here, which we'll look at in a moment, or you might use it just by itself, as we've done here to troubleshoot what's going on, why traffic perhaps is working on the LAN but cannot leave the LAN. There are two types of routing that we have to consider.

One is static routing, and what that means is that you are manually entering route table entries. And that's fine on a very tiny scale, but you can imagine how difficult that would be if you have to manage routing tables on dozens, hundreds, or thousands of routers. And so, to address that situation, we have dynamic routing protocols like Routing Information Protocol or RIP. There are a few versions of RIP, Open Shortest Path First (OSPF), Enhanced Interior Gateway Routing Protocol (EIGRP). These are dynamic routing protocols, which means routers will share the routes that they know about with other routers, which in turn will share it with other routers and so on.

So eventually routing table entries will be propagated to a multitude of routers within an infrastructure.

Of course, there are different settings for different types of dynamic routing protocols, like authentication, so you don't just hand off the routes that you know about as a router to any old router or maybe there is no authentication. So, there are many ways that that can be done, but it's important to understand the concept. So let's take a look at a couple of Linux routing commands. Let's focus on syntax for a moment. We know we can just issue the route command to view the Linux devices routing table. You could also issue the ip route show command. If you want to add a route to the default gateway, you could use route add default gw and then specify the appropriate IP address. If you want to add a routing table entry manually for a particular host and redirect connections to it, you can do that with route add -host, specify the IP, and then use the reject keyword.

You could also use ip route add, specify the network address, in this case, with a 24-bit mask, and then tie it to a device like Ethernet1, for example. You could also, of course, use the traceroute command to trace the path your traffic takes so all the routers that it goes through to get to a destination shown here as an IP address, but it just as well could be a DNS name. Now these commands would work fine, but they only persist for the current session, if the machine is restarted, these settings are lost. So how do you make routes persistent? How you do that might vary slightly from one Linux distribution to another. So, in Ubuntu Linux, for example, you can modify the /etc/netplan/ whatever the name of the configuration file is in there and add a routes directive.

So, routes: underneath you would have -to: and the target network. The next line would contain via, via: and you could tell it what to go through to get to that target network and assign it a metric value. When you have multiple routes, the metric values are consulted to see which one provides the quickest or more efficient route. So, Linux technicians then have to have an understanding of how network traffic gets routed in order to configure Linux hosts and troubleshoot them.

6. Video: Configuring Linux Routing in the Linux OS (it_oslsys_04_enus_06)

Learn how to configure Linux routing using the route command.
configure Linux routing using the route command
[Video description begins] Topic title: Configuring Linux Routing in the Linux OS. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I will be configuring routing within the Linux OS. So, we know that routing means that we can control how traffic gets sent to reach a target destination outside of the local area network. And we know that every client endpoint device has its own routing table configuration.

[Video description begins] A terminal window appears with the heading: cblackwell@ubuntuserver1: /. [Video description ends]

We can view that routing table here in Linux simply by typing route or by typing ip route show.

[Video description begins] Two commands are added: route. ip route show. [Video description ends]

For example, with the output of ip route show, we see that the default route is via 192.168.2.1, that is the IP address of our router interface on our local area network. Now we can get to that from this Linux host's perspective by going out of device ens33 and this machine is configured currently for dhcp, so our address is 192.168.2.41, and that has a metric of 100.

The metric can be used relative to other metrics to determine the least cost, so to speak, route to a target. Now we could add a route to the routing table. There might be times, for example, in some networks where you have more than one router connected to the network and you might want to direct certain types of traffic through that router. You still might want to have a default gateway for normal traffic. But if you're trying to connect to something on a specific target network, send it through a different exit doorway, so to speak, to get to the remote target network. Let's say, for instance, we ran sudo ip route add. We want to be able to send traffic from this machine to the 200.1.1 network, so .0/24 bits in the mask.

But we want to do that via or by going through a default gateway connected to our local area network. So, it has to be reachable on the LAN from this host's perspective. So, I'll put in the IP address of that. And finally, if you want to specify the interface, plus if you have more than one, you can with dev, so I'll go ahead and do that. So, we've got a new route added so that any traffic from this machine destined for a 200.1.1. something, it's going to be sent out to 192.168.2.90 which in our example is our default gateway. If I were to run ip route show yet again, notice here 200.1.1.0/24 via and there's our local router on our network. You can have more than one, that's where the traffic would be sent. Now, of course, you can also remove that entry.

[Video description begins] A new command is added: sudo ip route add 200.1.1.0/24 via 192.168.2.90 dev ens33. [Video description ends] 

[Video description begins] A command is inserted: ip route show. [Video description ends]

I could run sudo ip route delete 200.1.1.0, Enter.

[Video description begins] Another command is added: sudo ip route delete 200.1.1.0 . [Video description ends]

Now, of course, you could also remove that entry from the routing table by running sudo ip route delete 200.1.1.0/24, Enter.

So, now if you run ip route show, it's no longer shown in the list. Now while this is great to understand and there are some special use cases where you will want to statically manipulate routing tables on Linux, so it's possible. It's not common, but not only can this be very relevant for configuring Linux hosts, but it can also be very relevant when you're troubleshooting them. If there's been some kind of a problem with the configuration, and a given Linux host might not be able to communicate outside of the local area network. 

[Video description begins] Two more commands are added: sudo ip route delete 200.1.1.0/24, and ip route show. [Video description ends]

Now that's fine if you want to modify the routing table on this Linux host and have it in effect only in this session while the machine is running. What if we restart? All that routing information is lost. So, what we can do is we can modify the appropriate config file. Let's change directory to /etc/netplan.

If I do an ls there's my config file I'll run sudo nano against that config file to open it up. And what I'll do is add this routes section down here I just added routes:,on the next line, - to, as in to: space, the target network I want to create a route for using CIDR notation for the netmask, here's /24 and on the next line via:. So, what is the IP of the router that I will send traffic to to reach my target network? One thing about using these netplan network config files, they use YAML which is a markup language type, but they are very particular about how things are indented and you can't use tabs. You might be used to using tabs for proper indentation in the Word processor.

[Video description begins] A series of commands are added: / etc/ netplan$ ls 00 - installer - config.yaml/, and etc/ netplan$ sudo nano 00 - installer - config.yaml. [Video description ends]

That's fine in a Word processor, it's not fine here. It's going to break your netplan network config file, believe it or not, use spaces to line these things up correctly.

For example, the word via needs to start directly under to. You can't add an extra space or remove one and expect it to work right because it won't. OK, so I'm going to close that out and save that change. And to put that into effect, I can run sudo netplan apply.

[Video description begins] A new command is added: /etc / netplan$ sudo netplan apply. [Video description ends]

After which if I now run once again, ip route show, we now have our route here that's been read from our netplan configuration file. So, to make route entries manual entries persistent between reboots, modify the appropriate netplan file but watch out for the syntax in terms of using the spacebar for the space versus tab. Tab is bad, spacebar is good.

[Video description begins] Another command is added: /etc / netplan$ ip route show. [Video description ends] 

7. Video: Configuring Linux Routing in the Cloud (it_oslsys_04_enus_07)

In this video, find out how to configure Linux routing using cloud routing tables.
configure Linux routing using cloud routing tables
[Video description begins] Topic title: Configuring Linux Routing in the Cloud. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I'll be configuring Linux routing in the cloud. Specifically, I'll actually be configuring routing in the cloud that can be used by Linux virtual machines as well as other types of operating systems. The first thing I'll do here in Microsoft Azure where I've signed into the portal, is I will take a peek at the Virtual machines view. Now if the left-hand navigator isn't open, I can just go ahead and open it and I can click down on Virtual machines on the left. I've got one virtual machine here called Ubuntu1. 

[Video description begins] A page appears with the heading: Home - Microsoft Azure. It contains a toolbar with a search bar, a bell icon, a settings icon, and so on. The left navigation menu contains various options: Create a resource, Home, Dashboard, All Services, App Services, Virtual machines, Virtual networks, and More. The main pane contains two sections: Azure services and Resources. [Video description ends]

[Video description begins] The Virtual machines option is now active. It contains various buttons: Create, Switch to classic, Reservations, Manage view, Refresh, Export to CSV, Open query, and Assign tags. Below, it contains a table with the column headings: Name, Type, Subscription, Resource group, Location, Status, and Operating system. The table displays: Ubuntu1. [Video description ends]

What I want to do is open it up, go into its settings, and check out what network it's connected to in the cloud. So, I'm going to click on the name of the virtual machine to open up its properties and in the left-hand navigator, I'll go down under Settings, and I'm going to click Networking.

[Video description begins] A page titled: Ubuntu1 - Microsoft Azure appears. The left navigation menu contains various options: Networking, Connect, Disks, Size, Configuration, and More. The Networking option is highlighted. The main pane displays: Ubuntu1 | Networking. It contains three buttons: Feedback, Attach network interface, and Detach network interface. Further, it displays various information: Virtual network/subnet /: Ubuntu1-vnet/default, NIC Public IP: 20.84.40.117, NIC Private IP: 10.0.0.4 , and Accelerated networking: Disabled. [Video description ends]

Over on the right, I then have a listing for the Virtual network and subnet that this virtual machine belongs to. So, it's in a VNet, a virtual network in the cloud, Ubuntu1-vnet, and within that, it's connected to the default subnet. If I click on that link to open up that VNet, I can then click Subnets in the left-hand navigator of its properties, and there's the default subnet with its IPv4 address range.

[Video description begins] A page appears with the title: Ubuntu1-vnet - Microsoft Azure. The left navigation menu contains various options: Address space, Connected devices, Subnets, Bastion, and More. The main pane displays: Ubuntu1-vnet | Subnets. It contains following buttons: Subnet, Gateway subnet, Refresh, Manage users, and Delete. Below, it contains a table with the column headings: Name, IPv4, IPv6, Available IPs, and so on. The table displays: default. [Video description ends]

So, therefore, that Ubuntu Linux virtual machine will receive an IP configuration within that range. But here's what's interesting. If I click on the name of the default subnet here to open up its properties, notice one of the things we can associate with a subnet in the Microsoft Azure cloud is a Route table.

[Video description begins] A panel appears on the right titled: default. It contains various fields: Name, Subnet address range, NAT gateway, Network security group, Route table, and so on. [Video description ends]

Currently, it says None, and there's nothing selectable from the list.

So, a route table is just another cloud resource. It's like creating a storage account or a virtual machine or something like that. It's another item or object you create in the Azure cloud that you can then, in this case, associate with a subnet. Within the Route table, of course, you would have your routes to control where traffic gets routed to and through what. So, what this means then so I'll Cancel that. I'm going to go Home where I'll click Create a resource and I'll search for route table and I'll select it from the list and then for Microsoft Route Table I will click right on it and then click the Create button. As is the case when I deploy anything in the Azure cloud, I have to associate this with the Resource group just a way to organize resources.

[Video description begins] A new page appears with the heading: Create Route table - Microsoft Azure. It contains three tabs: Basics, Tags, Review + create. The Basics tab is active. It contains various field options: Subscriptions. Resource group, Region, Name, and Propagate gateway routes. [Video description ends] 

I'll choose HQ, for example.

[Video description begins] A drop-down menu appears under the Resource group option. It contains various options: AzureBackupRG_eastus_1, DefaultResourceGroup-EUS, East, HQ, and More. [Video description ends]

I'm going to create this in the East US Region and I'll call it eastroutetable1. Notice that the default is to Propagate gateway routes that's got a value of Yes, that's only really useful if you've got a connection to an on-premises environment. Do you want the on-premises routes to be propagated here in the cloud, such as if you have a site-to-site VPN? So, it really doesn't matter what I select for that, in this case, I'll just click the Review + create button in the bottom left, and I'll click Create. After a moment, the deployment is complete, I can choose to Go to the resource to open up its properties.

Of course, I can always go to the All resources view, where the route table will also show up here and is selectable. So, I'm going to click on it to open up its properties because the key here is we can then click Routes on the left and we can add multiple routes. It is a routing table after all, so maybe, I'll call this route SendOutboundTraffictoFW for firewall.

[Video description begins] A new page displays: Add route - Microsoft Azure. The left navigation menu contains various options: Configuration, Routes, Subnets, Properties, and so on. The main pane displays: eastroutetable1 | Routes. It contains three buttons: Add, Refresh, and Give feedback. [Video description ends]

 Let's say we've got a firewall appliance deployed in the cloud and we want to route traffic to it. For the Destination type, I can specify an IP Address or a Service Tag which really refers to a type of service that is available here in the Microsoft Azure cloud. I'm going to choose IP Addresses and let's say we want to force all traffic through this. So, therefore, for IPv4, we can refer to the default route to capture all traffic unless there's another more specific route by putting in 0.0.0.0/0. 

[Video description begins] A panel appears on the right with the heading: Add route. It contains four field options: Route name, Destination type, Destination IP address/CIDR ranges, Next hop type, and Next hop address. [Video description ends]

For the Next hop type, I'm going to choose Virtual appliance in this configuration and I will put in the firewall's IP address.

[Video description begins] A drop-down list appears under the Next hop type field option. It contains various options: Virtual network gateway, Virtual network, Internet, Virtual appliance, and None. [Video description ends] 

Now firewalls are going to have at least two interfaces. You're looking at the internal firewall IP here, so let's say 10.0.0.100, and I'll click Add. OK, so we've just added one route table entry for routing traffic into our route table object. So we will continue doing that as required, maybe to control routing to on-premises networks through a VPN or if we are linking VNets together here in the Azure cloud. However, that's all I'm going to do. But what I need to do now is go to Subnets on the left and associate this with the subnets. I'll click the Associate button and I'll make sure that this route table will be associated with the default subnet in the Ubuntu1-vnet. I'll click OK and it's done.

[Video description begins] The Subnets option is now active. It contains a button: Associate. Further, it contains a table with the column headings: Name, Address range, Virtual network, and Security group. [Video description ends]

[Video description begins] A panel appears on the right with the heading: Associate subnet. It contains two field options: Virtual network and Subnet. [Video description ends]

So, this is how we can begin to think about working with routing to control the movement of traffic in the Microsoft Azure cloud. So, then if we were to go back, let's say into our virtual network, back into the Subnets on the left, and if we were to click the subnet, the default subnet on the right, now notice that the eastroutetable1 resource is associated with our default subnet.

[Video description begins] The page with the title: Ubuntu1-vnet - Microsoft Azure appears again. The panel on the right titled: default is open. The Route table option now displays: eastroutetable. [Video description ends]

What this means is any virtual machines deployed into that subnet will use this route table. All of the routing table entries that we might add will be made visible to all virtual machines deployed in default. So, in this case, that means all of the virtual machines in the default subnet will be routing traffic through a firewall appliance before it goes anywhere else on its way out to the Internet.

8. Video: Capturing and Analyzing Network Traffic Using tcpdump (it_oslsys_04_enus_08)

Discover how to analyze network traffic using tcpdump.
analyze network traffic using tcpdump
[Video description begins] Topic title: Capturing and Analyzing Network Traffic Using tcpdump. Your host for this session is Dan Lachance. [Video description ends]
Yet another great command built into the Linux OS is tcpdump. This is a tool that lets us capture and analyze network traffic. And so, it's a command line tool where we can specify various parameters to control the behavior of what kind of network traffic that we wish to capture, through which network interface, and so on.

Let's go ahead and let's take a look at how tcpdump works. So, the first thing I'll do here in Linux is I'll run the ip a command.

[Video description begins] A terminal window appears with the heading cblackwell@ubuntuserver1:~. The following command is inserted: ip a. [Video description ends]

The reason I want to do this is because I want to know how many interfaces I have. Now the only real network interface I have here that is active on a network is ens33 and I can also see my IP address on that network, which in this case is 192.168.2.41. So, the first thing I'll do is run sudo tcpdump -i for interface ens33.

I can also add -v for verbose output and immediately it begins capturing network traffic.

[Video description begins] The command reads: sudo tcpdump -i ens33 -v. [Video description ends]

Now of course, it's going by quite quickly and it's even hard to tell what type of network traffic is going by. Although I see many references to SSH flying by the screen really quickly.

I'm going to press Ctrl+C and what we can also do is write that to a file. So, why don't I repeat that exact same command using the Up-arrow key, except what I want to do is use the -w parameter to write this to a standard pcap file. I want to store it in the current directory, which is the user home directory that I'm signed in with, and I'm going to call this packetcapture1.pcap and I'll press Enter.

[Video description begins] The command now reads: sudo tcpdump -i ens33 -v -w packetcapture1.pcap. [Video description ends]

OK, notice here instead of getting the output on the screen as we did previously, instead, it's being written to our packetcapture1.pcap file.

It is telling us the number of packets that it's been able to capture, and the number keeps increasing on the screen. I'll press Ctrl+C to quit out of that and if I do an ls, sure enough we've got a file here called packetcapture1.pcap. If I try to look at that with the cat command. It appears to be a binary-encoded type of file, which is normal. It's not a text file. It's a pcap or a packet capture type of file.

Now I could use other tools like Wireshark to open that up, but I can also simply use tcpdump. So, sudo tcpdump, but this time I'll use a -r for read and I'll specify that path and filename. I'll press Enter and what I can now do is see the output that the command originally resulted in. But this time it's not flying by the screen like it was when we were just displaying the output on the screen, and I can go back out and take a look at what's happening.

[Video description begins] The command now reads: sudo tcpdump -r packetcapture1.pcap. [Video description ends] 

For example, I can see from my localhost ubuntuserver1. It looks like we've got ssh response traffic going back to a client, which is the one I am using here at 192.168.2.11 on a higher-side client port. Now our ubuntuserver reference here uses .ssh notation, which means the standard SSH port, which of course is TCP port 22. But there really is so much more that you can do when it comes to using tcpdump.

If you're familiar with capturing network traffic, then you're definitely familiar with the concept of capture filters. In other words, filtering out what you capture. Now of course you could always filter the output. But let's go ahead and work with a few examples of filtering what we capture in the first place. So, for example, sudo tcpdump -i ens33 I can specify a host IP by using the host keyword and then specifying the IP address.

So, here I'll put in a particular host IP address.

[Video description begins] The command now reads: sudo tcpdump -i ens33 host 192.168.2.11 -v. [Video description ends]

I'll put in -v, I still want the verbose output here on the screen, so now I'm only seeing traffic that includes 192.168.2.11. If I press Ctrl+C to stop that, of course, I could also write that output with -w Let's call the file host filter.pcap. OK, and it's starting to capture traffic once again based on that.

[Video description begins] The command now reads: sudo tcpdump -i ens33 host 192.168.2.11 -v -w hostfilter.pcap. [Video description ends]

I'll press Ctrl+C to stop it, and let's read that file in, so sudo tcpdump -r specify our hostfilter.pcap file. And notice within it, all we have is traffic related to host 192.168.2.11. Now of course, you could use that read command line parameter and pipe the result to grep if we're looking for something specific. So, let's say I grep for netbios.

[Video description begins] The command now reads: sudo tcpdump -r hostfilter.pcap | grep netbios. [Video description ends]

So, now we only see the lines containing netbios that were captured within that pcap file. You can get more specific though with your filtering.

So, instead of just specifying that host which would capture traffic to and from that host, we might want to specify that only traffic destined to that host should be captured, so we could use the dst keyword to do that.

[Video description begins] The command now reads: sudo tcpdump -i ens33 dst 192.168.2.11 -v -w hostfilter.pcap. [Video description ends]

Let's press Enter. So we're going to overwrite that same host filter.pcap file. So, notice it's capturing, but we only have a handful of packets so far, so we're paring it down. It's not showing as many packets that it's capturing because we've got a filter, we're more selective. Ctrl+C

Let's clear the screen and let's read in that file again. Notice this time, we don't see 192.168.2.11 on the left because we're not interested in traffic from it, only interested in traffic in our example going to 192.168.2.11. Now of course, you could also filter by traffic type or port. For example, if I do an sudo tcpdump -i ens33 -v for verbose, let's say -n for the name of the protocol, let's say icmp.

Now currently, there's no traffic.

[Video description begins] The command reads: sudo tcpdump-i ens33 -v -n icmp. [Video description ends]

Why don't we go ahead and ping this host from another machine and as soon as we do that, notice that we see all kinds of icmp captured packets. OK, so that's one way to filter that way as well. We can also capture on specific port numbers, so sudo tcpdump -i -v for verbose and then I'll just use the port keyword, not dash port, just port. Let's say we want to see only port 22 traffic.

So, now that's the only type of traffic that we will be seeing in this capture.

[Video description begins] The command reads: sudo tcpdump-i ens33 -v port 22. [Video description ends]

Now we've only just looked at the bare bones in using tcpdump. If you look at the manual page man tcpdump, you'll see that there are many command line options, many filtering options, and so on. So, this can be very handy for the Linux technician in determining what type of network traffic is out there, or help troubleshoot network communication problems.

[Video description begins] The command reads: man tcpdump. [Video description ends]

9. Video: Capturing and Analyzing Network Traffic Using Wireshark (it_oslsys_04_enus_09)

During this video, you will learn how to analyze network traffic using Wireshark.
analyze network traffic using Wireshark
[Video description begins] Topic title: Capturing and Analyzing Network Traffic Using Wireshark. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, I will be capturing and analyzing network traffic using Wireshark. Here I'm on the wireshark.org website.

[Video description begins] A Wireshark . Go Deep page appears. It contains the following tabs: News, SharkFest, Get Acquainted, Get Help, Develop, Shop, and Members. It displays a message: Wireshark 4.0 Overview. [Video description ends]
Wireshark is a free open-source packet capturing and network analysis tool, and it runs on multiple platforms. So, whether you're running it on Linux or the macOS, or the Windows platform, it looks and feels the same. In this particular case, I have Wireshark running on a Windows host. Now, why is that relevant for a Linux technician? Well, Linux technician can capture network traffic that would include Linux traffic from any platform, whether it's macOS, Linux, or Windows. The key is to solve problems on the network or also to audit what type of traffic is on the network and whether or not it should be there.

[Video description begins] A page called The Wireshark Network Analyzer appears. It contains a toolbar with the following tabs: File, Edit, View, Go, Capture, Analyze, Statistics, Telephony, Wireless, Tools, and Help. The main pane contains 2 sections: Capture and Learn. The Capture section contains a filter bar. Below, it contains various networks such as: Local Area Connection 9, Local Area Connection 8, Wi-Fi, Ethernet, Local Area Connection, and so on. [Video description ends]

So, whether you run Wireshark from one platform or another, it's irrelevant. It looks and feels exactly the same. So, here in Wireshark where I've already installed it, I've got a Wi-Fi adapter available and I notice I have some activity. To start a capturing session on that network interface, I would simply double-click, each line here represents a separate captured packet.

[Video description begins] The corresponding page called Capturing from Wi-Fi displays. The similar toolbar appears with the following tabs: File, Edit, View, Go, Capture, Analyze, Statistics, Telephony, Wireless, Tools, and Help. Below, it contains a filter bar. The main pane is divided into 3 sections . The initial section contains a packets table with the following column headers: No. , Time, Source, Destination, Protocol, Length, and Info. The second section contains its interface details, and the last section contains various output codes. [Video description ends]

Now we haven't created a capture filter, so it's capturing all network traffic that is visible to this particular machine. In a network-switched environment like physical Ethernet switches, bear in mind that the only traffic you will see is traffic to or from your device, and that would include multi-casts and broadcasts.

So, unless you connect to a switch port specifically configured so you could see all network traffic, you're not really getting the full picture. I'm going to go ahead and stop this packet capture by clicking the Stop button in the upper left. If I were to select a single individual packet in the center of the screen, it presents us with the packet headers. The packet headers identify things like addressing information. For example, if I open up the Ethernet II header, we've got the Source, and we've got the Destination MAC addresses. These are the 48-bit hexadecimal addresses that represent the network interfaces in question, after which we have the IP header. Now the Ethernet II header here would map to layer 2 of the OSI model, where that applies to MAC addresses, whereas the IP header would map to layer 3, the network layer of the OSI model.

[Video description begins] Currently, section 2 is highlighted. It contains various headers such as: Frame 686, Ethernet II, Internet Protocol Version 4, and Transmission Control Protocol. It displays its source, destination, and many other details. [Video description ends] 

We've got a number of fields here, including the TTL, the Time to Live value, which specifies the maximum number of hops or routers through which this packet will go before it's discarded, and it's also, of course, got the Source and Destination IP address. Depending on the type of packet that you're looking at will determine what the next header is, in this case, it's a TCP, Transmission Control Protocol type of packet. If I expand that, it's got a number of fields. Notably, what we're really interested in here are the Source and the Destination Port numbers. The Destination Port is shown here as 443, which, of course, is normally used by web servers configured with HTTPS. So, this is a client making a connection to that host. Down at the bottom, we've also got the hexadecimal representation on the left, and the ASCII representation on the right of the packet payload.

Sometimes you can make sense of what's happening there, other times not. Now, up in the display filter bar, we can also filter the traffic for anything that we specifically want to see. For example, if I type tcp.port == 443, and press Enter, that is the only type of traffic that I'm going to see in this listing.

[Video description begins] The following port is added in the filter bar. The Port reads: tcp.port == 443. [Video description ends]

So, as I select my various packets, all of the port numbers in the TCP header are going to specifically show as being 443. We can simply delete that filter and type in something different. Now you can also go to File and Save your packet capture for later analysis. I've already done that and opened up an FTP capture file that includes other traffic as well. Now you can also filter on Protocol just by typing, for example, FTP, and pressing Enter. 

[Video description begins] A drop-down appears underneath the File tab. It contains various options such as: Open, Open Recent, Close, Save, Save As, File Set, Export Specified Packets, Export Packet Bytes, and so on. [Video description ends]

[Video description begins] The Port now reads: ftp. [Video description ends]

And that's the only traffic I'm looking at. Of course, one of the things that we can use a network analyzer like this to do is to audit what's happening on the network. Notice that the username is shown in clear text here as administrator, and the password is also shown in clear text. FTP is one of those protocols that sends credentials in plaintext or in the clear, and this is how easy it can be to retrieve those credentials if you're on the network at the right time and are able to see that type of traffic. I've opened up yet another packet capture file. Now what's interesting about this is that if you're using the tcpdump command in Linux, you can use the lowercase -w command line parameter to write what you capture out to a pcap file, which you can then open in Wireshark, whether you're running Wireshark on Linux or running it on Windows. Now, another important aspect of working with the packet capture here in Wireshark is that you can select a given packet within a conversation.

And you can go to the Analyze menu and choose Follow, in this case, TCP Stream, because I've selected a TCP packet. Now, instead of having to piece together what's happening in the session across a multitude of packets, this makes it a little bit easier to look at. For example, it appears that we've captured Telnet traffic for remote Telnet command line management, where the login name is shown here, as well as the Password, and we can even see the commands that were issued to the point where they logged out of the session. Telnet again is one of those notorious network protocols that sends credentials in clear text.

[Video description begins] A drop-down appears underneath the Analyze tab. It contains various options such as: Display Filters, Display Filter Expression, Apply as Column, Prepare as Filter, Enabled Protocols, Reload Lua Plugins, SCTP, Follow, and so on. The Follow option contains the following streams: TCP, UDP, TLS, HTTP, HTTP/2, and QUIC. [Video description ends]

[Video description begins] A dialog box called Wireshark . Follow TCP Stream (tcp.stream eq 0) . telnet.pcap appears. It contains information of its related details. [Video description ends]

If we were to keep that packet selected and go down to the TCP header, notice the Source port is 23, and 23, in fact, is the default port number used by Telnet servers that allow remote connections. Now instead of using Telnet for remote management at the command line, of course, we should be using Secure Shell or SSH, which provides an encrypted connection. But what's really important is that we have a sense of how we can capture network traffic, whether directly in Wireshark or with tcpdump and then have a way to analyze and make sense of the packet capture within Wireshark.

10. Video: Sychronizing Files Between Hosts Using rsync (it_oslsys_04_enus_10)

Find out how to synchronize files between Linux hosts using rsync.
synchronize files between Linux hosts using rsync
[Video description begins] Topic title: Synchronizing Files Between Hosts Using rsync. Your host for this session is Dan Lachance. [Video description ends]
In this demonstration, we're going to take a look at how you would copy and synchronize files between Linux hosts using rsync.

[Video description begins] A terminal window appears with the heading: cblackwell@ubuntu2: ~ $. [Video description ends]

The first thing we'll do here is check out what we've got on an Ubuntu server called ubuntu2. If I were to type pwd for print working directory, it shows that I am in /home/cblackwell. If I type in ls here, I've got a projects folder, if we take a look at what's in there, we've just got a couple of sample project files. Now, what we're going to be doing is using rsync to pull these files to another Linux host for backup purposes. In our example, we're just going to do this from the perspective of an Ubuntu desktop, a client computer. It could just as well be reversed. One thing that's important is to take a quick peek at the manpage for rsync.

[Video description begins] Two new commands are added: pwd, and ls. [Video description ends]

So, man rsync.

[Video description begins] Another command is added: man rsync. [Video description ends]

And way down under OPTION SUMMARY, we get a list of some of the command line parameters that can be very important. So, we can use either --verbose, or just -v, get a verbose listing of what is being copied and synchronized. We can use -a for archive mode, -r to recursively go into subdirectories, and notice that we also have options such as -H to preserve hard links, -p to preserve permissions. You're not just bringing over the file data, you can also bring over the metadata for it in terms of things like permissions. If you're also using extended acls for file system permissions, you can preserve those and make sure they're backed up or copied by specifying -A on the command line. And -o to preserve the owner of the file, -g to preserve the group ownership, and so on. So, clearly, there are many many options available with rsync.

There are plenty of command line parameters. OK, I'm going to type q to get out of the manpage, and here on the server I'll type ip a so we can get a sense of what the IP address is.

[Video description begins] A new command is added: ip a. [Video description ends]

Here it is. The server's IP address is 192.168.2.42 and if I were to type sudo service sshd status, it shows that the SSH daemon is up and running. It's active and running on this machine.

[Video description begins] A new command is added: /projects$ sudo service sshd status. [Video description ends]

Making an rsync connection over the network uses SSH. So here on Ubuntu Desktop, a different computer over the network. I'm going to go ahead and start a Terminal session. I'll just maximize it and I'll just click to increase the size. From my desktop, I'll just go ahead and make sure I can talk to the server by pinging it, ping 192.168.2.42 and we're getting a reply back, so that's good.

[Video description begins] A new terminal window appears with the heading: cblackwell@ubuntudesktop1 : ~. A new command is added: $ ping 192.168.2.42. [Video description ends]

Now, mind you, you have to think about the firewalls between the two systems that will communicate using rsync. In this day and age, the reality is that a lot of ping traffic is blocked, so you can always rely on that to test connectivity.

You might try to SSH into the server to see if that works, since that's what you're going to be using anyways. Here on the client if I were to type ip a, notice the client IP address is 192.168.2.40. So, from the server if I were to try to attempt an SSH connection using the SSH command line tool, cblackwell@192.168.2.40, we get an immediate statement about the connection being refused because there's no SSH daemon running on that host.

[Video description begins] A new command is added: ip a. [Video description ends]

[Video description begins] The following command is added: /projects$ ssh cblackwell@192.168.2.40. [Video description ends]

Which means that rsync would fail in this direction from the server reaching out to the client unless an SSH daemon was configured. Back on the client. Here we go. What we're going to do is run the following command rsync cblackwell, I know this is a user on the target server @ and I'll specify the IP of the target server. In this case, it's 192.168.2.42:. Now, on that server in the file system, I want to go into /home/cblackwell. So basically, I will be synchronizing, copying and synchronizing files in that user's home directory from the server onto this Ubuntu desktop. I'll specify command line parameters like -a for archive, r for recursive to go through all the subdirectory structures, v verbose, and I want to create a directory here in the current location on this machine called ubuntu_server_files and I'll press Enter.

[Video description begins] A new command is added in the second terminal window: rsync cblackwell@192.168.2.42 : / home/cblackwell -arv ubuntu_server_files. [Video description ends]

So, it asks me of course for the password for the account name cblackwell that I specified on the rsync command line, so I'll go ahead and enter that. After which, if we scroll back up because we asked for verbose output with -v, it gives us a list of all of the subdirectories and files, including hidden ones with the leading dots here that it copied over into the specified subdirectory. So, if I were to clear the screen here on this ubuntudesktop post and do an ls, we've got a subdirectory called ubuntu_server_files. If I go into that subdirectory and do an ls, it's backed up cblackwell. That's the user home directory. If we change directory into that and do an ls, well let's do an ls-a. We know that were hidden files that were copied, so there they are. And if we change directory into projects, those files were actually copied over as well. If we run the command again immediately, now I've put sudo in front of it.

[Video description begins] Another command is added in the second terminal window: ls. [Video description ends] 

[Video description begins] A series of new commands are added in the second terminal window: cd ubuntu_server_files/, ls, cd cblackwell/, ls, ls - a, cd projects/, and ls. [Video description ends]

If we run that command once again and press Enter and authenticate to the remote host, it says receiving incremental file list but nothing is shown. OK, well that's because nothing has changed on the source on the server.

[Video description begins] A new command is inserted: rsync cblackwell@192.168.2.42: / home /cblackwell -arv ubuntu_server_files. [Video description ends]

So, back on the server, I'm going to modify the Project_A.txt file with a new line that says This is newly added data, and I'll go ahead and save that out to the file. Back on our client machine if we run rsync again to pull down those files from the server.

[Video description begins] A screen appears that displays: GNU nano 6.2 Project_A.txt*, Sample text, This is newly added data. [Video description ends] 

[Video description begins] This command is added again in the second terminal: rsync cblackwell@192.168.2.42: / home /cblackwell -arv ubuntu_server_files. [Video description ends]

Notice this time when it says receiving incremental file list, it's showing us that in the projects folder it picked up that there was a change in the Project_A.txt file. So, in other words, rsync is doing an incremental copy only of changed data. This can be incredibly useful. You could even schedule rsync to run periodically via a cron job.

11. Video: Course Summary (it_oslsys_04_enus_11)

In this video, we will summarize the key concepts covered in this course.
summarize the key concepts covered in this course
[Video description begins] Topic title: Course Summary [Video description ends]
So, in this course, we've examined how to implement and manage IP addressing and routing in Linux, and also we managed to capture and analyze network traffic. We did this by exploring IP addressing for IPv4, and IPv6. We talked about common Linux networking commands, and managing network interfaces and IP addressing. We discussed network routing and how to configure routing in the OS and in the cloud. And we also captured and analyzed network traffic using tcpdump and Wireshark and we synchronized files between Linux hosts using rsync. In our next course, we'll move on to explore how to manage Linux processes, Daemons, scheduled tasks, and logging.

© 2024 Skillsoft Ireland Limited - All rights reserved.