Summary: 	Chinese and Japanese Handwriting Recognition
Name: 		tegaki
Version: 	0.3.1
Release: 	4
License: 	GPLv2+
Group: 		System/Internationalization
Source: 	http://www.tegaki.org/releases/%version/tegaki-python-%version.tar.gz
URL: 		https://www.tegaki.org
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	python-setuptools
BuildArch:	noarch
Requires:	tegaki-engine
Requires:	tegaki-models

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

%prep
%setup -qn tegaki-python-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{py_puresitedir}/tegaki*


%changelog
* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.3.1-3mdv2011.0
+ Revision: 592330
- req models

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.3.1-2mdv2011.0
+ Revision: 592287
- should req on engine

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 592248
- new version 0.3.1

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.1-4mdv2011.0
+ Revision: 592164
- rebuild for python 2.7

* Mon Mar 29 2010 Antoine Ginies <aginies@mandriva.com> 0.1-3mdv2010.1
+ Revision: 528772
- bump release (deps pb : tegaki-l10n[== 0.1])

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.1-2mdv2010.1
+ Revision: 445415
- rebuild

* Sun Feb 15 2009 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.1
+ Revision: 340630
- BR python
- import tegaki


