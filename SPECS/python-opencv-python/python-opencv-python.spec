# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global opencv_version 4.13.0

Name:           python-opencv-python
Version:        4.13.0.92
Release:        %autorelease
Summary:        Wrapper package for OpenCV Python bindings
License:        Apache-2.0
URL:            https://github.com/opencv/opencv-python
VCS:            git:https://github.com/opencv/opencv-python.git
# Source0: opencv core (cmake source tree)
#!RemoteAsset:  sha256:4621b18558f564915d6ac3bc65df5ddd94d405e00ea85410386eb96d4d279ae4
Source0:        https://github.com/opencv/opencv/archive/%{opencv_version}/opencv-%{opencv_version}.tar.gz
# Source1: opencv-python wrapper (license, version info, tests)
#!RemoteAsset:  sha256:0a3cc22dd1aaeeefcc5ce6045c46c1443da7c7878da7537d6ab188265a94e9b4
Source1:        https://github.com/opencv/opencv-python/archive/refs/tags/92.tar.gz#/opencv-python-92.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release
BuildOption(conf):  -DCMAKE_SKIP_INSTALL_RPATH=ON
BuildOption(conf):  -DENABLE_PRECOMPILED_HEADERS=OFF
# Use system libraries instead of bundled 3rdparty
BuildOption(conf):  -DBUILD_ZLIB=OFF
BuildOption(conf):  -DBUILD_TIFF=OFF
BuildOption(conf):  -DBUILD_OPENJPEG=OFF
BuildOption(conf):  -DBUILD_JASPER=OFF
BuildOption(conf):  -DBUILD_JPEG=OFF
BuildOption(conf):  -DBUILD_PNG=OFF
BuildOption(conf):  -DBUILD_OPENEXR=OFF
BuildOption(conf):  -DBUILD_WEBP=OFF
BuildOption(conf):  -DBUILD_TBB=OFF
BuildOption(conf):  -DBUILD_PROTOBUF=OFF
# Build options
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DBUILD_TESTS=OFF
BuildOption(conf):  -DBUILD_PERF_TESTS=OFF
BuildOption(conf):  -DBUILD_DOCS=OFF
BuildOption(conf):  -DBUILD_EXAMPLES=OFF
BuildOption(conf):  -DBUILD_opencv_apps=OFF
BuildOption(conf):  -DBUILD_JAVA=OFF
BuildOption(conf):  -DOPENCV_GENERATE_PKGCONFIG=OFF
BuildOption(conf):  -DOPENCV_GENERATE_SETUPVARS=OFF
# Library features (matching opencv package)
BuildOption(conf):  -DWITH_EIGEN=ON
BuildOption(conf):  -DWITH_FFMPEG=ON
BuildOption(conf):  -DWITH_GSTREAMER=ON
BuildOption(conf):  -DWITH_GTK=ON
BuildOption(conf):  -DWITH_JASPER=ON
BuildOption(conf):  -DWITH_JPEG=ON
BuildOption(conf):  -DWITH_OPENJPEG=ON
BuildOption(conf):  -DWITH_OPENEXR=ON
BuildOption(conf):  -DWITH_PNG=ON
BuildOption(conf):  -DWITH_TIFF=ON
BuildOption(conf):  -DWITH_WEBP=ON
BuildOption(conf):  -DWITH_TBB=ON
BuildOption(conf):  -DWITH_V4L=ON
BuildOption(conf):  -DWITH_LAPACK=ON
BuildOption(conf):  -DWITH_PROTOBUF=ON
BuildOption(conf):  -DWITH_FLATBUFFERS=ON
BuildOption(conf):  -DWITH_OPENCL=ON
BuildOption(conf):  -DWITH_CUDA=OFF
BuildOption(conf):  -DWITH_VTK=OFF
BuildOption(conf):  -DWITH_IPP=OFF
BuildOption(conf):  -DWITH_HALIDE=OFF
BuildOption(conf):  -DWITH_VULKAN=OFF
BuildOption(conf):  -DWITH_QT=OFF
BuildOption(conf):  -DWITH_OPENGL=OFF
BuildOption(conf):  -DWITH_OPENVINO=OFF
BuildOption(conf):  -DWITH_1394=OFF
BuildOption(conf):  -DWITH_AVIF=OFF
# Enable Python 3 bindings
BuildOption(conf):  -DBUILD_opencv_python2=OFF
BuildOption(conf):  -DBUILD_opencv_python3=ON
# Install Python bindings to the correct arch-dependent path
BuildOption(conf):  -DOPENCV_PYTHON3_INSTALL_PATH=%{python3_sitearch}

BuildRequires:  cmake
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-riff-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  jasper-devel
BuildRequires:  openblas-devel

Requires:       opencv%{?_isa} >= %{opencv_version}
Requires:       python3dist(numpy)

Provides:       python3-opencv-python = %{version}-%{release}
%python_provide python3-opencv-python

%description
Wrapper package for OpenCV Python bindings. This package provides the cv2
module that allows Python applications to use the computer vision and machine
learning functions provided by OpenCV.

# Remove everything except the Python bindings after install
%install -a
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_libdir}/libopencv_*
rm -rf %{buildroot}%{_libdir}/cmake
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_datadir}/opencv4
rm -rf %{buildroot}%{_datadir}/licenses/opencv4

# OpenCV test suite requires test data (opencv_extra repo) and display
# capabilities unavailable inside the OBS build chroot.
%check

%files
%license LICENSE
%{python3_sitearch}/cv2/

%changelog
%autochangelog
