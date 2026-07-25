%define modname	XML-SAX-Base
%define modver	1.09

Summary:	Simple API for XML Base
Name:		perl-%{modname}
Version:	%{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/grantm/XML-SAX-Base
Source0:	https://cpan.metacpan.org/authors/id/G/GR/GRANTM/XML-SAX-Base-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
Buildrequires:	perl(Test::More)
Buildrequires:	perl(Test)
Buildrequires:	perl-devel
BuildRequires:	perl(XML::NamespaceSupport)

%description
This module has a very simple task - to be a base class for 
PerlSAX drivers and filters.  It's default behaviour is to 
pass the input directly to the output unchanged. It can be 
useful to use this module as a base class so you don't 
have to, for example, implement the characters() callback.

%prep
%setup -qn %{modname}-%{modver}
chmod 644 Changes README

%build
%__perl Makefile.PL INSTALLDIRS=vendor <<EOF
N
EOF
%make

%check
%make test

%install
%makeinstall_std PERL="perl -I%{buildroot}%{perl_vendorlib}/"

%files
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/man3/XML::*.3*

