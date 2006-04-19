Summary:	OpenSync kdepim plugin
Summary(pl):	Wtyczka kdepim do OpenSync
Name:		libopensync-plugin-kdepim
Version:	0.18
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
# Source0-md5:	96c43911a0fbdaff4920bbc0f4cd3816
URL:		http://www.opensync.org/
BuildRequires:	kdepim-devel
BuildRequires:	libopensync-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains kdepim plugin for OpenSync framework.

%description -l pl
OpenSync to niezale�ny od platformy i dystrybucji szkielet do
synchronizacji danych.

Sk�ada si� z r�nych wtyczek, kt�rych mo�na u�ywa� do ��czenia z
urz�dzeniami, pot�nego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczk� kdepim dla szkieletu OpenSync.

%prep
%setup -q 

%build
%configure
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
