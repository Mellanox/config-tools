#!/usr/bin/python

import os
import yaml
import subprocess
from netaddr import *

from charmhelpers.core import (
  hookenv,
  unitdata,
)

MLNX_TOOLS = 'hooks/mellanox/mellanox-config-tools'

if not os.path.exists(MLNX_TOOLS):
  MLNX_TOOLS = 'mellanox/mellanox-config-tools'

if not os.path.exists(MLNX_TOOLS):
  MLNX_TOOLS = '/usr/bin/mellanox-config-tools'

def mellanox_config_tools_call(option):
  call_command = ['/bin/bash', MLNX_TOOLS] + option
  rc = (subprocess.call(call_command) == 0)
  if not rc:
    hookenv.log('Error call: ' + ' '.join(call_command))
  return rc

# --- Configure repositories -------------------------------------------
def mellanox_configure_apt_ofed(version=None):
  return mellanox_config_tools_call(['configure-apt-ofed', str(version)])

def mellanox_configure_apt_openstack(version='kilo'):
  return mellanox_config_tools_call(['configure-apt-openstack', str(version)])

# --- OFED -------------------------------------------------------------
def mellanox_ofed_install():
  return mellanox_config_tools_call(['ofed', 'install'])

def mellanox_ofed_remove():
  return mellanox_config_tools_call(['ofed', 'remove'])

# --- Ethernet via IPOIB -----------------------------------------------
def mellanox_e_ipoib_enable():
  return mellanox_config_tools_call(['e-ipoib', 'enable'])

def mellanox_e_ipoib_disable():
  return mellanox_config_tools_call(['e-ipoib', 'disable'])

# --- Openibd daemon --------------------------------------------------
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

# --- MST daemon ------------------------------------------------------
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

# --- Configure partions for opensm daemon ---------------------------
def mellanox_pk_to_vlan_map(vlan_min=1, vlan_max=16, pk_min=1):
  return mellanox_config_tools_call(['pk-to-vlan-map', str(vlan_min), str(vlan_max), str(pk_min)])

# --- Opensm daemon ---------------------------------------------------
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

# --- Configure ports mode via connectx-port-config -------------------
def mellanox_connectx_port_config(mode_port_0='ib', mode_port_1='ib'):
  return mellanox_config_tools_call(['connectx-port-config', str(mode_port_0), str(mode_port_1)])

# --- Configure SRIOV support by kernel (intel_iommu=on) --------------
def mellanox_sriov_enable():
  return mellanox_config_tools_call(['sriov', 'enable'])

def mellanox_sriov_disable():
  return mellanox_config_tools_call(['sriov', 'disable'])

# --- Configure SRIOV support by using mlxfwmanager_sriov_dis_x86_64 --
# --- mlxfwmanager_sriov_en_x86_64 utuls, reboot requires -------------
def mellanox_sriov_fw_enable():
  return mellanox_config_tools_call(['sriov-fw', 'enable'])

def mellanox_sriov_fw_disable():
  return mellanox_config_tools_call(['sriov-fw', 'disable'])

# --- Configure kernel parameters in /etc/sysctl.conf -----------------
def mellanox_sysctl_conf_set(var, val):
  return mellanox_config_tools_call(['sysctl-conf', 'set', str(var), str(val)])

def mellanox_sysctl_conf_unset(var):
  return mellanox_config_tools_call(['sysctl-conf', 'unset', str(var)])

# --- Configure network interface -------------------------------------
def mellanox_interface_set(if_name, if_alias, ip_address, net_mask='255.255.255.0'):
  return mellanox_config_tools_call(['interface', 'set', str(if_name), str(if_alias), str(ip_address), str(net_mask)])

def mellanox_interface_unset(if_name, if_alias):
  return mellanox_config_tools_call(['interface', 'unset', str(if_name), str(if_alias)])

def mellanox_interface_up(if_name, if_alias):
  return mellanox_config_tools_call(['interface', 'up', str(if_name), str(if_alias)])

def mellanox_interface_down(if_name, if_alias):
  return mellanox_config_tools_call(['interface', 'down', str(if_name), str(if_alias)])

# --- Configure SRIOV support by using /etc/modprobe.d/mlx4_core.conf,
# --- openibd restart requires
def mellanox_set_vf_type_num(mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0):
  return mellanox_config_tools_call(['set-vf-type-num', str(mode_port_0), str(mode_port_1), str(num_vf), str(probe_vf)])

# --- Configure SRIOV support by using mlxconfig util, reboot requires
def mellanox_burn_vfs_in_fw(num_vf=16):
  return mellanox_config_tools_call(['burn-vfs-in-fw', str(num_vf)])

# --- OOP API: Mellanox Config Tools ------------------------------------------
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

class MellanoxConfigToolsApt():

  def ofed (self, version=None):
    return mellanox_configure_apt_ofed(version)

  def openstack (self, version='kilo'):
    return mellanox_configure_apt_openstack(version)

class MellanoxConfigToolsOfed():

  def install (self):
    return mellanox_ofed_install()

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

class MellanoxConfigTools():

  def __init__(self):

    self._debug     = False
    try:
      dm = os.environ['MLNX_DEBUG']
    except:
      dm = 'no'
      os.environ['MLNX_DEBUG'] = dm
    if dm == 'yes':
      self._debug   = True

    self.opensmd    = MellanoxConfigToolsOpensmdService('opensmd')
    self.openibd    = MellanoxConfigToolsService('openibd')
    self.mst        = MellanoxConfigToolsService('mst')
    self.apt        = MellanoxConfigToolsApt()
    self.ofed       = MellanoxConfigToolsOfed()
    self.eipoib     = MellanoxConfigToolsEIPOIB()
    self.sysctl     = MellanoxConfigToolsSysctl()
    self.interface  = MellanoxConfigToolsInterface()
    self.sriov      = MellanoxConfigToolsSRIOV()
    self.connectx   = MellanoxConfigToolsConnectx()

  @property
  def debug(self):
    return self._debug

  @debug.setter
  def debug(self, v):
    self._debug = v
    allow_debug = "no"
    if self._debug:
      allow_debug = "yes"
    os.environ["MLNX_DEBUG"] = allow_debug

# --- OOP API: Mellanox Config Options ------------------------------------
class MellanoxCharmConfigOption(object):

  def __init__(self, config, db, option, default, configured):
    self._db = db
    self._config = config
    self._option = option
    self._current = self._config[self._option]
    self._previous = None
    self._default = default
    self._is_defined_in_config_file = configured
    self._previous = self._db.get(self._option)
    self.change_current()

  def change_current(self):
    self._changed = (self._previous is None or self._previous != self._current)
    self._db.set(self._option, self._current)
    self._db.flush()

  @property
  def configured(self):
    return self._is_defined_in_config_file

  @configured.setter
  def configured(self, v):
    pass

  @property
  def default(self):
    return self._default

  @default.setter
  def default(self, v):
    pass

  @property
  def current(self):
    return self._current

  @current.setter
  def current(self, v):
    self._current = v
    self._config[self._option] = self._current
    self.change_current()

  @property
  def changed(self):
    return self._changed

  @changed.setter
  def changed(self, changed):
    pass

  @property
  def previous(self):
    return self._previous

  @previous.setter
  def previous(self, v):
    pass

class MellanoxCharmConfig(dict):

  def __init__(self, opmap):
    self._db = unitdata.kv()
    self._config = hookenv.config()
    self._config_file = './config.yaml'
    self._config_file_data = None
    self._error = True

    try:
      f = open(self._config_file)
      self._error = False
    except:
      hookenv.log("Cannot open config file " + self._config_file)

    if not self._error:
      self._config_file_data = yaml.safe_load(f)
      f.close()
      for pkey, pdata in self._config_file_data['options'].items():
        self['_conf_' + pkey] = {
          'type':     pdata['type'],
          'default':  pdata['default'],
        }

    if type(opmap) is dict:
      for pkey, pname in opmap.items():
        default = None
        configured = False
        try:
          pkey_in_config = self['_conf_' + pkey]
          configured = True
          try:
            default = self['_conf_' + pkey]['default']
          except:
            pass
        except:
          pass
        self['_int_' + pname] = MellanoxCharmConfigOption(self._config, self._db, pkey, default, configured)
        setattr(self, pname, self['_int_' + pname])

# --- OOP API: Mellanox current node IP address -------------------------------
class MellanoxNodeIpAddress(object):

  def __init__(self, n):
    self._network = n
    self._ip_network = IPNetwork(self._network)
    self._ip_address = str(IPAddress(int(self._ip_network.ip) + int(os.environ['JUJU_MACHINE_ID']) + 1))
    self._network_mask = str(self._ip_network.netmask)

  @property
  def ip(self):
    return self._ip_address

  @ip.setter
  def ip(self, v):
    pass

  @property
  def network(self):
    return self._network

  @network.setter
  def network(self, v):
    pass

  @property
  def netmask(self):
    return self._network_mask

  @netmask.setter
  def netmask(self, v):
    pass

