Summary: 	Chinese and Japanese Handwriting Recognition
Name: 		tegaki
Version: 	0.3.1
Release: 	%mkrel 3
License: 	GPLv2+
Group: 		System/Internationalization
Source: 	http://www.tegaki.org/releases/%version/tegaki-python-%version.tar.gz
URL: 		http://www.tegaki.org
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
