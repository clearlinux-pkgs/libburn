#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xE9CBDFC0ABC0A854 (scdbackup@gmx.net)
#
Name     : libburn
Version  : 1.5.6
Release  : 10
URL      : https://files.libburnia-project.org/releases/libburn-1.5.6.tar.gz
Source0  : https://files.libburnia-project.org/releases/libburn-1.5.6.tar.gz
Source1  : https://files.libburnia-project.org/releases/libburn-1.5.6.tar.gz.asc
Summary  : Library to read/write optical discs
Group    : Development/Tools
License  : GPL-2.0
Requires: libburn-bin = %{version}-%{release}
Requires: libburn-lib = %{version}-%{release}
Requires: libburn-license = %{version}-%{release}
Requires: libburn-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(libcdio)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
------------------------------------------------------------------------------
libburnia-project.org
------------------------------------------------------------------------------
This all is under GPL.
(See GPL reference, our clarification and commitment at the end of this text)
------------------------------------------------------------------------------
libburnia-project.org
By Mario Danic <mario.danic@gmail.com> and Thomas Schmitt <scdbackup@gmx.net>
Still containing parts of Libburn. By Derek Foreman <derek@signalmarketing.com>
and Ben Jansens <xor@orodu.net>

%package bin
Summary: bin components for the libburn package.
Group: Binaries
Requires: libburn-license = %{version}-%{release}

%description bin
bin components for the libburn package.


%package dev
Summary: dev components for the libburn package.
Group: Development
Requires: libburn-lib = %{version}-%{release}
Requires: libburn-bin = %{version}-%{release}
Provides: libburn-devel = %{version}-%{release}
Requires: libburn = %{version}-%{release}

%description dev
dev components for the libburn package.


%package lib
Summary: lib components for the libburn package.
Group: Libraries
Requires: libburn-license = %{version}-%{release}

%description lib
lib components for the libburn package.


%package license
Summary: license components for the libburn package.
Group: Default

%description license
license components for the libburn package.


%package man
Summary: man components for the libburn package.
Group: Default

%description man
man components for the libburn package.


%prep
%setup -q -n libburn-1.5.6
cd %{_builddir}/libburn-1.5.6
pushd ..
cp -a libburn-1.5.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687270550
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1687270550
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libburn
cp %{_builddir}/libburn-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libburn/5405311284eab5ab51113f87c9bfac435c695bb9 || :
cp %{_builddir}/libburn-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/libburn/a640a4b001c62a6f231213c9e10d5b985b05288b || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cdrskin
/usr/bin/cdrskin

%files dev
%defattr(-,root,root,-)
/usr/include/libburn/libburn.h
/usr/lib64/libburn.so
/usr/lib64/pkgconfig/libburn-1.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libburn.so.4.109.0
/usr/lib64/libburn.so.4
/usr/lib64/libburn.so.4.109.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libburn/5405311284eab5ab51113f87c9bfac435c695bb9
/usr/share/package-licenses/libburn/a640a4b001c62a6f231213c9e10d5b985b05288b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cdrskin.1
