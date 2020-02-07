import cv2
import os

path = './my_clips_01Jan2020/'
write_path = './my_full_frames/'
# Function to extract frames 
for file in os.listdir(path):
	if file.endswith('.mp4'):
		if not os.path.isdir(write_path + file.split('.')[0] + '_images'):
			os.makedirs(write_path + file.split('.')[0] + '_images')
		vidObj = cv2.VideoCapture(path + file) 
		fps = vidObj.get(cv2.CAP_PROP_FPS)
		frame_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
		duration = frame_count/fps
		count = 1
		success, image = vidObj.read()
		while success:
			cv2.imwrite("%s/%s/%s_1%06d.jpg" % (write_path, file.split('.')[0]+ '_images', file.split('.')[0], count), image) 
			count += 1
			success, image = vidObj.read()
