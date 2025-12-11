# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lua-json
Version:        1.3.4
Release:        %autorelease
Summary:        JSON Parser/Constructor for Lua
License:        MIT
URL:            https://github.com/harningt/luajson
#!RemoteAsset
Source:         https://github.com/harningt/luajson/archive/refs/tags/%{version}.tar.gz
Patch:          0001-support-lpeg1.1.0.patch
BuildSystem:    autotools

BuildRequires:  lua-devel

Requires:       lua >= 5.1
Requires:       lua-lpeg >= 0.8.1
BuildArch:      noarch

%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

# No configure
%conf

# TODO: package lunit to enable check
%check

%install
install -d -m 755 %{buildroot}%{lua_pkgdir}
install -p -m 0644 lua/*.lua %{buildroot}%{lua_pkgdir}/

%files
%doc LICENSE docs/LuaJSON.txt docs/ReleaseNotes-1.0.txt
%{lua_pkgdir}/*.lua

%changelog
%{?autochangelog}
