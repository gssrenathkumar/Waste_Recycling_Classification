# Waste Classification Project
## Network Architecture

![Waste Classification]([https://raw.githubusercontent.com/username/repository/main/images/waste_classification.png](https://github.com/gssrenathkumar/Waste_Recycling_Classification/blob/main/waste_image.png?raw=true))

This project aims to address the significant problem of waste management by developing a waste classification system. The system utilizes deep learning techniques and a diverse dataset of waste images to accurately classify different types of waste materials.

## Table of Contents
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Data Augmentation](#data-augmentation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset used for training and evaluation consists of a total of 22,564 images. These images were divided into two sets: a training set containing 22,564 images and a testing set containing 2,513 images. The dataset encompasses a wide range of different types of waste items, providing a diverse and comprehensive representation of the waste materials encountered in real-world scenarios.

## Model Architecture

Initially, a Convolutional Neural Network (CNN) deep learning model was employed for the training process. However, the model's performance in terms of accuracy fell short of the desired level. To address this issue and improve the accuracy of the model, the MobileV2Net architecture was incorporated. The MobileV2Net architecture has demonstrated effectiveness in various image classification tasks and is renowned for its efficiency in terms of computational resources and memory utilization.

## Data Augmentation

To further enhance the performance and robustness of the model, data augmentation techniques were applied to the dataset. Data augmentation involves the application of diverse transformations to the existing images, such as rotation, scaling, and flipping. By augmenting the dataset in this manner, the aim was to increase the variability and diversity of the training samples, thereby improving the model's ability to generalize and make accurate predictions on unseen data.

## Getting Started

To get started with the project, follow these steps:

1. Clone the project repository:
git clone https://github.com/gssrenathkumar/Waste_Recycling_Classification.git

2. Create a virtual environment using conda:
conda create -n waste_classification python=3.8 -y


3. Activate the virtual environment:
conda activate waste_classification


4. Install the required dependencies:
pip install -r requirements.txt


## Usage

To use the waste classification system, you can run the provided `app.py` file. This file contains the necessary code to load the trained model and classify waste images. Make sure you have the required dependencies installed and activate the virtual environment before running the application.

```bash
python app.py
```
The application will prompt you to provide an image path or directory containing waste images. It will then classify the images and display the results.

Contributing
Contributions to this project are welcome. You can contribute by:

Adding more waste images to the dataset
Experimenting with different model architectures and training techniques
Improving the accuracy and efficiency of the waste classification system
Reporting and fixing issues or bugs
If you'd like to contribute, please open an issue or submit a pull request with your changes.

License
This project is licensed under the MIT License.
