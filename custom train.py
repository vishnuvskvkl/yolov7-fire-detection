

# Download YOLOv7 repository and install requirements
!git clone https://github.com/WongKinYiu/yolov7
# %cd yolov7
!pip install -r requirements.txt

"""# Importing data from google drive


"""

from google.colab import drive

drive.mount('/content/drive/')

unzip /content/drive/MyDrive/fire.zip -d /content/yolov7/data



"""# Begin Custom Training


"""

# %cd /content/yolov7
wget "https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt"





!pip install wandb



# run this cell to begin training
# %cd /content/yolov7
!python train.py --batch 16 --cfg cfg/training/yolov7.yaml --epochs 10 --data data/coco.yaml --weights 'yolov7.pt' --device 0



'''
We can evaluate the performance of our custom training using the provided evalution script.

'''
# Run evaluation
python detect.py --weights /content/yolov7/runs/train/exp2/weights/best.pt --conf 0.1 --source 663.jpg

cp /content/yolov7/runs/train/exp2/weights/best.pt /content/drive/MyDrive

