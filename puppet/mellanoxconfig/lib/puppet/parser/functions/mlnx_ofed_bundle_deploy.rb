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
  newfunction(:mlnx_ofed_bundle_deploy, :type => :rvalue, :arity => -1, :doc => <<-EOD
  EOD
  ) do |arg|
    version = arg[0]
    mlnx = Mellanoxconfig.new()
    return mlnx.ofed.bundle_deploy(version)
  end
end
