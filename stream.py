import os
import subprocess
import sys
from datetime import datetime

def main():
    print("=" * 50)
    print("flybers Universal Live Stream Recorder")
    print("=" * 50)
    print()
    print("Drag and drop a stream URL onto this window, then press Enter")
    print()
    
    url = input("URL: ").strip().strip('"')
    
    if not url:
        print("No URL entered. Exiting.")
        input("Press Enter to close...")
        return
    
    # Extract the room/channel name from the URL
    # Handles URLs like: https://twitch.tv/name, https://youtube.com/@name, etc.
    name = os.path.basename(url.rstrip('/'))
    if not name or name in ['http:', 'https:']:
        name = "stream"
    
    # Create a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create the Recordings folder if it doesn't exist
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    recordings_dir = os.path.join(script_dir, "Recordings")
    if not os.path.exists(recordings_dir):
        os.makedirs(recordings_dir)
        print(f"Created Recordings folder: {recordings_dir}")
    
    # Output filename
    output_file = os.path.join(recordings_dir, f"{name}_{timestamp}.ts")
    
    # Path to mpv.exe (same folder as this script)
    mpv_path = os.path.join(script_dir, "mpv.exe")
    
    if not os.path.exists(mpv_path):
        print(f"ERROR: mpv.exe not found in {script_dir}")
        print("Make sure mpv.exe is in the same folder as this program.")
        input("Press Enter to close...")
        return
    
    print(f"\nRecording to: {output_file}")
    print("Opening mpv...")
    print("Close mpv when done. Recording will save automatically.\n")
    
    # Play and record
    cmd = [mpv_path, "--ytdl", f"--stream-record={output_file}", url]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\nRecording saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"\nError occurred: {e}")
    except KeyboardInterrupt:
        print("\nRecording stopped by user.")
    
    print("\n" + "=" * 50)
    input("Press Enter to close...")

if __name__ == "__main__":
    main()