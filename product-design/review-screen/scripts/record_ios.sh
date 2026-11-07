#!/usr/bin/env bash
# Record the booted iOS Simulator so Claude can watch the motion of a flow.
#
# usage: record_ios.sh <out-dir> [seconds]
#
# Start the flow (a UI test, `xcrun simctl openurl booted <url>`, or by hand) while
# this records. Writes sim.mp4, still.png (first frame) and frames.jpg (6 frames a
# second) to <out-dir>. Needs Xcode command line tools and ffmpeg (brew install ffmpeg).
set -euo pipefail
out="${1:?usage: record_ios.sh <out-dir> [seconds]}"
seconds="${2:-15}"
mkdir -p "$out"
raw="$out/sim-raw.mp4"

xcrun simctl io booted recordVideo --codec=h264 --force "$raw" &
rec=$!
sleep "$seconds"
kill -INT "$rec"
wait "$rec" || true

# Simulator video has a variable frame rate; resample it to 30 fps so frames are evenly spaced.
ffmpeg -v error -y -i "$raw" -vf "fps=30,scale=-2:900:flags=lanczos" -c:v libx264 -preset veryfast -crf 20 \
  -pix_fmt yuv420p -movflags +faststart "$out/sim.mp4"
rm -f "$raw"
ffmpeg -v error -y -i "$out/sim.mp4" -frames:v 1 "$out/still.png"
ffmpeg -v error -y -i "$out/sim.mp4" -vf "fps=6,scale=240:-2,tile=10x$(( (seconds*6+10)/10 )):padding=4:color=white" -frames:v 1 "$out/frames.jpg"
echo "$out: sim.mp4, still.png, frames.jpg"
