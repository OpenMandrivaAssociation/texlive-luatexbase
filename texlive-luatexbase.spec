Name:		texlive-luatexbase
Version:	1.3
Release:	2
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
%{_texmfdistdir}/tex/luatex/luatexbase
%doc %{_texmfdistdir}/doc/luatex/luatexbase
#- source
%doc %{_texmfdistdir}/source/luatex/luatexbase

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
