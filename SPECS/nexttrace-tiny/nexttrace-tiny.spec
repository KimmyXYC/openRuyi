# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Go -trimpath removes filesystem source paths, leaving no files for an
# automatically generated debugsource subpackage.
%undefine _debugsource_packages

%define _name           nexttrace-tiny
%define go_import_path  github.com/nxtrace/NTrace-core

Name:           nexttrace-tiny
Version:        1.7.1
Release:        %autorelease
Summary:        Lightweight visual route tracing tool
License:        GPL-3.0-only
URL:            https://github.com/nxtrace/NTrace-core
VCS:            git:https://github.com/nxtrace/NTrace-core.git
#!RemoteAsset:  sha256:ac5c3f4181b061b8fff2430e2b34eee165e7a8f41eb694a07ab0b4b219e5a4bb
Source0:        https://github.com/nxtrace/NTrace-core/archive/refs/tags/v%{version}.tar.gz#/NTrace-core-%{version}.tar.gz
# Corresponding source for the WinDivert 2.2.2-A DLL/SYS files in Source0.
#!RemoteAsset:  sha256:300c1b14e08652e0f8647bf06e9b212f924af76cb2459bd0f88da481c9b08336
Source1:        https://github.com/basil00/WinDivert/archive/refs/tags/v2.2.2.tar.gz#/WinDivert-2.2.2.tar.gz
BuildSystem:    golang

BuildOption(build):  -tags flavor_tiny
BuildOption(build):  -ldflags "-X github.com/nxtrace/NTrace-core/config.Version=v1.7.1 -X github.com/nxtrace/NTrace-core/config.BuildDate=2026-06-16T12:29:35Z -X github.com/nxtrace/NTrace-core/config.CommitID=c991982"

# Avoid embedding and shipping Windows-only prebuilt DLL/SYS files on Linux.
Patch2000:      2000-disable-windivert-on-non-windows.patch

BuildRequires:  go >= 1.26.4
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/akamensky/argparse)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/google/gopacket)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/oschwald/maxminddb-golang)
BuildRequires:  go(github.com/rodaine/table)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/syndtr/gocapability)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tsosunchia/powclient)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)

%description
NextTrace is an open source visual route tracing tool. This package builds the
reduced nexttrace-tiny flavor without the full server, MCP, Globalping, MTR,
speed-test, or Nali feature set.

%prep
%autosetup -p1 -n NTrace-core-%{version}
rm -rf assets/windivert/x64 assets/windivert/x86

# Audit that the corresponding WinDivert source archive is intact and licensed.
windivert_source_dir="$(mktemp -d)"
tar -xzf %{SOURCE1} -C "${windivert_source_dir}"
test -f "${windivert_source_dir}/WinDivert-2.2.2/LICENSE"
rm -rf "${windivert_source_dir}"

%go_prep

%check
%go_common
cd %{_builddir}/go/src/%{go_import_path}
go test -tags flavor_tiny . ./cmd ./dn42 ./fast_trace ./ipgeo ./pow ./printer ./reporter ./trace/... ./tracelog ./tracemap ./util ./wshandle

%files
%{_bindir}/%{_name}
%license LICENSE
%doc README.md

%changelog
%autochangelog
