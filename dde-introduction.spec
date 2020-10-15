%bcond_with check
%global debug_package   %{nil}
Name:           dde-introduction
Version:        5.5.6.1
Release:        2
Summary:        Qt platform theme integration plugins
License:        GPLv3+
Source0:        %{name}-%{version}.orig.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  cmake
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkcore-devel
BuildRequires:  dde-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libdmr-devel

%description
Qt platform theme integration plugins for DDE
 Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
%autosetup


%build
export PATH=$PATH:/usr/lib64/qt5/bin
mkdir build && cd build
%{_libdir}/qt5/bin/qmake ..
%{__make}

%install
pushd %{_builddir}/%{name}-%{version}/build
%make_install INSTALL_ROOT=%{buildroot}
popd

%files
%{_bindir}/dde-introduction
%{_datadir}/applications/*
%{_datadir}/dde-introduction/*
%{_datadir}/icons/*


%changelog
* Thu Oct 15 2020 weidong <weidong@openeuler.org> - 5.5.6.1-2
- add buildrequires

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.5.6.1-1
- Package init
