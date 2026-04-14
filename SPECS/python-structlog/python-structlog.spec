# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname structlog

Name:           python-%{srcname}
Version:        25.5.0
Release:        %autorelease
Summary:        Structured logging for Python
License:        Apache-2.0 OR MIT
URL:            https://github.com/hynek/structlog
VCS:            git:https://github.com/hynek/structlog.git
#!RemoteAsset:  sha256:098522a3bebed9153d4570c6d0288abf80a031dfdb2048d59a49e9dc2190fc98
Source:         https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e %{srcname}.twisted

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
structlog provides structured logging for Python. It wraps loggers with
configurable processors that add context and format output as key-value pairs
or JSON.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE-APACHE
%license LICENSE-MIT
%license NOTICE
%doc README.md

%changelog
%autochangelog
