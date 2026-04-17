# Skin Cancer Classification using Deep Learning

## Abstract

Melanoma is one of the deadliest forms of skin cancer, responsible for a majority of skin cancer-related deaths despite being less common. Early detection significantly improves survival rates. This project proposes a deep learning-based approach for automated classification of skin lesions using dermoscopic images. A Convolutional Neural Network (CNN) with EfficientNet architecture is used to classify lesions into multiple categories, aiming to assist dermatologists in early diagnosis.

---

## Problem Statement

Traditional diagnosis of skin cancer involves biopsy and clinical examination, which is time-consuming and resource-intensive. This project aims to develop a **Computer-Aided Diagnosis (CAD)** system that can:

* Classify skin lesions as benign or malignant
* Reduce diagnosis time
* Support early-stage detection using image-based analysis

---

## Dataset

* Source: SIIM-ISIC Melanoma Classification (Kaggle)
* Total Images: ~44,000
* Training Set: ~33,000
* Test Set: ~11,000

### Key Challenge

* Severe **class imbalance**:

  * ~98% benign
  * ~2% malignant

### Solution

To address imbalance:

* Combined datasets from **ISIC 2018, 2019, and 2020**
* Increased malignant sample ratio for stable training

---

## Methodology

### 1. Data Preprocessing

* Image resizing (512×512, 768×768)
* Noise reduction via cropping
* Label mapping across datasets
* Handling missing metadata

### 2. Data Augmentation

To prevent overfitting and improve generalization:

* Flip, Rotate, Transpose
* Brightness & Contrast adjustment
* Gaussian Noise & Blur
* Distortion & Elastic Transform

---

## Model Architecture

### CNN Backbone

* EfficientNet (B4, B5, B7)
* Transfer Learning applied

### Why EfficientNet?

* Uses **compound scaling** (depth, width, resolution)
* More efficient than traditional CNNs (ResNet, VGG)
* Achieves higher accuracy with fewer parameters

### Training Details

* Loss Function: Cross-Entropy
* Optimizer: Adam
* Learning Rate: Cosine Decay with Warmup
* Epochs: 15
* Batch Size: 4–8 (GPU constrained)

---

## Classification Categories

The model predicts 9 classes:

* Melanoma (MEL)
* Nevus (NV)
* Basal Cell Carcinoma (BCC)
* Benign Keratosis (BKL)
* Actinic Keratosis (AK)
* Squamous Cell Carcinoma (SCC)
* Dermatofibroma (DF)
* Vascular Lesion (VASC)
* Unknown (UNK)

---

## Results

| Model              | Training Accuracy | Validation Accuracy |
| ------------------ | ----------------- | ------------------- |
| EfficientNet B4    | 81%               | 91%                 |
| EfficientNet B5    | 85%               | 93%                 |
| EfficientNet B7    | 83%               | 92%                 |
| **Ensemble Model** | 83%               | 92%                 |

### Key Observations

* Ensemble improves stability and reduces variance
* Model generalizes well on validation data
* EfficientNet B5 performs best individually

---

## Model Optimization

* Converted trained weights to **ONNX format**
* Reduced model size by ~36%
* Improved inference speed and portability

---

## Limitations

* High computational requirements (GPU-intensive)
* Small batch size affects convergence
* Class imbalance still impacts performance
* Limited metadata usage

---

## Future Work

* Use **K-Fold Cross Validation** for robustness
* Incorporate **patient metadata features**
* Increase dataset size and diversity
* Use **multi-GPU training** for better performance
* Implement lesion localization (bounding boxes)
* Deploy scalable inference system (e.g., Kubernetes)

---

## Conclusion

This project demonstrates that deep learning, particularly EfficientNet-based CNNs, can effectively classify skin cancer from dermoscopic images. The ensemble approach improves accuracy and robustness, making it a promising tool for assisting early melanoma detection.

---

## References

1. SIIM-ISIC Melanoma Classification (2020)
2. ISIC Challenge Datasets (2018, 2019)
3. Tan & Le (2019), *EfficientNet: Rethinking Model Scaling for CNNs*
4. Tong et al. (2018), *Bag of Tricks for Image Classification*
5. Huang et al. (2020), *Melanoma Detection using EfficientNet Ensemble*

---
