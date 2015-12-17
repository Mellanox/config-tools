require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_opensmd_vlan2pk, :type => :rvalue, :arity => -2, :doc => <<-EOD
  EOD
  ) do |arg|
    vlan_min = arg[0]
    vlan_max = arg[1]
    pk_min = arg[2]
    mlnx = Mellanoxconfig.new()
    return mlnx.opensmd.vlan2pk(vlan_min, vlan_max, pk_min)
  end
end
