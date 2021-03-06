#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE9CBDFC0ABC0A854 (scdbackup@gmx.net)
#
Name     : libburn
Version  : 1.5.4
Release  : 9
URL      : http://files.libburnia-project.org/releases/libburn-1.5.4.tar.gz
Source0  : http://files.libburnia-project.org/releases/libburn-1.5.4.tar.gz
Source1  : http://files.libburnia-project.org/releases/libburn-1.5.4.tar.gz.asc
Summary  : Library to read/write optical discs
Group    : Development/Tools
License  : GPL-2.0
Requires: libburn-bin = %{version}-%{release}
Requires: libburn-lib = %{version}-%{release}
Requires: libburn-license = %{version}-%{release}
Requires: libburn-man = %{version}-%{release}
BuildRequires : pkgconfig(libcdio)

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
%setup -q -n libburn-1.5.4
cd %{_builddir}/libburn-1.5.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612800752
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1612800752
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libburn
cp %{_builddir}/libburn-1.5.4/COPYING %{buildroot}/usr/share/package-licenses/libburn/5405311284eab5ab51113f87c9bfac435c695bb9
cp %{_builddir}/libburn-1.5.4/COPYRIGHT %{buildroot}/usr/share/package-licenses/libburn/a640a4b001c62a6f231213c9e10d5b985b05288b
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cdrskin

%files dev
%defattr(-,root,root,-)
/usr/include/libburn/libburn.h
/usr/lib64/libburn.so
/usr/lib64/pkgconfig/libburn-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libburn.so.4
/usr/lib64/libburn.so.4.107.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libburn/5405311284eab5ab51113f87c9bfac435c695bb9
/usr/share/package-licenses/libburn/a640a4b001c62a6f231213c9e10d5b985b05288b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cdrskin.1
