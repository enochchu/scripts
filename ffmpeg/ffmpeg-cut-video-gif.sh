#/usr/bin/env bash
input="$1"
output="$2"
begin_ts="$3"
end_ts="$4"

if [ "$#" -eq  "0" ]
  then
    echo "Insufficent arguments supplied"
    echo "Usage example: ffmpeg-cut-video-gif.sh 01.mp4 output.mp4 00:00:00 00:00:05"
    exit 1
fi

echo $input
echo $output
echo $begin_ts
echo $end_ts

# Cut Video
ffmpeg -ss $begin_ts -to $end_ts \
	-i $input \
	-vsync 0 \
	-c copy $output

ffmpeg -y -i $output -vf palettegen palette.png

# Generate GIF
ffmpeg -i $output \
    -i palette.png \
 	-vf "fps=30,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
    -loop 0 $output.gif

# -vf "fps=30,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \

# Generate webp
ffmpeg -i $output \
	-vcodec libwebp \
	-filter:v fps=fps=30 -lossless 0  -compression_level 3 -q:v 70 -loop 1 \
	-preset picture -an \
	-vsync 0 output.webp
