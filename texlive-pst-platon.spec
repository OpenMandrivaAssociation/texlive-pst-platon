Name:		texlive-pst-platon
Version:	16538
Release:	1
Summary:	Platonic solids in PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-platon
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-platon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-platon.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-platon.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds to PSTricks the ability to draw 3-dimensional
views of the five Platonic solids.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-platon/pst-platon.sty
%doc %{_texmfdistdir}/doc/generic/pst-platon/Changes
%doc %{_texmfdistdir}/doc/generic/pst-platon/README
%doc %{_texmfdistdir}/doc/generic/pst-platon/pst-platon-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-platon/pst-platon-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-platon/pst-platon-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-platon/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
