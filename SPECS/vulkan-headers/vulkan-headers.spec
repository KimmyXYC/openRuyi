# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vulkan-headers
Version:        1.4.357.0
Release:        %autorelease
Summary:        Vulkan Header files and API registry
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
#!RemoteAsset:  git+https://github.com/KhronosGroup/Vulkan-Headers.git#vulkan-sdk-%{version}
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Vulkan Header files and API registry.

%files
%doc README.md
%license LICENSE.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/
%dir %{_datadir}/cmake/VulkanHeaders/
%{_datadir}/cmake/VulkanHeaders/*.cmake

%changelog
%autochangelog
