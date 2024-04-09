# NORMAL VIDEO
import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('video1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))
while True:
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    writer.write(frame)
    cv2.imshow('frame', frame)
cap.release()
writer.release()
cv2.destroyAllWindows()

# REVERSED VIDEO
cap_rev = cv2.VideoCapture("video1.mp4")
check, vid = cap_rev.read()
frame_list = []
while(check == True):
    check, vid = cap_rev.read()
    if check:
        frame_list.append(vid)
frame_list.reverse()
writer_rev = cv2.VideoWriter('video2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

for frame in frame_list:
    cv2.imshow("Frame", frame)
    writer_rev.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
writer_rev.release()
cv2.destroyAllWindows()

# JOINED VIDEO
videos = ["video1.mp4", "video2.mp4"]
video = cv2.VideoWriter("videos_juntos.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 20,(width, height))

for v in videos:
    curr_v = cv2.VideoCapture(v)
    while curr_v.isOpened():
        r, frame = curr_v.read()
        if not r:
            break
        video.write(frame)

video.release()