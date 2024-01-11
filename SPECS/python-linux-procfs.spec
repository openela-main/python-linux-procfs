Name: python-linux-procfs
Version: 0.7.1
Release: 1%{?dist}
License: GPLv2
Summary: Linux /proc abstraction classes
Group: System Environment/Libraries
URL: https://git.kernel.org/pub/scm/libs/python/%{name}/%{name}.git
Source: https://www.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%global _description\
Abstractions to extract information from the Linux kernel /proc files.

# PATCHES

%description %_description

%package -n python3-linux-procfs
Summary: %summary
%{?python_provide:%python_provide python3-linux-procfs}

Requires: python3-six

%description -n python3-linux-procfs %_description

%prep
%autosetup -p1

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files -n python3-linux-procfs
%defattr(0755,root,root,0755)
%{_bindir}/pflags
%{python3_sitelib}/procfs/
%defattr(0644,root,root,0755)
%{python3_sitelib}/python_linux_procfs*.egg-info
%license COPYING

%changelog
* Fri Nov 18 2022 John Kacur <jkacur@redhat.com> - 0.7.1-1
- Rebase to upstream version python-linux-procfs-0.7.1
Resolves: rhbz#2121522

* Tue Jan 11 2022 John Kacur <jkacur@redhat.com> - 0.7.0-1
- Rebase to upstream version python-linux-procfs-0.7.0
Resolves: rhbz#2031158

* Thu Dec 09 2021 John Kacur <jkacur@redhat.com> - 0.6.3-4
- various clean-ups including using 'with' context managers in try-except
- Fix to ignore UnicodeDecodeError when it occurs
Resolves: rhbz#2016204

* Tue Nov 23 2021 John Kacur <jkacur@redhat.com> - 0.6.3-3
- Propagate error to user if pid completed
- Handle pid completed in pflags
Resolves: rhbz#1820709

* Fri Nov 19 2021 John Kacur <jkacur@redhat.com> - 0.6.3-2
- Fix traceback with non-utf8 chars
Resolves: rhbz#2016204

* Tue Jan 12 2021 John Kacur <jkacur@redhat.com> - 0.6.3-1
- Rebase to latest upstream
- Correct URL and Source
- Simplify specfile
Resolves: rhbz#1890557

* Wed Jun 24 2020 John Kacur <jkacur@redhat.com> - 0.6.2-2
Resolves: rhbz#1850391

* Mon Jun 22 2020 John Kacur <jkacur@redhat.com> - 0.6.2-1
- Add bitmasklist_test
- Clean-ups including using a more modern python spacing, tabbing, etc
- Fix to parse number of cpus correctly on s390(x)
Resolves: rhbz#1849215

* Wed Apr 03 2019 Clark Williams <williams@redhat.com> - 0.6-7
- OSCI gating framework added
Resolves: rhbz#1682424

* Mon Jan 28 2019 John Kacur <jkacur@redhat.com> - 0.6-6
- fix refreshing the cache
- fix removing vanished processes in pidstats
Resolves: rhbz#1669294

* Fri Nov 30 2018 John Kacur <jkacur@redhat.com> - 0.6-5
- pflags - Ignore non-existent pids or process names
Resolves: rhbz#1654312

* Wed Nov 28 2018 John Kacur <jkacur@redhat.com> - 0.6-4
- Use argparse to create a help option
Resolves: rhbz#1650159

* Tue Oct 16 2018 John Kacur <jkacur@redhat.com> - 0.6-3
- python3 doesn't supply "reduce" by default, so import it
Resolves: rhbz#1639430

* Mon Aug 13 2018 John Kacur <jkacur@redhat.com> - 0.6-2
- Obsoltes python-linux-procfs (just build the python3 version)
Resolves: rhbz#1589042

* Fri Aug 10 2018 John Kacur <jkacur@redhat.com> - 0.6-1
- Sync with upstream source
Resolves: rhbz#1614869

* Wed Aug 8 2018 John Kacur <jkacur@redhat.com> - 0.5.1-7
- Add some functions related to affinity from tuna
Resolves: rhbz#1522868

* Tue Jun 26 2018 John Kacur <jkacur@redhat.com> - 0.5.1-6
- Fix upstream URL reference and source
Resolves: rhbz#1589938

* Thu May 31 2018 John Kacur <jkacur@redhat.com> - 0.5.1-5
- Build only the python3 subpackage (needs to be done in rhel-8.0 too)
Resolves: rhbz#1567234

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Nov 21 2017 Jiri Kastner <jkastner@redhat.com> - 0.5.1-2
- missing defattr for _bindir

* Tue Nov 21 2017 Jiri Kastner <jkastner@redhat.com> - 0.5.1-1
- missed snippet in specfile for python2 only
- added scripts to setup.py, pflags renamed and added to setup.py

* Mon Nov 20 2017 Jiri Kastner <jkastner@redhat.com> - 0.5-1
- update to 0.5

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.10-4
- Python 2 binary package renamed to python2-linux-procfs
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Jiri Kastner <jkastner@redhat.com> - 0.4.10-1
- update to latest release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 10 2014 Jiri Kastner <jkastner@redhat.com> - 0.4.6-4
- fix source and url

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.6-1
- updated to 0.4.6

* Thu Jun  6 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.5-1
- Added support for parsing cgroups as a per thread attribute

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.4-1
- Even more fixes due to the fedora review process

* Mon Feb  9 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.3-1
- Fixups due to the fedora review process

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.2-1
- interrupts: Add find_by_user_regex
- process: Always set the "cmdline" array, even if empty
- pidstats: Remove dead processes in find_by_name()
- pidstats: Add process class to catch dict references for late parsing
- pidstats: Move the /proc/PID/{stat,status} parsing to classes
- pidstats: Introduce process_flags method

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4-1
- Per process flags needed by tuna

* Fri Jun 13 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.3-1
- Support CPU hotplug

* Mon Feb 25 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-1
- package created
