require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_opensmd_stop, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.opensmd.stop()
  end
end
