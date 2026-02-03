%global         debug_package %{nil}
%global         __strip /bin/true
%global         _missing_build_ids_terminate_build 0
%global         _build_id_links none
%global         cuda_version 13

Name:           cuda-cudnn
Version:        9.18.1.3
Release:        1%{?dist}
Epoch:          1
Summary:        NVIDIA CUDA Deep Neural Network library (cuDNN)
License:        NVIDIA Software Development Kit
URL:            https://developer.nvidia.com/cudnn
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-%{version}_cuda%{cuda_version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-sbsa/cudnn-linux-sbsa-%{version}_cuda%{cuda_version}-archive.tar.xz

%description
The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated
library of primitives for deep neural networks. cuDNN provides highly tuned
implementations for standard routines such as forward and backward convolution,
pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep
Learning SDK.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cuda%{?_isa} >= %{?epoch:%{epoch}:}%{cuda_version}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    static
Static library files for %{name}.

%prep
%ifarch x86_64
%setup -q -n cudnn-linux-x86_64-%{version}_cuda%{cuda_version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n cudnn-linux-sbsa-%{version}_cuda%{cuda_version}-archive
%endif

%install
mkdir -p %{buildroot}%{_libdir}
cp -a lib/*.so* %{buildroot}%{_libdir}/
chmod 755 %{buildroot}%{_libdir}/*.so*
cp -a lib/*.a %{buildroot}%{_libdir}/
chmod 644 %{buildroot}%{_libdir}/*.a

mkdir -p %{buildroot}%{_includedir}
cp -a include/* %{buildroot}%{_includedir}/
chmod 644 %{buildroot}%{_includedir}/*

%files
%license LICENSE
%{_libdir}/libcudnn*.so.*

%files devel
%{_includedir}/cudnn*
%{_libdir}/libcudnn*.so

%files static
%{_libdir}/libcudnn*.a

%changelog
* Tue Feb 03 2026 Simone Caronni <negativo17@gmail.com> - 1:9.18.1.3-1
- Update to 9.18.1.3.
- Trim changelog.

* Sun Oct 26 2025 Simone Caronni <negativo17@gmail.com> - 1:9.14.0.64-1
- Upda to 9.14.0.64.

* Fri Feb 07 2025 Simone Caronni <negativo17@gmail.com> - 1:9.7.1.26-1
- Update to 9.7.1.26.

* Sat Dec 14 2024 Simone Caronni <negativo17@gmail.com> - 1:9.6.0.74-1
- Update to 9.6.0.74.

* Tue Sep 24 2024 Simone Caronni <negativo17@gmail.com> - 1:9.4.0.58-1
- Update to 9.4.0.58.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:9.2.1.18-1
- Update to 9.2.1.18.

* Mon Mar 18 2024 Simone Caronni <negativo17@gmail.com> - 1:9.0.0.312-2
- Fix typo.
- Trim changelog.

* Sat Mar 16 2024 Simone Caronni <negativo17@gmail.com> - 1:9.0.0.312-1
- Update to 9.0.0.312.

* Sat Jan 06 2024 Simone Caronni <negativo17@gmail.com> - 1:8.9.7.29-1
- Update to 8.9.7.29.
