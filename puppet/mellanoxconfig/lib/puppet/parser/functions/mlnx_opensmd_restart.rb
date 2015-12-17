require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_opensmd_restart, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.opensmd.restart()
  end
end
