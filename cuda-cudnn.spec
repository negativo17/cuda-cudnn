%global         cuda_version 8.0

Name:           cuda-cudnn
Version:        5.1
Release:        2%{?dist}
Epoch:          1
Summary:        NVIDIA CUDA Deep Neural Network library (cuDNN)
License:        ASD
URL:            https://developer.nvidia.com/cudnn
ExclusiveArch:  x86_64

Source0:        cudnn-%{cuda_version}-linux-x64-v%{version}-tgz.tgz
Source1:        cudnn-%{cuda_version}-samples-v%{version}.tgz
Source2:        CUDNN_Library.pdf
Source3:        cuDNN_v5.1_ReleaseNotes.pdf
Source4:        EULA.txt

Requires:       cuda >= %{?epoch:%{epoch}:}%{cuda_version}

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
%setup -a1 -qn cuda
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/cuda
mkdir -p %{buildroot}%{_includedir}/cuda

install -p -m 755 %{_lib}/*.so* %{buildroot}%{_libdir}/
install -p -m 644 %{_lib}/*.a %{buildroot}%{_libdir}/
install -p -m 644 include/* %{buildroot}%{_includedir}/cuda/
cp -frp *samples* %{buildroot}%{_datadir}/cuda/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license EULA.txt
%{_libdir}/libcudnn.so.*

%files devel
%doc *pdf
%{_datadir}/cuda/*
%{_includedir}/cuda/*
%{_libdir}/libcudnn.so
%{_libdir}/libcudnn_static.a

%changelog
* Wed Oct 26 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-2
- Fix cuda dependency.

* Thu Oct 20 2016 Simone Caronni <negativo17@gmail.com> - 1:5.1-1
- First build.
