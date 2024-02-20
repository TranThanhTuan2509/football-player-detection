import os
import shutil
import cv2
import glob
import json

if __name__ == '__main__':
    root = "./football-20230818T081210Z-001/football/train"
    global_width = 3840
    global_height = 1200
    output_dir = "football_yolo"
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    os.makedirs(os.path.join(output_dir, "images"))
    os.makedirs(os.path.join(output_dir, "images", "train"))
    os.makedirs(os.path.join(output_dir, "images", "val"))
    os.makedirs(os.path.join(output_dir, "labels"))
    os.makedirs(os.path.join(output_dir, "labels", "train"))
    os.makedirs(os.path.join(output_dir, "labels", "val"))

    video_paths = list(glob.iglob("{}/*/*.mp4".format(root)))
    video_paths = [video_path.replace(".mp4", "") for video_path in video_paths]
    anno_paths = list(glob.iglob("{}/*/*.json".format(root)))
    anno_paths = [anno_path.replace(".json", "") for anno_path in anno_paths]
    paths = set(video_paths).intersection(set(anno_paths))

    for image_id, path in enumerate(paths):
        count = 1
        video = cv2.VideoCapture("{}.mp4".format(path))
        num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        with open("{}.json".format(path), "r") as json_file:
            json_data = json.load(json_file)
        while video.isOpened():
            flag, frame = video.read()
            if not flag:
                break
            cv2.imwrite(os.path.join(output_dir, "images", "train", "{}_{}.jpg".format(image_id + 1, count)), frame)
            current_bboxes = [[obj["bbox"], obj["category_id"]] for obj in json_data["annotations"] if
                              obj["image_id"] == count and int(obj["category_id"]) in [1, 3, 4]]
            with open(os.path.join(output_dir, "labels", "train", "{}_{}.txt".format(image_id + 1, count)),
                      "w") as text_file:
                for box in current_bboxes:
                    (xmin, ymin, width, height), cat = box
                    xcent = (xmin + width / 2) / global_width
                    ycent = (ymin + height / 2) / global_height
                    width /= global_width
                    height /= global_height
                    if cat == 4:  # player
                        category = 0
                    elif cat == 3:  # ball
                        category = 1
                    elif cat == 1:
                        category = 2

                    text_file.write("{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(category, xcent, ycent, width, height))

            count += 1
