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

def mellanox_config_tools_call(option):
  if MELLANOX_TOOLS == '':
    print >> sys.stderr, 'Error requirements: not found Mellanox configuration tools'
    return 1
  call_command = ['/bin/bash', MELLANOX_TOOLS] + option
  rc = (subprocess.call(call_command) == 0)
  if not rc:
    print >> sys.stderr, 'Error call: ' + ' '.join(call_command)
  return rc

def mellanox_configure_repository_ofed(version=None):
  return mellanox_config_tools_call(['configure-repository-ofed', str(version)])

def mellanox_configure_repository_openstack(version='kilo'):
  return mellanox_config_tools_call(['configure-repository-openstack', str(version)])

def mellanox_ofed_install(version=None):
  return mellanox_config_tools_call(['ofed', 'install', str(version)])

def mellanox_ofed_bundle_deploy(version=None):
  return mellanox_config_tools_call(['ofed-bundle-deploy', str(version)])

def mellanox_ofed_remove():
  return mellanox_config_tools_call(['ofed', 'remove'])

def mellanox_e_ipoib_enable():
  return mellanox_config_tools_call(['e-ipoib', 'enable'])

def mellanox_e_ipoib_disable():
  return mellanox_config_tools_call(['e-ipoib', 'disable'])

def mellanox_openibd_enable():
  return mellanox_config_tools_call(['openibd', 'enable'])

def mellanox_openibd_disable():
  return mellanox_config_tools_call(['openibd', 'disable'])

def mellanox_openibd_stop():
  return mellanox_config_tools_call(['openibd', 'stop'])

def mellanox_openibd_start():
  return mellanox_config_tools_call(['openibd', 'start'])

def mellanox_openibd_restart():
  return mellanox_config_tools_call(['openibd', 'restart'])

def mellanox_mst_enable():
  return mellanox_config_tools_call(['mst', 'enable'])

def mellanox_mst_disable():
  return mellanox_config_tools_call(['mst', 'disable'])

def mellanox_mst_stop():
  return mellanox_config_tools_call(['mst', 'stop'])

def mellanox_mst_start():
  return mellanox_config_tools_call(['mst', 'start'])

def mellanox_mst_restart():
  return mellanox_config_tools_call(['mst', 'restart'])

def mellanox_pk_to_vlan_map(vlan_min=1, vlan_max=16, pk_min=1):
  return mellanox_config_tools_call(['pk-to-vlan-map', str(vlan_min), str(vlan_max), str(pk_min)])

def mellanox_opensmd_enable():
  return mellanox_config_tools_call(['opensmd', 'enable'])

def mellanox_opensmd_disable():
  return mellanox_config_tools_call(['opensmd', 'disable'])

def mellanox_opensmd_stop():
  return mellanox_config_tools_call(['opensmd', 'stop'])

def mellanox_opensmd_start():
  return mellanox_config_tools_call(['opensmd', 'start'])

def mellanox_opensmd_restart():
  return mellanox_config_tools_call(['opensmd', 'restart'])

def mellanox_connectx_port_config(mode_port_0='ib', mode_port_1='ib'):
  return mellanox_config_tools_call(['connectx-port-config', str(mode_port_0), str(mode_port_1)])

def mellanox_sriov_enable():
  return mellanox_config_tools_call(['sriov', 'enable'])

def mellanox_sriov_disable():
  return mellanox_config_tools_call(['sriov', 'disable'])

def mellanox_sriov_fw_enable():
  return mellanox_config_tools_call(['sriov-fw', 'enable'])

def mellanox_sriov_fw_disable():
  return mellanox_config_tools_call(['sriov-fw', 'disable'])

def mellanox_sysctl_conf_set(var, val):
  return mellanox_config_tools_call(['sysctl-conf', 'set', str(var), str(val)])

def mellanox_sysctl_conf_unset(var):
  return mellanox_config_tools_call(['sysctl-conf', 'unset', str(var)])

def mellanox_interface_set(if_name, if_alias, ip_address, net_mask='255.255.255.0'):
  return mellanox_config_tools_call(['interface', 'set', str(if_name), str(if_alias), str(ip_address), str(net_mask)])

def mellanox_interface_unset(if_name, if_alias):
  return mellanox_config_tools_call(['interface', 'unset', str(if_name), str(if_alias)])

def mellanox_interface_up(if_name, if_alias):
  return mellanox_config_tools_call(['interface', 'up', str(if_name), str(if_alias)])

def mellanox_interface_down(if_name, if_alias):
  return mellanox_config_tools_call(['interface', 'down', str(if_name), str(if_alias)])

def mellanox_set_vf_type_num(mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0):
  return mellanox_config_tools_call(['set-vf-type-num', str(mode_port_0), str(mode_port_1), str(num_vf), str(probe_vf)])

def mellanox_burn_vfs_in_fw(num_vf=16):
  return mellanox_config_tools_call(['burn-vfs-in-fw', str(num_vf)])

def mellanox_udev_namer_enable():
  return mellanox_config_tools_call(['udev-namer', 'enable'])

def mellanox_udev_namer_disable():
  return mellanox_config_tools_call(['udev-namer', 'disable'])

class MellanoxConfigToolsService():

  def __init__(self, srv):
    self.srv = srv

  def _call_ (self, cmd):
    if self.srv == 'opensmd' or self.srv == 'openibd' or self.srv == 'mst':
      return mellanox_config_tools_call([self.srv, cmd])
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

class MellanoxConfigToolsOpensmdService(MellanoxConfigToolsService):

  def vlan2pk (self, vlan_min=1, vlan_max=16, pk_min=1):
    return mellanox_pk_to_vlan_map(vlan_min, vlan_max, pk_min)

class MellanoxConfigToolsRepository():

  def ofed (self, version=None):
    return mellanox_configure_repository_ofed(version)

  def openstack (self, version='kilo'):
    return mellanox_configure_repository_openstack(version)

class MellanoxConfigToolsOfed():

  def install (self, version=None):
    return mellanox_ofed_install(version)

  def bundle_deploy (self, version=None):
    return mellanox_ofed_bundle_deploy(version)

  def remove (self):
    return mellanox_ofed_remove()

class MellanoxConfigToolsEIPOIB():

  def enable (self):
    return mellanox_e_ipoib_enable()

  def disable (self):
    return mellanox_e_ipoib_disable()

class MellanoxConfigToolsSysctl():

  def set (self, var, val):
    return mellanox_sysctl_conf_set(var, val)

  def unset (self, var):
    return mellanox_sysctl_conf_unset(var)

class MellanoxConfigToolsInterface():

  def set (self, if_name, if_alias, ip_address, net_mask='255.255.255.0'):
    return mellanox_interface_set(if_name, if_alias, ip_address, net_mask)

  def unset (self, if_name, if_alias):
    return mellanox_interface_unset(if_name, if_alias)

  def up (self, if_name, if_alias):
    return mellanox_interface_up(if_name, if_alias)

  def down (self, if_name, if_alias):
    return mellanox_interface_down(if_name, if_alias)

class MellanoxConfigToolsSRIOVKernel():

  def enable (self):
    return mellanox_sriov_enable()

  def disable (self):
    return mellanox_sriov_disable()

class MellanoxConfigToolsSRIOVFirmware():

  def enable (self):
    return mellanox_sriov_fw_enable()

  def disable (self):
    return mellanox_sriov_fw_disable()

  def burn (self, num_vf=16):
    return mellanox_burn_vfs_in_fw(num_vf)

class MellanoxConfigToolsSRIOVModprobe():

  def set (self, mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0):
    return mellanox_set_vf_type_num(mode_port_0, mode_port_1, num_vf, probe_vf)

class MellanoxConfigToolsSRIOV():

  def __init__(self):
    self.kernel     = MellanoxConfigToolsSRIOVKernel()
    self.firmware   = MellanoxConfigToolsSRIOVFirmware()
    self.modprobe   = MellanoxConfigToolsSRIOVModprobe()

class MellanoxConfigToolsConnectx():

  def set (self, mode_port_0='ib', mode_port_1='ib'):
    return mellanox_connectx_port_config(mode_port_0, mode_port_1)

class MellanoxConfigToolsUDEVNamer():

  def enable (self):
    return mellanox_udev_namer_enable()

  def disable (self):
    return mellanox_udev_namer_disable()

class MellanoxConfigTools(object):

  def __init__(self):

    self._debug     = False
    try:
      dm = os.environ[MELLANOX_DEBUG_ENV_VAR]
    except:
      dm = 'no'
      os.environ[MELLANOX_DEBUG_ENV_VAR] = dm
    if dm == 'yes':
      self._debug   = True

    self.opensmd    = MellanoxConfigToolsOpensmdService('opensmd')
    self.openibd    = MellanoxConfigToolsService('openibd')
    self.mst        = MellanoxConfigToolsService('mst')
    self.repository = MellanoxConfigToolsRepository()
    self.ofed       = MellanoxConfigToolsOfed()
    self.eipoib     = MellanoxConfigToolsEIPOIB()
    self.sysctl     = MellanoxConfigToolsSysctl()
    self.interface  = MellanoxConfigToolsInterface()
    self.sriov      = MellanoxConfigToolsSRIOV()
    self.connectx   = MellanoxConfigToolsConnectx()
    self.udevnamer  = MellanoxConfigToolsUDEVNamer()

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
