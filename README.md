# [PYTHON] FOOTBALL - PLAYER - DETECTION

# Introduction
![pexels-tima-miroshnichenko-6079623online-video-cutter com-ezgif com-video-to-gif-converter](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/17a54a71-491b-4ad2-b0d7-c49bd9ebe9b8)


- Here is an example

![football3_cut_video-ezgif com-video-to-gif-converter](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/68086542-3ea1-47e3-9dcc-2123a20fd16c)

- And here is another example

- These examples above had still some incorrect detections such as: player...These are the best results I got after almost training 100 epochs

# Requirementss
- Numpy
- Matplotlib
- Pandas
- Pytorch
- Tensorboard
- The other libs you could check in the requirements file from yolov5 of Ultralytics

- To download all of the yolov5 libs following:
- Access to yolov5 repository and make sure that you installed git and registered GitHub account
  
      git clone https://github.com/ultralytics/yolov5

- Change your terminal path to yolov5

      pip install -r requirements.txt

# Training
- This is how my data-changing works:
- Extracting processing uses only your original data in video type

- /path/to/dataset -> extract each frame -> data_extracting_folder

      data_extracting_folder
          │
          ├── Train
          │ ├── annotations
          │ │   ├── image1.txt
          │ │   ├── image2.txt
          │ │   └── ...
          │ ├── images
          │ │   ├── image1.jpg
          │ │   ├── image2.jpg
          │ │   └── ...
          │  
          ├── Validation
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

![Screenshot from 2024-02-20 16-27-31](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/aac9d033-7e9b-42fb-9dd6-f9336f92a1c2)


# Validation
- Same idea with training processing i extracted each frame from the validation video but the difference is video quantity. In validation, i used only 1 video

# Inference 
- I found a random video on google to test my model accuracy
- The weakness of Yolo models is still the difficulty of identifying small objects, Although yolo models are very fast in detecting

# Experiments
- These tensorboard results below represented my first 2 epochs with yolov5n model
- The training/test loss curves for each experiment are shown below:
![Screenshot from 2024-02-19 23-01-26](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/948cd162-d07c-4f2d-8b5a-c864a7bf5542)

- Statistics for mAP:
![Screenshot from 2024-02-19 23-01-55](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/534366e8-c1c5-4b90-87d5-2d96551edb35)

# Results
- Some output predictions for experiments for each dataset are shown below:
![image](https://github.com/TranThanhTuan2509/football-player-detection/assets/119112296/f0209830-01bd-4316-b5ee-d50baec728c8)


      COPYRIGHT: PIXELLOT AIR



