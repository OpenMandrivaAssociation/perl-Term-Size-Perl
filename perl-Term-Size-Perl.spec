
%define realname   Term-Size-Perl
%define version    0.029
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Probes some machine configuration parameters for Term::Size::Perl's sake
Source:     http://www.cpan.org/modules/by-module/Term/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
Yet another implementation of 'Term::Size'. Now in pure Perl, with the
exception of a C probe run on build time.

FUNCTIONS
    * *chars*

          ($columns, $rows) = chars($h);
          $columns = chars($h);

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


