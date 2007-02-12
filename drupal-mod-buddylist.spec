%define		modname buddylist
Summary:	Drupal Buddylist Module
Summary(pl.UTF-8):   Moduł Buddylist dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	22a9370ae0ac4937283e2970513852aa
URL:		http://drupal.org/project/buddylist
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules
%define		_podir		%{_drupaldir}/po/%{modname}

%description
This module allows users to put each other on a personal 'Buddy List',
also enabling them to keep up with their friend's postings via the 'My
Friend's Blogs' block.

%description -l pl.UTF-8
Ten moduł pozwala użytkownikom umieszczać siebie nawzajem na
prywatnych "Buddy Lists", umożliwiając im także otrzymywanie postów
przyjaciół poprzez blok "My Friend's Blogs".

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_moddir},%{_podir}}

install *.module $RPM_BUILD_ROOT%{_moddir}
cp -a po/*.po $RPM_BUILD_ROOT%{_podir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
If you want to use localization, then you need to upload .po files
from %{_podir} via drupal locatization admin.

To create Buddylist MySQL database tables, import:
zcat %{_docdir}/%{name}-%{version}/%{modname}.mysql.gz | mysql drupal
For Postgresql file is:
%{_docdir}/%{name}-%{version}/%{modname}.pgsql.gz

EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt %{modname}.{mysql,pgsql}
%doc CHANGELOG CREDITS INSTALL TODO
%{_moddir}/*.module
%{_podir}
