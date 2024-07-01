#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0x2A3F414E736060BA (djm@mindrot.org)
#
Name     : openssh
Version  : 9.8p1
Release  : 121
URL      : https://openbsd.cs.toronto.edu/pub/OpenBSD/OpenSSH/portable/openssh-9.8p1.tar.gz
Source0  : https://openbsd.cs.toronto.edu/pub/OpenBSD/OpenSSH/portable/openssh-9.8p1.tar.gz
Source1  : openssh.tmpfiles
Source2  : sshd-keygen.service
Source3  : sshd.service
Source4  : sshd.socket
Source5  : sshd@.service
Source6  : https://openbsd.cs.toronto.edu/pub/OpenBSD/OpenSSH/portable/openssh-9.8p1.tar.gz.asc
Source7  : 2A3F414E736060BA.pkey
Summary  : The OpenSSH implementation of SSH protocol version 2.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause Beerware ISC MIT Public-Domain
Requires: openssh-bin = %{version}-%{release}
Requires: openssh-config = %{version}-%{release}
Requires: openssh-data = %{version}-%{release}
Requires: openssh-libexec = %{version}-%{release}
Requires: openssh-license = %{version}-%{release}
Requires: openssh-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : groff
BuildRequires : krb5-dev
BuildRequires : libcap-dev
BuildRequires : libfido2
BuildRequires : libfido2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Make-SSH-stateless.patch
Patch2: 0002-Stateless-moduli.patch
Patch3: 0003-Increase-ECDSA-default-length-to-521.patch
Patch4: 0004-Default-default-secure-ciphers.patch
Patch5: 0005-Always-use-PAM-by-default.patch
Patch6: 0006-Set-default-server-keep-alive.patch
Patch7: 0007-Make-OpenSSH-print-a-MOTD-file-in-usr-share-defaults.patch
Patch8: default-revert-scp.patch
Patch9: statelessconfig.patch

%description
SSH (Secure SHell) is a program for logging into and executing
commands on a remote machine. SSH is intended to replace rlogin and
rsh, and to provide secure encrypted communications between two
untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's version of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to separate libraries.

This package includes the core files necessary for both the OpenSSH
client and server. To make this package useful, you should also
install openssh-clients, openssh-server, or both.

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
Requires: openssh-license = %{version}-%{release}
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
Requires: openssh-license = %{version}-%{release}

%description libexec
libexec components for the openssh package.


%package license
Summary: license components for the openssh package.
Group: Default

%description license
license components for the openssh package.


%package man
Summary: man components for the openssh package.
Group: Default

%description man
man components for the openssh package.


%package services
Summary: services components for the openssh package.
Group: Systemd services
Requires: systemd

%description services
services components for the openssh package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE7}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE6} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2A3F414E736060BA' gpg.status
%setup -q -n openssh-9.8p1
cd %{_builddir}/openssh-9.8p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
pushd ..
cp -a openssh-9.8p1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719844670
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --with-ssl-engine \
--with-pam \
--sysconfdir=/etc/ssh \
--with-xauth=/usr/bin/xauth \
--without-ssh1 \
--disable-strip \
--disable-lastlog \
--with-kerberos5
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --with-ssl-engine \
--with-pam \
--sysconfdir=/etc/ssh \
--with-xauth=/usr/bin/xauth \
--without-ssh1 \
--disable-strip \
--disable-lastlog \
--with-kerberos5
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719844670
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openssh
cp %{_builddir}/openssh-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/openssh/0121ac714539ad1d1acc30625cbdacc74639241b || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
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
mkdir -p %{buildroot}/usr/share/defaults/ssh/
cp sshd_config ssh_config %{buildroot}/usr/share/defaults/ssh/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sockets.target.wants/sshd.socket

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/scp
/V3/usr/bin/sftp
/V3/usr/bin/ssh
/V3/usr/bin/ssh-add
/V3/usr/bin/ssh-agent
/V3/usr/bin/ssh-keygen
/V3/usr/bin/ssh-keyscan
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
/usr/share/defaults/ssh/ssh_config
/usr/share/defaults/ssh/sshd_config

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/openssh/*

%files extras-server
%defattr(-,root,root,-)
/V3/usr/bin/sshd
/V3/usr/libexec/sftp-server
/usr/bin/sshd
/usr/lib/systemd/system/sshd-keygen.service
/usr/lib/systemd/system/sshd.service
/usr/lib/systemd/system/sshd.socket
/usr/lib/systemd/system/sshd@.service
/usr/libexec/sftp-server

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/ssh-pkcs11-helper
/V3/usr/libexec/ssh-sk-helper
/V3/usr/libexec/sshd-session
/usr/libexec/ssh-keysign
/usr/libexec/ssh-pkcs11-helper
/usr/libexec/ssh-sk-helper
/usr/libexec/sshd-session

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openssh/0121ac714539ad1d1acc30625cbdacc74639241b

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
