# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-rerunfailures
%global pypi_name pytest_rerunfailures

%bcond tests 1

Name:           python-%{srcname}
Version:        16.1
Release:        %autorelease
Summary:        Re-run flaky pytest failures
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-rerunfailures
VCS:            git:https://github.com/pytest-dev/pytest-rerunfailures.git
#!RemoteAsset:  sha256:c38b266db8a808953ebd71ac25c381cb1981a78ff9340a14bcb9f1b9bff1899e
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pytest_rerunfailures

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools) >= 40
%if %{with tests}
BuildRequires:  python3dist(packaging) >= 17.1
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(pytest) >= 7.4
BuildRequires:  python3dist(pytest-xdist)
%endif

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
pytest-rerunfailures is a pytest plugin that re-runs failed tests to reduce
noise from flaky failures.

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitelib}${PYTHONPATH:+:$PYTHONPATH}
%pytest -v tests
%endif

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGES.rst

%changelog
%{?autochangelog}
