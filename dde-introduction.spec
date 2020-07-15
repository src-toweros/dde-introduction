# Run tests in check section
# disable for bootstrapping

%bcond_with check


%global debug_package   %{nil}



###dde-introduction-5.5.6.1.orig.tar.xz

Name:           dde-introduction
Version:        5.5.6.1
Release:        1
Summary:        Qt platform theme integration plugins
License:        GPLv3+
Source0:        %{name}-%{version}.orig.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  cmake
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkcore-devel
BuildRequires:  dde-qt-dbus-factory-devel
#BuildRequires:  libdmr-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
#BuildRequires:  ffmpegthumbnailer-devel
#BuildRequires:  ffmpegthumbnailer


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
* Tue May 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.17.0-2
- Fix a security issue

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 3.17.0-1
- Update to 3.17.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.16.0-2
- Rebuilt against fixed atk (#1626575)

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Thu Jan 31 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.12.0-3
- Create deepin-sound-player user

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 3.1.26-1
- Update to 3.1.26
- build error with gobject-introspection 1.58 by gir-generator
  https://github.com/linuxdeepin/developer-center/issues/604

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.1.20-3
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 3.1.20-1
- Update to 3.1.20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.18.1-2
- Remove obsolete scriptlets

* Thu Dec 21 2017 mosquito <sensor.wen@gmail.com> - 3.1.18.1-1
- Update to 3.1.18.1

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 3.1.17-1
- Update to 3.1.17

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 3.1.15-1
- Update to 3.1.15

* Mon Oct 16 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-2
- Fix out of memory on armv7hl

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-1
- Update to 3.1.14

* Sat Aug 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.13-1
- Update to 3.1.13

* Tue Aug  8 2017 mosquito <sensor.wen@gmail.com> - 3.1.11-2
- Rename deepin-api-devel to golang-deepin-api-devel

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 3.1.11-1
- Update to 3.1.11

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.10-1.git79125e7
- Update to 3.1.10

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.7-1.git4c8e030
- Update to 3.1.7

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.2-1.gitf93dbd7
- Update to 3.1.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.16.1-1.gitcfdb295
- Update to 3.0.16.1

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.16-1
- Update to version 3.0.16

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.15-1
- Update to version 3.0.15

* Wed Dec 07 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-2
- Changed compilation procedure

* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-1
- Initial package build