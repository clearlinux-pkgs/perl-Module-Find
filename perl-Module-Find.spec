#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Find
Version  : 0.13
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/C/CR/CRENZ/Module-Find-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CR/CRENZ/Module-Find-0.13.tar.gz
Summary  : 'Find and use installed modules in a (sub)category'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
Module::Find
============
Module::Find lets you find and use modules in categories. This can be very
useful for auto-detecting driver or plugin modules. You can differentiate
between looking in the category itself or in all subcategories.

%package dev
Summary: dev components for the perl-Module-Find package.
Group: Development
Provides: perl-Module-Find-devel = %{version}-%{release}

%description dev
dev components for the perl-Module-Find package.


%prep
%setup -q -n Module-Find-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Module/Find.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Find.3
