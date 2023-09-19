%define url_ver %(echo %{version}|cut -d. -f1,2)

%define pkgname	gtkmm
%define api	2.4
%define major	1
%define libname	%mklibname %{pkgname} %{api} %{major}
%define libgdkmm %mklibname gdkmm %{api} %{major}
%define devname	%mklibname -d %{pkgname} %{api}

Summary:	C++ interface for popular GUI library gtk+
Name:		%{pkgname}%{api}
Version:	2.24.5
Release:	10
#gw lib is LGPL, tool is GPL
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
Url:		https://gtkmm.sourceforge.net/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gtkmm/%{url_ver}/%{pkgname}-%{version}.tar.xz

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(atkmm-1.6)
BuildRequires:	pkgconfig(cairomm-1.0)
BuildRequires:	pkgconfig(pangomm-1.4)

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package	-n %{libname}
Summary:	C++ interface for popular GUI library gtk+
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}
Provides:	%{pkgname}%{api} = %{version}-%{release}

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{pkgname}.

%package	-n %{libgdkmm}
Summary:	C++ interface for popular GUI library gtk+
Group:		System/Libraries
Conflicts:	%{_lib}gtkmm2.4_1 < 2.24.2-8

%description	-n %{libgdkmm}
This package contains the library needed to run programs dynamically
linked with %{pkgname}.

%package	-n %{devname}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgdkmm} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-doc < 2.24.2-8

%description	-n %{devname}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.

%prep
%setup -qn %{pkgname}-%{version}

%build
%configure \
	--enable-shared

%make
# make check does nothing

%install
%makeinstall_std MMDOCTOOLDIR=%{_datadir}/mm-common/doctool

%files -n %{libgdkmm}
%{_libdir}/libgdkmm-%{api}.so.%{major}*

%files -n %{libname}
%{_libdir}/libgtkmm-%{api}.so.%{major}*

%files -n %{devname}
%doc PORTING ChangeLog AUTHORS COPYING NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/gtkmm-%{api}/
%{_libdir}/gdkmm-%{api}/
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/doc/gtkmm-%{api}/
%doc %{_datadir}/devhelp/books/*

