%global upstream jsamr
%global gitbase  https://github.com

Summary:  Script to securely create a bootable USB device
Name:     bootiso
Version:  4.2.0
Release:  %mkrel 1
License:  GPLv3
Group:    System/Kernel and hardware
Url:      https://${upstream}.github.io/%{name}
Source0:  %{gitbase}/%{upstream}/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch0:   fix-dep-packages.patch
Patch1:   fix-syslinux-path.patch

BuildArch: noarch

Requires: bc
Requires: binutils
Requires: coreutils
Requires: curl
Requires: findutils
Requires: file
Requires: gawk
Requires: glibc
Requires: grep
Requires: jq
Requires: ncurses
Requires: rsync
Requires: sed
Requires: tar
Requires: util-linux
Requires: wimtools

Provides: bootiso = %{version}-%{release}

%description
A command-line utility aimed at simplifying the task of “burning”
a USB storage device with a bootable disk image.

One can use dd utility for hybrid images, but not all images are hybrid
and the operation is error-prone, especially for amateur UNIX users,
thus its “disk destroyer” nickname.

In addition to offering a safety layer,
bootiso will handle hybrid and non-hybrid SYSLINUX or UEFI
compliant images such as any GNU-Linux,
Windows or rescue live-cds like UltimateBootCD images.

This program also offers additional features,
such as quickly format a USB drive,
inspecting an image file or listing USB-connected drives.

Supported images format are plain disk images (img) and ISO 9660 files.

%prep
%autosetup -p 1 -n %{name}-%{version}

sed -i 's|/usr/local|%{_prefix}|' Makefile

%install
%make_install

%files
%doc changelog.md docs/*
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
