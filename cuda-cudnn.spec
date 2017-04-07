%global         cuda_version 8.0

Name:           cuda-cudnn
Version:        6.0
Release:        1%{?dist}
Epoch:          1
Summary:        NVIDIA CUDA Deep Neural Network library (cuDNN)
License:        NVIDIA License
URL:            https://developer.nvidia.com/cudnn
ExclusiveArch:  x86_64

Source0:        cudnn-%{cuda_version}-linux-x64-v%{version}.tgz
Source1:        libcudnn6-doc_%{version}.20-1+cuda%{cuda_version}_amd64.deb
Source2:        CUDNN_Library.pdf
Source3:        cuDNN_v%{version}_ReleaseNotes.pdf
Source4:        NVIDIA_SLA+cuDNN_Supp_Feb2017_release.pdf

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

%prep
%setup -qn cuda
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} .

# Samples
ar x %{SOURCE1}
tar -xvJf data.tar.xz ./usr/src --strip-components=3
rm -f data.tar.xz

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
%license NVIDIA_SLA+cuDNN_Supp_Feb2017_release.pdf
%{_libdir}/libcudnn.so.*

%files devel
%doc CUDNN_Library.pdf cuDNN_v%{version}_ReleaseNotes.pdf
%{_datadir}/cuda/*
%{_includedir}/cuda/*
%{_libdir}/libcudnn.so
%{_libdir}/libcudnn_static.a

%changelog
* Fri Apr 07 2017 Simone Caronni <negativo17@gmail.com> - 1:6.0-1
- Update to version 6.0.

* Thu Nov 17 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-3
- Fix symlink for libraries.

* Wed Oct 26 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-2
- Remove useless CUDA dependency.

* Thu Oct 20 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-1
- First build.
