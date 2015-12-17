require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_sysctl_set, :type => :rvalue, :arity => 2, :doc => <<-EOD
  EOD
  ) do |arg|
    var = arg[0]
    val = arg[1]
    mlnx = Mellanoxconfig.new()
    return mlnx.sysctl.set(var, val)
  end
end
