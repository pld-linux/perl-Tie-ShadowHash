%include	/usr/lib/rpm/macros.perl
Summary:	Tie::ShadowHash perl module
Summary(pl):	Modu³ perla Tie::ShadowHash
Name:		perl-Tie-ShadowHash
Version:	0.07
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/ShadowHash-%{version}.tar.gz
# Source0-md5:	aecf81359cabd38cb139cc0c6e8ab0f8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::ShadowHash merges multiple data sources into a hash.

%description -l pl
Tie::ShadowHash ³±czy wiele danych w hasz.

%prep
%setup -q -n ShadowHash-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/Tie/ShadowHash.pm
%{_mandir}/man3/*
