# revision 22560
# category Package
# catalog-ctan /macros/luatex/generic/luatexbase
# catalog-date 2011-05-21 16:06:38 +0200
# catalog-license pd
# catalog-version 0.31
Name:		texlive-luatexbase
Version:	0.31
Release:	3
Summary:	Basic resource management for LuaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luatexbase
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexbase.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexbase.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexbase.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides basic facilities for LuaTeX macro
programmers, mostly resource allocation and convenience
packages. Provided are: - luatexbase-attr: attribute
allocation; - luatexbase-cctb: catcode table allocation; -
luatexbase-compat: compatibility helpers; - luatexbase-loader:
Lua module loading; - luatexbase-modutils: Lua module
declaration; - luatexbase-mcb: callbacks extension; and -
luatexbase-regs: allocation of registers and the like. In
addition, the (unadorned) luatexbase package loads all the
above in one fell swoop.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/luatexbase/attr.lua
%{_texmfdistdir}/tex/luatex/luatexbase/cctb.lua
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-attr.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-cctb.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-compat.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-loader.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-mcb.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-modutils.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-regs.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase.loader.lua
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase.sty
%{_texmfdistdir}/tex/luatex/luatexbase/mcb.lua
%{_texmfdistdir}/tex/luatex/luatexbase/modutils.lua
%doc %{_texmfdistdir}/doc/luatex/luatexbase/Changes
%doc %{_texmfdistdir}/doc/luatex/luatexbase/README
%doc %{_texmfdistdir}/doc/luatex/luatexbase/TODO
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase-attr.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase-cctb.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase-compat.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase-loader.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase-mcb.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase-modutils.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase-regs.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/luatexbase.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-attr-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-attr-plain.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-base-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-base-plain.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-cctb-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-cctb-plain.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-compat-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-compat-plain.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-loader-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-loader-plain.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-loader.lua
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-loader.sub.lua
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-mcb-aux.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-mcb-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-mcb-plain.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-mcb.lua
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-modutils-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-modutils-plain.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-modutils.lua
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-regs-latex.tex
%doc %{_texmfdistdir}/doc/luatex/luatexbase/test-regs-plain.tex
#- source
%doc %{_texmfdistdir}/source/luatex/luatexbase/Makefile
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase-attr.dtx
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase-cctb.dtx
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase-compat.dtx
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase-loader.dtx
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase-mcb.dtx
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase-modutils.dtx
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase-regs.dtx
%doc %{_texmfdistdir}/source/luatex/luatexbase/luatexbase.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.31-2
+ Revision: 753604
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.31-1
+ Revision: 718931
- texlive-luatexbase
- texlive-luatexbase
- texlive-luatexbase
- texlive-luatexbase

