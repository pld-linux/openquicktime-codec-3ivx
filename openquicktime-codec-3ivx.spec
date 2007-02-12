Summary:	3ivX codec for OpenQuickTime
Summary(pl.UTF-8):   Kodek 3ivX dla OpenQuickTime
Name:		openquicktime-codec-3ivx
Version:	3.5
Release:	1
License:	unknown
# README mentions http://www.3ivx.com/download.html, but no word about license there
Group:		Libraries
Source0:	http://www.3ivx.com/codec/unix/3ivxopenqt1i686linuxglibc21.tgz
# NoSource0-md5:	1c7d2590d8d59b62da22fbd6485ff085
NoSource:	0
URL:		http://www.3ivx.com/
Requires:	openquicktime >= 1.0
ExclusiveArch:	i686 pentium3 pentium4 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3ivX codec for OpenQuickTime.

%description -l pl.UTF-8
Kodek 3ivX dla OpenQuickTime.

%prep
%setup -q -n 3ivx-openquicktime-1.0-i686linux-glibc21

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

install quicktime_codec_3IV1.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/quicktime_codec_3IV1.so
