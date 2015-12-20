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
  newfunction(:mlnx_sriov_modprobe_set, :type => :rvalue, :arity => -3, :doc => <<-EOD
  EOD
  ) do |arg|
    mode_port_0 = arg[0]
    mode_port_1 = arg[1]
    num_vf = arg[2]
    probe_vf = arg[3]
    mlnx = Mellanoxconfig.new()
    return mlnx.sriov.modprobe.set(mode_port_0, mode_port_1, num_vf, probe_vf)
  end
end
