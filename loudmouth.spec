%define lib_name %mklibname %{name}- %{api_version} %{lib_major}
%define devel_name %mklibname -d %{name} 
%define lib_major 0
%define api_version 1

Summary: C library for programming with the Jabber protocol
Name: loudmouth
Version: 1.4.0
Release: %mkrel 2
License: LGPLv2+
Group: System/Libraries
URL: http://www.loudmouth-project.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel
BuildRequires: gnutls-devel >= 1.0.0
BuildRequires: libidn-devel
BuildRequires: gtk-doc

%description
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}

%description -n %{lib_name}
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

%package -n %{devel_name}
Summary:	Libraries and include files for loudmouth
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	glib2-devel
Obsoletes:	%mklibname -d %{name}- 1 0

%description -n %{devel_name}
Loudmouth is a lightweight and easy-to-use C library for programming with the
Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

This package includes libraries and header files for developing
Loudmouth applications.

%prep
%setup -q

%build

%configure2_5x --enable-gtk-doc --with-asyncns

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{lib_name}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{lib_name}
%endif

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/*-%{api_version}.so.%{lib_major}*

%files -n %{devel_name}
%defattr(-,root,root,-)
%doc README AUTHORS NEWS ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


