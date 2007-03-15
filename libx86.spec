Summary:	A hardware-independent library for executing real-mode x86 code
Summary(pl.UTF-8):	Niezależna od sprzętu biblioteka do wykonywania kodu trybu rzeczywistego x86
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
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's often useful to be able to make real-mode x86 BIOS calls from
userland. lrmi provides a simple interface to this for x86 machines,
but this doesn't help on other platforms. libx86 provides the lrmi
interface, but will also run on platforms such as amd64 and alpha.

%description -l pl.UTF-8
Często przydaje się możliwość wykonania wywołań trybu rzeczywistego
BIOS-u x86 z przestrzeni użytkownika. lrmi udostępnia prosty interfejs
do tego dla maszyn x86, ale nie pomaga to na innych platformach.
libx86 udostępnia interfejs lrmi, ale działający także na platformach
takich jak amd64 czy alpha.

%package devel
Summary:	Header files for libx86 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libx86
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libx86 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libx86.

%package static
Summary:	Static libx86 library
Summary(pl.UTF-8):	Statyczna biblioteka libx86
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libx86 library.

%description static -l pl.UTF-8
Statyczna biblioteka libx86.

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
