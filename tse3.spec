#
# Conditional build:
%bcond_with	arts	# with aRts support
%bcond_without	oss	# without OSS drivers support
%bcond_without	alsa	# without ALSA support
#
Summary:	Trax Sequencer Engine
Summary(pl.UTF-8):	Silnik sekwencera Trax
Name:		tse3
Version:	0.3.1
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/tse3/%{name}-%{version}.tar.gz
# Source0-md5:	3b7e35505160e2d761e5b43abb636f3c
Patch0:		%{name}-alsa1_0.patch
Patch1:		%{name}-types.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-awe_voice.patch
Patch4:		gcc.patch
URL:		http://tse3.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0}
%{?with_arts:BuildRequires:	arts-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TSE3 is a powerful open source sequencer engine written in C++. It is
a 'sequencer engine' because it provides the actual driving force
elements of a sequencer but provides no form of fancy interface.
Sequencer applications or multimedia presentation packages will
incorporate the TSE3 libraries to provide a user with MIDI sequencing
facilities.

%description -l pl.UTF-8
TSE3 jest potężnym silnikiem sekwencera napisanym w C++ z
wolnodostępnymi źródłami. Jest to "silnik sekwencera", ponieważ
dostarcza właściwe elementy "napędzające" sekwencer, ale nie
zawiera żadnego ładnego interfejsu. Aplikacje sekwencera lub
prezentacji multimedialnych mogą korzystać z bibliotek TSE3, aby
dostarczyć użytkownikowi możliwości sekwencera MIDI.

%package devel
Summary:	Tse3 header files
Summary(pl.UTF-8):	Pliki nagłówkowe tse3
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_alsa:Requires:	alsa-lib-devel >= 1.0}
%{?with_arts:Requires:	arts-devel}
Requires:	libstdc++-devel

%description devel
Tse3 header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe tse3.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_arts:--without-aRts} \
	%{!?with_alsa:--without-alsa} \
	%{!?with_oss:--without-oss} \
	--without-win32
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/songs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp demos/*.tse3 $RPM_BUILD_ROOT%{_datadir}/%{name}/songs
rm -f doc/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/{*.html,*.png,*.gif} AUTHORS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.0
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/songs
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
