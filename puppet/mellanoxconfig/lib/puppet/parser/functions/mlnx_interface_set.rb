require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_interface_unset, :type => :rvalue, :arity => -4, :doc => <<-EOD
  EOD
  ) do |arg|
    if_name = arg[0]
    if_alias = arg[1]
    ip_address = arg[2]
    net_mask = arg[3]
    mlnx = Mellanoxconfig.new()
    return mlnx.interface.set(if_name, if_alias, ip_address, net_mask)
  end
end
