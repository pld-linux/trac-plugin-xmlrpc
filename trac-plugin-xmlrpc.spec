%define		trac_ver	0.12
%define		plugin		xmlrpc
Summary:	Remote Procedure Call plugin for Trac
Name:		trac-plugin-%{plugin}
Version:	1.1.2
Release:	1
License:	BSD
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/xmlrpcplugin?old_path=/&filename=xmlrpcplugin&format=zip#/%{plugin}-%{version}.zip
# Source0-md5:	c7dc2526551d2955721fc10d55a3a86b
URL:		http://trac-hacks.org/wiki/XmlRpcPlugin
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
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
%setup -qc
mv %{plugin}plugin/trunk/* .

%build
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
trac-enableplugin "tracrpc.*"

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/tracrpc
%{py_sitescriptdir}/TracXMLRPC-*.egg-info
