# Extract Frames from Video

This file can be used to extract all or some of the frames from the videos in a directory.

## Usage:
* to run the code with default values<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python extractFrames.py <br/>
* to run the code with parameters<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python extractFrames.py --input_path=[INPUT_PATH] --output_path=[OUTPUT_PATH] --sec=[SECONDS_VALUE]
<br/>

><ins>input_path</ins>: input directory which contains the videos to be extracted into their frames (default value is the current directory)<br/>
><ins>output_path</ins>: output directory to save the extracted images (default value is a new folder named images in the current directory)<br/>
><ins>sec</ins>: extracts 1 frame per every 'sec' seconds (default value is -1, which is used to extract all of the frames in the videos)
  
