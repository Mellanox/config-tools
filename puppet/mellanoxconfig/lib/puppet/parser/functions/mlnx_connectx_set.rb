require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_connectx_set, :type => :rvalue, :arity => 2, :doc => <<-EOD
  EOD
  ) do |arg|
    mode_port_0 = arg[0]
    mode_port_1 = arg[1]
    mlnx = Mellanoxconfig.new()
    return mlnx.connectx.set(mode_port_0, mode_port_1)
  end
end
