# *flybers* Universal Live Stream Recorder (Portable)

**Version 1.0 — May 2026**

Drag and drop any streaming URL to watch AND record simultaneously.
Works from any USB drive, any PC, no installation required.

---

## 📌 How to use

1. Double-click `stream.exe` — a black terminal window will open
2. Drag a URL from your browser into the black window
3. Press Enter
4. mpv player opens — watch your stream
5. **To stop watching:** Close the mpv player window
6. **To close the terminal:** Click on the terminal window and press any key

**Recording happens automatically** while mpv is open. Close mpv to save the recording.

---

## 📂 Where recordings go

Recordings are saved inside the tool folder, in a subfolder called `Recordings`:

Your USB, SSD or HDD Drive (any letter)
└── Universal_LiveStream_Recorder_Portable_v1.0
├── stream.exe ← Double-click this to start
├── updater.bat ← Double-click this to update
├── flybers.ico ← Icon file (leave it here)
├── README.md ← This guide
└── Recordings\ ← Your recordings go here
└── stream_2026-05-13_14-23-05.ts


The `Recordings` folder is created automatically the first time you run `stream.exe`.
Works on any PC, any drive letter.

---

## 📺 Important: Adverts & Recording Behaviour

- **Static adverts on some streaming services:** Some services will start with a static advert.
Simply wait 20-30 seconds and the live feed will appear. Later, you can crop that section out
with a simple video editor (https://losslesscut.net/ - is perfect for cropping and converting) 
— cropping will also fix any time/duration display issues in the video file.
- **Non-live (VOD) recordings:** The recording will end automatically when the stream/video ends.
- **Live stream recordings:** The recording may NOT end automatically. To stop a live recording:
  - Click on the black terminal window to select it
  - Hold down the `Ctrl` key and press `C` (`Ctrl+C`)
  - It may take a few seconds to register — be patient

---

## 🔄 How to update (Important!)

Websites change constantly. Keep your tools updated or streams may stop working.

**To update:** Double-click `updater.bat` inside the tool folder.

That's it — it automatically updates everything. Run this every few weeks.

---

## ⚡ Troubleshooting

- **"mpv.exe not found"** → Make sure `stream.exe` is inside the tool folder (where `mpv.exe` lives)
- **403 error / stream won't play** → Close your browser completely, then run `updater.bat` and try again
- **File shows weird duration in Windows** → Normal for `.ts` files. They play fine. Cropping with a video editor will fix the display.
- **mpv takes a long time to open** → If you're using a VPN, try disconnecting it temporarily. VPNs add latency which slows down stream negotiation. First launch after update is also slower.
- **A site doesn't work** → Run `updater.bat` first. If still broken, the site may not be supported yet.

---

## 🌐 What works great

| Site | Status |
|------|--------|
| YouTube | ✅ Perfect |
| Facebook Live | ✅ Works |
| Twitter/X | ✅ Works |
| Vimeo | ✅ Works |
| Educational sites (MIT, Khan Academy, etc.) | ✅ Works |
| Public domain / government streams | ✅ Works |
| And 1,800+ more... | ✅ Most major streaming sites |

If a site works in your browser, it will probably work here.
Run `updater.bat` regularly to keep support for new sites.

---

## ⚖️ Legal & Responsible Use

**Perfectly legal uses include:**
- ✅ Recording **your own live streams** (your content, your rights)
- ✅ Recording **public domain or Creative Commons** content
- ✅ Recording **educational lectures** for personal study
- ✅ Recording **government proceedings or public broadcasts**
- ✅ Recording content where you have **explicit permission** from the creator

**Users are responsible for:**
- Respecting copyright laws in their jurisdiction
- Complying with platform Terms of Service
- Obtaining necessary permissions for non-public content
- Not using recordings for harassment, stalking, or commercial infringement

> **⚠️ USE AT YOUR OWN RISK.** This tool is provided "as is" without warranty.
The creator assumes no liability for how users choose to use it. By using this tool,
you acknowledge that you are solely responsible for your actions.

---

## 🙏 Credits & Thanks

This tool would not exist without these amazing open-source projects:

- **[mpv player](https://mpv.io/)** — The powerful, elegant video player
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — The swiss army knife of video extraction
- **[FFmpeg](https://ffmpeg.org/)** — The backbone of multimedia processing

Huge respect to all their developers and contributors. This tool is simply a
convenient wrapper around their incredible work.

---

## ☕ Support This Project

If you find this tool useful, consider supporting further development.

**[Support on Ko-fi](https://ko-fi.com/flybers)**

(Ko-fi has no fees — your support goes entirely to the creator)

---

## 💡 Tips

- **Run updater.bat every few weeks** — one click keeps everything working
- **Close mpv player** to stop watching and save your recording
- **Click terminal window + any key** to close it after the mpv player is closed
- **The whole folder is portable** — copy to any USB drive and it works on any Windows 64bit PC
- **Keep a backup** — save the entire tool folder somewhere safe
- **Recordings are .ts files** — they play in Windows Media Player, VLC, or any video player
- **First launch after update may be slower** — this is normal
- **VPN users:** Disconnecting your VPN temporarily may speed up stream loading

--- VirusTotal scan: 2/72 detections (both from lesser-known engines, likely false positives).
--- All major antivirus engines (Microsoft, Kaspersky, BitDefender, Avast, McAfee) give it a clean bill of health.
--- The source code stream.py will be included for anyone to check the code for themselves

---

*Created by **flybers** — Free. Open. Always.*