#!/usr/bin/env bash
# =============================================================================
# WSL2 PulseAudio TCP Bridge Setup
# =============================================================================
# This script configures PulseAudio in WSL2 to connect to a PulseAudio server
# running on the Windows host, enabling microphone & speaker access for
# whisper-real-time.
#
# PREREQUISITES (Windows side):
#   1. Install PulseAudio for Windows:
#      Download from: https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/
#      Or use: https://pgaskin.net/pulseaudio-win32/
#
#   2. Edit the Windows PulseAudio config files:
#
#      In <PulseAudio-install-dir>/etc/pulse/default.pa, ADD these lines:
#        load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;172.16.0.0/12 auth-anonymous=1
#        load-module module-esound-protocol-tcp auth-ip-acl=127.0.0.1;172.16.0.0/12 auth-anonymous=1
#
#      In <PulseAudio-install-dir>/etc/pulse/daemon.conf, SET:
#        exit-idle-time = -1
#
#   3. Allow PulseAudio through Windows Firewall:
#      - Open Windows Defender Firewall → Advanced Settings
#      - Inbound Rules → New Rule → Program
#      - Browse to pulseaudio.exe → Allow the connection
#      - Check Domain, Private, Public → Name it "PulseAudio"
#
#   4. Start PulseAudio on Windows:
#      Run: pulseaudio.exe --use-pid-file=false
#      (from the PulseAudio bin directory)
#
# USAGE:
#   chmod +x setup_wsl2_audio.sh
#   source setup_wsl2_audio.sh
#
# =============================================================================

set -e

# Get the Windows host IP from /etc/resolv.conf
WIN_HOST_IP=$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}')
echo "Windows Host IP: $WIN_HOST_IP"

# Set PulseAudio environment variable to point to Windows host
export PULSE_SERVER=tcp:${WIN_HOST_IP}

# Persist the setting for future shell sessions
if ! grep -q "PULSE_SERVER" ~/.bashrc 2>/dev/null; then
    echo "" >> ~/.bashrc
    echo "# PulseAudio TCP bridge to Windows host (WSL2)" >> ~/.bashrc
    echo "export PULSE_SERVER=tcp:\$(grep -m 1 nameserver /etc/resolv.conf | awk '{print \$2}')" >> ~/.bashrc
    echo "PULSE_SERVER added to ~/.bashrc"
else
    echo "PULSE_SERVER already in ~/.bashrc"
fi

echo ""
echo "=== Testing PulseAudio connection ==="
if pactl info 2>/dev/null | head -5; then
    echo ""
    echo "SUCCESS: PulseAudio connection to Windows host is working!"
    echo ""
    echo "Available audio sources (microphones):"
    pactl list short sources 2>/dev/null || echo "  (none found - check Windows PulseAudio)"
    echo ""
    echo "Available audio sinks (speakers):"
    pactl list short sinks 2>/dev/null || echo "  (none found - check Windows PulseAudio)"
else
    echo ""
    echo "FAILED: Cannot connect to PulseAudio on Windows host ($WIN_HOST_IP)."
    echo ""
    echo "Troubleshooting:"
    echo "  1. Make sure PulseAudio is running on Windows (pulseaudio.exe --use-pid-file=false)"
    echo "  2. Check Windows Firewall allows PulseAudio (TCP port 4713)"
    echo "  3. Verify the config changes in default.pa and daemon.conf"
    echo "  4. Try: pactl -s tcp:${WIN_HOST_IP} info"
fi
