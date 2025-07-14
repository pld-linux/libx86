Summary:	A hardware-independent library for executing real-mode x86 code
Summary(pl.UTF-8):	Niezależna od sprzętu biblioteka do wykonywania kodu trybu rzeczywistego x86
Name:		libx86
Version:	1.1
Release:	3
License:	MIT (libx86), BSD (x86emu)
Group:		Libraries
Source0:	http://www.codon.org.uk/~mjg59/libx86/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	41bee1f8e22b82d82b5f7d7ba51abc2a
Patch0:		%{name}-lrmi.patch
URL:		http://www.codon.org.uk/~mjg59/libx86/
# it's supposed to be arch independant emu library but unfortunately right now it doesn't build
# on other architectures; check with newer versions!
ExclusiveArch:	%{ix86} %{x8664} x32
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
%patch -P0 -p0

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
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx86.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx86.so
%{_includedir}/libx86.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libx86.a
