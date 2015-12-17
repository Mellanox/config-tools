require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_repository_ofed, :type => :rvalue, :arity => -1, :doc => <<-EOD
  EOD
  ) do |arg|
    version = arg[0]
    mlnx = Mellanoxconfig.new()
    return mlnx.repository.ofed(version)
  end
end
