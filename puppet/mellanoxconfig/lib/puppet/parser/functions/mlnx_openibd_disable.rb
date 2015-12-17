require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_openibd_disable, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.openibd.disable()
  end
end
