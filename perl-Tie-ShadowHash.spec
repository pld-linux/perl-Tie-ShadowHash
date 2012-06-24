%include	/usr/lib/rpm/macros.perl
Summary:	Tie-ShadowHash perl module
Summary(pl):	Modu� perla Tie-ShadowHash
Name:		perl-Tie-ShadowHash
Version:	0.05
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/ShadowHash-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tie-ShadowHash merges multiple data sources into a hash.

%description -l pl
Tie-ShadowHash ��czy wiele danych w hasz.

%prep
%setup -q -n ShadowHash-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tie/ShadowHash
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO}.gz

%{perl_sitelib}/Tie/ShadowHash.pm
%{perl_sitearch}/auto/Tie/ShadowHash

%{_mandir}/man3/*
