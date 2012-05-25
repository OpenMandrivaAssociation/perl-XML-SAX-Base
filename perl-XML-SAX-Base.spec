%define upstream_name	 XML-SAX-Base
%define upstream_version 1.08

# skipping requires on perl modules not in perl-base but in perl pkg
# those requires are only used by PurePerl module, whereas we often use perl-XML-LibXML
# this is useful to ensure urpmi only need perl-base, not perl
%define _requires_exceptions perl(File::Temp)\\|perl(Encode)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:	Simple API for XML Base
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
BuildRequires:	perl(XML::NamespaceSupport)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module has a very simple task - to be a base class for PerlSAX drivers and filters. 
It's default behaviour is to pass the input directly to the output unchanged. It 
can be useful to use this module as a base class so you don't have to, for example, 
implement the characters() callback.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
N
EOF
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std PERL="perl -I%{buildroot}%{perl_vendorlib}/"

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/man3/XML::*.3*
