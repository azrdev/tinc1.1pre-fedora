Name:           tinc
Version:        1.1
Summary:        A virtual private network daemon
License:        GPLv2+
URL:            http://www.tinc-vpn.org/

%global commit0 3f6c663a06aac728912c4e47cbc2dc4343a3798c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Epoch:          1
Release:        0.12.20160501git%{shortcommit0}%{?dist}
Source0:        https://github.com/gsliepen/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:        %{name}d@.service
# TODO: systemd unit should be upstream now
# TODO: firewalld config file

BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  openssl-devel
BuildRequires:  lzo-devel
BuildRequires:  systemd
BuildRequires:  systemd-units
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  texinfo

Requires:  openssl
Requires:  lzo
Requires:  readline
Requires:  ncurses-libs

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
%autosetup -n %{name}-%{commit0}

%build
autoreconf -fsi
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
%doc AUTHORS COPYING COPYING.README NEWS README THANKS doc/sample* doc/*.tex
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.gz
%{_bindir}/%{name}-gui
%{_sbindir}/%{name}
%{_sbindir}/%{name}d
%{_sbindir}/sptps_keypair
%{_sbindir}/sptps_speed
%{_sbindir}/sptps_test
%{_unitdir}/%{name}d@.service

%changelog
* Sun May 01 2016 Jonathan Biegert <azrdev@qrdn.de> - 1.1-0.12.20160501git3f6c663
- Staying to git HEAD, for builds of pre-releases only see https://copr.fedorainfracloud.org/coprs/azrdev/tinc-prerelease/

* Mon Feb 15 2016 Jonathan Biegert <azrdev@qrdn.de> - 1.1pre11-3.20160213gitd8ca00fe
- Fix Release number
- Fix systemd unit script (--kill does not exist anymore, add reload)

* Sun Feb 14 2016 Jonathan Biegert <azrdev@qrdn.de> - 1.1pre11-20160213gitd8ca00fe
- Update to git branch 1.1 HEAD

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

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
