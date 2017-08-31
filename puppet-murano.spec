%{!?upstream_version: %global upstream_version %{commit}}
%global commit 75837136f0c8a9c7b334d6a3d757425382058934
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-murano
Version:                11.3.0
Release:                1%{?alphatag}%{?dist}
Summary:                Puppet module for OpenStack Murano
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-murano

Source0:                https://github.com/openstack/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:              noarch

BuildRequires:          git

Requires:               puppet-inifile
Requires:               puppet-keystone
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-oslo

Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Murano (Application Catalog).

%prep
%autosetup -n openstack-murano-%{upstream_version} -S git


find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/murano/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/murano/



%files
%{_datadir}/openstack-puppet/modules/murano/


%changelog
* Thu Aug 31 2017 Yatin Karel <ykarel@redhat.org> - 11.3.0-1.75837136git
- Pike update (75837136f0c8a9c7b334d6a3d757425382058934)

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 11.3.0-1
- Update to 11.3.0

