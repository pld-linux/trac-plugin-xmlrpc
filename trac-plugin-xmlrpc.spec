%define		trac_ver	0.12
%define		plugin		xmlrpc
%define		module		tracrpc
%define		egg_name	TracXMLRPC
%define		pypi_name	TracXMLRPC
Summary:	Remote Procedure Call plugin for Trac
Name:		trac-plugin-%{plugin}
Version:	1.1.6
Release:	1
License:	BSD
Group:		Applications/WWW
Source0:	https://files.pythonhosted.org/packages/source/T/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	dca985ad9f056e9851f575b52e139d6b
URL:		https://trac-hacks.org/wiki/XmlRpcPlugin
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows Trac plugins to export select parts of their
interface via XML-RPC and JSON-RPC (if json or simplejson is
available). Latest trunk version includes a pluggable API for
extending protocols, and see for instance TracRpcProtocolsPlugin for
more protocols.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py_build build
%py_build egg_info

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
trac-enableplugin "tracrpc.*"

%files
%defattr(644,root,root,755)
%doc README.wiki
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
