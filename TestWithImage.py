from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")  

model.predict(
    source=r"C:/Users/ASUS/ProjectTesting/PythonMLProjects/MyProject/dataset/train/10.jpg",  # Path to the image
    classes=[0],  
    conf=0.5,  
    show=True, 
    save=True,  
    save_txt=True  
)
