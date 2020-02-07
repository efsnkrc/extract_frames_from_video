import cv2
import os
import argparse

#python extractFrames.py --input_path=./my_clips_01Jan2020 --output_path=./my_full_frames

parser = argparse.ArgumentParser()

parser.add_argument("--input_path", help="input path for mp4 files", type=str, default='.')
parser.add_argument("--output_path", help="output path for images to be extracted", type=str, default='./images')
parser.add_argument("--sec", help="extract 1 frame per ? seconds", type=int, default = -1)

args = parser.parse_args()

input_path=args.input_path
output_path = args.output_path
sec = args.sec

# Function to extract frames 
for file in os.listdir(input_path):
	if file.endswith('.mp4'):
		im_path = os.path.join(output_path, file.split('.')[0] + '_images')
		if not os.path.isdir(im_path):
			os.makedirs(im_path)
		vidObj = cv2.VideoCapture(os.path.join(input_path, file)) 
		
		fps = round(vidObj.get(cv2.CAP_PROP_FPS))
		frame_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
		duration = frame_count/fps
		
		count = 0
		frame = 1
		success, image = vidObj.read()
		while success:
			if sec == -1 or count % (sec * fps) == 0:
				cv2.imwrite("%s/%s_1%06d.jpg" % (im_path, file.split('.')[0], frame), image) 
				frame += 1
			count += 1
			success, image = vidObj.read()
