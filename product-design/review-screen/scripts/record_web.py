#!/usr/bin/env python3
"""Record a web page or HTML mock so Claude can look at it and watch its motion.

usage: record_web.py <page.html | URL> <out-dir> [--demo JS] [--width 1280] [--height 900] [--seconds 20]

Writes to <out-dir>:
  still.png    the page at rest after load
  demo.webm    the full recording
  phone.mp4    the recording cropped to the phone frame, if one is found (else the full frame)
  frames.jpg   a frame sheet of phone.mp4 at 6 frames a second, to read transition by transition
  end.png      the last state
  console.txt  console messages and page errors

--demo is a JavaScript expression that plays the flow and returns a promise, for
example "window.__demo()". Without it the script records --seconds of the page alone.
Needs Python Playwright with Chromium, and ffmpeg.
"""
import argparse, glob, os, shutil, subprocess

from playwright.sync_api import sync_playwright

FIND_PHONE = """() => {
  let best = null, area = 0;
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.height < 500 || r.width < 220) continue;
    const a = r.width / r.height;
    if (a < 0.40 || a > 0.58) continue;
    if (r.width * r.height > area) { area = r.width * r.height; best = r; }
  }
  return best && {x: best.x, y: best.y, w: best.width, h: best.height};
}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target"); ap.add_argument("out")
    ap.add_argument("--demo"); ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=900); ap.add_argument("--seconds", type=float, default=20)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    url = a.target if "://" in a.target else "file://" + os.path.abspath(a.target)
    vid_dir = os.path.join(a.out, "_vid")
    log = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": a.width, "height": a.height}, record_video_dir=vid_dir,
                            record_video_size={"width": a.width, "height": a.height})
        pg = ctx.new_page()
        pg.on("console", lambda m: log.append(f"{m.type}: {m.text}"))
        pg.on("pageerror", lambda e: log.append(f"pageerror: {e}"))
        pg.goto(url)
        pg.wait_for_timeout(1200)
        pg.screenshot(path=os.path.join(a.out, "still.png"))
        box = pg.evaluate(FIND_PHONE)
        if a.demo:
            try:
                pg.evaluate(f"Promise.race([{a.demo}, new Promise(r => setTimeout(r, {int(a.seconds * 1000)}))])")
            except Exception as e:  # report and keep the recording
                log.append(f"demo error: {e}")
        else:
            pg.wait_for_timeout(int(a.seconds * 1000))
        pg.wait_for_timeout(600)
        pg.screenshot(path=os.path.join(a.out, "end.png"))
        ctx.close(); b.close()
    webm = os.path.join(a.out, "demo.webm")
    shutil.move(glob.glob(os.path.join(vid_dir, "*.webm"))[0], webm)
    shutil.rmtree(vid_dir)
    crop = ""
    if box:
        pad = 12
        x, y = max(0, int(box["x"] - pad)), max(0, int(box["y"] - pad))
        w = min(a.width - x, int(box["w"] + 2 * pad)); h = min(a.height - y, int(box["h"] + 2 * pad))
        crop = f"crop={w - w % 2}:{h - h % 2}:{x}:{y},"
    phone = os.path.join(a.out, "phone.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", webm, "-vf", f"{crop}scale=-2:900:flags=lanczos",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-movflags", "+faststart", phone], check=True)
    # 6 frames a second, as many rows as the recording needs (10 frames a row).
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                         "-of", "csv=p=0", phone]).decode())
    rows = max(1, -(-int(dur * 6 + 1) // 10))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", phone, "-vf",
                    f"fps=6,scale=240:-2,tile=10x{rows}:padding=4:color=white", "-frames:v", "1",
                    os.path.join(a.out, "frames.jpg")], check=True)
    open(os.path.join(a.out, "console.txt"), "w").write("\n".join(log))
    print(f"{a.out}: phone {'found' if box else 'not found'}, {len(log)} console lines")


if __name__ == "__main__":
    main()
