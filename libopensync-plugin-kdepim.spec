Summary:	OpenSync kdepim plugin
Summary(pl):	Wtyczka kdepim do OpenSync
Name:		libopensync-plugin-kdepim
Version:	0.19
Release:	0.1
License:	LGPL
Group:		Libraries
# Source0Download:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	258defed0c5f8d39eac42f6c294c8f1c
URL:		http://www.opensync.org/
BuildRequires:	kdepim-devel
BuildRequires:	libopensync-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains kdepim plugin for OpenSync framework.

%description -l pl
OpenSync to niezale¿ny od platformy i dystrybucji szkielet do
synchronizacji danych.

Sk³ada siê z ró¿nych wtyczek, których mo¿na u¿ywaæ do ³±czenia z
urz±dzeniami, potê¿nego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkê kdepim dla szkieletu OpenSync.

%prep
%setup -q

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
#%{_datadir}/opensync/defaults/*
