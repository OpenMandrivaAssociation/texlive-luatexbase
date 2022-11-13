Name:		texlive-luatexbase
Version:	52663
Release:	1
Summary:	Basic resource management for LuaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luatexbase
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexbase.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexbase.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexbase.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
