%define pkgname gtkmm
%define api_version 2.4
%define major 1
%define libname %mklibname %{pkgname} %{api_version} %{major}
%define libnamedev %mklibname -d %{pkgname} %{api_version}

Name:		%{pkgname}%{api_version}
Summary:	C++ interface for popular GUI library gtk+
Version:	2.24.2
Release:	7
#gw lib is LGPL, tool is GPL
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/

Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
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
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{pkgname}.


%package	-n %{libnamedev}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	-n %{libnamedev}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.

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
%configure2_5x \
    --enable-shared \
    --disable-static
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std MMDOCTOOLDIR=%{_datadir}/mm-common/doctool

%files -n %{libname}
%{_libdir}/libgdkmm-%{api_version}.so.%{major}*
%{_libdir}/libgtkmm-%{api_version}.so.%{major}*


%files -n %{libnamedev}
%doc PORTING ChangeLog AUTHORS COPYING NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/gtkmm-%{api_version}/
%{_libdir}/gdkmm-%{api_version}/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_datadir}/doc/gtkmm-%{api_version}/
%doc %{_datadir}/devhelp/books/*


%changelog
* Mon Apr 16 2012 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.2-6
+ Revision: 791290
- rebuild for missing devel provides

* Fri Mar 16 2012 Andrey Bondrov <abondrov@mandriva.org> 2.24.2-5
+ Revision: 785326
- Rebuild with new RPM dependency generator

* Tue Dec 06 2011 ZÃ© <ze@mandriva.org> 2.24.2-4
+ Revision: 738047
- last touches
- set buildrquires with pkg usage
- clean static entries
- clean useless macros
- arrange provides
- need to set requires to release
- clean requires on devel

* Tue Dec 06 2011 ZÃ© <ze@mandriva.org> 2.24.2-3
+ Revision: 738045
- clean defattr, BR, clean section and mkrel
- disable static
- clean .la files
- move docs to devel

  + Andrey Bondrov <abondrov@mandriva.org>
    - Rebuild to fix problems caused by Matthew Dawkins (.la issue)

* Mon Sep 19 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.2-2
+ Revision: 700353
- rebuild

* Mon Jul 11 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.2-1
+ Revision: 689453
- new version
- xz tarball

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.24.0-2
+ Revision: 664955
- mass rebuild

* Mon Apr 04 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1
+ Revision: 650201
- new version
- bump gtk dep
- fix installation

* Wed Mar 23 2011 Funda Wang <fwang@mandriva.org> 2.22.0-2
+ Revision: 648119
- rebuild

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2011.0
+ Revision: 581522
- update to new version 2.22.0

* Sun Sep 26 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.9-1mdv2011.0
+ Revision: 581067
- update to new version 2.21.9

* Mon Sep 20 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.8.1-1mdv2011.0
+ Revision: 579978
- update to new version 2.21.8.1

* Tue Sep 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.8-1mdv2011.0
+ Revision: 578313
- new version
- bump gtk dep

* Thu Sep 02 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.7-1mdv2011.0
+ Revision: 575220
- new version
- remove atkmm and depend on external version

* Tue May 04 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.3-1mdv2011.0
+ Revision: 541987
- update to new version 2.20.3

* Fri Apr 16 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.2-1mdv2010.1
+ Revision: 535451
- update to new version 2.20.2

* Wed Apr 07 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2010.1
+ Revision: 532791
- update to new version 2.20.1

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 529689
- new version
- bump glibmm dep

* Thu Mar 18 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.7-1mdv2010.1
+ Revision: 524905
- update to new version 2.19.7

* Wed Feb 24 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2010.1
+ Revision: 510579
- update to new version 2.19.6

* Tue Jan 26 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.4-1mdv2010.1
+ Revision: 496741
- new version
- bump gtk dep

* Mon Jan 04 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.2-1mdv2010.1
+ Revision: 486186
- update to new version 2.19.2

* Sun Oct 04 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2010.0
+ Revision: 453733
- new version

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2010.0
+ Revision: 446720
- new version
- update file list

* Mon Sep 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.11-1mdv2010.0
+ Revision: 432734
- new version
- bump gtk dep

* Sat Aug 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.9.3-1mdv2010.0
+ Revision: 422132
- update to new version 2.17.9.3
- update to new version 2.17.9.1

* Wed Aug 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.9-1mdv2010.0
+ Revision: 421449
- new version
- update deps
- update file list

* Tue Jul 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-1mdv2010.0
+ Revision: 395970
- update to new version 2.17.2

* Mon Jun 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.1-1mdv2010.0
+ Revision: 390593
- bump gtk+ dep
- new version
- drop merged patch

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2009.1
+ Revision: 355983
- update to new version 2.16.0

* Tue Mar 03 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.5-1mdv2009.1
+ Revision: 348121
- update to new version 2.15.5

* Fri Feb 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.3-1mdv2009.1
+ Revision: 338044
- update to new version 2.15.3

* Sun Jan 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.1-1mdv2009.1
+ Revision: 333556
- update to new version 2.15.1

* Mon Jan 05 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.0-1mdv2009.1
+ Revision: 324963
- new version
- bump deps
- fix format strings

* Fri Nov 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.3-1mdv2009.1
+ Revision: 303146
- update to new version 2.14.3

* Mon Nov 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2009.1
+ Revision: 301809
- update to new version 2.14.2

* Thu Sep 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.1-1mdv2009.0
+ Revision: 288069
- new version

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdv2009.0
+ Revision: 286602
- new version
- bump pangomm dep

* Wed Sep 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.8-1mdv2009.0
+ Revision: 283475
- new version
- drop patch
- update license

* Tue Sep 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.7-2mdv2009.0
+ Revision: 282904
- patch for gtk api changes (fixes crash reportet as #43623)

* Wed Aug 20 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.7-1mdv2009.0
+ Revision: 274125
- new version

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.6-1mdv2009.0
+ Revision: 263349
- new version

* Wed Jul 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.5-1mdv2009.0
+ Revision: 242538
- new version
- depend on pangomm

* Wed Jul 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.4-1mdv2009.0
+ Revision: 236587
- new version
- update file list

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.13.1-2mdv2009.0
+ Revision: 231287
- new version
- bump deps
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.12.7-2mdv2009.0
+ Revision: 221116
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.7-1mdv2008.1
+ Revision: 191629
- new version

* Tue Apr 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.6-1mdv2008.1
+ Revision: 191359
- new version
- new version
- update file list

* Sun Jan 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.4-2mdv2008.1
+ Revision: 158507
- rebuild for broken build system
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdv2008.1
+ Revision: 106900
- new version

* Mon Nov 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdv2008.1
+ Revision: 106016
- new version

* Wed Oct 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-1mdv2008.1
+ Revision: 96635
- new version
- bump glibmm dep

* Fri Sep 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-1mdv2008.0
+ Revision: 85532
- new version
- bump deps

* Fri Aug 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.8-1mdv2008.0
+ Revision: 76898
- new version

* Fri Aug 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.7-1mdv2008.0
+ Revision: 65168
- new version
- new devel name

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.6-1mdv2008.0
+ Revision: 56519
- new version

* Sun Jul 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.5-1mdv2008.0
+ Revision: 54395
- new version
- bump deps

* Mon Jul 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.4-1mdv2008.0
+ Revision: 46963
- new version

* Tue Jun 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.3-2mdv2008.0
+ Revision: 41463
- rebuild

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.3-1mdv2008.0
+ Revision: 40798
- new version

* Wed Jun 06 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.2-1mdv2008.0
+ Revision: 36045
- new version
- bump deps

* Wed May 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.10-1mdv2008.0
+ Revision: 20405
- new version

* Tue Apr 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.9-1mdv2008.0
+ Revision: 17910
- new version


* Sun Mar 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.8-1mdv2007.0
+ Revision: 132017
- new version

* Sun Jan 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.7-1mdv2007.1
+ Revision: 114594
- new version

* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.5-1mdv2007.1
+ Revision: 87442
- new version

* Tue Nov 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.4-1mdv2007.1
+ Revision: 85902
- new version
- bump deps

* Thu Nov 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.3-1mdv2007.1
+ Revision: 79232
- new version

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.2-2mdv2007.1
+ Revision: 63813
- rebuild
- Import gtkmm2.4

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdv2007.1
- bump deps
- New version 2.10.2

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2007.0
- bump deps
- New release 2.10.1

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.10-1mdv2007.0
- New release 2.9.10

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.9.9-1mdv2007.0
- bump deps
- New release 2.9.9

* Thu Jul 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.8-1mdv2007.0
- New release 2.9.8

* Fri Jul 07 2006 Götz Waschk <waschk@mandriva.org> 2.9.7-1mdv2007.0
- drop patch
- New release 2.9.7

* Fri Jun 30 2006 Götz Waschk <waschk@mandriva.org> 2.9.5-2mdv2007.0
- patch for new gtk

* Tue Jun 20 2006 Götz Waschk <waschk@mandriva.org> 2.9.5-1mdv2007.0
- New release 2.9.5
- bump deps
- depend on cairomm

* Sun May 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.8-1mdk
- New release 2.8.8

* Sat May 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.7-1mdk
- New release 2.8.7

* Sat Apr 15 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.5-1mdk
- New release 2.8.5

* Wed Feb 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.3-1mdk
- New release 2.8.3

* Fri Dec 16 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.2-1mdk
- New release 2.8.2
- use mkrel

* Thu Oct 20 2005 Götz Waschk <waschk@mandriva.org> 2.8.1-1mdk
- bump deps
- New release 2.8.1

* Sun Oct 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.0-1mdk
- New release 2.8.0

* Wed Jul 27 2005 Götz Waschk <waschk@mandriva.org> 2.6.4-1mdk
- New release 2.6.4

* Sat Jun 11 2005 Götz Waschk <waschk@mandriva.org> 2.6.3-1mdk
- New release 2.6.3

* Tue Apr 19 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- New release 2.6.2

* Mon Mar 14 2005 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- fix source URL
- New release 2.6.1

* Mon Mar 07 2005 Götz Waschk <waschk@linux-mandrake.com> 2.6.0-1mdk
- add the demo
- requires new atk
- requires new glibmm
- fix source URL
- New release 2.6.0

* Thu Feb 03 2005 Goetz Waschk <waschk@linux-mandrake.com> 2.4.11-1mdk
- New release 2.4.11

* Sun Jan 30 2005 Goetz Waschk <waschk@linux-mandrake.com> 2.4.10-1mdk
- New release 2.4.10

* Wed Dec 01 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.4.8-1mdk
- New release 2.4.8

* Wed Nov 03 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.4.7-1mdk
- New release 2.4.7

* Fri Oct 29 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.4.6-1mdk
- New release 2.4.6

* Wed Aug 11 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.5-1mdk
- fix source url
- New release 2.4.5

* Wed Jul 07 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.4-1mdk
- fix summary
- New release 2.4.4

* Sun Jun 20 2004 Abel Cheung <deaddog@mandrakesoft.com> 2.4.3-1mdk
- New release 2.4.3
- fix source URL

* Tue Jun 08 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.4.2-1mdk
- fix source URL
- reenable libtoolize
- New release 2.4.2

* Fri May 07 2004 Abel Cheung <deaddog@deaddog.org> 2.4.1-1mdk
- New version

* Wed Apr 28 2004 Abel Cheung <deaddog@deaddog.org> 2.4.0-1mdk
- New major release

* Tue Apr 27 2004 Abel Cheung <deaddog@deaddog.org> 2.2.11-1mdk
- New version
- Drop patch, not needed

