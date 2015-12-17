require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_mst_restart, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.mst.restart()
  end
end
