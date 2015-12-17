# Mellanox Configuration Tools, Puppet API

### Releases
|Type|Version|
|---:|:---|
|Development|0.0.1|
|Last Stable|N/A|

### Installation
Redhat/Centos/Fedora:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-redhat-repository.repo -O /etc/yum.repos.d/mellanox-redhat-repository.repo
# sudo yum install -y mellanox-config-tools-puppet
```
Ubuntu:
```
# sudo wget http://bgate.mellanox.com/openstack/repository/repo/mellanox-ubuntu-repository.list -O /etc/yum.repos.d/mellanox-ubuntu-repository.list
# sudo apt-get update -y
# sudo apt-get update install -y mellanox-config-tools-puppet
```

### Functions list

**Repositories configuration**
+ *mlnx_repository_ofed(version='')*
+ *mlnx_repository_openstack(version='')*

**Mellanox OFED install/remove**
+ *mlnx_ofed_install(version='')*
+ *mlnx_ofed_remove()*

**E_IPOIB enable/disable**
+ *mlnx_eipoib_enable()*
+ *mlnx_eipoib_disable()*

**Openibd daemon management**
+ *mlnx_openibd_enable()*
+ *mlnx_openibd_disable()*
+ *mlnx_openibd_stop()*
+ *mlnx_openibd_start()*
+ *mlnx_openibd_restart()*

**Mst daemon management**
+ *mlnx_mst_enable()*
+ *mlnx_mst_disable()*
+ *mlnx_mst_stop()*
+ *mlnx_mst_start()*
+ *mlnx_mst_restart()*

**Opensmd daemon management**
+ *mlnx_opensmd_enable()*
+ *mlnx_opensmd_disable()*
+ *mlnx_opensmd_stop()*
+ *mlnx_opensmd_start()*
+ *mlnx_opensmd_restart()*
+ *mlnx_opensmd_vlan2pk(vlan_min=1, vlan_max=16, pk_min=1)*

**Set/unset configration parameters in file /etc/sysctl.conf**
+ *mlnx_sysctl_set(var, val)*
+ *mlnx_sysctl_unset(var)*

**Network interfaces aliases management**
+ *mlnx_interface_set(if_name, if_alias, ip_address, net_mask='255.255.255.0')*
+ *mlnx_interface_unset(if_name, if_alias)*
+ *mlnx_interface_up(if_name, if_alias)*
+ *mlnx_interface_down(if_name, if_alias)*

**SRIOV configuration**
+ *mlnx_sriov_kernel_enable()*
+ *mlnx_sriov_kernel_disable()*
+ *mlnx_sriov_firmware_enable()*
+ *mlnx_sriov_firmware_disable()*
+ *mlnx_sriov_firmware_burn(num_vf=16)*
+ *mlnx_sriov_modprobe_set(mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0)*

**Configure Mellanox adaptors by using 'connectx'**
+ *mlnx_connectx_set(mode_port_0='ib', mode_port_1='ib')*

**Mellanox UDEV namer configuration and management**
+ *mlnx_udevnamer_enable()*
+ *mlnx_udevnamer_disable()*
+ *mlnx_udevnamer_set(var, val)*
+ *mlnx_udevnamer_unset(var)*

### Return values
All functions returns Bash shell script exit code, rc=0 is successfully runned function.

