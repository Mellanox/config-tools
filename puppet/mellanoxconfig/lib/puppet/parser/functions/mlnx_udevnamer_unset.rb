require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_udevnamer_unset, :type => :rvalue, :arity => 1, :doc => <<-EOD
  EOD
  ) do |arg|
    var = arg[0]
    mlnx = Mellanoxconfig.new()
    return mlnx.udevnamer.unset(var)
  end
end
