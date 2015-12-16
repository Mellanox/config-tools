# Mellanox Configuration Tools

Bash shell script for deployment and configuration Mellanox OFED, Mellanox Ethernet/Infiniband adaptors, Linux OS parameters.

### Releases
|Type|Version|
|---:|:---|
|Development|0.0.1|
|Stable|N/A|

### Installation
Redhat/Centos/Fedora:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-redhat-repository.repo -O /etc/yum.repos.d/mellanox-redhat-repository.repo
# sudo yum install -y mellanox-config-tools
```
Ubuntu:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-ubuntu-repository.list -O /etc/yum.repos.d/mellanox-ubuntu-repository.list
# sudo apt-get update -y
# sudo apt-get update install -y mellanox-config-tools
```
### Supported versions and releases

|OS/Software|Version|
|---:|:---|
|Redhat|6.X, 7.X|
|Ubuntu|14.04, 15.04|
|Openstack|kilo|
|OFED|2.4-2.0.3, 3.1-1.0.3|

|OS Vendor|OS Version| OFED Version|
|---:|:---:|:---|
|Redhat|6|2.4-2.0.3, 3.1-1.0.3|
|Redhat|7|2.4-2.0.3, 3.1-1.0.3|
|Ubuntu|14.04|2.4-2.0.3, 3.1-1.0.3|
|Ubuntu|15.04|3.1-1.0.3|

>Notes: OS vendor 'Redhat' means \<Redhat|Centos|Fedora\>. Supported
Fedora release > 11, is recognized by script as Redhat v 6 for
Fedora release < 20, Redhat v 7 for other Fedora releases.

### Usage

```
# sudo mellanox-config-tools <function> [<parameters list>]
```

### Function list

+ Configure OFED repository

  ***configure-repository-ofed*** \<ofed-version-number\>
  
+ Configure Openstack repository

   ***configure-repository-openstack*** \<openstack-release-codename\>

+ Mellanox OFED install/remove

   ***ofed*** \<install|remove\> \[\<ofed-version-number\>\] \[force\]

+ Ethernet IP over IB enable/disable

  ***e-ipoib*** \<enable|disable\>

+ Ethernet IP over IB kernel module load delay

  ***e-ipoib-pre-start-delay*** \<delay in seconds\>
  
+ Configuration OPENIBD daemon

  ***openibd*** \<enable|disable|restart|stop|start\>
  
+ Configuration OPENSMD daemon

  ***opensmd*** \<enable|disable|restart|stop|start\>

+ OPENSM partitions configuration

  ***pk-to-vlan-map*** \<vlan-min\> \<vlan-max\> \[\<pk-min=1\>\]

+ Configuration MST daemon

  ***mst*** \<enable|disable|restart|stop|start\>

+ Change and apply /etc/sysctl.conf parameters

  ***sysctl-conf*** \<set|unset\> \<var\> \<val\>

+ Configure and manage network interfaces aliases

  ***interface*** \<set|unset|up|down\> \<if-name\> \<if-alias\> \[\<ip-address\>  \[\<netmask\>\]\]

+ Configure Mellanox adapters ports by using *'connectx-port-config'*

  ***connectx-port-config*** \<port_0_mode\> \<port_1_mode\>

+ Enable/disable SRIOV support by kernel (intel_iommu=on/off)

  ***sriov*** \<enable|disable\>

+ Enable/disable SRIOV support by Mellanox adapter

  ***sriov-fw*** \<enable|disable\>

+ Configure Mellanox adapter ports types and number of VF

  ***set-vf-type-num*** \<port_0_mode\> \<port_1_mode\> \[\<num-vf\> \[\<probe-vf\>\]\]

+ Configure maximum supported by Mellanox adapter number of VF

  ***burn-vfs-in-fw*** \<num-vf\>

+ Enable/disable Mellanox UDEV namer

  ***udev-namer*** \<enable|disable\>

+ Configure Mellanox UDEV namer, for supported variables please refer to the entries in the configuration file *'/etc/udev/mlnx-udev-namer.conf'*

   ***udev-namer-config*** \<set|unset\> \<variable\> \[\<value\>\]




