#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	parent
Summary:	parent - Establish an ISA relationship with base classes at compile time
Name:		perl-parent
Version:	0.221
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
URL:		http://search.cpan.org/dist/parent/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Source0:	http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{pdir}-%{version}.tar.gz
# Source0-md5:	4bacb68147a063ec475fd1a63c949d74
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to both load one or more modules, while setting up inheritance from those modules at the same time.

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes 
%{perl_vendorlib}/parent.pm
%{_mandir}/man3/*
