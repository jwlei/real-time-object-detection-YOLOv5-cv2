
# Realtime-DWLS
Detection - Warning - Logging - Scraping

This project was developed as a result of my bachelor thesis:  
*«Detection and warning of game in vicinity of roads with deep learning»*

The goal was to develop a deep learning model and program to detect  
and warn against game in vicinity of public roads.

An application utilizing PyTorch with YOLOv5 and cv2 to process video input in    
and perform detections in realtime.

The application uses a PyTorch and a custom trained YOLOv5s model to accurately detect  
game based on video input. Video data for GUI is processed with cv2.

A simple MQTT messaging client is used to send information about warnings to remote  
units, which makes the application able to run in two configurations where you can  
process the input locally or remotely.

This application can also be used as a tool to gather new training data for future  
iterations of your machine learning model. Images are saved in .png to avoid  
artifacts from .jpg


## Authors

- [@jwlei](https://github.com/jwlei)

## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Demo

![Demo](https://github.com/jwlei/real-time-object-detection-YOLOv5-cv2/blob/master/Realtime-dwls/resources/media/demo.gif)

## YOLOv5 Results

| Modell         | Precision | Recall    | mAP@0.5 | mAP@0.5:.95 |
| :---           | :---      | :---      | :---    | :---        | 
| YOLOv5 Nano    | 0.893     | 0.837     | 0.869   | 0.544       |
| YOLOv5 Small   | 0.897     | 0.865     | 0.898   | 0.564       |
| YOLOv5 Medium  | 0.963     | 0.910     | 0.945   | 0.691       |
| YOLOv5 Large   | 0.966     | 0.915     | 0.964   | 0.726       |
| YOLOv5 X-Large | 0.970     | 0.895     | 0.947   | 0.687       |

## Features

- Video input from remote URL, Local camera or local media file
- Can scrape images of detections at user defined interval
- Local or remote processing and warning independently
- Can push new YOLOv5 model from remote by supplying a URL in a message
- Downloads remote model on first startup
- Customizable configuration
  - Resize video output
  - Run with setup or straight from configuration
  - Set default video/model and remote model source
  - Save images on detection, with user defined interval
  - User defined confidence threshold at which detections are made
  - Run headlessly or with GUI


## Installation

Clone the project

```bash
git clone https://github.com/jwlei/real-time-object-detection-YOLOv5-cv2
```

Go to the project directory

```bash
cd Realtime-dwls
```

Optional: Create and activate a virtual environment
```bash
python -m venv name_environment
```
```bash
name_environment\Scripts\activate.bat
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install PyTorch for your version, supplied is for Python 3.10:

* CUDA
```bash
pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu113
```

* Non-CUDA
```bash
pip install torch torchvision
```

## Run Locally

Run the main application

```bash
python main.py
```

External MQTT Subscriber with a simple warning GUI
```bash
python external_mqtt/ext_mqtt_subscriber.py
```

External MQTT Publisher which can supply an URL for a model for the main application to download
```
python external_mqtt/ext_mqtt_publisher.py http://url.to/yourmodel.pt
```

## Links to trained models
_The URL supplied can be used to directly download the model to the program_

[YOLOv5-Nano](https://dl.dropboxusercontent.com/s/cbvc681akdp9rc1/yolov5N.pt) 
(https://dl.dropboxusercontent.com/s/cbvc681akdp9rc1/yolov5N.pt)

[YOLOv5-Small](https://dl.dropboxusercontent.com/s/nxobi6gciwsaygb/yolov5S.pt)
(https://dl.dropboxusercontent.com/s/nxobi6gciwsaygb/yolov5S.pt)

[YOLOv5-Medium](https://dl.dropboxusercontent.com/s/3y47tbcz6e33a40/yolov5M.pt) 
(https://dl.dropboxusercontent.com/s/3y47tbcz6e33a40/yolov5M.pt)

[YOLOv5-Large](https://dl.dropboxusercontent.com/s/a1t8w7tetq4naov/yolov5L.pt) 
(https://dl.dropboxusercontent.com/s/a1t8w7tetq4naov/yolov5L.pt)

[YOLOv5-XLarge](https://dl.dropboxusercontent.com/s/d4ouyyqj4ji49a3/yolov5XL.pt)
(https://dl.dropboxusercontent.com/s/d4ouyyqj4ji49a3/yolov5XL.pt)

## License

[MIT](https://choosealicense.com/licenses/mit/)



