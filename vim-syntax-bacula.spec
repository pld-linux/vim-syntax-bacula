%define		syntax	bacula
Summary:	Vim syntax: %{syntax}
Name:		vim-syntax-%{syntax}
Version:	1.0
Release:	1
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	http://bacula.svn.sourceforge.net/viewvc/bacula/trunk/bacula/scripts/bacula.vim
# Source0-md5:	03b47503e1e5465c037f361593395109
Source1:	http://bacula.svn.sourceforge.net/viewvc/bacula/trunk/bacula/scripts/filetype.vim
# Source1-md5:	046460b17974bd5c7eb8809c587a12ff
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This plugin provides syntax highlighting for bacula config files.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
install %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
