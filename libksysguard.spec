#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libksysguard
Version  : 5.13.3
Release  : 1
URL      : https://github.com/KDE/libksysguard/archive/v5.13.3.tar.gz
Source0  : https://github.com/KDE/libksysguard/archive/v5.13.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libksysguard-lib
Requires: libksysguard-data
Requires: libksysguard-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kiconthemes-dev
BuildRequires : kpackage-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : plasma-framework-dev
BuildRequires : zlib-dev

%description
To create a script:
* Make a folder here with any name
* Inside create a file with any name, ending .desktop, looking like:

%package data
Summary: data components for the libksysguard package.
Group: Data

%description data
data components for the libksysguard package.


%package dev
Summary: dev components for the libksysguard package.
Group: Development
Requires: libksysguard-lib
Requires: libksysguard-data
Provides: libksysguard-devel

%description dev
dev components for the libksysguard package.


%package lib
Summary: lib components for the libksysguard package.
Group: Libraries
Requires: libksysguard-data
Requires: libksysguard-license

%description lib
lib components for the libksysguard package.


%package license
Summary: license components for the libksysguard package.
Group: Default

%description license
license components for the libksysguard package.


%prep
%setup -q -n libksysguard-5.13.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532445982
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532445982
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libksysguard
cp COPYING.LIB %{buildroot}/usr/share/doc/libksysguard/COPYING.LIB
cp COPYING %{buildroot}/usr/share/doc/libksysguard/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/ksysguardprocesslist_helper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
/usr/share/ksysguard/scripts/README
/usr/share/ksysguard/scripts/smaps/helper.js
/usr/share/ksysguard/scripts/smaps/index.html
/usr/share/ksysguard/scripts/smaps/main.js
/usr/share/ksysguard/scripts/smaps/smaps.desktop
/usr/share/ksysguard/scripts/smaps/sorttable.js
/usr/share/ksysguard/scripts/smaps/style.css

%files dev
%defattr(-,root,root,-)
/usr/include/ksysguard/ksgrd/SensorAgent.h
/usr/include/ksysguard/ksgrd/SensorClient.h
/usr/include/ksysguard/ksgrd/SensorManager.h
/usr/include/ksysguard/ksgrd/SensorShellAgent.h
/usr/include/ksysguard/ksgrd/SensorSocketAgent.h
/usr/include/ksysguard/ksignalplotter.h
/usr/include/ksysguard/lsof.h
/usr/include/ksysguard/processcore/process.h
/usr/include/ksysguard/processcore/processes.h
/usr/include/ksysguard/processui/KTextEditVT.h
/usr/include/ksysguard/processui/ProcessFilter.h
/usr/include/ksysguard/processui/ProcessModel.h
/usr/include/ksysguard/processui/ksysguardprocesslist.h
/usr/lib64/cmake/KF5SysGuard/KF5SysGuardConfig.cmake
/usr/lib64/cmake/KF5SysGuard/KF5SysGuardConfigVersion.cmake
/usr/lib64/cmake/KF5SysGuard/KF5SysGuardLibraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5SysGuard/KF5SysGuardLibraryTargets.cmake
/usr/lib64/libksgrd.so
/usr/lib64/libksignalplotter.so
/usr/lib64/liblsofui.so
/usr/lib64/libprocesscore.so
/usr/lib64/libprocessui.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libksgrd.so.5.13.3
/usr/lib64/libksgrd.so.7
/usr/lib64/libksignalplotter.so.5.13.3
/usr/lib64/libksignalplotter.so.7
/usr/lib64/liblsofui.so.5.13.3
/usr/lib64/liblsofui.so.7
/usr/lib64/libprocesscore.so.5.13.3
/usr/lib64/libprocesscore.so.7
/usr/lib64/libprocessui.so.5.13.3
/usr/lib64/libprocessui.so.7

%files license
%defattr(-,root,root,-)
/usr/share/doc/libksysguard/COPYING
/usr/share/doc/libksysguard/COPYING.LIB
