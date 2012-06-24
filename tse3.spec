Summary:	Trax Sequencer Engine
Summary(pl):	Trax Sequencer Engine
Name:		tse3
Version:	0.0.14
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
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

%package devel
Summary:	Tse3 header files
Summary(pl):	Pliki nag��wkowe tse3
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Tse3 header files.

%description -l pl devel
Pliki nag��wkowe tse3.

%prep
%setup -q

%build
CXXFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -fno-rtti"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README* ChangeLog* NEWS

rm -f doc/Makefile*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
