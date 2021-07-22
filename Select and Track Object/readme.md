#### Tracker
- By default opencv provide different tracker :
    1. Boosting
    2. KCF
    3. Medium Flow
- For each we have to initiate the tracker.
- For High Speed use MOSSE Tracker use `cv2.TrackerMOSSE_create()`
- For High Accuracy CSRT Tracker use `cv2.TrackerCSRT_create()`
- In order to run the tracker we have to initlize it with bounding box. So we take first frame from webcam and take a bounding box from there.
- `cv2.SelectROI` used to choose bounding box
- Then use this bbox and img to initlize the tracker
- Then run the tracker and update it by using `tracker.update(img)`