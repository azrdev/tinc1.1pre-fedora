Name:           tinc
Version:        1.1
Summary:        A virtual private network daemon
License:        GPLv2+
URL:            http://www.tinc-vpn.org/
Group:          Applications/Internet

%global commit0 2b0aeec02d64bb4724da9ff1dbc19b7d35d7c904
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Epoch:          1
Release:        0.67.20190317git%{shortcommit0}%{?dist}
Source0:        https://github.com/gsliepen/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake

BuildRequires:  gcc
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
%configure --with-systemd=%{_unitdir}
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :
%systemd_post %{name}@.service

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi
%systemd_preun %{name}@.service

%postun
%systemd_postun_with_restart %{name}@.service

%files
%doc AUTHORS COPYING.README NEWS README THANKS doc/sample* doc/*.tex
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.gz
%{_sbindir}/%{name}
%{_sbindir}/%{name}d
%{_unitdir}/%{name}*.service
%{_datarootdir}/bash-completion/completions/%{name}

%changelog
* Tue Oct  9 2018 Jonathan Biegert <azrdev@qrdn.de> - 1.1-0.60.20181009git45ad0de
- Merge .spec changes from f29 into tinc1.1pre-branch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.33-3
- Fix BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.33-1
- Update to new upstream version 1.0.33

* Sat Sep 30 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.32-1
- Update to new upstream version 1.0.32

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.31-1
- Update to new upstream version 1.0.31

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.30-1
- Update to new upstream version 1.0.30

* Thu May 19 2016 Jonathan Biegert <azrdev@qrdn.de> - 1.1-0.15.20160501git3f6c663
- Remove firewalld service file: Already provided by packet firewalld
- Bump git commit (as always)

* Tue May 17 2016 Jonathan Biegert <azrdev@qrdn.de> - 1.1-0.14.20160501git3f6c663
- Add firewalld service file

* Sun May 01 2016 Jonathan Biegert <azrdev@qrdn.de> - 1.1-0.11.20160501git3f6c663
- Staying to git HEAD, for builds of pre-releases only see https://copr.fedorainfracloud.org/coprs/azrdev/tinc-prerelease/

* Sat Apr 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.28-1
- Use upstream service units
- Update to new upstream version 1.0.28

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
