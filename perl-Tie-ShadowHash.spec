%include	/usr/lib/rpm/macros.perl
Summary:	Tie-ShadowHash perl module
Summary(pl):	Modu³ perla Tie-ShadowHash
Name:		perl-Tie-ShadowHash
Version:	0.06
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Tie/ShadowHash-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-ShadowHash merges multiple data sources into a hash.

%description -l pl
Tie-ShadowHash ³±czy wiele danych w hasz.

%prep
%setup -q -n ShadowHash-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/ShadowHash.pm
%{_mandir}/man3/*
