#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	ShadowHash
Summary:	Tie::ShadowHash perl module
Summary(pl.UTF-8):	Moduł perla Tie::ShadowHash
Name:		perl-Tie-ShadowHash
Version:	0.07
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/ShadowHash-%{version}.tar.gz
# Source0-md5:	aecf81359cabd38cb139cc0c6e8ab0f8
URL:		http://search.cpan.org/dist/Tie-ShadowHash/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::ShadowHash merges multiple data sources into a hash.

%description -l pl.UTF-8
Tie::ShadowHash łączy wiele danych w hasz.

%prep
%setup -q -n ShadowHash-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/Tie/ShadowHash.pm
%{_mandir}/man3/*
