#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openssh
Version  : 7.1p1
Release  : 29
URL      : http://ftp3.usa.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-7.1p1.tar.gz
Source0  : http://ftp3.usa.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-7.1p1.tar.gz
Source1  : openssh.tmpfiles
Source2  : sshd-keygen.service
Source3  : sshd.service
Source4  : sshd.socket
Source5  : sshd@.service
Summary  : The OpenSSH implementation of SSH protocol versions 1 and 2.
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: openssh-bin
Requires: openssh-config
Requires: openssh-data
Requires: openssh-doc
BuildRequires : Linux-PAM-dev
BuildRequires : groff
BuildRequires : libcap-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
Patch1: stateless.patch
Patch2: moduli-lookup.patch
Patch3: ciphers.patch
Patch4: default-ciphers-configuration.patch

%description
Ssh (Secure Shell) is a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing it
up to date in terms of security and features, as well as removing all
patented algorithms to seperate libraries (OpenSSL).

This package includes all files necessary for both the OpenSSH
client and server.

%package bin
Summary: bin components for the openssh package.
Group: Binaries
Requires: openssh-data
Requires: openssh-config

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

%description doc
doc components for the openssh package.


%package extras
Summary: extras components for the openssh package.
Group: Default

%description extras
extras components for the openssh package.


%prep
%setup -q -n openssh-7.1p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure --disable-static --with-ssl-engine --with-pam  --sysconfdir=/etc/ssh --with-xauth=/usr/bin/xauth --without-ssh1 --disable-strip
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/sshd-keygen.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/sshd.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/sshd.socket
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/sshd@.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/openssh.conf
## make_install_append content
mkdir -p %{buildroot}%{_datadir}/defaults/ssh/
mv %{buildroot}%{_sysconfdir}/ssh/moduli %{buildroot}%{_datadir}/defaults/ssh/
mkdir -p %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../sshd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/sshd.socket
mkdir -p %{buildroot}/usr/bin
cp contrib/ssh-copy-id %{buildroot}/usr/bin/
chmod +x %{buildroot}/usr/bin/ssh-copy-id
mkdir -p %{buildroot}/usr/share/man/man1/
cp contrib/ssh-copy-id.1 %{buildroot}/usr/share/man/man1/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/sshd
%exclude /usr/libexec/sftp-server
/usr/bin/scp
/usr/bin/sftp
/usr/bin/slogin
/usr/bin/ssh
/usr/bin/ssh-add
/usr/bin/ssh-agent
/usr/bin/ssh-copy-id
/usr/bin/ssh-keygen
/usr/bin/ssh-keyscan
/usr/libexec/ssh-keysign
/usr/libexec/ssh-pkcs11-helper

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sockets.target.wants/sshd.socket
%exclude /usr/lib/systemd/system/sshd-keygen.service
%exclude /usr/lib/systemd/system/sshd.service
%exclude /usr/lib/systemd/system/sshd.socket
%exclude /usr/lib/systemd/system/sshd@.service
/usr/lib/tmpfiles.d/openssh.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ssh/moduli

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/bin/sshd
/usr/lib/systemd/system/sockets.target.wants/sshd.socket
/usr/lib/systemd/system/sshd-keygen.service
/usr/lib/systemd/system/sshd.service
/usr/lib/systemd/system/sshd.socket
/usr/lib/systemd/system/sshd@.service
/usr/libexec/sftp-server
