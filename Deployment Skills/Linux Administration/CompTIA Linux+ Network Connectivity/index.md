## 1. Video: IP Addressing

After completing this video, you will be able to plan for IPv4 and IPv6 addressing needs.

### Overview
- **Host:** Dan Lachance
- **Focus:** Understanding IPv4 and IPv6 addressing in a Linux environment.

### IPv4 Addressing
- **Definition:** IPv4 uses 32-bit IP addresses in dotted decimal notation (e.g., 192.126.128.190).
- **Structure:** Composed of four octets (8 bits each), separated by periods.
- **Mathematical Range:** Each octet ranges from 0 to 255.

### Reserved Ranges
- **10.0.0.0 - 10.255.255.255**
- **172.16.0.0 - 172.31.255.255**
- **192.168.0.0 - 192.168.255.255**

### Subnet Masks
- **Purpose:** Defines the network and host portions of an IP address.
- **Example:** `255.255.255.0` indicates the first three octets identify the network.
- **CIDR Notation:** `/24` represents 24 bits set to 1.

### IPv6 Addressing
- **Definition:** IPv6 uses 128-bit addresses with hexadecimal representation, separated by colons (e.g., fe80::20c:29ff).
- **Adoption:** Gaining traction in consumer products and operating systems.

---

## 2. Video: Common Linux Networking Commands

Upon completion of this video, you will be able to use common Linux networking commands such as `ip`, `ifconfig`, `hostname`, `arp`, `route`, `dig`, `nslookup`, `traceroute`, `curl`, `wget`, `nc`, and `netstat`.

### Overview
- **Host:** Dan Lachance
- **Focus:** Mastering network configurations and statistics via the command line.

### Network Interfaces
- **Common Interfaces:**
  - `lo` - Local loopback interface
  - `eth0`, `eth1` - Ethernet interfaces
  - `wlan0`, `wlan1` - Wireless interfaces

### Key Commands
1. **ifconfig:** Older command for interface configuration.
   - `ifconfig -a` - List all active configurations.
   - `ifconfig eth0 up/down` - Bring interface up or down.
   - Assign an IP: `ifconfig eth0 <IP_ADDRESS>`.

2. **ip command:** Modern replacement for `ifconfig`.
   - `ip a` - Show all IP addresses.
   - `ip -4 a` / `ip -6 a` - Show IPv4 or IPv6 addresses.
   - `ip a add <IP_ADDRESS>/<MASK> dev eth0` - Assign IP to an interface.

3. **Other Networking Commands:**
   - `hostname` - Displays local machine name.
   - `arp` - View/manage ARP cache.
   - `route` - View/manage IP routing table.
   - `traceroute` - Trace path to target.
   - `dig` / `nslookup` - DNS name resolution tools.
   - `curl` - Transfer data using protocols (FTP, HTTP).
   - `wget` - Download files from URLs.
   - `netstat` - Monitor network connections and sockets.
   - `nc` (netcat) - Transfer data over TCP/UDP.

### Examples
- `hostname` - Returns the hostname.
- `ip -6 a` - Displays IPv6 information.
- `netstat | grep ssh` - Checks if SSH service is listening.
- `wget <URL>` - Downloads files from the specified URL.
