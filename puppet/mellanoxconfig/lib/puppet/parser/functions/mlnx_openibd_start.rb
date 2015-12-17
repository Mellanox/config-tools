require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_openibd_start, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.openibd.start()
  end
end
