Serialization

### Network Layer
ipconfig /all
show interfaces vlan 1
show arp
show mac address-table
S1(config-if)# no shutdow
hop
Layer 3 switch
Connectionless -  no initial exchange of control information to establish an end-to-end connection
Best effort - unreliable 
MTU
Fragmenting - not in ipv6 by router
Diagrams - visual interpretaion
DS DSCP ECN
Because the router decrements the TTL of each packet, the router must also recalculate the Header Checksum.
ICMP (1), TCP (6), and UDP (17).
source always unicast
340 undecillio 10^36
20-60 v4
40    v6
protocol -> next header
total lenght -> payload length
TTL -> Hope Limit
ICPv6 time limit exceeded
flow label + in ipv6
EUI-64
NDP
ULAs
::1
Default Gateway
DHCP -> Application layer
default route
route print
netstat -r
direct connections
local network
local default routes
Directly-connected networks
Remote networks
Default route
A static route is appropriate for a small network and when there are few or no redundant links
OSPF
EIGRP
*show ip route*
IPsec
flat addressing
ARP messages are encapsulated directly within an Ethernet frame. There is no IPv4 header
0x806
ARP table are time stamped  15-45 sec
Static ARP table entries do not expire over time
neighbor solicitation and neighbor advertisement messages, similar to IPv4 ARP requests and ARP replies.
*show ip arp*
arp -a
DAI
ARP stored in RAM
ARP spoffing and poisoning
Neighbor Cache
SN Multicast
ND = NDP
Neighbor Solicitation messages
Neighbor Advertisement messages
Router Solicitation messages  -> ↓
Router Advertisement messages -> dynamic address allocation and StateLess Address AutoConfiguration (SLAAC).
Redirect Message
IETF RFC 4861
netstat -r both of IPv4 and IPv6
