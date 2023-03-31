Name:		texlive-ucs
Epoch:		1
Version:	64114
Release:	2
Summary:	Extended UTF-8 input encoding support for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides the ucs package, and utf8x.def, together
with a large number of support files. The utf8x.def definition
file for use with inputenc covers a wider range of Unicode
characters than does utf8.def in the LaTeX distribution. The
package provides facilities for efficient use of its large sets
of Unicode characters. Glyph production may be controlled by
various options, which permits use of non-ASCII characters when
coding mathematical formulae. Note that the bundle previously
had an alias "unicode"; that alias has now been withdrawn, and
no package of that name now exists.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ucs
%doc %{_texmfdistdir}/doc/latex/ucs

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
