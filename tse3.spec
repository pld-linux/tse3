#
# Conditional build:
# _with_arts		- with arts library
# _with_oss		- with OSS kernel sound drivers
# _without_alsa		- without ALSA support
#
Summary:	Trax Sequencer Engine
Summary(pl):	Trax Sekwencer
Name:		tse3
Version:	0.2.7
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6ccab942cc51a648af76653771479eed
URL:		http://tse3.sourceforge.net/
%{!?_without_alsa:BuildRequires:       alsa-lib-devel}
%{?_with_arts:BuildRequires:	arts-devel}
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
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{?_with_arts:--with-aRts} \
        %{?_without_alsa:--without-alsa} \
        %{?_with_oss:--with-oss} \
        --without-win32

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/songs

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp demos/*.tse3 $RPM_BUILD_ROOT%{_datadir}/%{name}/songs
rm -f doc/Makefile*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{*.html,*.png,*.gif} AUTHORS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/songs/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
