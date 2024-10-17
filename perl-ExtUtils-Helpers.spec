%define upstream_name  	    ExtUtils-Helpers

Name:		perl-%{upstream_name}
Version:	0.028
Release:	1
Summary:	Various portability utilities for module builders
License:	GPL or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{version}.tar.gz
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl-devel
# For make test
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Various portability utilities for module builders.

%prep
%autosetup -p1 -n %{upstream_name}-%{version} 
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files 
%doc Changes
%{perl_vendorlib}/ExtUtils
%{_mandir}/man3/*
