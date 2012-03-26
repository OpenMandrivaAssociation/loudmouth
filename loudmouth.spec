%define api		1
%define major	0
%define libname %mklibname %{name}- %{api} %{major}
%define develname %mklibname -d %{name} 

Summary: C library for programming with the Jabber protocol
Name: loudmouth
Version: 1.4.3
Release: 8
License: LGPLv2+
Group: System/Libraries
URL: http://www.loudmouth-project.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: loudmouth-1.4.3-gnutls-2.8.patch
Patch1:	loudmouth-1.4.3_glib_h.patch

# Debian patches, from upstream
# Fix sasl md5 digest-uri when using SRV lookups, which prevented
# loudmouth from logging into recent versions of ejabberd
Patch101: 01-fix-sasl-md5-digest-uri.patch
# Fix sync resolving, patch from upstream git. (fixes assertion
# when trying to log in to some XMPP servers)
Patch102: 02-fix-async-resolving.patch
# Drop stanzas that can't be parsed instead of blocking the
# parser. Patch from upstream bug tracker.
Patch103: 03-drop-stanzas-on-fail.patch

BuildRequires: gtk-doc
BuildRequires: glib2-devel
BuildRequires: gnutls-devel >= 1.0.0
BuildRequires: libidn-devel

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
Obsoletes:	%mklibname -d %{name}- 1 0

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


