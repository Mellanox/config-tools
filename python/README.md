# Mellanox Configuration Tools, Python API

### Releases
|Type|Version|
|---:|:---|
|Development|0.0.1|
|Stable|N/A|

### Installation
Redhat/Centos/Fedora:
```
# sudo yum install -y mellanox-config-tools-python
```
Ubuntu:
```
# sudo apt-get update install -y mellanox-config-tools-python
```

### Usage

```
 import mellanoxconfig
 mlnx = mellanoxconfig.ConfigTools()
```

### Objects/Functions list

**repository**
+ **ofed(version='')**
+ **openstack(version='')**

**ofed**
+ **install(version='')**
+ **remove()**

**eipoib**
+ **enable()**
+ **disable()**

**openibd**
+ **enable()**
+ **disable()**
+ **stop()**
+ **start()**
+ **restart()**

**mst**
+ **enable()**
+ **disable()**
+ **stop()**
+ **start()**
+ **restart()**

**opensmd**
+ **enable()**
+ **disable()**
+ **stop()**
+ **start()**
+ **restart()**
+ **restart()**
+ **vlan2pk (vlan_min=1, vlan_max=16, pk_min=1)**


