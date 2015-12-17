require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_eipoib_disable, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.eipoib.disable()
  end
end
