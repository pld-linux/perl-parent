#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	parent
Summary:	parent - Establish an ISA relationship with base classes at compile time
Summary(pl.UTF-8):	parent - ustanawianie relacji ISA z klasami bazowymi w czasie kompilacji
Name:		perl-parent
Version:	0.237
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CO/CORION/%{pdir}-%{version}.tar.gz
# Source0-md5:	9c30dfb44a8d749e8e87603d4560cefa
URL:		http://search.cpan.org/dist/parent/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to both load one or more modules, while setting up
inheritance from those modules at the same time.

%description -l pl.UTF-8
Ten moduł pozwala wczytać jeden lub więcej modułów, ustawiając w tym
samym czasie dziedziczenie tych modułów.

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
%{_mandir}/man3/parent.3pm*
