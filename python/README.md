# Mellanox Configuration Tools, Python API

### Releases
|Type|Version|
|---:|:---|
|Development|0.0.1|
|Last Stable|N/A|

### Installation
Redhat/Centos/Fedora:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-redhat-repository.repo -O /etc/yum.repos.d/mellanox-redhat-repository.repo
# sudo yum install -y mellanox-config-tools-python
```
Ubuntu:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-ubuntu-repository.list -O /etc/yum.repos.d/mellanox-ubuntu-repository.list
# sudo apt-get update -y
# sudo apt-get update install -y mellanox-config-tools-python
```

### Usage

```
 import mellanoxconfig
 mlnx = mellanoxconfig.ConfigTools()
 mlnx.<object>.<function>([<paramlist>])
```

### Objects/Functions list

**debug**
+ *enable()*
+ *disable()*

**repository**
+ *ofed(version='')*
+ *openstack(version='')*

**ofed**
+ *install(version='')*
+ *remove()*

**eipoib**
+ *enable()*
+ *disable()*

**openibd**
+ *enable()*
+ *disable()*
+ *stop()*
+ *start()*
+ *restart()*

**mst**
+ *enable()*
+ *disable()*
+ *stop()*
+ *start()*
+ *restart()*

**opensmd**
+ *enable()*
+ *disable()*
+ *stop()*
+ *start()*
+ *restart()*
+ *vlan2pk(vlan_min=1, vlan_max=16, pk_min=1)*

**sysctl**
+ *set(var, val)*
+ *unset(var)*

**interface**
+ *set(if_name, if_alias, ip_address, net_mask='255.255.255.0')*
+ *unset(if_name, if_alias)*
+ *up(if_name, if_alias)*
+ *down(if_name, if_alias)*

**sriov.kernel**
+ *enable()*
+ *disable()*

**sriov.firmware**
+ *enable()*
+ *disable()*
+ *burn(num_vf=16)*

**sriov.modprobe**
+ *set(mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0)*

**connectx**
+ *set(mode_port_0='ib', mode_port_1='ib')*

**udevnamer**
+ *enable()*
+ *disable()*
+ *set(var, val)*
+ *unset(var)*

### Return values
All functions returns Bash shell script exit code, rc=0 is successfully runned function.

