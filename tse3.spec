Summary:	Trax Sequencer Engine
Summary(pl):	Trax Sekwencer
Name:		tse3
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://download.sourceforge.net/TSE3/%{name}-%{version}.tar.gz
URL:		http://download.sourceforge.net/TSE3/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TSE3 is a powerful open source sequencer engine written in C++. It is
a 'sequencer engine' because it provides the actual driving force
elements of a sequencer but provides no form of fancy interface.
Sequencer applications or multimedia presentation packages will
incorporate the TSE3 libraries to provide a user with MIDI sequencing
facilities.

%description -l pl
TSE3 jest potê¿nym enginem sekwencera napisanym w C++ z
wolnodostêpnymi ¼ród³ami.

%package devel
Summary:	Tse3 header files
Summary(pl):	Pliki nag³ówkowe tse3
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Tse3 header files.

%description devel -l pl
Pliki nag³ówkowe tse3.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-rtti"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f doc/Makefile*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS README* ChangeLog* NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
