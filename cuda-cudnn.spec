%global         debug_package %{nil}
%global         __strip /bin/true
%global         _missing_build_ids_terminate_build 0
%global         _build_id_links none
%global         cuda_version 12

Name:           cuda-cudnn
Version:        9.0.0.312
Release:        1%{?dist}
Epoch:          1
Summary:        NVIDIA CUDA Deep Neural Network library (cuDNN)
License:        NVIDIA Software Development Kit
URL:            https://developer.nvidia.com/cudnn
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-%{version}_cuda%{cuda_version}-archive.tar.xz
Source2:        https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-sbsa/cudnn-linux-sbsa-%{version}_cuda%{cuda_version}-archive.tar.xz

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

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/libcudnn*.so.*

%files devel
%{_includedir}/cudnn*
%{_libdir}/libcudnn*.so

%files static
%{_libdir}/libcudnn*.a

%changelog
* Sat Mar 16 2024 Simone Caronni <negativo17@gmail.com> - 1:9.0.0.312-1
- Update to 9.0.0.312.

* Sat Jan 06 2024 Simone Caronni <negativo17@gmail.com> - 1:8.9.7.29-1
- Update to 8.9.7.29.

* Wed Nov 29 2023 Simone Caronni <negativo17@gmail.com> - 1:8.9.6.50-1
- Update to version 8.9.6.50.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:8.9.5.29-1
- Update to 8.9.5.29.

* Wed Jul 12 2023 Simone Caronni <negativo17@gmail.com> - 1:8.9.3.28-1
- Update to 8.9.3.28.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:8.8.1.3-1
- Update to 8.8.1.3.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:8.8.0.121-1
- Update to 8.8.0.121.

* Tue Dec 20 2022 Simone Caronni <negativo17@gmail.com> - 1:8.7.0.84-1
- Update to 8.7.0.84 (still CUDA 11).

* Fri Oct 07 2022 Simone Caronni <negativo17@gmail.com> - 1:8.6.0.163-1
- Update to 8.6.0.163.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:8.3.3.40-1
- Update to 8.3.3.40, allow building on ppc64le and aarch64.
- Drop samples subpackage.
- Move headers one level above.

* Tue Nov 02 2021 Simone Caronni <negativo17@gmail.com> - 1:8.2.4.15-1
- Update to 8.2.4.15

* Wed Jul 21 2021 Simone Caronni <negativo17@gmail.com> - 1:8.2.2.26-1
- Update to 8.2.2.26.

* Mon Apr 26 2021 Simone Caronni <negativo17@gmail.com> - 1:8.2.0.53-1
- Update to 8.2.0.53.
- Split static libraries in separate subpackage.

* Thu Feb 18 2021 Simone Caronni <negativo17@gmail.com> - 1:8.1.0.77-1
- Update to 8.1.0.77.

* Mon Nov 16 2020 Simone Caronni <negativo17@gmail.com> - 1:8.0.5.39-1
- Update to 8.0.5.39.

* Tue Mar 03 2020 Simone Caronni <negativo17@gmail.com> - 1:7.6.5.32-1
- Update to 7.6.5.32.

* Mon Nov 04 2019 Simone Caronni <negativo17@gmail.com> - 1:7.6.4.38-2
- Split samples subpackage.

* Mon Oct 07 2019 Simone Caronni <negativo17@gmail.com> - 1:7.6.4.38-1
- Update to 7.6.4.38.

* Tue Jun 11 2019 Simone Caronni <negativo17@gmail.com> - 1:7.6.0.64-1
- Update to 7.6.0.64.

* Sat Apr 06 2019 Simone Caronni <negativo17@gmail.com> - 1:7.5.0.56-1
- Update to 7.5.0.56 for CUDA 10.1.

* Thu Jan 03 2019 Simone Caronni <negativo17@gmail.com> - 1:7.4.2.24-1
- Update to 7.4.2.24 for CUDA 10.

* Tue Aug 28 2018 Simone Caronni <negativo17@gmail.com> - 1:7.2.1.38-1
- Update to 7.2.1.38 for CUDA 9.2.

* Thu Apr 26 2018 Simone Caronni <negativo17@gmail.com> - 1:7.1.3.16-1
- Update to 7.1.3.16.

* Thu Feb 15 2018 Simone Caronni <negativo17@gmail.com> - 1:7.0.5.15-3
- Fix upgrade path from 5.1/6.0.

* Fri Feb 02 2018 Simone Caronni <negativo17@gmail.com> - 1:7.0.5.15-2
- Obsoletes cuDNN 5.x and 6.x on upgrades to CUDA 9.1.

* Thu Dec 14 2017 Simone Caronni <negativo17@gmail.com> - 1:7.0.5.15-1
- Update to 7.0.5.15.

* Thu Oct 05 2017 Simone Caronni <negativo17@gmail.com> - 1:7.0.3.11-1
- Update to 7.0.3.11.

* Wed Aug 30 2017 Simone Caronni <negativo17@gmail.com> - 1:7-1
- Update to 7.

* Fri Apr 07 2017 Simone Caronni <negativo17@gmail.com> - 1:6.0-1
- Update to version 6.0.

* Thu Nov 17 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-3
- Fix symlink for libraries.

* Wed Oct 26 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-2
- Remove useless CUDA dependency.

* Thu Oct 20 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-1
- First build.
