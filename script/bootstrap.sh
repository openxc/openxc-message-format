#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd $DIR/..

# TODO this is kind of a hacky way of determining if root is required -
# ideally we wouuld set up a little virtualenv in the dependencies folder
SUDO_CMD=
if command -v sudo >/dev/null 2>&1; then
    SUDO_CMD="sudo -E"

    echo "The bootstrap script needs to install a few packages to your system as an admin, and we will use the 'sudo' command - enter your password to continue"
    $SUDO_CMD ls > /dev/null
fi

KERNEL=`uname`
if [ ${KERNEL:0:7} == "MINGW32" ]; then
    OS="windows"
elif [ ${KERNEL:0:6} == "CYGWIN" ]; then
    OS="cygwin"
elif [ $KERNEL == "Darwin" ]; then
    OS="mac"
else
    OS="linux"
    if ! command -v lsb_release >/dev/null 2>&1; then
        # Arch Linux
        if command -v pacman>/dev/null 2>&1; then
            $SUDO_CMD pacman -S lsb-release
        fi
    fi

    DISTRO=`lsb_release -si`
fi

die() {
    echo >&2 "${bldred}$@${txtrst}"
    exit 1
}

_cygwin_error() {
    echo
    echo "${bldred}Missing \"$1\"${txtrst} - run the Cygwin installer again and select the base package set:"
    echo "    $CYGWIN_PACKAGES"
    echo "After installing the packages, re-run this bootstrap script."
    die
}

if ! command -v tput >/dev/null 2>&1; then
    if [ $OS == "cygwin" ]; then
        echo "OPTIONAL: Install the \"ncurses\" package in Cygwin to get colored shell output"
    fi
else
    txtrst=$(tput sgr0) # reset
    bldred=${txtbld}$(tput setaf 1)
    bldgreen=${txtbld}$(tput setaf 2)
fi

_pushd() {
    pushd $1 > /dev/null
}

_popd() {
    popd > /dev/null
}

_wait() {
    if [ -z $CI ]; then
        echo "Press Enter when done"
        read
    fi
}

_install() {
    if [ $OS == "cygwin" ]; then
        _cygwin_error $1
    elif [ $OS == "mac" ]; then
        # brew exists with 1 if it's already installed
        set +e
        brew install $1
        set -e
    else
        if [ -z $DISTRO ]; then
            echo
            echo "Missing $1 - install it using your distro's package manager or build from source"
            _wait
        else
            if [ $DISTRO == "arch" ]; then
                $SUDO_CMD pacman -S $1
            elif [ $DISTRO == "Ubuntu" ]; then
                $SUDO_CMD apt-get update -qq
                $SUDO_CMD apt-get install $1 -y
            else
                echo
                echo "Missing $1 - install it using your distro's package manager or build from source"
                _wait
            fi
        fi
    fi
}

CYGWIN_PACKAGES="make curl, libsasl2, ca-certificates, ncurses, python-setuptools"

download() {
    url=$1
    filename=$2
    curl $url -L --O $filename
}

if [ `id -u` == 0 ]; then
    die "Error: running as root - don't use 'sudo' with this script"
fi

if ! command -v curl >/dev/null 2>&1; then
    if [ $OS == "cygwin" ]; then
        _cygwin_error "curl"
    else
        _install curl
    fi
fi

if [ $OS == "windows" ]; then
    die "Sorry, the bootstrap script for compiling from source doesn't support the Windows console - try Cygwin."
fi

if [ $OS == "mac" ] && ! command -v brew >/dev/null 2>&1; then
    echo "Installing Homebrew..."
    ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
fi

if ! command -v make >/dev/null 2>&1; then
    if [ $OS == "cygwin" ]; then
        _cygwin_error "make"
    elif [ $OS == "mac" ]; then
            die "Missing 'make' - install the Xcode CLI tools"
    else
        if [ $DISTRO == "arch" ]; then
            $SUDO_CMD pacman -S base-devel
        elif [ $DISTRO == "Ubuntu" ]; then
            $SUDO_CMD apt-get update -qq
            $SUDO_CMD apt-get install build-essential -y
        fi
    fi
fi

if ! command -v python >/dev/null 2>&1; then
    echo "Installing Python..."
    _install "python"
fi

if ! command -v pip >/dev/null 2>&1; then
    echo "Installing Pip..."
    if ! command -v easy_install >/dev/null 2>&1; then
        die "easy_install not available, can't install pip"
    fi

    $SUDO_CMD easy_install pip
fi

$SUDO_CMD pip install -U pip
$SUDO_CMD pip install --pre -Ur pip-requirements.txt

if ! command -v protoc >/dev/null 2>&1; then
    if [ $OS == "cygwin" ]; then
        _cygwin_error "protobuf"
    elif [ $OS == "mac" ] || [ $OS == "linux" ]; then
        if [ $DISTRO == "Ubuntu" ]; then
            _install protobuf-compiler
        else
            _install protobuf
        fi
    fi
fi

popd

echo
echo "${bldgreen}All developer dependencies installed, ready to compile.$txtrst"
