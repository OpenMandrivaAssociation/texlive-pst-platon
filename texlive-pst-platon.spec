# revision 16538
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-platon
# catalog-date 2010-01-01 00:46:51 +0100
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-pst-platon
Version:	0.01
Release:	3
Summary:	Platonic solids in PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-platon
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-platon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-platon.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-platon.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.01-2
+ Revision: 755398
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.01-1
+ Revision: 719380
- texlive-pst-platon
- texlive-pst-platon
- texlive-pst-platon
- texlive-pst-platon

