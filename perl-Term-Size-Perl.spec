%define realname   Term-Size-Perl
%define upstream_version    0.029

Name:       perl-%{realname}
Version:    %perl_convert_version %{upstream_version}
Release:    5
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Probes some machine configuration parameters for Term::Size::Perl's sake
Source:     http://www.cpan.org/modules/by-module/Term/%{realname}-%{upstream_version}.tar.gz
Url:        https://search.cpan.org/dist/%{realname}
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
%setup -q -n %{realname}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.029-2mdv2011.0
+ Revision: 658430
- rebuild for updates rpm-setup

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.029-1mdv2010.0
+ Revision: 376244
- import perl-Term-Size-Perl


* Fri May 15 2009 cpan2dist 0.029-1mdv
- initial mdv release, generated with cpan2dist

