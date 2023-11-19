%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api 1
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname -d %{name}

Summary:	C library for programming with the Jabber protocol
Name:		loudmouth
Version:	1.4.3
Release:	23
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.loudmouth-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/loudmouth/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		loudmouth-1.4.3_glib_h.patch
Patch2:		loudmouth-automake-1.13.patch
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
Patch104:	loudmouth-1.4.3-certs_location.patch
Patch105:	04-use-pkg-config-for-gnutls.patch
Patch106:	gnutls-3.4.0.patch

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
Obsoletes:	%{_lib}loudmouth-1_0 < 1.4.3-9

%description -n %{libname}
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

%package -n %{devname}
Summary:	Libraries and include files for loudmouth
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

This package includes libraries and header files for developing
Loudmouth applications.

%prep
%autosetup -p1
autoreconf -fi

%build
%configure \
	--disable-static \
	--disable-gtk-doc \
	--with-asyncns

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libloudmouth-%{api}.so.%{major}*

%files -n %{devname}
%doc README AUTHORS NEWS ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
