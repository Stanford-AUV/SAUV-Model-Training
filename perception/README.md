- python train.py --img 640 --epochs 30 --data ../dataset-configs/datasets/amy_house.yaml --weights yolov5s.pt

- python detect.py --weights runs/train/exp6/weights/best.pt --source "~/Downloads/combined_yolo_dataset_v2/images/val/*.png"
