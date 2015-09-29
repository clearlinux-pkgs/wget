#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wget
Version  : 1.16.3
Release  : 17
URL      : http://ftp.gnu.org/gnu/wget/wget-1.16.3.tar.xz
Source0  : http://ftp.gnu.org/gnu/wget/wget-1.16.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0
Requires: wget-bin
Requires: wget-data
Requires: wget-doc
Requires: wget-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : flex
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : perl(HTTP::Daemon)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(IO::Socket::SSL)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(Net::SSLeay)
BuildRequires : perl(URI)
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : texinfo
Patch1: stateless.patch
Patch2: 0001-Use-correct-gettext-version.patch

%description
GNU Wget
========
Current Web home: http://www.gnu.org/software/wget/
GNU Wget is a free utility for non-interactive download of files from
the Web.  It supports HTTP, HTTPS, and FTP protocols, as well as
retrieval through HTTP proxies.

%package bin
Summary: bin components for the wget package.
Group: Binaries
Requires: wget-data

%description bin
bin components for the wget package.


%package data
Summary: data components for the wget package.
Group: Data

%description data
data components for the wget package.


%package doc
Summary: doc components for the wget package.
Group: Documentation

%description doc
doc components for the wget package.


%package locales
Summary: locales components for the wget package.
Group: Default

%description locales
locales components for the wget package.


%prep
%setup -q -n wget-1.16.3
%patch1 -p1
%patch2 -p1

%build
%reconfigure --disable-static --with-ssl=openssl --disable-psl --disable-ntlm
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang wget

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wget

%files data
%defattr(-,root,root,-)
/usr/share/defaults/wget/wgetrc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files locales -f wget.lang 
%defattr(-,root,root,-)

