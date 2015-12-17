require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_ofed_install, :type => :rvalue, :arity => -1, :doc => <<-EOD
  EOD
  ) do |arg|
    version = arg[0]
    mlnx = Mellanoxconfig.new()
    return mlnx.ofed.install(version)
  end
end
