
%define         os_usr_bin                      /usr/bin
%define         mlnx_project_name               config-tools
%define         mlnx_python_module              MellanoxConfig
%define         mlnx_home                       /opt/mellanox
%define         mlnx_bin                        %{mlnx_home}/bin
%define         mlnx_src                        %{mlnx_home}/src
%define         mlnx_sf_mellanox_config_tools   mellanox-config-tools
%define         mlnx_sd_mlnx_udev_namer         mlnx-udev-namer
%define         mlnx_sd_mlnx_python             python
%define         mlnx_sf_mlnx_python_setup       mellanoxconfig-setup.py
%define         mlnx_sd_mlnx_ruby               ruby
%define         mlnx_sf_mlnx_ruby_install       install.rb
%define         mlnx_sf_mlnx_ruby_uninstall     uninstall.rb
%define         mlnx_sd_mlnx_puppet             puppet
%define         mlnx_sf_mlnx_puppet_install     install.sh
%define         mlnx_sf_mlnx_puppet_uninstall   uninstall.sh

Name:           mellanox-%{mlnx_project_name}
Version:        %{?build_version}%{!?build_version:0.0.1}
Release:        %{?build_release}%{!?build_release:1}
Summary:        Mellanox Configuration Tools
Group:          System Environment/Base
BuildArch:      noarch
License:        GPLv2+
URL:            https://github.com/mellanox/%{mlnx_project_name}
Source0:        %{mlnx_project_name}.tar.gz
Requires:       boost boost-devel boost-static

%description
Mellanox Configuration Tools

%package python
Summary:        Mellanox Configuration Tools, Python API
Requires:       python python-pip mellanox-%{mlnx_project_name}
%description python
Mellanox Configuration Tools , Python API

%package ruby
Summary:        Mellanox Configuration Tools, Ruby API
Requires:       ruby mellanox-%{mlnx_project_name}
%description ruby
Mellanox Configuration Tools , Ruby API

%package puppet
Summary:        Mellanox Configuration Tools, Puppet API
Requires:       puppet mellanox-%{mlnx_project_name}-ruby
%description puppet
Mellanox Configuration Tools , Puppet API

%prep
%setup -q -n %{mlnx_project_name}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{mlnx_bin}
cp -f %{mlnx_sf_mellanox_config_tools} $RPM_BUILD_ROOT/%{mlnx_bin}
chmod +x $RPM_BUILD_ROOT/%{mlnx_bin}/%{mlnx_sf_mellanox_config_tools}

mkdir -p $RPM_BUILD_ROOT/%{mlnx_src}
cp -rf %{mlnx_sd_mlnx_udev_namer} $RPM_BUILD_ROOT/%{mlnx_src}
cp -rf %{mlnx_sd_mlnx_python} $RPM_BUILD_ROOT/%{mlnx_src}
cp -rf %{mlnx_sd_mlnx_ruby} $RPM_BUILD_ROOT/%{mlnx_src}
cp -rf %{mlnx_sd_mlnx_puppet} $RPM_BUILD_ROOT/%{mlnx_src}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%{mlnx_bin}/%{mlnx_sf_mellanox_config_tools}
%{mlnx_src}/%{mlnx_sd_mlnx_udev_namer}

%files python
%{mlnx_src}/%{mlnx_sd_mlnx_python}

%files ruby
%{mlnx_src}/%{mlnx_sd_mlnx_ruby}

%files puppet
%{mlnx_src}/%{mlnx_sd_mlnx_puppet}

%post
{
  [ -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} -o \
    -L %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} ] && \
      rm -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools}

  ln -s %{mlnx_bin}/%{mlnx_sf_mellanox_config_tools} \
        %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools}
} > /dev/null 2>&1

%preun
{
  %{mlnx_bin}/%{mlnx_sf_mellanox_config_tools} \
    udev-namer disable

  [ -f %{mlnx_bin}/%{mlnx_sf_mlnx_udev_namer} ] && \
    rm -f %{mlnx_bin}/%{mlnx_sf_mlnx_udev_namer}

  [ -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} -o \
    -L %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools} ] && \
      rm -f %{os_usr_bin}/%{mlnx_sf_mellanox_config_tools}
} > /dev/null 2>&1

%post python
{
  if [ -f %{mlnx_src}/%{mlnx_sd_mlnx_python}/%{mlnx_sf_mlnx_python_setup} ]; then
    cd %{mlnx_src}/%{mlnx_sd_mlnx_python}
    python %{mlnx_sf_mlnx_python_setup} install
    python %{mlnx_sf_mlnx_python_setup} clean --all
    cd -
  fi
} > /dev/null 2>&1

%preun python
{
  pip uninstall -y %{mlnx_python_module}
} > /dev/null 2>&1

%post ruby
{
  if [ -f %{mlnx_src}/%{mlnx_sd_mlnx_ruby}/%{mlnx_sf_mlnx_ruby_install} ]; then
    cd %{mlnx_src}/%{mlnx_sd_mlnx_ruby}
    ruby %{mlnx_sf_mlnx_ruby_install}
    cd -
  fi
} > /dev/null 2>&1

%preun ruby
{
  if [ -f %{mlnx_src}/%{mlnx_sd_mlnx_ruby}/%{mlnx_sf_mlnx_ruby_uninstall} ]; then
    cd %{mlnx_src}/%{mlnx_sd_mlnx_ruby}
    ruby %{mlnx_sf_mlnx_ruby_uninstall}
    cd -
  fi
} > /dev/null 2>&1

%post puppet
{
  [ -f %{mlnx_src}/%{mlnx_sd_mlnx_puppet}/%{mlnx_sf_mlnx_puppet_install} ] && \
    /bin/bash %{mlnx_src}/%{mlnx_sd_mlnx_puppet}/%{mlnx_sf_mlnx_puppet_install}
} > /dev/null 2>&1

%preun puppet
{
  [ -f %{mlnx_src}/%{mlnx_sd_mlnx_puppet}/%{mlnx_sf_mlnx_puppet_uninstall} ] && \
    /bin/bash %{mlnx_src}/%{mlnx_sd_mlnx_puppet}/%{mlnx_sf_mlnx_puppet_uninstall}
} > /dev/null 2>&1

%changelog
