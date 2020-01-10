Name:           libkscreen
Epoch:          1
Version:        1.0.1
Release:        8%{?dist}
Summary:        Display configuration library

License:        GPLv2+
URL:            https://projects.kde.org/projects/playground/libs/libkscreen

Source0:        http://download.kde.org/stable/libkscreen/libkscreen-%{version}.tar.bz2

Patch0:         libkscreen-bz#1056251-check-max-active-screens-count.patch
Patch1:         libkscreen-bz#1082654-crash-when-disabling-output.patch
Patch2:         libkscreen-bz#1361220-do-not-crash-on-empty-config.patch
Patch3:         libkscreen-bz#1267281-do-not-crash-when-changing-resolution.patch

BuildRequires:  kdelibs4-devel
BuildRequires:  libXrandr-devel
BuildRequires:  qjson-devel >= 0.8.1

%description
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%patch0 -p1 -b .bz1056251
%patch1 -p1 -b .bz1082654
%patch2 -p1 -b .bz1361220
%patch3 -p1 -b .bz#1267281

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING
%{_kde4_libdir}/libkscreen.so.*
%{_kde4_libdir}/kde4/plugins/kscreen/

%files devel
%{_includedir}/kscreen/
%{_kde4_libdir}/libkscreen.so
%{_kde4_libdir}/cmake/LibKScreen/
%{_kde4_libdir}/pkgconfig/kscreen.pc


%changelog
* Mon Sep 11 2017 Jan Grulich <jgrulich@redhat.com> - 1:1.0.1-8
- Fix crash when changing resolution
  Resolves: bz#1267281

* Mon Sep 11 2017 Jan Grulich <jgrulich@redhat.com> - 1:1.0.1-7
- Fix crash when trying to apply empty configuration
  Resolves: bz#1361220

* Tue Apr 01 2014 Daniel Vrátil <dvratil@redhat.com> - 1:1.0.1-5
- Fix crash when disabling output (resolves #1082654)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1:1.0.1-5
- Mass rebuild 2014-01-24

* Thu Jan 23 2014 Daniel Vrátil <dvratil@redhat.com> - 1:1.0.1-4
- Backport patch for RHBZ#1056251 from upstream

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:1.0.1-3
- Mass rebuild 2013-12-27

* Fri Aug 09 2013 Dan Vrátil <dvratil@redhat.com> - 1:1.0.1-2
 - fix Source0 URL

* Thu Aug 01 2013 Dan Vrátil <dvratil@redhat.com> - 1:1.0.1-1
 - libkscreen 1.0.1

* Mon Jun 17 2013 Dan Vrátil <dvratil@redhat.com> - 1:1.0-1
 - libkscreen 1.0

* Thu May 02 2013 Dan Vrátil <dvratil@redhat.com> - 1:0.0.92-1
 - libkscreen 0.0.92

* Tue Apr 23 2013 Dan Vrátil <dvratil@redhat.com> - 1:0.0.82.git20130423-1
 - dev git build

* Wed Mar 27 2013 Dan Vrátil <dvratil@redhat.com> - 1:0.0.81-1
 - libkscreen 0.0.81

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-2
 - fix dependency of libkscreen-devel

* Sun Jan 20 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-1
 - update to 0.0.71 - first official release
 - remove kscreen-console, it's now shipped in kscreen package

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-2.20121228git
- remove redundant BR's
- BR: qjson-devel >= 0.8.1
- fix dir ownership

* Fri Dec 28 2012 Dan Vrátil <dvratil@redhat.com> 0.9.0-1.20121228git
 - Fixed versioning
 - Added instructions how to retrieve sources
 - Fixed URL
 - Removed 'rm -rf $RPM_BUILD_ROOT'

* Wed Dec 26 2012 Dan Vrátil <dvratil@redhat.com> 20121226gitecc8d1a-1
 - Initial SPEC
