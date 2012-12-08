%define api 1
%define major 0
%define libname %mklibname %{name}- %{api} %{major}
%define develname %mklibname -d %{name}

Summary:	C library for programming with the Jabber protocol
Name:		loudmouth
Version:	1.4.3
Release:	8
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.loudmouth-project.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		loudmouth-1.4.3-gnutls-2.8.patch
Patch1:		loudmouth-1.4.3_glib_h.patch

# Debian patches, from upstream
# Fix sasl md5 digest-uri when using SRV lookups, which prevented
# loudmouth from logging into recent versions of ejabberd
Patch101:	01-fix-sasl-md5-digest-uri.patch
# Fix sync resolving, patch from upstream git. (fixes assertion
# when trying to log in to some XMPP servers)
Patch102:	02-fix-async-resolving.patch
# Drop stanzas that can't be parsed instead of blocking the
# parser. Patch from upstream bug tracker.
Patch103:	03-drop-stanzas-on-fail.patch

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libidn)

%description
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

%package -n %{develname}
Summary:	Libraries and include files for loudmouth
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d loudmouth- 1 0} < 1.4.3-8

%description -n %{develname}
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

This package includes libraries and header files for developing
Loudmouth applications.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-gtk-doc \
	--with-asyncns

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{develname}
%doc README AUTHORS NEWS ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*




%changelog
* Mon Mar 26 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.3-8
+ Revision: 787036
- rebuild
- added p1 for glib header strictness
- cleaned up spec
- employed apply_patches macro

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-7
+ Revision: 666094
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-6mdv2011.0
+ Revision: 606418
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-5mdv2010.1
+ Revision: 523205
- rebuilt for 2010.1

* Sat Jun 06 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4.3-4mdv2010.0
+ Revision: 383285
- Add 3 Debian patches fixing crashes and login failures

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 1.4.3-3mdv2010.0
+ Revision: 381471
- rebuild with latest gnutls 2.8

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 1.4.3-2mdv2009.1
+ Revision: 309153
- rebuild to get rid of libtasn1 dep

* Wed Oct 29 2008 Götz Waschk <waschk@mandriva.org> 1.4.3-1mdv2009.1
+ Revision: 298653
- update to new version 1.4.3

* Thu Aug 28 2008 Götz Waschk <waschk@mandriva.org> 1.4.2-1mdv2009.0
+ Revision: 276875
- new version

* Thu Jul 31 2008 Götz Waschk <waschk@mandriva.org> 1.4.1-1mdv2009.0
+ Revision: 257599
- new version

* Mon Jul 21 2008 Götz Waschk <waschk@mandriva.org> 1.4.0-2mdv2009.0
+ Revision: 239313
- enable Asynchronous DNS as recommended by gossip

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 09 2008 Frederic Crozat <fcrozat@mandriva.com> 1.4.0-1mdv2009.0
+ Revision: 217063
- Release 1.4.0

* Tue Apr 15 2008 Götz Waschk <waschk@mandriva.org> 1.3.4-2mdv2009.0
+ Revision: 194079
- obsolete the right package
- fix typo in deps

* Mon Apr 14 2008 Frederik Himpe <fhimpe@mandriva.org> 1.3.4-1mdv2009.0
+ Revision: 193009
- New version
- New license policy
- New library policy (devel name)

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-4mdv2008.1
+ Revision: 170967
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-2mdv2008.1
+ Revision: 152865
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Frederic Crozat <fcrozat@mandriva.com>
    - Update url

* Sun Jun 10 2007 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2008.0
+ Revision: 37905
- new version

* Thu May 31 2007 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdv2008.0
+ Revision: 33398
- new version
- fix buildrequires


* Fri Feb 02 2007 Frederic Crozat <fcrozat@mandriva.com> 1.2.0-1mdv2007.0
+ Revision: 115974
- Release 1.2.0
- Import loudmouth

* Tue Sep 12 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.5-1mdv2007.0
- Release 1.0.5

* Tue Jul 04 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.4-1mdv2007.0
- Release 1.0.4

* Sat Apr 29 2006 Jerome Soyer <saispo@mandriva.org> 1.0.3-1mdk
- New release 1.0.3

* Wed Aug 17 2005 Frederic Crozat <fcrozat@mandriva.com> 1.0.1-1mdk 
- Release 1.0.1

* Tue May 10 2005 Frederic Crozat <fcrozat@mandriva.com> 0.90-1mdk 
- Release 0.90

* Tue Dec 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.17.2-2mdk 
- Rebuild with latest gnutls

* Tue Nov 16 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.17.2-1mdk
- New release 0.17.2

* Wed Sep 01 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.17.1-1mdk
- New release 0.17.1

* Sat Aug 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.17-1mdk
- New release 0.17
- Enable libtoolize

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.16-2mdk
- Rebuild against latest gnutls

* Sat Apr 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.16-1mdk
- Release 0.16

