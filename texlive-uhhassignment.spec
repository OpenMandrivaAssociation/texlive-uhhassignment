Name:		texlive-uhhassignment
Version:	44026
Release:	2
Summary:	A document class for typesetting homework assignments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uhhassignment
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uhhassignment.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uhhassignment.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uhhassignment.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This document class was created for typesetting solutions to
homework assignments at the university of Hamburg (Universitat
Hamburg).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uhhassignment
%{_texmfdistdir}/tex/latex/uhhassignment
%doc %{_texmfdistdir}/doc/latex/uhhassignment

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
