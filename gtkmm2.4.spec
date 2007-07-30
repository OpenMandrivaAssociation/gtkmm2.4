%define version 2.11.6
%define release %mkrel 1

%define glibmm_version 2.12.3
%define gtk_version 2.11.6

%define pkgname	gtkmm
%define api_version 2.4
%define major 1
%define libname_orig %mklibname %{pkgname} %{api_version}
%define libname %mklibname %{pkgname} %{api_version} %{major}

Name:		%{pkgname}%{api_version}
Summary:	C++ interface for popular GUI library gtk+
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel >= %{gtk_version}
BuildRequires:	glibmm2.4-devel >= %{glibmm_version}
BuildRequires:	atk-devel >= 1.9.0
BuildRequires:	cairomm-devel  >= 1.1.12

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package	-n %{libname}
Summary:	C++ interface for popular GUI library gtk+
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{pkgname}.


%package	-n %{libname}-devel
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Requires:	gtk+2-devel >= %{gtk_version}
Requires:	glibmm2.4-devel >= %{glibmm_version}

%description	-n %{libname}-devel
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.


%package	-n %{libname}-static-devel
Summary:	Static libraries of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname}-devel = %{version}
Provides:	%{libname_orig}-static-devel = %{version}-%{release}

%description	-n %{libname}-static-devel
This package contains the static libraries of %{pkgname}.


%package	doc
Summary:	GTKmm documentation
Group:		Books/Other

%description	doc
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for gtkmm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --enable-static --enable-shared
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std
mv %buildroot%_bindir/demo %buildroot%_bindir/%name-demo

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc CHANGES COPYING PORTING ChangeLog
%_bindir/%name-demo
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/gtkmm-%{api_version}
%{_libdir}/gdkmm-%{api_version}
%{_libdir}/pkgconfig/*.pc

%files -n %{libname}-static-devel
%defattr(-, root, root)
%doc COPYING
%{_libdir}/*.a

%files doc
%defattr(-, root, root)
%doc %{_datadir}/doc/gtkmm-%{api_version}
%doc %{_datadir}/devhelp/books/*


