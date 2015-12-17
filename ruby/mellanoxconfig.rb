# -------------------------------------------------------------------------------
class Mellanoxconfig

  VERSION                 = "0.0.1"
  CONFIG_TOOLS_ENV_DEBUG  = 'MLNX_DEBUG'
  CONFIG_TOOLS_FILENAME   = 'mellanox-config-tools'
  CONFIG_TOOLS_LOCATION   = ['/usr/bin', '/opt/mellanox/bin']

end

# -------------------------------------------------------------------------------
class MellanoxconfigDebug

  def initialize(m)
    @mlnx = m
  end

  def enable()
    @mlnx.config_tools_debug = true
    return true
  end

  def disable()
    @mlnx.config_tools_debug = false
    return true
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigRepository

  def initialize(m)
    @mlnx = m
  end

  def ofed(v='')
    return @mlnx.config_tools_run(['configure-repository-ofed', v])
  end

  def openstack(v='')
    return @mlnx.config_tools_run(['configure-repository-openstack', v])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigOfed

  def initialize(m)
    @mlnx = m
  end

  def install(v='')
    return @mlnx.config_tools_run(['install', v])
  end

  def bundle_deploy(v='')
    return @mlnx.config_tools_run(['ofed-bundle-deploy', v])
  end

  def remove()
    return @mlnx.config_tools_run(['remove'])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigEIPOIB

  def initialize(m)
    @mlnx = m
  end

  def enable()
    return @mlnx.config_tools_run(['e-ipoib', 'enable'])
  end

  def disable()
    return @mlnx.config_tools_run(['e-ipoib', 'disable'])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigService

  def initialize(m, s)
    @mlnx = m
    @srv = s
  end

  def _call_(cmd)
    rc = 255
    if @srv == 'opensmd' or @srv == 'openibd' or @srv == 'mst'
      $rc = @mlnx.config_tools_run([@srv, cmd])
    end
    return rc
  end

  def enable()
    return _call_('enable')
  end

  def disable()
    return _call_('disable')
  end

  def start()
    return _call_('start')
  end

  def stop()
    return _call_('stop')
  end

  def restart()
    return _call_('restart')
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigServiceOpensmd < MellanoxconfigService

  def vlan2pk(vlan_min=1, vlan_max=16, pk_min=1)
    return @mlnx.config_tools_run(['pk-to-vlan-map', vlan_min, vlan_max, pk_min])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigSysctl

  def initialize(m)
    @mlnx = m
  end

  def set(var, val)
    return @mlnx.config_tools_run(['sysctl-conf', 'set', var, val])
  end

  def unset(var)
    return @mlnx.config_tools_run(['sysctl-conf', 'unset', var])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigInterface

  def initialize(m)
    @mlnx = m
  end

  def set(if_name, if_alias, ip_address, net_mask='255.255.255.0')
    return @mlnx.config_tools_run(['interface', 'set', if_name, if_alias, ip_address, net_mask])
  end

  def unset(if_name, if_alias)
    return @mlnx.config_tools_run(['interface', 'unset', if_name, if_alias])
  end

  def up(if_name, if_alias)
    return @mlnx.config_tools_run(['interface', 'up', if_name, if_alias])
  end

  def down(if_name, if_alias)
    return @mlnx.config_tools_run(['interface', 'down', if_name, if_alias])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigSRIOVKernel

  def initialize(m)
    @mlnx = m
  end

  def enable()
    return @mlnx.config_tools_run(['sriov', 'enable'])
  end

  def disable()
    return @mlnx.config_tools_run(['sriov', 'disable'])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigSRIOVFirmware

  def initialize(m)
    @mlnx = m
  end

  def enable()
    return @mlnx.config_tools_run(['sriov-fw', 'enable'])
  end

  def disable()
    return @mlnx.config_tools_run(['sriov-fw', 'disable'])
  end

  def burn(num_vf=16)
    return @mlnx.config_tools_run(['burn-vfs-in-fw', num_vf])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigSRIOVModprobe

  def initialize(m)
    @mlnx = m
  end

  def set(mode_port_0='ib', mode_port_1='ib', num_vf=0, probe_vf=0)
    return @mlnx.config_tools_run(['set-vf-type-num', mode_port_0, mode_port_1, num_vf, probe_vf])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigSRIOV

  def initialize(m)
    @mlnx = m
    @kernel   = MellanoxconfigSRIOVKernel.new(@mlnx)
    @firmware = MellanoxconfigSRIOVFirmware.new(@mlnx)
    @modprobe = MellanoxconfigSRIOVModprobe.new(@mlnx)
  end

  def kernel
    @kernel
  end

  def firmware
    @firmware
  end

  def modprobe
    @modprobe
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigConnectx

  def initialize(m)
    @mlnx = m
  end

  def set(mode_port_0='ib', mode_port_1='ib')
    return @mlnx.config_tools_run(['connectx-port-config', mode_port_0, mode_port_1])
  end

end

# -------------------------------------------------------------------------------
class MellanoxconfigUDEVNamer

  def initialize(m)
    @mlnx = m
  end

  def enable()
    return @mlnx.config_tools_run(['udev-namer', 'enable'])
  end

  def disable()
    return @mlnx.config_tools_run(['udev-namer', 'disable'])
  end

  def set(var, val)
    return @mlnx.config_tools_run(['udev-namer-config', 'set', var, val])
  end

  def unset(var)
    return @mlnx.config_tools_run(['udev-namer-config', 'unset', var])
  end

end

# -------------------------------------------------------------------------------
class Mellanoxconfig

  def initialize()
    @config_tools_exec = nil
    CONFIG_TOOLS_LOCATION.each do |d|
      f = d + '/' + CONFIG_TOOLS_FILENAME
      if File.exist?(f)
        @config_tools_exec = f
      end
    end
    if @config_tools_exec == nil
      print "ERROR: Not found Mellanox Config Tools\n"
    end
    @config_tools_debug = false
    @debug      = MellanoxconfigDebug.new(self)
    @repository = MellanoxconfigRepository.new(self)
    @ofed       = MellanoxconfigOfed.new(self)
    @eipoib     = MellanoxconfigEIPOIB.new(self)
    @openibd    = MellanoxconfigService.new(self, 'openibd')
    @mst        = MellanoxconfigService.new(self, 'mst')
    @opensmd    = MellanoxconfigServiceOpensmd.new(self, 'opensmd')
    @sysctl     = MellanoxconfigSysctl.new(self)
    @interface  = MellanoxconfigInterface.new(self)
    @sriov      = MellanoxconfigSRIOV.new(self)
    @connectx   = MellanoxconfigConnectx.new(self)
    @udevnamer  = MellanoxconfigUDEVNamer.new(self)
  end

  def VERSION
    return VERSION
  end

  def config_tools_debug=(m)
    @config_tools_debug = m
  end

  def debug
    @debug
  end

  def repository
    @repository
  end

  def ofed
    @ofed
  end

  def eipoib
    @eipoib
  end

  def openibd
    @openibd
  end

  def mst
    @mst
  end

  def opensmd
    @opensmd
  end

  def sysctl
    @sysctl
  end

  def interface
    @interface
  end

  def sriov
    @sriov
  end

  def connectx
    @connectx
  end

  def udevnamer
    @udevnamer
  end

  def config_tools_run(params=[])
    rc = 255
    if @config_tools_exec == nil
      print "ERROR: Not specified path of Mellanox Config Tools\n"
    else
      run_str = 'export ' + CONFIG_TOOLS_ENV_DEBUG + '='
      if @config_tools_debug
        run_str += 'true'
      else
        run_str += 'false'
      end
      run_str += '; /bin/bash ' + @config_tools_exec
      params.each do |p|
        if p == nil
          run_str += " ''"
        else
          run_str += " '" + p.to_s + "'"
        end
      end
      system run_str
      rc = $?
      if rc != 0 and @config_tools_debug
        print "ERROR: Running '" + run_str + "'\n"
        print "       Return error code=" + rc + "\n"
      end
    end
    return rc
  end

end

