%define major	0
%define major1	1
%define libipu	%mklibname ipu %{major}
%define libcec	%mklibname cec %{major1}
%define libpxp	%mklibname pxp %{major}

%define devname	%mklibname imx -d
%define micro	1.1.0

Summary:	Platform specific libraries for imx platform
Name:		imx-lib
Version:	3.10.53
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libusb.info
Source0:	http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/%{name}-%{version}-%{micro}.tar.gz
BuildRequires:	kernel-sabreboard-devel
BuildRequires:	kernel-headers = 1:3.10.53-2

%description
Platform specific libraries for imx platform

%package -n	%{libipu}
summary:	Platform specific i.mx6 libraries
group:		System/Libraries

%description -n	%{libipu}
Ipu library for imx6 platform

%package -n	%{libcec}
summary:	Platform specific i.mx6 libraries
group:		System/Libraries

%description -n	%{libcec}
Libcec library for imx6 platform

%package -n	%{libpxp}
summary:	Platform specific i.mx6 libraries
group:		System/Libraries

%description -n	%{libpxp}
PXP library for imx6 platform

%package	common
summary:	Platform specific i.mx6 libraries
group:		System/Libraries
Requires:	%{libipu} = %{EVRD}
Requires:	%{libpxp} = %{EVRD}
Requires:	%{libcec} = %{EVRD}

%description	common
PXP library for imx6 platform

%description -n	%{libpxp}
PXP library for imx6 platform

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libipu} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -qn %{name}-%{version}-%{micro}

%build
%make all CC=%{__cc} CXX=%{__cxx} PLATFORM=IMX6Q CFLAGS="%{optflags}"

%install
%makeinstall_std PLATFORM=IMX6Q DEST_DIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.a

%files -n %{libipu}
%{_libdir}/libipu.so.%{major}

%files -n %{libcec}
%{_libdir}/libcec.so.%{major1}

%files -n %{libpxp}
%{_libdir}/libpxp.so.%{major}

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/libcec.so
%{_libdir}/libipu.so
%{_libdir}/libpxp.so

%files common
