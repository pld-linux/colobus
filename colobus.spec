# TODO:
# - finish spec
# - rc-inetd support
Summary:	NNTP server for ezmlm mailing list archives
Summary(pl):	Serwer NNTP dla archiwów list mailowych ezmlm
Name:		colobus
Version:	2.0
Release:	1
License:	MIT/X
Group:		Networking/Daemons
Source0:	http://trainedmonkey.com/colobus/%{name}-%{version}.tar.gz
# Source0-md5:	432dc0b5efb4ce86fc21081b2abe1d7b
URL:		http://trainedmonkey.com/colobus/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
colobus is an NNTP server written in Perl for ezmlm mailing list
archives. It is used by news.php.net and nntp.perl.org to provide
access to the PHP and Perl mailing lists via news clients.

%description -l pl
colobus to napisany w Perlu serwer NNTP dla archiwów list mailowych
ezmlm. Jest u¿ywany przez news.php.net oraz nntp.perl.org, aby
umo¿liwiæ dostêp do list mailowych PHP i Perla z poziomu klientów
news.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
