#!/usr/bin/python

import os
import sys
import yaml
import subprocess

MELLANOX_TOOLS = ''

MELLANOX_DEBUG_ENV_VAR = 'MLNX_DEBUG'

MELLANOX_TOOLS_LOCATION = [
  '/usr/bin/mellanox-config-tools',
  '/opt/mellanox/bin/mellanox-config-tools',
]

for location in MELLANOX_TOOLS_LOCATION:
  if os.path.exists(location):
    MELLANOX_TOOLS = location
    break

def config_tools_call(option):
  if MELLANOX_TOOLS == '':
    print >> sys.stderr, 'Error requirements: not found Mellanox configuration tools'
    return 1
  call_command = ['/bin/bash', MELLANOX_TOOLS] + option
  rc = (subprocess.call(call_command) == 0)
  if not rc:
    print >> sys.stderr, 'Error call: ' + ' '.join(call_command)
  return rc

def configure_repository_ofed(version=''):
  return config_tools_call(['configure-repository-ofed', str(version)])

def configure_repository_openstack(version='kilo'):
  return config_tools_call(['configure-repository-openstack', str(version)])

def ofed_install(version=''):
  return config_tools_call(['ofed', 'install', str(version)])

def ofed_bundle_deploy(version=''):
  return config_tools_call(['ofed-bundle-deploy', str(version)])

def ofed_remove():
  return config_tools_call(['ofed', 'remove'])

def e_ipoib_enable():
  return config_tools_call(['e-ipoib', 'enable'])

def e_ipoib_disable():
  return config_tools_call(['e-ipoib', 'disable'])

def openibd_enable():
  return config_tools_call(['openibd', 'enable'])

def openibd_disable():
  return config_tools_call(['openibd', 'disable'])

def openibd_stop():
  return config_tools_call(['openibd', 'stop'])

def openibd_start():
  return config_tools_call(['openibd', 'start'])

def openibd_restart():
  return config_tools_call(['openibd', 'restart'])

def mst_enable():
  return config_tools_call(['mst', 'enable'])

def mst_disable():
  return config_tools_call(['mst', 'disable'])

def mst_stop():
  return config_tools_call(['mst', 'stop'])

def mst_start():
  return config_tools_call(['mst', 'start'])

def mst_restart():
  return config_tools_call(['mst', 'restart'])

def pk_to_vlan_map(vlan_min=1, vlan_max=16, pk_min=1):
  return config_tools_call(['pk-to-vlan-map', str(vlan_min), str(vlan_max), str(pk_min)])

def opensmd_enable():
  return config_tools_call(['opensmd', 'enable'])

def opensmd_disable():
  return config_tools_call(['opensmd', 'disable'])

def opensmd_stop():
  return config_tools_call(['opensmd', 'stop'])

def opensmd_start():
  return config_tools_call(['opensmd', 'start'])

def opensmd_restart():
  return config_tools_call(['opensmd', 'restart'])

def connectx_port_config(mode_port_0='ib', mode_port_1='ib'):
  return config_tools_call(['connectx-port-config', str(mode_port_0), str(mode_port_1)])

def sriov_enable():
  return config_tools_call(['sriov', 'enable'])

def sriov_disable():
  return config_tools_call(['sriov', 'disable'])

def sriov_fw_enable():
  return config_tools_call(['sriov-fw', 'enable'])

def sriov_fw_disable():
  return config_tools_call(['sriov-fw', 'disable'])

def sysctl_conf_set(var, val):
  return config_tools_call(['sysctl-conf', 'set', str(var), str(val)])

def sysctl_conf_unset(var):
  return config_tools_call(['sysctl-conf', 'unset', str(var)])

def interface_set(if_name, if_alias, ip_address, net_mask='255.255.255.0'):
  return config_tools_call(['interface', 'set', str(if_name), str(if_alias), str(ip_address), str(net_mask)])

def interface_unset(if_name, if_alias):
  return config_tools_call(['interface', 'unset', str(if_name), str(if_alias)])

def interface_up(if_name, if_alias):
  return config_tools_call(['interface', 'up', str(if_name), str(if_alias)])

def interface_down(if_name, if_alias):
  return config_tools_call(['interface', 'down', str(if_name), str(if_alias)])

def set_vf_type_num(mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0):
  return config_tools_call(['set-vf-type-num', str(mode_port_0), str(mode_port_1), str(num_vf), str(probe_vf)])

def burn_vfs_in_fw(num_vf=16):
  return config_tools_call(['burn-vfs-in-fw', str(num_vf)])

def udev_namer_enable():
  return config_tools_call(['udev-namer', 'enable'])

def udev_namer_disable():
  return config_tools_call(['udev-namer', 'disable'])

def udev_namer_config_set(var, val):
  return config_tools_call(['udev-namer-config', 'set', str(var), str(val)])

def udev_namer_config_unset(var):
  return config_tools_call(['udev-namer-config', 'unset', str(var)])

class ConfigToolsService():

  def __init__(self, srv):
    self.srv = srv

  def _call_ (self, cmd):
    if self.srv == 'opensmd' or self.srv == 'openibd' or self.srv == 'mst':
      return config_tools_call([self.srv, cmd])
    else:
      return False

  def enable (self):
    return self._call_('enable')

  def disable (self):
    return self._call_('disable')

  def start (self):
    return self._call_('start')

  def stop (self):
    return self._call_('stop')

  def restart (self):
    return self._call_('restart')

class ConfigToolsOpensmdService(ConfigToolsService):

  def vlan2pk (self, vlan_min=1, vlan_max=16, pk_min=1):
    return pk_to_vlan_map(vlan_min, vlan_max, pk_min)

class ConfigToolsRepository():

  def ofed (self, version=''):
    return configure_repository_ofed(version)

  def openstack (self, version='kilo'):
    return configure_repository_openstack(version)

class ConfigToolsOfed():

  def install (self, version=''):
    return ofed_install(version)

  def bundle_deploy (self, version=''):
    return ofed_bundle_deploy(version)

  def remove (self):
    return ofed_remove()

class ConfigToolsEIPOIB():

  def enable (self):
    return e_ipoib_enable()

  def disable (self):
    return e_ipoib_disable()

class ConfigToolsSysctl():

  def set (self, var, val):
    return sysctl_conf_set(var, val)

  def unset (self, var):
    return sysctl_conf_unset(var)

class ConfigToolsInterface():

  def set (self, if_name, if_alias, ip_address, net_mask='255.255.255.0'):
    return interface_set(if_name, if_alias, ip_address, net_mask)

  def unset (self, if_name, if_alias):
    return interface_unset(if_name, if_alias)

  def up (self, if_name, if_alias):
    return interface_up(if_name, if_alias)

  def down (self, if_name, if_alias):
    return interface_down(if_name, if_alias)

class ConfigToolsSRIOVKernel():

  def enable (self):
    return sriov_enable()

  def disable (self):
    return sriov_disable()

class ConfigToolsSRIOVFirmware():

  def enable (self):
    return sriov_fw_enable()

  def disable (self):
    return sriov_fw_disable()

  def burn (self, num_vf=16):
    return burn_vfs_in_fw(num_vf)

class ConfigToolsSRIOVModprobe():

  def set (self, mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0):
    return set_vf_type_num(mode_port_0, mode_port_1, num_vf, probe_vf)

class ConfigToolsSRIOV():

  def __init__(self):
    self.kernel     = ConfigToolsSRIOVKernel()
    self.firmware   = ConfigToolsSRIOVFirmware()
    self.modprobe   = ConfigToolsSRIOVModprobe()

class ConfigToolsConnectx():

  def set (self, mode_port_0='ib', mode_port_1='ib'):
    return connectx_port_config(mode_port_0, mode_port_1)

class ConfigToolsUDEVNamer():

  def enable (self):
    return udev_namer_enable()

  def disable (self):
    return udev_namer_disable()

  def set (self, var, val):
    return udev_namer_config_set(var, val)

  def unset (self, var):
    return udev_namer_config_unset(var)

class ConfigTools(object):

  def __init__(self):

    self._debug     = False
    try:
      dm = os.environ[MELLANOX_DEBUG_ENV_VAR]
    except:
      dm = 'no'
      os.environ[MELLANOX_DEBUG_ENV_VAR] = dm
    if dm == 'yes':
      self._debug   = True

    self.opensmd    = ConfigToolsOpensmdService('opensmd')
    self.openibd    = ConfigToolsService('openibd')
    self.mst        = ConfigToolsService('mst')
    self.repository = ConfigToolsRepository()
    self.ofed       = ConfigToolsOfed()
    self.eipoib     = ConfigToolsEIPOIB()
    self.sysctl     = ConfigToolsSysctl()
    self.interface  = ConfigToolsInterface()
    self.sriov      = ConfigToolsSRIOV()
    self.connectx   = ConfigToolsConnectx()
    self.udevnamer  = ConfigToolsUDEVNamer()

  @property
  def debug(self):
    return self._debug

  @debug.setter
  def debug(self, v):
    self._debug = v
    allow_debug = "no"
    if self._debug:
      allow_debug = "yes"
    os.environ[MELLANOX_DEBUG_ENV_VAR] = allow_debug
