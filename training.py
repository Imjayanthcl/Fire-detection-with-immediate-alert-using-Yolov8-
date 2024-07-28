from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(
    task="detect",
    epochs=5,  
    data='data_custom.yaml',
    imgsz=640,
    batch=8
)
