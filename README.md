# Whisper Real Time Document

Project whisper-real-time.

## Project description

What can whisper-real-time do for you?

Just as the name suggests, it is a real time offline transcriber with GUI.

## Features

Why choose whisper-real-time?

### 1. Real time:

customise the delay seconds yourself.

### 2. Three modes of transcription:

Record mode, Real Time mode, Live mode.

### 3. Offline totally:

no online API, no privacy issues, no time limits.

## Usage

### 1. The first tab

You could record the audio and transcribe it in the first tab.

![Tab-1](readme/tab-1.webp)

Play: play the audio file selected (or double-click the item in the table).

Delete: delete the audio file selected.

Record: start recording.

Submit: stop recording and transcribe the audio record.

### 2. The second tab

The second tab is the real time zone, it will transcribe your voice continuously.

![Tab-2](readme/tab-2.webp)

Begin: start recording and transcribe automatically.

End: stop recording and transcribe the whole audio record.

### 3. The third tab

In the third tab, you could control the pace of transcription yourself.

![Tab-2](readme/tab-3.webp)

Live: start recording or transcribe the previous part and keep recording.

Continue: give up the previous part and keep recording.

stop: stop recording and give up the transcription.

Finish: stop recording and transcribe the whole audio record.

## Installation

It is built on the base of OpenAI Whisper, so you need to follow the instruction of installing Whisper.

Whisper document: https://github.com/openai/whisper

**Main steps of Installation:**

### 1. Download and install software

Download and install the following software (skip if already installed):

- Python 3.10+: https://www.python.org/downloads/
- FFmpeg: https://ffmpeg.org/download.html

### 2. Install the python packages

Install the python packages automatically:

```shell
pip install -r requirements.txt
```

Or with `uv`:

```shell
uv sync
```

### 3. Run `main.py`

```shell
python main.py
```

## WSL2 Setup (Windows Subsystem for Linux)

To run whisper-real-time in WSL2, audio must be bridged from Windows via PulseAudio over TCP.

### 1. Install PulseAudio on Windows

Download PulseAudio for Windows from: https://pgaskin.net/pulseaudio-win32/

### 2. Configure Windows PulseAudio

In `<PulseAudio-install-dir>/etc/pulse/default.pa`, add:

```
load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;172.16.0.0/12 auth-anonymous=1
load-module module-esound-protocol-tcp auth-ip-acl=127.0.0.1;172.16.0.0/12 auth-anonymous=1
```

In `<PulseAudio-install-dir>/etc/pulse/daemon.conf`, set:

```
exit-idle-time = -1
```

### 3. Allow PulseAudio through Windows Firewall

- Open Windows Defender Firewall → Advanced Settings
- Inbound Rules → New Rule → Program
- Browse to `pulseaudio.exe` → Allow the connection
- Check Domain, Private, Public → Name it "PulseAudio"

### 4. Start PulseAudio on Windows

```
pulseaudio.exe --use-pid-file=false
```

### 5. Set up audio in WSL2

Run the setup script:

```shell
source setup_wsl2_audio.sh
```

Or manually set the environment variable:

```shell
export PULSE_SERVER=tcp:$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}')
```

### 6. Using VB-Audio Virtual Cable (optional)

If you use VB-Audio Virtual Cable to route audio:

1. On Windows, set the **default recording device** (Input) to **"CABLE Output (VB-Audio Virtual Cable)"**
2. Set the **default playback device** (Output) to **"CABLE Input (VB-Audio Virtual Cable)"** (or route your target app's audio to it)
3. Restart the Windows PulseAudio server so it picks up the new default device

### 7. Run in WSL2

```shell
PULSE_SERVER=tcp:<WINDOWS_HOST_IP> uv run python main.py
```

### 8. Test audio recording

Use the included test script to verify the microphone works:

```shell
PULSE_SERVER=tcp:<WINDOWS_HOST_IP> uv run python test_record.py
```

You should see non-zero volume levels if audio is being captured correctly.

## Tips

### 1. First time installation

The process of downloading the Whisper model to your device might take several minutes. Be patient on the first
transcription after installation.

### 2. First transcription task after startup

Loading the Whisper model into RAM takes about ten seconds. Wait until the text box shows words before interacting
with the first transcription task after startup.

### 3. Customization

The default configuration may not suit everyone. Modify the language or model type in `config/constants.py` for
better results.

### 4. Supported Platforms

Developed on Windows. Also works on WSL2 (Ubuntu) with PulseAudio TCP bridge (see setup above).
macOS and native Linux are not yet verified and may have issues.



