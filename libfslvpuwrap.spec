%define	major	3
%define	libname	%mklibname fslvpuwrap %{major}
%define	devname	%mklibname -d fslvpuwrap

Summary:	Freescale VPUwrap library
Name:		libfslvpuwrap
Version:	1.0.57
Release:	2
License:	Proprietary
Group:		System/Libraries
# downloaded and repackaged from:
# http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/libfslvpuwrap-1.0.46.bin
URL:		http://www.freescale.com
Source0:	http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/%{name}-%{version}.tar.xz
BuildRequires:	libvpu-devel
ExclusiveArch:	armv7hl armv7hnl

%description
Freescale VPUwrap library.

%package -n	%{libname}
Summary:	Freescale VPUwrap library
Group:		System/Libraries

%description -n	%{libname}
Freescale VPUwrap library.

%package -n	%{devname}
Summary:	Development files for Freescale VPUwrap library
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Development files for Freescale VPUwrap library.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fiv
libtoolize --copy --force
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%doc %{_docdir}/%{name}
%{_libdir}/libfslvpuwrap.so.%{major}*

%files -n %{devname}
%dir %{_datadir}/imx-mm
%dir %{_datadir}/imx-mm/video-codec/
%doc %{_datadir}/imx-mm/video-codec/examples
%{_libdir}/libfslvpuwrap.so
%{_libdir}/pkgconfig/libfslvpuwrap.pc
%dir %{_includedir}/imx-mm/
%dir %{_includedir}/imx-mm/vpu
%{_includedir}/imx-mm/vpu/vpu_wrapper.h
