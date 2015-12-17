require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_ofed_remove, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.ofed.remove()
  end
end
