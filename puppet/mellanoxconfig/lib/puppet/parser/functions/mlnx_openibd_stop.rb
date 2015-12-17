require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_openibd_stop, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.openibd.stop()
  end
end
