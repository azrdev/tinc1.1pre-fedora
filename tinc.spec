Name:           tinc
Version:        1.0.28
Release:        1%{?dist}
Summary:        A virtual private network daemon

License:        GPLv2+
URL:            http://www.tinc-vpn.org/
Source0:        http://www.tinc-vpn.org/packages/%{name}-%{version}.tar.gz
Source1:        %{name}d@.service

BuildRequires:  openssl-devel
BuildRequires:  lzo-devel
BuildRequires:  systemd
BuildRequires:  systemd-units

Requires(post):   info
Requires(post):   systemd
Requires(preun):  info
Requires(preun):  systemd
Requires(postun): systemd

%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}d@.service
rm -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :
%systemd_post %{name}d@.service

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi
%systemd_preun %{name}d@.service

%postun
%systemd_postun_with_restart %{name}d@.service

%files
%doc AUTHORS COPYING.README NEWS README THANKS doc/sample* doc/*.tex
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.gz
%{_sbindir}/%{name}d
%{_unitdir}/%{name}d@.service

%changelog
* Sat Apr 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.28-1
- Update to new upstream version 1.0.28

* Fri Jan 29 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.26-1
- Update to new upstream version 1.0.26

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-6
- Fix service file (rhbz#1155666)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-3
- Update systemd

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-2
- Migration to systemd (rhbz#1078237)

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.24-1
- Update to new upstream version 1.0.24

* Tue Oct 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.23-1
- Update to new upstream version 1.0.23

* Mon Aug 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.22-1
- Update to new upstream version 1.0.22

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.21-1
- Update to new upstream version 1.0.21

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.19-1
- Update to new upstream version 1.0.16

* Sat Mar 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.18-1
- Update to new upstream version 1.0.18

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-1
- Update to new upstream version 1.0.16

* Wed Apr 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.13-1
- Update to new upstream version 1.0.13

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 15 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.12-1
- Update to new upstream version 1.0.12

* Mon Dec 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.11-1
- Update to new upstream version 1.0.11

* Thu Oct 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.10-1
- Removed translation stuff
- Update to new upstream version 1.0.10

* Mon Dec 29 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.9-1
- Initial package for Fedora
