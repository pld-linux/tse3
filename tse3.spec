Summary:	Trax Sequencer Engine.
Summary(pl):	Trax Sequencer Engine.
Name:		tse3
Version:	0.0.7
Release:	1
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
License:	GPL
Source0:	http://download.sourceforge.net/TSE3/%{name}-%{version}.tar.gz
URL:		http://download.sourceforge.net/TSE3/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TSE3 is a powerful open source sequencer engine written in C++. 
It is a 'sequencer engine' because it provides the actual driving 
force elements of a sequencer but provides no form of fancy interface. 
Sequencer applications or multimedia presentation packages will incorporate 
the TSE3 libraries to provide a user with MIDI sequencing facilities. 

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description -l pl devel
Pliki nag³ówkowe %{name}.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
CXXFLAGS="$RPM_OPT_FLAGS"; export CXXFLAGS
#aclocal
#automake
#autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	AUTHORS README* ChangeLog* NEWS

rm -f doc/Makefile*

%post
/sbin/ldconfig

%postun 
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
