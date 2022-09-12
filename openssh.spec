#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2A3F414E736060BA (djm@mindrot.org)
#
Name     : openssh
Version  : 9.0p1
Release  : 90
URL      : https://openbsd.cs.toronto.edu/pub/OpenBSD/OpenSSH/portable/openssh-9.0p1.tar.gz
Source0  : https://openbsd.cs.toronto.edu/pub/OpenBSD/OpenSSH/portable/openssh-9.0p1.tar.gz
Source1  : openssh.tmpfiles
Source2  : sshd-keygen.service
Source3  : sshd.service
Source4  : sshd.socket
Source5  : sshd@.service
Source6  : https://openbsd.cs.toronto.edu/pub/OpenBSD/OpenSSH/portable/openssh-9.0p1.tar.gz.asc
Summary  : The OpenSSH implementation of SSH protocol version 2.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause Beerware ISC MIT Public-Domain
Requires: openssh-bin = %{version}-%{release}
Requires: openssh-config = %{version}-%{release}
Requires: openssh-data = %{version}-%{release}
Requires: openssh-libexec = %{version}-%{release}
Requires: openssh-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : groff
BuildRequires : libcap-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
Patch1: 0001-Make-SSH-stateless.patch
Patch2: 0002-Stateless-moduli.patch
Patch3: 0003-Increase-ECDSA-default-length-to-521.patch
Patch4: 0004-Default-default-secure-ciphers.patch
Patch5: 0005-Always-use-PAM-by-default.patch
Patch6: 0006-Set-default-server-keep-alive.patch
Patch7: 0007-Make-OpenSSH-print-a-MOTD-file-in-usr-share-defaults.patch
Patch8: default-revert-scp.patch

%description
Ssh (Secure Shell) is a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing it
up to date in terms of security and features, as well as removing all
patented algorithms to separate libraries (OpenSSL).

This package includes all files necessary for both the OpenSSH
client and server.

%package autostart
Summary: autostart components for the openssh package.
Group: Default

%description autostart
autostart components for the openssh package.


%package bin
Summary: bin components for the openssh package.
Group: Binaries
Requires: openssh-data = %{version}-%{release}
Requires: openssh-libexec = %{version}-%{release}
Requires: openssh-config = %{version}-%{release}
Requires: openssh-services = %{version}-%{release}

%description bin
bin components for the openssh package.


%package config
Summary: config components for the openssh package.
Group: Default

%description config
config components for the openssh package.


%package data
Summary: data components for the openssh package.
Group: Data

%description data
data components for the openssh package.


%package doc
Summary: doc components for the openssh package.
Group: Documentation
Requires: openssh-man = %{version}-%{release}

%description doc
doc components for the openssh package.


%package extras-server
Summary: extras-server components for the openssh package.
Group: Default
Requires: openssh-autostart = %{version}-%{release}
Requires: openssh-services = %{version}-%{release}

%description extras-server
extras-server components for the openssh package.


%package libexec
Summary: libexec components for the openssh package.
Group: Default
Requires: openssh-config = %{version}-%{release}

%description libexec
libexec components for the openssh package.


%package man
Summary: man components for the openssh package.
Group: Default

%description man
man components for the openssh package.


%package services
Summary: services components for the openssh package.
Group: Systemd services

%description services
services components for the openssh package.


%prep
%setup -q -n openssh-9.0p1
cd %{_builddir}/openssh-9.0p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663022857
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --with-ssl-engine \
--with-pam \
--sysconfdir=/etc/ssh \
--with-xauth=/usr/bin/xauth \
--without-ssh1 \
--disable-strip \
--disable-lastlog
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1663022857
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/sshd-keygen.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/sshd.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/sshd.socket
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/sshd@.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/openssh.conf
## Remove excluded files
rm -f %{buildroot}*/etc/systemd/system/multi-user.target.wants/sshd.service
rm -f %{buildroot}*/etc/ssh/ssh_config
rm -f %{buildroot}*/etc/ssh/sshd_config
## install_append content
mkdir -p %{buildroot}%{_datadir}/defaults/ssh/
mv %{buildroot}%{_sysconfdir}/ssh/moduli %{buildroot}%{_datadir}/defaults/ssh/
mkdir -p %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../sshd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/sshd.socket
mkdir -p %{buildroot}/usr/bin
cp contrib/ssh-copy-id %{buildroot}/usr/bin/
chmod +x %{buildroot}/usr/bin/ssh-copy-id
mkdir -p %{buildroot}/usr/share/man/man1/
cp contrib/ssh-copy-id.1 %{buildroot}/usr/share/man/man1/
mkdir -p %{buildroot}/usr/share/doc/openssh/
cp sshd_config ssh_config %{buildroot}/usr/share/doc/openssh/
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sockets.target.wants/sshd.socket

%files bin
%defattr(-,root,root,-)
/usr/bin/scp
/usr/bin/sftp
/usr/bin/ssh
/usr/bin/ssh-add
/usr/bin/ssh-agent
/usr/bin/ssh-copy-id
/usr/bin/ssh-keygen
/usr/bin/ssh-keyscan

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/openssh.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ssh/moduli

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/openssh/*

%files extras-server
%defattr(-,root,root,-)
/usr/bin/sshd
/usr/lib/systemd/system/sshd-keygen.service
/usr/lib/systemd/system/sshd.service
/usr/lib/systemd/system/sshd.socket
/usr/lib/systemd/system/sshd@.service
/usr/libexec/sftp-server

%files libexec
%defattr(-,root,root,-)
/usr/libexec/ssh-keysign
/usr/libexec/ssh-pkcs11-helper
/usr/libexec/ssh-sk-helper

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/scp.1
/usr/share/man/man1/sftp.1
/usr/share/man/man1/ssh-add.1
/usr/share/man/man1/ssh-agent.1
/usr/share/man/man1/ssh-copy-id.1
/usr/share/man/man1/ssh-keygen.1
/usr/share/man/man1/ssh-keyscan.1
/usr/share/man/man1/ssh.1
/usr/share/man/man5/moduli.5
/usr/share/man/man5/ssh_config.5
/usr/share/man/man5/sshd_config.5
/usr/share/man/man8/sftp-server.8
/usr/share/man/man8/ssh-keysign.8
/usr/share/man/man8/ssh-pkcs11-helper.8
/usr/share/man/man8/ssh-sk-helper.8
/usr/share/man/man8/sshd.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sockets.target.wants/sshd.socket
