<!--
SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
SPDX-FileContributor: lzyprime <2383518170@qq.com>

SPDX-License-Identifier: MulanPSL-2.0
-->

## 检查项

- 检查 spec 文件, Release 标签上需要有 `%autorelease`
- source 里像 url 的链接上面需要有 `#!RemoteAssert`

## 流程图

```mermaid
---
config:
  layout: elk
---
flowchart TD
    n1(["pull_request 请求"]) --> n2["拉取仓库和pr分支"] --> n3[解析涉及的变动文件列表]
    n3 -- "changed-files.txt 变动文件列表" --> n4["检查变动列表记录的.spec文件规范性"]
    n4 --> n5(["end"])

```
