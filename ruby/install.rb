#!/usr/bin/ruby

require "rbconfig"
modname = 'mellanoxconfig.rb'
rubylib = RbConfig::CONFIG["rubylibdir"]
libname = rubylib + '/' + modname
File::open(libname, "w") do |f|
  f.write File::open(modname).read
end
File::chmod 0644, libname
