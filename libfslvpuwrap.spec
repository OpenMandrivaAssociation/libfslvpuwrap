%define	major	3
%define	libname	%mklibname fslvpuwrap %{major}
%define	devname	%mklibname -d fslvpuwrap

Summary:	Freescale VPUwrap library
Name:		libfslvpuwrap
Version:	1.0.46	
Release:	1
License:	Proprietary
Group:		System/Libraries
# downloaded and repackaged from:
# http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/libfslvpuwrap-1.0.46.bin
URL:		http://www.freescale.com
Source0:	%{name}-%{version}.tar.xz
Patch0:		libfslvpuwrap-0001-vpu_wrapper-fix-tests-of-return-value-from-IOGetVirt.patch
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
%patch0 -p1 -b .IOGetVirt~

%build
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
