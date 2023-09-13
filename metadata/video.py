# import cv2
# import numpy as np
# import mutagen

# video_path = 'The Crimson Threat - Vladimir Champion Trailer - League of Legends- Wild Rift.mp4'
# cap = cv2.VideoCapture(video_path)
# print(cap)

# if (cap.isOpened() == False):
#     print("Error opening video stream or file")
# # Read until video is completed
# while (cap.isOpened()):
#
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     if ret == True:
#         # Display the resulting frame
#         cv2.imshow('Frame', frame)
#         # Press Q on keyboard to  exit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     # Break the loop
#     else:
#         break
# # When everything done, release the video capture object
# cap.release()
# # Closes all the frames
# cv2.destroyAllWindows()


from moviepy.editor import VideoFileClip

def remove_metadata(input_video_path, output_video_path):
    # Create a VideoFileClip object
    video_clip = VideoFileClip(input_video_path)

    # Remove metadata
    video_clip.reader.close()  # Close the video reader to release the file

    # Create a new VideoFileClip without metadata
    video_clip_without_metadata = VideoFileClip(input_video_path, audio=True)

    # Write the new video to the output file
    # video_clip_without_metadata.write_videofile(output_video_path, codec="libx265")
    video_clip_without_metadata.write_videofile(output_video_path)


input_video_path = "Vladimir.mp4"  # Replace with the path to your input video
output_video_path = "output_video.mp4"  # Replace with the desired output file path

remove_metadata(input_video_path, output_video_path)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import subprocess
#
# def remove_metadata(video_file):
#     try:
#         # Use the exiftool command to remove all metadata from the video file
#         subprocess.run(['exiftool', '-all=', video_file], check=True)
#         print(f"Metadata removed from {video_file}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")
#         print(f"Failed to remove metadata from {video_file}")
#
#
# # video_path = "Vladimir.mp4"  # Replace with your input video file
# input_video_path = "Vladimir.mp4"  # Replace with your input video file
# # input_video_path = VideoFileClip(video_path)
#
# remove_metadata(input_video_path)



# import subprocess
#
# def remove_metadata(input_file, output_file):
#     # Run the ffmpeg command to remove metadata
#     command = [
#         'ffmpeg',
#         '-i', input_file,            # Input file
#         '-map_metadata', '-1',      # Remove all metadata
#         '-c:v', 'copy',             # Copy video codec
#         '-c:a', 'copy',             # Copy audio codec
#         output_file                 # Output file
#     ]
#
#     try:
#         subprocess.run(command, check=True)
#         print("Metadata removed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error removing metadata: {e}")
#
# input_video_path = "Vladimir.mp4"  # Replace with your input video file
# output_video_path = "Vladimir2.mp4"  # Replace with your desired output video file
#
# remove_metadata(input_video_path, output_video_path)

