# Mellanox UDEV namer

UDEV namer can provide custom persistent names for Mellanox adapters interfaces.

### Releases
|Type|Version|
|---:|:---|
|Development|0.0.1|
|Stable|N/A|

### Installation
Redhat/Centos/Fedora:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-redhat-repository.repo -O /etc/yum.repos.d/mellanox-redhat-repository.repo
# sudo yum install -y mellanox-udev-namer
```
Ubuntu:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-ubuntu-repository.list -O /etc/yum.repos.d/mellanox-ubuntu-repository.list
# sudo apt-get update -y
# sudo apt-get update install -y mellanox-udev-namer
```
### Supported versions and releases

|OS|Version|
|---:|:---|
|Redhat| > 6.X|
|Ubuntu| > 14.04|

>Notes: OS vendor 'Redhat' means \<Redhat|Centos|Fedora\>. Supported
Fedora release > 11, is recognized by script as Redhat v 6 for
Fedora release < 20, Redhat v 7 for other Fedora releases.

### Configure
Mellanox UDEV namer can be configured by changing file /etc/udev/mlnx-udev-namer.conf

### Parameters list

>Notes: Due BOOST bug https://svn.boost.org/trac/boost/ticket/5379
in BOOST versions < 1.45 not supported comments started with '#'

>Notes: Case sensitive parameters names, case insensitive parameters values.

+ **enable**

   Enable/disable use Mellanox UDEV namer.

   *Allow:* true|false|yes|no.

   *Default:* false.

+ **generate_eipoib_mac_address**

   Generate MAC addreses for E_IPOIB virtual functions interfaces, case insensitive value.

   *Allow:* true|false|yes|no.

+ *Default:* false.

+ prefix_eipoib_mac_address
MAC address prefix for E_IPOIB virtual functions interfaces,
case insensitive value.
Allow: from half to 4 byte heximal ":" separated number.
Default: 'fe'.

+ prefix_infiniband
Infiniband intrefaces prefix, case insensitive value,
reducing to lowercase.
Allow: up to 4 charters, started from alpha value.
Default: 'ib'.

+ prefix_ethernet
Ethernet intrefaces prefix, case insensitive value,
reducing to lowercase
Allow: Up to 4 <alpha|num|-|_> charcters, started from alpha value.
Default: 'me'.

+ prefix_eipoib
E_IPOIB intrefaces prefix, case insensitive value, reducing to lowercase.
Allow: Up to 4 <alpha|num|-|_> charcters, started from alpha value.
Default: 'mi'.

+ prefix_port
Port number prefix, case insensitive value, reducing to lowercase.
Allow: 1 or 2 alpha charcters.
Default: 'p'.

+ prefix_virtfn
Virtual function prefix, case insensitive value, reducing to lowercase.
Allow: 1 or 2 alpha charcters.
Default: 'f'.
