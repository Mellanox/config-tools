require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_sriov_firmware_burn, :type => :rvalue, :arity => -1, :doc => <<-EOD
  EOD
  ) do |arg|
    num_vf = arg[0]
    mlnx = Mellanoxconfig.new()
    return mlnx.sriov.firmware.burn(num_vf)
  end
end
