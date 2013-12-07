# revision 30472
# category Package
# catalog-ctan /macros/latex/contrib/ucs
# catalog-date 2013-05-12 16:23:52 +0200
# catalog-license lppl1.3
# catalog-version 2.2
Name:		texlive-ucs
Epoch:		1
Version:	2.2
Release:	2
Summary:	Extended UTF-8 input encoding support for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/ucs/data/uni-0.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-1.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-100.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-101.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-102.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-103.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-104.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-105.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-106.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-107.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-108.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-109.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-110.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-111.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-112.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-113.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-114.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-115.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-116.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-117.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-118.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-119.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-12.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-120.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-121.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-122.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-123.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-124.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-125.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-126.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-127.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-128.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-129.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-130.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-131.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-132.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-133.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-134.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-135.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-136.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-137.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-138.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-139.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-14.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-140.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-141.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-142.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-143.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-144.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-145.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-146.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-147.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-148.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-149.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-150.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-151.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-152.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-153.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-154.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-155.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-156.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-157.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-158.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-159.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-167.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-172.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-173.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-174.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-175.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-176.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-177.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-178.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-179.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-18.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-180.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-181.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-182.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-183.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-184.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-185.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-186.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-187.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-188.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-189.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-19.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-190.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-191.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-192.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-193.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-194.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-195.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-196.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-197.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-198.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-199.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-2.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-200.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-201.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-202.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-203.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-204.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-205.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-206.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-207.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-208.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-209.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-210.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-211.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-212.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-213.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-214.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-215.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-24.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-248.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-249.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-250.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-251.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-254.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-255.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-29.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-3.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-30.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-31.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-32.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-33.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-34.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-35.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-3584.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-36.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-37.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-38.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-39.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-4.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-40.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-42.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-44.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-46.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-465.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-468.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-469.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-47.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-470.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-471.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-48.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-49.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-497.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-498.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-5.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-50.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-51.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-760.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-761.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-762.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-78.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-79.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-80.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-81.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-82.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-83.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-84.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-85.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-86.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-87.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-88.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-89.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-9.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-90.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-91.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-92.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-93.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-94.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-95.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-96.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-97.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-98.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-99.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-global.def
%{_texmfdistdir}/tex/latex/ucs/data/uninames.dat
%{_texmfdistdir}/tex/latex/ucs/ucs.sty
%{_texmfdistdir}/tex/latex/ucs/ucsencs.def
%{_texmfdistdir}/tex/latex/ucs/ucshyper.sty
%{_texmfdistdir}/tex/latex/ucs/ucsutils.sty
%{_texmfdistdir}/tex/latex/ucs/utf8x.def
%{_texmfdistdir}/tex/latex/ucs/utils/UnicodeT.sfd
%{_texmfdistdir}/tex/latex/ucs/utils/autofe.sty
%{_texmfdistdir}/tex/latex/ucs/utils/c00enc.def
%{_texmfdistdir}/tex/latex/ucs/utils/c10enc.def
%{_texmfdistdir}/tex/latex/ucs/utils/c40enc.def
%{_texmfdistdir}/tex/latex/ucs/utils/c42enc.def
%{_texmfdistdir}/tex/latex/ucs/utils/c61enc.def
%{_texmfdistdir}/tex/latex/ucs/utils/cenccmn.tex
%{_texmfdistdir}/tex/latex/ucs/utils/cp1252.enc
%{_texmfdistdir}/tex/latex/ucs/utils/ldvarial.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ldvc2000.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ldvenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/letc2000.fd
%{_texmfdistdir}/tex/latex/ucs/utils/letenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/letgfzem.fd
%{_texmfdistdir}/tex/latex/ucs/utils/letjiret.fd
%{_texmfdistdir}/tex/latex/ucs/utils/lklenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/lklkli.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltaarial.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltac2000.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltaenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/ltgc2000.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltgenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/ltlcmr.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltlenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/ltwdsnol.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltwdsque.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltwdssin.fd
%{_texmfdistdir}/tex/latex/ucs/utils/ltwenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/lucarial.fd
%{_texmfdistdir}/tex/latex/ucs/utils/lucc2000.fd
%{_texmfdistdir}/tex/latex/ucs/utils/lucenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/mkrenc.def
%{_texmfdistdir}/tex/latex/ucs/utils/mkrezra.fd
%{_texmfdistdir}/tex/latex/ucs/utils/mkrhadas.fd
%{_texmfdistdir}/tex/latex/ucs/utils/mkromega.fd
%{_texmfdistdir}/tex/latex/ucs/utils/mkrrashi.fd
%{_texmfdistdir}/tex/latex/ucs/utils/t2dcmr.fd
%{_texmfdistdir}/tex/latex/ucs/utils/t2denc.def
%{_texmfdistdir}/tex/latex/ucs/utils/tengwarDS.enc
%{_texmfdistdir}/tex/latex/ucs/utils/xscmr.fd
%{_texmfdistdir}/tex/latex/ucs/utils/xsenc.def
%doc %{_texmfdistdir}/doc/latex/ucs/FAQ
%doc %{_texmfdistdir}/doc/latex/ucs/GNUmakefile
%doc %{_texmfdistdir}/doc/latex/ucs/INSTALL
%doc %{_texmfdistdir}/doc/latex/ucs/LICENSE
%doc %{_texmfdistdir}/doc/latex/ucs/README
%doc %{_texmfdistdir}/doc/latex/ucs/VERSION
%doc %{_texmfdistdir}/doc/latex/ucs/config/ascii.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/boxdraw.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/braille.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-bg5.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-gb.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-globals.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-hangul.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-jis.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/combining.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/control.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/ctrlglyphs.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/currency.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/cyrillic.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/devanagari.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/ethiopic.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/geometric.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/greek.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/hebrew.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/ipa.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/klingon.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin-a.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin-b.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin-e-a.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin1.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/math.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/mathalpha.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/miscsymb.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/modifier.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/mongolian.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/pifont.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/punct.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/supersub.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/tags.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/telugu.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/config/thai.ucf
%doc %{_texmfdistdir}/doc/latex/ucs/discovermacro.pl
%doc %{_texmfdistdir}/doc/latex/ucs/languages.ps.gz
%doc %{_texmfdistdir}/doc/latex/ucs/latexout.pl
%doc %{_texmfdistdir}/doc/latex/ucs/ltxmacrs.txt
%doc %{_texmfdistdir}/doc/latex/ucs/makeunidef.pl
%doc %{_texmfdistdir}/doc/latex/ucs/ucs.dtx
%doc %{_texmfdistdir}/doc/latex/ucs/ucs.ins
%doc %{_texmfdistdir}/doc/latex/ucs/ucs.pdf
%doc %{_texmfdistdir}/doc/latex/ucs/unsupported/README
%doc %{_texmfdistdir}/doc/latex/ucs/unsupported/sym-to-fontenc.txt
%doc %{_texmfdistdir}/doc/latex/ucs/unsupported/tables.inc
%doc %{_texmfdistdir}/doc/latex/ucs/unsupported/u2ps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
