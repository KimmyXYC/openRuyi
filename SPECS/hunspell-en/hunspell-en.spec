# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global dict_dirname hunspell

Name:           hunspell-en
Version:        2026.02.25
Release:        %autorelease
Summary:        English hunspell dictionaries
License:        LGPL-2.1-or-later AND LGPL-2.1-only AND BSD-3-Clause-Modification
URL:            http://wordlist.sourceforge.net/
VCS:            git:https://github.com/en-wl/wordlist
#!RemoteAsset:  sha256:74e7cc3e9e03e609c1c74bb7e8862fcd988cdd64768dcbee4611581b7e633852
Source0:        https://github.com/en-wl/wordlist/archive/refs/tags/rel-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  hunspell
BuildRequires:  aspell
BuildRequires:  zip
BuildRequires:  python3
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  make

Provides:       myspell-en = %{version}-%{release}

%description
English (US, UK, etc.) hunspell dictionaries

%prep
%autosetup -n wordlist-rel-2026.02.25

%build
make
cd speller
make hunspell
for i in README_en_CA.txt README_en_US.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

cd speller
cp -p en_*.dic en_*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

cd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

if [ -f en_GB-ise.dic ]; then
    ln -s en_GB-ise.dic en_GB.dic
    ln -s en_GB-ise.aff en_GB.aff
fi

en_GB_aliases="en_AG en_BS en_BW en_BZ en_DK en_GH en_HK en_IE en_IN en_JM en_MW en_NA en_NG en_NZ en_SG en_TT en_ZA en_ZM en_ZW"
for lang in $en_GB_aliases; do
    ln -s en_GB.aff $lang.aff
    ln -s en_GB.dic $lang.dic
done

en_US_aliases="en_PH"
for lang in $en_US_aliases; do
    ln -s en_US.aff $lang.aff
    ln -s en_US.dic $lang.dic
done

%files
%{_datadir}/%{dict_dirname}/*

%changelog
%autochangelog
