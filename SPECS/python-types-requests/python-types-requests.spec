# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname types-requests
%global pypi_name types_requests

Name:           python-%{srcname}
Version:        2.33.0.20260508
Release:        %autorelease
Summary:        Typing stubs for requests
License:        Apache-2.0
URL:            https://github.com/python/typeshed
#!RemoteAsset:  sha256:81b2ae5f0d20967714a6aa5ef9284c05570d7cb06b7de8f2a77b918b63ddd411
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  requests-stubs

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%check
# This package contains only typing stubs (.pyi files) with no executable code.

%description
Typing stubs for the requests library, providing type annotations for static
type checkers such as mypy, pyright, and pytype.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
