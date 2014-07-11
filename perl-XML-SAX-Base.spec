%define modname	XML-SAX-Base
%define modver	1.08

Summary:	Simple API for XML Base
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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

