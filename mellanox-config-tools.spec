
%define         os_usr_bin                      /usr/bin
%define         mlnx_project_name               config-tools
%define         mlnx_python_module              MellanoxConfig
%define         mlnx_home                       /opt/mellanox
%define         mlnx_bin                        %{mlnx_home}/bin
%define         mlnx_src                        %{mlnx_home}/src
%define         mlnx_sd_mellanoxconfig          mellanoxconfig
%define         mlnx_sd_mlnx_udev_namer         mlnx-udev-namer
%define         mlnx_sf_mlnx_udev_namer         mlnx-udev-namer
%define         mlnx_sf_mellanox_config_tools   mellanox-config-tools
%define         mlnx_sf_mellanoxconfig_setup    mellanoxconfig-setup.py

Name:           mellanox-%{mlnx_project_name}
Version:        %{?build_version}%{!?build_version:0.0.1}
Release:        %{?build_release}%{!?build_release:1}
Summary:        Mellanox Configuration Tools
Group:          System Environment/Base
BuildArch:      noarch
License:        GPLv2+
URL:            https://github.com/mellanox/%{mlnx_project_name}
Source0:        %{mlnx_project_name}.tar.gz

Requires:       python python-pip boost boost-devel boost-static

%description
Mellanox Configuration Tools

%prep
%setup -q -n %{mlnx_project_name}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{mlnx_bin}
cp -f %{mlnx_sf_mellanox_config_tools} $RPM_BUILD_ROOT/%{mlnx_bin}
chmod +x $RPM_BUILD_ROOT/%{mlnx_bin}/%{mlnx_sf_mellanox_config_tools}

mkdir -p $RPM_BUILD_ROOT/%{mlnx_src}
cp -rf %{mlnx_sd_mellanoxconfig} $RPM_BUILD_ROOT/%{mlnx_src}
cp -f %{mlnx_sf_mellanoxconfig_setup} $RPM_BUILD_ROOT/%{mlnx_src}
cp -rf %{mlnx_sd_mlnx_udev_namer} $RPM_BUILD_ROOT/%{mlnx_src}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%{mlnx_bin}
%{mlnx_src}

%post
[ -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} -o \
  -L %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} ] && \
    rm -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools}

ln -s %{mlnx_bin}/%{mlnx_sf_mellanox_config_tools} \
      %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools}

if [ -d %{mlnx_src} -a \
      -d %{mlnx_src}/%{mlnx_sd_mellanoxconfig} -a \
      -f %{mlnx_src}/%{mlnx_sf_mellanoxconfig_setup} ]; then
  {
    cd %{mlnx_src}
    python %{mlnx_sf_mellanoxconfig_setup} install
    python %{mlnx_sf_mellanoxconfig_setup} clean --all
    cd -
  } > /dev/null 2>&1
fi

%preun
{
  %{mlnx_bin}/%{mlnx_sf_mellanox_config_tools} \
    udev-namer disable

  [ -f %{mlnx_bin}/%{mlnx_sf_mlnx_udev_namer} ] && \
    rm -f %{mlnx_bin}/%{mlnx_sf_mlnx_udev_namer}

  [ -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} -o \
    -L %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} ] && \
      rm -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools}

  pip uninstall -y %{mlnx_python_module}
} > /dev/null 2>&1

%changelog
