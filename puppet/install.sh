#!/bin/bash

ignoredeps=''
[ "x$1" == 'xignoredeps' ] && ignoredeps='--ignore-dependencies'
modname=mellanox-mellanoxconfig
builddir=$(dirname "`readlink -f "$0"`")/mellanoxconfig
[ "x$builddir" == ''x ] && exit 1
{
  [ -d $builddir/pkg ] && rm -rfv $builddir/pkg
  puppet module uninstall $modname --force 2>&1 > /dev/null
  puppet module build $builddir
  find $builddir/pkg -name ${modname}-*.tar.gz -exec puppet module install {} $ignoredeps \;
  [ -d $builddir/pkg ] && rm -rfv $builddir/pkg
} 2>&1 > /dev/null
