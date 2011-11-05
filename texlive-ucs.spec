# revision 17090
# category Package
# catalog-ctan /macros/latex/contrib/unicode
# catalog-date 2010-02-19 00:25:14 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-ucs
Version:	20100219
Release:	1
Summary:	Extended UTF-8 input encoding for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unicode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This bundle provides the ucs package, and utf8x.def, together
with a large number of support files. The utf8x.def definition
file for use with inputenc covers a wider range of Unicode
characters than does utf8.def in the LaTeX distribution. The
ucs package provides facilities for efficient use of large sets
of Unicode characters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ucs/UnicodeT.sfd
%{_texmfdistdir}/tex/latex/ucs/autofe.sty
%{_texmfdistdir}/tex/latex/ucs/c00enc.def
%{_texmfdistdir}/tex/latex/ucs/c10enc.def
%{_texmfdistdir}/tex/latex/ucs/c40enc.def
%{_texmfdistdir}/tex/latex/ucs/c42enc.def
%{_texmfdistdir}/tex/latex/ucs/c61enc.def
%{_texmfdistdir}/tex/latex/ucs/cenccmn.tex
%{_texmfdistdir}/tex/latex/ucs/cp1252.enc
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
%{_texmfdistdir}/tex/latex/ucs/data/uni-46.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-468.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-469.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-47.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-470.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-471.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-48.def
%{_texmfdistdir}/tex/latex/ucs/data/uni-49.def
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
%{_texmfdistdir}/tex/latex/ucs/ldvarial.fd
%{_texmfdistdir}/tex/latex/ucs/ldvc2000.fd
%{_texmfdistdir}/tex/latex/ucs/ldvenc.def
%{_texmfdistdir}/tex/latex/ucs/letc2000.fd
%{_texmfdistdir}/tex/latex/ucs/letenc.def
%{_texmfdistdir}/tex/latex/ucs/letgfzem.fd
%{_texmfdistdir}/tex/latex/ucs/letjiret.fd
%{_texmfdistdir}/tex/latex/ucs/lklenc.def
%{_texmfdistdir}/tex/latex/ucs/lklkli.fd
%{_texmfdistdir}/tex/latex/ucs/ltaarial.fd
%{_texmfdistdir}/tex/latex/ucs/ltac2000.fd
%{_texmfdistdir}/tex/latex/ucs/ltaenc.def
%{_texmfdistdir}/tex/latex/ucs/ltgc2000.fd
%{_texmfdistdir}/tex/latex/ucs/ltgenc.def
%{_texmfdistdir}/tex/latex/ucs/ltlcmr.fd
%{_texmfdistdir}/tex/latex/ucs/ltlenc.def
%{_texmfdistdir}/tex/latex/ucs/ltwdsnol.fd
%{_texmfdistdir}/tex/latex/ucs/ltwdsque.fd
%{_texmfdistdir}/tex/latex/ucs/ltwdssin.fd
%{_texmfdistdir}/tex/latex/ucs/ltwenc.def
%{_texmfdistdir}/tex/latex/ucs/lucarial.fd
%{_texmfdistdir}/tex/latex/ucs/lucc2000.fd
%{_texmfdistdir}/tex/latex/ucs/lucenc.def
%{_texmfdistdir}/tex/latex/ucs/mkrenc.def
%{_texmfdistdir}/tex/latex/ucs/mkrezra.fd
%{_texmfdistdir}/tex/latex/ucs/mkrhadas.fd
%{_texmfdistdir}/tex/latex/ucs/mkromega.fd
%{_texmfdistdir}/tex/latex/ucs/mkrrashi.fd
%{_texmfdistdir}/tex/latex/ucs/t2dcmr.fd
%{_texmfdistdir}/tex/latex/ucs/t2denc.def
%{_texmfdistdir}/tex/latex/ucs/tengwarDS.enc
%{_texmfdistdir}/tex/latex/ucs/ucs.sty
%{_texmfdistdir}/tex/latex/ucs/ucsencs.def
%{_texmfdistdir}/tex/latex/ucs/ucshyper.sty
%{_texmfdistdir}/tex/latex/ucs/ucsutils.sty
%{_texmfdistdir}/tex/latex/ucs/utf8x.def
%{_texmfdistdir}/tex/latex/ucs/xscmr.fd
%{_texmfdistdir}/tex/latex/ucs/xsenc.def
%doc %{_texmfdistdir}/doc/latex/ucs/FAQ
%doc %{_texmfdistdir}/doc/latex/ucs/INSTALL
%doc %{_texmfdistdir}/doc/latex/ucs/LICENSE
%doc %{_texmfdistdir}/doc/latex/ucs/README
%doc %{_texmfdistdir}/doc/latex/ucs/VERSION
%doc %{_texmfdistdir}/doc/latex/ucs/config/ascii.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/boxdraw.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/braille.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-bg5.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-gb.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-globals.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-hangul.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/cjk-jis.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/combining.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/control.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/ctrlglyphs.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/currency.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/cyrillic.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/devanagari.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/ethiopic.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/geometric.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/greek.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/hebrew.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/ipa.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/klingon.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin-a.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin-b.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin-e-a.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/latin1.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/math.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/mathalpha.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/miscsymb.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/modifier.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/mongolian.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/pifont.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/punct.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/supersub.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/tags.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/telugu.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/config/thai.ucf.gz
%doc %{_texmfdistdir}/doc/latex/ucs/discovermacro.pl
%doc %{_texmfdistdir}/doc/latex/ucs/languages.pdf
%doc %{_texmfdistdir}/doc/latex/ucs/latexout.pl
%doc %{_texmfdistdir}/doc/latex/ucs/ltxmacrs.txt
%doc %{_texmfdistdir}/doc/latex/ucs/makeunidef.pl
%doc %{_texmfdistdir}/doc/latex/ucs/ucs.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
