#!/usr/bin/ruby

require "rbconfig"
modname = 'mellanoxconfig.rb'
rubylib = RbConfig::CONFIG["rubylibdir"]
File::delete(rubylib + '/' + modname)
