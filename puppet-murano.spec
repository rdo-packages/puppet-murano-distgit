%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-murano
Version:                15.5.0
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Murano
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-murano

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-keystone
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-oslo

Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Murano (Application Catalog).

%prep
%setup -q -n openstack-murano-%{upstream_version}


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
* Wed Jun 16 2021 RDO <dev@lists.rdoproject.org> 15.5.0-1
- Update to 15.5.0

* Fri Oct 04 2019 RDO <dev@lists.rdoproject.org> 15.4.0-1
- Update to 15.4.0


