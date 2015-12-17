require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_sriov_kernel_disable, :type => :rvalue, :arity => 0, :doc => <<-EOD
  EOD
  ) do |arg|
    mlnx = Mellanoxconfig.new()
    return mlnx.sriov.kernel.disable()
  end
end
