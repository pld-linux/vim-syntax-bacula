%define		syntax	bacula
Summary:	Vim syntax: %{syntax}
Name:		vim-syntax-%{syntax}
Version:	1.0
Release:	2
License:	Extended GPL v2
Group:		Applications/Editors/Vim
Source0:	http://bacula.svn.sourceforge.net/viewvc/bacula/trunk/bacula-old/scripts/bacula.vim
# Source0-md5:	ea685e214581f5f8edadbf418b32f79e
Source1:	http://bacula.svn.sourceforge.net/viewvc/bacula/trunk/bacula-old/scripts/filetype.vim
# Source1-md5:	f36ef7e68216ddc28a24554ddfd54598
Patch0:     bacula.vim-extended.patch
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This plugin provides syntax highlighting for bacula config files.

%prep
%setup -qcT
cp -a %{SOURCE0} .
cp -a %{SOURCE1} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
cp -a %{syntax}.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
cp -a filetype.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
