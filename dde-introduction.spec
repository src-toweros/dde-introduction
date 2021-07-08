Name:           dde-introduction
Version:        5.6.0.7
Release:        1
Summary:        Introduction for UOS
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: qt5-devel

BuildRequires: dtkcore-devel dtkwidget-devel
BuildRequires: pkgconfig(dframeworkdbus)
#BuildRequires: pkgconfig(libdmr)
BuildRequires: pkgconfig(gsettings-qt)

#BuildRequires: ffmpegthumbnailer-devel

BuildRequires: deepin-desktop-server
Requires:      deepin-desktop-server

%description
When you log into the system for the first time, a welcome program will automatically start.
Watch the introduction video to get new features, customize your desktop, enable the window
effect and know more about UnionTech OS.

%prep
%autosetup

# disable dmr lib
sed -i 's/contains(TARGET_ARCH, x86_64)/contains(TARGET_ARCH, mips)/' introduction.pro

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../ VERSION=%{version}  DEFINES+="VERSION=%{version}"
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"
# bugfix#50424
pushd %{buildroot}%{_datadir}/dde-introduction
ln -svf server.mp4 demo.mp4
popd

%files
%doc CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/

%changelog
* Fri Oct 23 2020 panchenbo <panchenbo@uniontech.com> - 5.6.0.7-1
- update to 5.6.0.7

* Thu Oct 15 2020 weidong <weidong@openeuler.org> - 5.5.6.1-4
- Fix compilation errors

* Thu Oct 15 2020 weidong <weidong@openeuler.org> - 5.5.6.1-3
- Fix compilation errors

* Thu Oct 15 2020 weidong <weidong@openeuler.org> - 5.5.6.1-2
- add buildrequires

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.5.6.1-1
- Package init
