%global real_name cuda_cuxxfilt

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-0

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.0.76
Release:        1%{?dist}
Summary:        CUDA cuxxfilt (demangler)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 ppc64le aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-ppc64le/%{real_name}-linux-ppc64le-%{version}-archive.tar.xz
Source2:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-aarch64/%{real_name}-linux-aarch64-%{version}-archive.tar.xz

%description
CUDA cuxxfilt (demangler).

%package devel
Summary:        CUDA cuxxfilt (demangler)
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
CUDA cuxxfilt (demangler).

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch ppc64le
%setup -q -T -b 1 -n %{real_name}-linux-ppc64le-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 2 -n %{real_name}-linux-aarch64-%{version}-archive
%endif

%install
install -m 0755 -p -D bin/cu++filt %{buildroot}%{_bindir}/cu++filt
install -m 0644 -p -D include/nv_decode.h %{buildroot}%{_includedir}/nv_decode.h
install -m 0644 -p -D lib/libcufilt.a %{buildroot}%{_libdir}/libcufilt.a

%files devel
%license LICENSE
%{_bindir}/cu++filt
%{_includedir}/nv_decode.h
%{_libdir}/libcufilt.a

%changelog
* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.76-1
- Update to 12.0.76.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:11.8.86-1
- Update to 11.8.86.
- Use aarch64 archive in place of sbsa.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.91-1
- Update to 11.7.91.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:11.7.50-1
- Update to 11.7.50.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.124-1
- Update to 11.6.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.112-1
- Update to 11.6.112 (CUDA 11.6.1).

* Tue Jan 25 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.55-1
- First build with the new tarball components.

