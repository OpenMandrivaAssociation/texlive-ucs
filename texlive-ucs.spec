%global tl_name ucs
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Extended UTF-8 input encoding support for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ucs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides the ucs package, and utf8x.def, together with a
large number of support files. The utf8x.def definition file for use
with inputenc covers a wider range of Unicode characters than does
utf8.def in the LaTeX distribution. The package provides facilities for
efficient use of its large sets of Unicode characters. Glyph production
may be controlled by various options, which permits use of non-ASCII
characters when coding mathematical formulae. Note that the bundle
previously had an alias "unicode"; that alias has now been withdrawn,
and no package of that name now exists.

