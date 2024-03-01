#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : libksysguard
Version  : 6.0.0
Release  : 93
URL      : https://download.kde.org/stable/plasma/6.0.0/libksysguard-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.0/libksysguard-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.0/libksysguard-6.0.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: libksysguard-data = %{version}-%{release}
Requires: libksysguard-lib = %{version}-%{release}
Requires: libksysguard-license = %{version}-%{release}
Requires: libksysguard-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev
BuildRequires : libcap-dev
BuildRequires : libpcap-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-route-3.0)
BuildRequires : qt6base-dev
BuildRequires : qtsensors-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Per-process Network Usage Plugin
================================
This plugin tries to track per-process network usage and feeds that back to
ksysguard. Unfortunately, at the moment there is no unprivileged API available
for this information, so this plugin uses a small helper application to work
around that. The helper uses libpcap to do packet capture. To do the packet
capture it needs `cap_net_raw`, but nothing else. To ensure the helper has
`cap_net_raw`, run `setcap cap_net_raw+ep ksgrd_network_helper` as root.

%package data
Summary: data components for the libksysguard package.
Group: Data

%description data
data components for the libksysguard package.


%package dev
Summary: dev components for the libksysguard package.
Group: Development
Requires: libksysguard-lib = %{version}-%{release}
Requires: libksysguard-data = %{version}-%{release}
Provides: libksysguard-devel = %{version}-%{release}
Requires: libksysguard = %{version}-%{release}

%description dev
dev components for the libksysguard package.


%package lib
Summary: lib components for the libksysguard package.
Group: Libraries
Requires: libksysguard-data = %{version}-%{release}
Requires: libksysguard-license = %{version}-%{release}

%description lib
lib components for the libksysguard package.


%package license
Summary: license components for the libksysguard package.
Group: Default

%description license
license components for the libksysguard package.


%package locales
Summary: locales components for the libksysguard package.
Group: Default

%description locales
locales components for the libksysguard package.


%prep
%setup -q -n libksysguard-6.0.0
cd %{_builddir}/libksysguard-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709333104
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709333104
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksysguard
cp %{_builddir}/libksysguard-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/libksysguard/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libksysguard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libksysguard/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksysguard/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksysguard/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libksysguard-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang KSysGuardSensorFaces
%find_lang ksgrd
%find_lang ksysguard_face_org.kde.ksysguard.barchart
%find_lang ksysguard_face_org.kde.ksysguard.colorgrid
%find_lang ksysguard_face_org.kde.ksysguard.facegrid
%find_lang ksysguard_face_org.kde.ksysguard.linechart
%find_lang ksysguard_face_org.kde.ksysguard.piechart
%find_lang ksysguard_face_org.kde.ksysguard.textonly
%find_lang ksysguard_sensors
%find_lang ksysguardlsofwidgets
%find_lang processcore
%find_lang processui
%find_lang KSysGuardFormatter
%find_lang ksysguard_face_org.kde.ksysguard.horizontalbars
## install_append content
#mv %{buildroot}/etc/dbus-1/* %{buildroot}/usr/share/dbus-1/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kauth/ksysguardprocesslist_helper
/V3/usr/lib64/libexec/ksysguard/ksgrd_network_helper
/usr/lib64/libexec/kf6/kauth/ksysguardprocesslist_helper
/usr/lib64/libexec/ksysguard/ksgrd_network_helper
/usr/lib64/qt6/qml/org/kde/ksysguard/faces/Choices.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/faces/ExtendedLegend.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/faces/SensorFace.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/faces/SensorRangeSpinBox.qml
/usr/lib64/qt6/qml/org/kde/ksysguard/faces/qmldir
/usr/lib64/qt6/qml/org/kde/ksysguard/formatter/qmldir
/usr/lib64/qt6/qml/org/kde/ksysguard/process/qmldir
/usr/lib64/qt6/qml/org/kde/ksysguard/sensors/qmldir

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.ksystemstats1.xml
/usr/share/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
/usr/share/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
/usr/share/knsrcfiles/systemmonitor-faces.knsrc
/usr/share/knsrcfiles/systemmonitor-presets.knsrc
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/BarChart.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/contents/ui/FaceGrid.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/contents/ui/SensorRect.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.colorgrid/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/FaceControl.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/FaceGrid.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/ui/Bar.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/LineChart.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/PieChart.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/UsedTotalDisplay.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/GroupedText.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/metadata.json
/usr/share/qlogging-categories6/libksysguard.categories

%files dev
%defattr(-,root,root,-)
/usr/include/ksysguard/faces/FaceLoader.h
/usr/include/ksysguard/faces/SensorFaceController.h
/usr/include/ksysguard/faces/SensorFace_p.h
/usr/include/ksysguard/faces/sensorfaces_export.h
/usr/include/ksysguard/formatter/Formatter.h
/usr/include/ksysguard/formatter/Unit.h
/usr/include/ksysguard/formatter/formatter_export.h
/usr/include/ksysguard/processcore/formatter.h
/usr/include/ksysguard/processcore/process.h
/usr/include/ksysguard/processcore/process_attribute.h
/usr/include/ksysguard/processcore/process_attribute_model.h
/usr/include/ksysguard/processcore/process_controller.h
/usr/include/ksysguard/processcore/process_data_model.h
/usr/include/ksysguard/processcore/process_data_provider.h
/usr/include/ksysguard/processcore/processcore_export.h
/usr/include/ksysguard/processcore/processes.h
/usr/include/ksysguard/processcore/unit.h
/usr/include/ksysguard/sensors/Sensor.h
/usr/include/ksysguard/sensors/SensorDataModel.h
/usr/include/ksysguard/sensors/SensorInfo_p.h
/usr/include/ksysguard/sensors/SensorQuery.h
/usr/include/ksysguard/sensors/SensorTreeModel.h
/usr/include/ksysguard/sensors/SensorUnitModel.h
/usr/include/ksysguard/sensors/sensors_export.h
/usr/include/ksysguard/systemstats/AggregateSensor.h
/usr/include/ksysguard/systemstats/DBusInterface.h
/usr/include/ksysguard/systemstats/SensorContainer.h
/usr/include/ksysguard/systemstats/SensorInfo.h
/usr/include/ksysguard/systemstats/SensorObject.h
/usr/include/ksysguard/systemstats/SensorPlugin.h
/usr/include/ksysguard/systemstats/SensorProperty.h
/usr/include/ksysguard/systemstats/SensorsFeatureSensor.h
/usr/include/ksysguard/systemstats/SysFsSensor.h
/usr/include/ksysguard/systemstats/SysctlSensor.h
/usr/include/ksysguard/systemstats/org.kde.ksystemstats1.h
/usr/include/ksysguard/systemstats/systemstats_export.h
/usr/lib64/cmake/KSysGuard/KSysGuardConfig.cmake
/usr/lib64/cmake/KSysGuard/KSysGuardConfigVersion.cmake
/usr/lib64/cmake/KSysGuard/KSysGuardLibraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KSysGuard/KSysGuardLibraryTargets.cmake
/usr/lib64/libKSysGuardFormatter.so
/usr/lib64/libKSysGuardSensorFaces.so
/usr/lib64/libKSysGuardSensors.so
/usr/lib64/libKSysGuardSystemStats.so
/usr/lib64/libprocesscore.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKSysGuardFormatter.so.6.0.0
/V3/usr/lib64/libKSysGuardSensorFaces.so.6.0.0
/V3/usr/lib64/libKSysGuardSensors.so.6.0.0
/V3/usr/lib64/libKSysGuardSystemStats.so.6.0.0
/V3/usr/lib64/libprocesscore.so.6.0.0
/V3/usr/lib64/qt6/plugins/kf6/packagestructure/ksysguard_sensorface.so
/V3/usr/lib64/qt6/plugins/ksysguard/process/ksysguard_plugin_network.so
/V3/usr/lib64/qt6/plugins/ksysguard/process/ksysguard_plugin_nvidia.so
/V3/usr/lib64/qt6/qml/org/kde/ksysguard/faces/libFacesPlugin.so
/V3/usr/lib64/qt6/qml/org/kde/ksysguard/formatter/libFormatterPlugin.so
/V3/usr/lib64/qt6/qml/org/kde/ksysguard/process/libProcessPlugin.so
/V3/usr/lib64/qt6/qml/org/kde/ksysguard/sensors/libSensorsPlugin.so
/usr/lib64/libKSysGuardFormatter.so.2
/usr/lib64/libKSysGuardFormatter.so.6.0.0
/usr/lib64/libKSysGuardSensorFaces.so.2
/usr/lib64/libKSysGuardSensorFaces.so.6.0.0
/usr/lib64/libKSysGuardSensors.so.2
/usr/lib64/libKSysGuardSensors.so.6.0.0
/usr/lib64/libKSysGuardSystemStats.so.2
/usr/lib64/libKSysGuardSystemStats.so.6.0.0
/usr/lib64/libprocesscore.so.10
/usr/lib64/libprocesscore.so.6.0.0
/usr/lib64/qt6/plugins/kf6/packagestructure/ksysguard_sensorface.so
/usr/lib64/qt6/plugins/ksysguard/process/ksysguard_plugin_network.so
/usr/lib64/qt6/plugins/ksysguard/process/ksysguard_plugin_nvidia.so
/usr/lib64/qt6/qml/org/kde/ksysguard/faces/libFacesPlugin.so
/usr/lib64/qt6/qml/org/kde/ksysguard/formatter/libFormatterPlugin.so
/usr/lib64/qt6/qml/org/kde/ksysguard/process/libProcessPlugin.so
/usr/lib64/qt6/qml/org/kde/ksysguard/sensors/libSensorsPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksysguard/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/libksysguard/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/libksysguard/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/libksysguard/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/libksysguard/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libksysguard/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/libksysguard/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/libksysguard/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/libksysguard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libksysguard/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/libksysguard/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f KSysGuardSensorFaces.lang -f ksgrd.lang -f ksysguard_face_org.kde.ksysguard.barchart.lang -f ksysguard_face_org.kde.ksysguard.colorgrid.lang -f ksysguard_face_org.kde.ksysguard.facegrid.lang -f ksysguard_face_org.kde.ksysguard.linechart.lang -f ksysguard_face_org.kde.ksysguard.piechart.lang -f ksysguard_face_org.kde.ksysguard.textonly.lang -f ksysguard_sensors.lang -f ksysguardlsofwidgets.lang -f processcore.lang -f processui.lang -f KSysGuardFormatter.lang -f ksysguard_face_org.kde.ksysguard.horizontalbars.lang
%defattr(-,root,root,-)

