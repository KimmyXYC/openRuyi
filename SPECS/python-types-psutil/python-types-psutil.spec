# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname types-psutil
%global pypi_name types_psutil

Name:           python-%{srcname}
Version:        7.2.2.20260508
Release:        %autorelease
Summary:        Typing stubs for psutil
License:        Apache-2.0
URL:            https://github.com/python/typeshed
#!RemoteAsset:  sha256:8cfd8339f5e898570f80486423e65d87558d89d0181bf723d20ac5e778fe218e
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  psutil-stubs

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Typeshed contains external type annotations for the Python standard library and Python builtins, as well as third-party packages that are contributed by people external to those projects.

%check
# This is a type stubs package, there are no runtime modules to import and check.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
