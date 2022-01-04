#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libksysguard
Version  : 5.23.5
Release  : 60
URL      : https://download.kde.org/stable/plasma/5.23.5/libksysguard-5.23.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.5/libksysguard-5.23.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: libksysguard-data = %{version}-%{release}
Requires: libksysguard-lib = %{version}-%{release}
Requires: libksysguard-license = %{version}-%{release}
Requires: libksysguard-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libcap-dev
BuildRequires : libpcap-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-route-3.0)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtsensors-dev
BuildRequires : qtwebchannel-dev
BuildRequires : qtwebengine-dev
BuildRequires : qtx11extras-dev
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
%setup -q -n libksysguard-5.23.5
cd %{_builddir}/libksysguard-5.23.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641328386
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641328386
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksysguard
cp %{_builddir}/libksysguard-5.23.5/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libksysguard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/libksysguard-5.23.5/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/libksysguard-5.23.5/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksysguard/3cb34cfc72e87654683f2894299adf912d14b284
cp %{_builddir}/libksysguard-5.23.5/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/2123756e0b1fc8243547235a33c0fcabfe3b9a51
cp %{_builddir}/libksysguard-5.23.5/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksysguard/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/libksysguard-5.23.5/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/libksysguard-5.23.5/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libksysguard/19d98e1b6f8ef12849ea4012a052d3907f336c91
cp %{_builddir}/libksysguard-5.23.5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/libksysguard-5.23.5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/libksysguard-5.23.5/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/libksysguard-5.23.5/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libksysguard/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang ksgrd
%find_lang ksysguardlsofwidgets
%find_lang processcore
%find_lang processui
%find_lang KSysGuardSensorFaces
%find_lang ksysguard_face_org.kde.ksysguard.barchart
%find_lang ksysguard_face_org.kde.ksysguard.linechart
%find_lang ksysguard_face_org.kde.ksysguard.piechart
%find_lang ksysguard_face_org.kde.ksysguard.textonly
%find_lang ksysguard_plugins_process
%find_lang ksysguard_face_org.kde.ksysguard.facegrid
## install_append content
#mv %{buildroot}/etc/dbus-1/* %{buildroot}/usr/share/dbus-1/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/ksysguardprocesslist_helper
/usr/lib64/libexec/ksysguard/ksgrd_network_helper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.ksystemstats.xml
/usr/share/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
/usr/share/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
/usr/share/knsrcfiles/systemmonitor-faces.knsrc
/usr/share/knsrcfiles/systemmonitor-presets.knsrc
/usr/share/ksysguard/scripts/README
/usr/share/ksysguard/scripts/smaps/helper.js
/usr/share/ksysguard/scripts/smaps/index.html
/usr/share/ksysguard/scripts/smaps/main.js
/usr/share/ksysguard/scripts/smaps/smaps.desktop
/usr/share/ksysguard/scripts/smaps/sorttable.js
/usr/share/ksysguard/scripts/smaps/style.css
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/BarChart.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/metadata.desktop
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.barchart/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/FaceControl.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/FaceGrid.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/metadata.desktop
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.facegrid/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/ui/Bar.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/metadata.desktop
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.horizontalbars/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/contents/ui/LineChart.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/metadata.desktop
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.linechart/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/PieChart.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/contents/ui/UsedTotalDisplay.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/metadata.desktop
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.piechart/metadata.json
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/config/main.xml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/faceproperties
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/CompactRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/Config.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/FullRepresentation.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/contents/ui/GroupedText.qml
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/metadata.desktop
/usr/share/ksysguard/sensorfaces/org.kde.ksysguard.textonly/metadata.json
/usr/share/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
/usr/share/qlogging-categories5/libksysguard.categories

%files dev
%defattr(-,root,root,-)
/usr/include/ksysguard/faces/FaceLoader.h
/usr/include/ksysguard/faces/SensorFaceController.h
/usr/include/ksysguard/faces/SensorFace_p.h
/usr/include/ksysguard/faces/sensorfaces_export.h
/usr/include/ksysguard/formatter/Formatter.h
/usr/include/ksysguard/formatter/Unit.h
/usr/include/ksysguard/formatter/formatter_export.h
/usr/include/ksysguard/ksgrd/SensorAgent.h
/usr/include/ksysguard/ksgrd/SensorClient.h
/usr/include/ksysguard/ksgrd/SensorManager.h
/usr/include/ksysguard/ksgrd/SensorShellAgent.h
/usr/include/ksysguard/ksgrd/SensorSocketAgent.h
/usr/include/ksysguard/ksignalplotter.h
/usr/include/ksysguard/lsof.h
/usr/include/ksysguard/processcore/formatter.h
/usr/include/ksysguard/processcore/process.h
/usr/include/ksysguard/processcore/process_attribute.h
/usr/include/ksysguard/processcore/process_attribute_model.h
/usr/include/ksysguard/processcore/process_controller.h
/usr/include/ksysguard/processcore/process_data_model.h
/usr/include/ksysguard/processcore/process_data_provider.h
/usr/include/ksysguard/processcore/processes.h
/usr/include/ksysguard/processcore/unit.h
/usr/include/ksysguard/processui/KTextEditVT.h
/usr/include/ksysguard/processui/ProcessFilter.h
/usr/include/ksysguard/processui/ProcessModel.h
/usr/include/ksysguard/processui/ksysguardprocesslist.h
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
/usr/include/ksysguard/systemstats/org.kde.ksystemstats.h
/usr/include/ksysguard/systemstats/systemstats_export.h
/usr/lib64/cmake/KF5SysGuard/KF5SysGuardConfig.cmake
/usr/lib64/cmake/KSysGuard/KSysGuardConfig.cmake
/usr/lib64/cmake/KSysGuard/KSysGuardConfigVersion.cmake
/usr/lib64/cmake/KSysGuard/KSysGuardLibraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KSysGuard/KSysGuardLibraryTargets.cmake
/usr/lib64/libKSysGuardFormatter.so
/usr/lib64/libKSysGuardSensorFaces.so
/usr/lib64/libKSysGuardSensors.so
/usr/lib64/libKSysGuardSystemStats.so
/usr/lib64/libksgrd.so
/usr/lib64/libksignalplotter.so
/usr/lib64/liblsofui.so
/usr/lib64/libprocesscore.so
/usr/lib64/libprocessui.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKSysGuardFormatter.so.1
/usr/lib64/libKSysGuardFormatter.so.5.23.5
/usr/lib64/libKSysGuardSensorFaces.so.1
/usr/lib64/libKSysGuardSensorFaces.so.5.23.5
/usr/lib64/libKSysGuardSensors.so.1
/usr/lib64/libKSysGuardSensors.so.5.23.5
/usr/lib64/libKSysGuardSystemStats.so.1
/usr/lib64/libKSysGuardSystemStats.so.5.23.5
/usr/lib64/libksgrd.so.5.23.5
/usr/lib64/libksgrd.so.9
/usr/lib64/libksignalplotter.so.5.23.5
/usr/lib64/libksignalplotter.so.9
/usr/lib64/liblsofui.so.5.23.5
/usr/lib64/liblsofui.so.9
/usr/lib64/libprocesscore.so.5.23.5
/usr/lib64/libprocesscore.so.9
/usr/lib64/libprocessui.so.5.23.5
/usr/lib64/libprocessui.so.9
/usr/lib64/qt5/plugins/designer/ksignalplotter5widgets.so
/usr/lib64/qt5/plugins/designer/ksysguard5widgets.so
/usr/lib64/qt5/plugins/designer/ksysguardlsof5widgets.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/sensorface_packagestructure.so
/usr/lib64/qt5/plugins/ksysguard/process/ksysguard_plugin_network.so
/usr/lib64/qt5/plugins/ksysguard/process/ksysguard_plugin_nvidia.so
/usr/lib64/qt5/qml/org/kde/ksysguard/faces/ExtendedLegend.qml
/usr/lib64/qt5/qml/org/kde/ksysguard/faces/SensorFace.qml
/usr/lib64/qt5/qml/org/kde/ksysguard/faces/SensorRangeSpinBox.qml
/usr/lib64/qt5/qml/org/kde/ksysguard/faces/libFacesPlugin.so
/usr/lib64/qt5/qml/org/kde/ksysguard/faces/qmldir
/usr/lib64/qt5/qml/org/kde/ksysguard/formatter/libFormatterPlugin.so
/usr/lib64/qt5/qml/org/kde/ksysguard/formatter/qmldir
/usr/lib64/qt5/qml/org/kde/ksysguard/process/libProcessPlugin.so
/usr/lib64/qt5/qml/org/kde/ksysguard/process/qmldir
/usr/lib64/qt5/qml/org/kde/ksysguard/sensors/libSensorsPlugin.so
/usr/lib64/qt5/qml/org/kde/ksysguard/sensors/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksysguard/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/libksysguard/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/libksysguard/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/libksysguard/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libksysguard/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/libksysguard/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/libksysguard/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libksysguard/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/libksysguard/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f ksgrd.lang -f ksysguardlsofwidgets.lang -f processcore.lang -f processui.lang -f KSysGuardSensorFaces.lang -f ksysguard_face_org.kde.ksysguard.barchart.lang -f ksysguard_face_org.kde.ksysguard.linechart.lang -f ksysguard_face_org.kde.ksysguard.piechart.lang -f ksysguard_face_org.kde.ksysguard.textonly.lang -f ksysguard_plugins_process.lang -f ksysguard_face_org.kde.ksysguard.facegrid.lang
%defattr(-,root,root,-)

