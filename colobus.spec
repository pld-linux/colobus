# TODO:
# - finish spec
# - rc-inetd support
Summary:	NNTP server for ezmlm mailing list archives
Name:		colobus
Version:	1.1
Release:	1
License:	MIT/X
Group:		Networking/Daemons
Source0:	http://trainedmonkey.com/colobus/%{name}-%{version}.tar.gz
URL:		http://trainedmonkey.com/colobus/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
colobus is an NNTP server written in Perl for ezmlm mailing list
archives. It is used by news.php.net and nntp.perl.org to provide
access to the PHP and Perl mailing lists via news clients.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
