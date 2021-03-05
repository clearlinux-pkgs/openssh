#!/usr/bin/bash

set -euo pipefail

fullver=$(< versions)

if [ -f ChangeLog ] && grep -q "^# OpenSSH $fullver Release Notes:$" ChangeLog; then
  # file already updated
  exit 0
fi

basever=$(cut -d. -f1 <<< "$fullver")
patchver=$(cut -d. -f2 <<< "$fullver")

# p1 patch version release notes (in the modern era) lack the p1 suffix, so
# assume this convention will continue...
if grep -q "p1$" <<< "$patchver"; then
  patchver="${patchver%p1}"
fi
new=$(mktemp)
trap "rm -f $new" EXIT

(
  echo -en "# OpenSSH $fullver Release Notes:\n\n"
  curl -LsSf https://openssh.com/txt/release-"$basever"."$patchver"
  echo ""
  if [ -f ChangeLog ]; then
    cat ChangeLog
  fi
) > "$new"

mv "$new" ChangeLog


# vi: ft=sh et sw=2 sts=2
