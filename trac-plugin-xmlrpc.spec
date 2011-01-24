%define		trac_ver	0.12
%define		plugin		xmlrpc
Summary:	Remote Procedure Call plugin for Trac
Name:		trac-plugin-%{plugin}
Version:	0
Release:	0.4
License:	BSD
Group:		Applications/WWW
# Source0Download:	http://trac-hacks.org/changeset/latest/xmlrpcplugin?old_path=/&filename=xmlrpcplugin&format=zip
Source0:	%{plugin}plugin.zip
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
%setup -q -n %{plugin}plugin

%build
cd trunk
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd trunk
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	To enable the %{plugin} plugin, add to conf/trac.ini:

	[components]
	tracrpc.* = enabled
EOF
fi

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/tracrpc
%{py_sitescriptdir}/TracXMLRPC-*.egg-info
