# [PYTHON] FOOTBALL - PLAYER - DETECTION

# Introduction
![football2(1)](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/829cd9cd-bb8d-4e58-8068-6f6b56454eb0)
- Here is an example

![football](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/72dab2bc-14a4-4ec0-b339-adf19d895e87)
- And here is another example

- These examples above had some incorrect detections because I trained with only 2 epochs.

# Requirement
- Numpy
- Matplotlib
- Pandas
- Pytorch
- Tensorboard
- The other libs you could check in requirements file from yolov5 of ultralytics

- To download all of yolov5 libs following to:
- Access to yolov5 repository and make sure that you installed git and registed github account
  
      git clone https://github.com/ultralytics/yolov5

- Change your terminal path to yolov5

      pip install -r requirements.txt

# Training
- This is how my data-changing works:
-Extracting processing use only your original data is video type

- /path/to/dataset -> extract each frame -> data_extracting_folder

      data_extracting_folder
          |
          |- Train
          | ├── annotations
          | │   ├── image1.txt
          | │   ├── image2.txt
          | │   └── ...
          | ├── images
          | │   ├── image1.jpg
          | │   ├── image2.jpg
          | │   └── ...
          |  
          |- Test
            ├── annotations
            │   ├── image1.txt
            │   ├── image2.txt
            │   └── ...
            ├── images
            │   ├── image1.jpg
            │   ├── image2.jpg
            │   └── ...
  
- During the training process, I used 3 videos, each lasting 60 seconds with a frame rate of 25fps.
- I utilized YOLOv5 for training this project. After creating a data-extracting folder, I also generated a YAML file for my football data.
- The three objects I focused on are players, balls, and corners.
- Here is the YOLOv5 repository on the Ultralytics website, which guides us on how to run their model in the field of object detection: https://github.com/ultralytics/yolov5
- YOLOv5 supports 10 models, but I could only use YOLOv5n with my sufficiently large batch size, expecting it to be 8 or even 16. I trained the model with a 24GB GTX 3060 GPU.

![image](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/9b99c47e-34c9-4e20-a6ef-462e1e8ff5f5)

# Validation
- Same idea with training processing i extracted each frame from validation video but the difference is video quantity. In validation i used only 1 video

# Inference 
- I found random video on google to testing my model accuracy
- The weakness of yolo models is still the difficulty of identifying small objects, Although yolo models are very fast in detecting

# Experiemnts
- The training/test loss curves for each experiment are shown below:
![Screenshot from 2024-02-19 23-01-26](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/838875d8-3d10-4127-8b35-9f3d8198073b)

- Statistics for mAP:
![Screenshot from 2024-02-19 23-01-55](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/16bea47c-7892-4718-80b1-ae6ef31c7b3e)

# Results
- Some output predictions for experiments for each dataset are shown below:
- ![image](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/214181d7-9e8a-4565-b3bc-56a6f8061fae)

      COPYRIGHT: PIXELLOT AIR



