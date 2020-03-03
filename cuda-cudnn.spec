%global         cuda_version 10.2
%global         cuda_cudnn_major 7.6

Name:           cuda-cudnn
Version:        7.6.5.32
Release:        1%{?dist}
Epoch:          1
Summary:        NVIDIA CUDA Deep Neural Network library (cuDNN)
License:        NVIDIA License
URL:            https://developer.nvidia.com/cudnn
ExclusiveArch:  x86_64

Source0:        cudnn-%{cuda_version}-linux-x64-v%{version}.tgz
Source1:        libcudnn7-doc_%{version}-1+cuda%{cuda_version}_amd64.deb

Obsoletes:      %{name}5.1 <= %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}6.0 <= %{?epoch:%{epoch}:}%{version}-%{release}

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

%package        samples
Summary:        NVIDIA CUDA Deep Neural Network library samples
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cuda%{?_isa} >= %{?epoch:%{epoch}:}%{cuda_version}

%description    samples
Contains an extensive set of example cuDNN programs.

%prep
%setup -qn cuda
chmod -x *.txt

# Samples
ar x %{SOURCE1}
tar -xvJf data.tar.xz ./usr/src --strip-components=3
rm -f data.tar.xz

find . -name "*py" -exec sed -i -e 's|/usr/bin/env python|/usr/bin/python2|g' {} \;

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/cuda
mkdir -p %{buildroot}%{_includedir}/cuda

cp -pa %{_lib}/*.so* %{_lib}/*.a %{buildroot}%{_libdir}/
install -p -m 644 include/* %{buildroot}%{_includedir}/cuda/
cp -frp *samples* %{buildroot}%{_datadir}/cuda/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license *.txt
%{_libdir}/libcudnn.so.*

%files devel
%{_includedir}/cuda/*
%{_libdir}/libcudnn.so
%{_libdir}/libcudnn_static.a

%files samples
%{_datadir}/cuda/*

%changelog
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
