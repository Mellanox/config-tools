require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_sriov_modprobe_set, :type => :rvalue, :arity => -3, :doc => <<-EOD
  EOD
  ) do |arg|
    mode_port_0 = arg[0]
    mode_port_1 = arg[1]
    num_vf = arg[2]
    probe_vf = arg[3]
    mlnx = Mellanoxconfig.new()
    return mlnx.sriov.modprobe.set(mode_port_0, mode_port_1, num_vf, probe_vf)
  end
end
