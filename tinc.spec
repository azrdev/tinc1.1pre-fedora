Name:           tinc
Version:        1.0.19
Release:        1%{?dist}
Summary:        A virtual private network daemon

Group:          Applications/Internet
License:        GPLv2+
URL:            http://www.tinc-vpn.org/
Source0:        http://www.tinc-vpn.org/packages/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel
BuildRequires:  lzo-devel

Requires(post):  info
Requires(preun): info


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
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_infodir}/dir


%clean
rm -rf %{buildroot}


%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :


%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.README NEWS README THANKS doc/sample* doc/*.tex
%{_mandir}/man*/%{name}*.*
%{_infodir}/%{name}.info.gz
%{_sbindir}/%{name}d


%changelog
* Tue Jun 26 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.19-1
- Updated to new upstream version 1.0.16

* Sat Mar 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.18-1
- Updated to new upstream version 1.0.18

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.16-1
- Updated to new upstream version 1.0.16

* Wed Apr 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.13-1
- Updated to new upstream version 1.0.13

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 15 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.12-1
- Updated to new upstream version 1.0.12

* Mon Dec 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.11-1
- Updated to new upstream version 1.0.11

* Thu Oct 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.10-1
- Removed translation stuff
- Updated to new upstream version 1.0.10

* Mon Dec 29 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.9-1
- Initial package for Fedora
