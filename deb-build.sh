#!/bin/bash

                       mlnx_bin=/opt/mellanox/bin
                       mlnx_src=/opt/mellanox/src
  mlnx_sf_mellanox_config_tools=mellanox-config-tools
        mlnx_sd_mlnx_udev_namer=mlnx-udev-namer
                 mlnx_sd_python=python

mlnx_bin=deb${mlnx_bin}
mlnx_src=deb${mlnx_src}

rm -rfv deb/opt
mkdir -p ${mlnx_bin} ${mlnx_src}
cp -f ${mlnx_sf_mellanox_config_tools} ${mlnx_bin}
chmod +x ${mlnx_bin}/${mlnx_sf_mellanox_config_tools}
cp -rf ${mlnx_sd_mlnx_udev_namer} ${mlnx_src}
cp -rf ${mlnx_sd_python} ${mlnx_src}
cd deb
dpkg-buildpackage -b -tc -uc
cd -
rm -rfv deb/opt
