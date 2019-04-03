#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-Babel
Version  : 2.6.0
Release  : 64
URL      : https://pypi.debian.net/Babel/Babel-2.6.0.tar.gz
Source0  : https://pypi.debian.net/Babel/Babel-2.6.0.tar.gz
Summary  : Internationalization utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: deprecated-Babel-bin = %{version}-%{release}
Requires: deprecated-Babel-license = %{version}-%{release}
Requires: deprecated-Babel-python = %{version}-%{release}
Requires: pytz
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : pytz

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package bin
Summary: bin components for the deprecated-Babel package.
Group: Binaries
Requires: deprecated-Babel-license = %{version}-%{release}

%description bin
bin components for the deprecated-Babel package.


%package legacypython
Summary: legacypython components for the deprecated-Babel package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-Babel package.


%package license
Summary: license components for the deprecated-Babel package.
Group: Default

%description license
license components for the deprecated-Babel package.


%package python
Summary: python components for the deprecated-Babel package.
Group: Default
Provides: deprecated-babel-python

%description python
python components for the deprecated-Babel package.


%prep
%setup -q -n Babel-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554305814
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test tests || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-Babel
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-Babel/LICENSE
cp docs/_themes/LICENSE %{buildroot}/usr/share/package-licenses/deprecated-Babel/docs__themes_LICENSE
cp docs/license.rst %{buildroot}/usr/share/package-licenses/deprecated-Babel/docs_license.rst
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybabel

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-Babel/LICENSE
/usr/share/package-licenses/deprecated-Babel/docs__themes_LICENSE
/usr/share/package-licenses/deprecated-Babel/docs_license.rst

%files python
%defattr(-,root,root,-)
