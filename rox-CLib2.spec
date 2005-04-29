%define _name ROX-CLib2
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	A library for ROX applications
Summary(pl):	Biblioteka dla aplikacji ROXa
Name:		rox-CLib2
Version:	2.1.4
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://www.kerofin.demon.co.uk/rox/ROX-CLib-%{version}.tar.gz
# Source0-md5:	891dad75c0f5f98e4ef288bc6e417dd2
URL:		http://www.kerofin.demon.co.uk/rox/ROX-CLib.html
BuildRequires:	X11-devel
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	gtk+2-devel >= 2.0.1
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig
Requires:	rox >= 2.2.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
A library for ROX applications. It is a GTK+2 version.

%description -l pl
Biblioteka dla aplikacji ROXa. To jest wersja dla GTK+2.

%package devel
Summary:	ROX-CLib2 header files
Summary(pl):	Pliki nag³ówkowe do ROX-CLib2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0.1

%description devel
Header files for the ROX-CLib2 libraries.

%description devel -l pl
Pliki nag³ówkowe do bibliotek ROX-CLib2.

%package static
Summary:	ROX-CLib2 static libraries
Summary(pl):	Biblioteki statyczne ROX-CLib2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0.1

%description static
Static libraries for the ROX-CLib2 libraries.

%description static -l pl
Biblioteki statyczne dla ROX-CLib2.

%prep
%setup -q -n ROX-CLib

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{%{_platform}/bin,Help}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{_name},%{_libdir}}
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

install .DirIcon App* $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/{README,*.html} $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
cd %{_platform}
install bin/rox_run $RPM_BUILD_ROOT%{_bindir}
rm -f bin/{rox_run,test}
install bin/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}/bin
install lib/*.pc $RPM_BUILD_ROOT%{_pkgconfigdir}
install lib/librox-clib.{a,la,so,so.*.*.*} $RPM_BUILD_ROOT%{_libdir}
install include/rox/*.h $RPM_BUILD_ROOT%{_includedir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Help/{Authors,Changes,README,ToDo,Versions}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/librox-clib.so.*.*.*
%dir %{_appsdir}/%{_name}
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%dir %{_appsdir}/%{_name}/%{_platform}
%dir %{_appsdir}/%{_name}/%{_platform}/bin
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}/bin/*
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/.DirIcon
%dir %{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/Help/README

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_appsdir}/%{_name}/Help/*.html
%{_libdir}/*.la
%{_includedir}/%{_name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
