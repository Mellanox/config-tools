#!/bin/bash

modname=mellanox-mellanoxconfig
builddir=$(dirname "`readlink -f "$0"`")/mellanoxconfig
[ "x$builddir" == ''x ] && exit 1
{
  [ -d $builddir/pkg ] && rm -rfv $builddir/pkg
  puppet module uninstall $modname --force 2>&1 > /dev/null
} 2>&1 > /dev/null
