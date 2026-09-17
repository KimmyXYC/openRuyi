# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spirv-headers
Version:        1.4.357.0
Release:        %autorelease
Summary:        Header files from the SPIR-V registry
License:        MIT
URL:            https://github.com/KhronosGroup/SPIRV-Headers
#!RemoteAsset:  git+https://github.com/KhronosGroup/SPIRV-Headers.git#vulkan-sdk-%{version}
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Header files from the SPIR-V registry.
This includes:
* Header files for various languages.
* JSON files describing the grammar.
* The XML registry file.

%package        devel
Summary:        Development files for %{name}

%description    devel
Development files for %{name}.

%prep -a
chmod a-x include/spirv/1.2/spirv.py

%files devel
%doc README.md
%license LICENSE
%{_includedir}/spirv/
%dir %{_datadir}/cmake/SPIRV-Headers/
%{_datadir}/cmake/SPIRV-Headers/*.cmake
%{_datadir}/pkgconfig/SPIRV-Headers.pc

%changelog
%autochangelog
