Summary:	A hardware-independent library for executing real-mode x86 code
Name:		libx86
Version:	0.99
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.codon.org.uk/~mjg59/libx86/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c426d4f29fdf3499158cf49d4f374315
URL:		http://www.codon.org.uk/~mjg59/libx86/
# it's supposed to be arch independant emu library but unfortunately right now it doesn't build
# on other architectures; check with newer versions!
ExclusiveArch: %{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's often useful to be able to make real-mode x86 BIOS calls from
userland. lrmi provides a simple interface to this for x86 machines,
but this doesn't help on other platforms. libx86 provides the lrmi
interface, but will also run on platforms such as amd64 and alpha.

%package devel
Summary:	Header files for libxdiff library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxdiff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libxdiff library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxdiff.

%package static
Summary:	Static libxdiff library
Summary(pl.UTF-8):	Statyczna biblioteka libxdiff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxdiff library.

%description static -l pl.UTF-8
Statyczna biblioteka libxdiff.

%prep
%setup -q
sed -i -e 's#/usr/lib/#%{_libdir}/#g' Makefile

%build
%{__make} \
%ifnarch %{ix86}
	BACKEND="x86emu" \
%endif
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
