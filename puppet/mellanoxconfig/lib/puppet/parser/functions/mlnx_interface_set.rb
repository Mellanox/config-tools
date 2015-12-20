# Copyright 2015 Mellanox Technologies, Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

require 'mellanoxconfig'
module Puppet::Parser::Functions
  newfunction(:mlnx_interface_unset, :type => :rvalue, :arity => -4, :doc => <<-EOD
  EOD
  ) do |arg|
    if_name = arg[0]
    if_alias = arg[1]
    ip_address = arg[2]
    net_mask = arg[3]
    mlnx = Mellanoxconfig.new()
    return mlnx.interface.set(if_name, if_alias, ip_address, net_mask)
  end
end
