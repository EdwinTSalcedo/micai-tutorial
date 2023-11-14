# Image Clasification: OpenVINO Model Optimizer
In this section, we will learn how to use the OpenVINO Model Optimizer to convert a custom model to the Intermediate Representation format.

## 1. Train a custom classification deep learning model
We will train a custom classification model using the [image_classification_model_training](image_classification/image_classification_model_training.ipynb) notebook. This notebook contains the code to train a custom classification model using the [Intel Image Classification](https://www.kaggle.com/datasets/puneet6060/intel-image-classification) dataset. The dataset contains images of natural scenes around the world. The dataset contains 25,000 images of size 150x150 distributed under 6 categories:

- buildings
- forest
- glacier
- mountain
- sea
- street

For following this part of the workshop you will need to upload the [image_classification_model_training](image_classification/image_classification_model_training.ipynb) notebook in Google Colab or use your own resources to train the model if you prefer, however, is recommended to use Google Colab GPU resources.

Download the dataset from [here](https://www.kaggle.com/puneet6060/intel-image-classification/download) and upload it to your Google Drive. Then, follow the instructions in the notebook to train the model.

<div style="text-align:center; background-color:#ffff; padding:10px; color:black;">
💡 Additionally, you will find another method for approaching this exercise. You can apply Transfer Learning to the MobileNetV2 model and compare the results with our model.
</div>

## 2. Converting a custom model to the Intermediate Representation format
The Intermediate Representation (IR) format is a pair of files that describe the whole model. The files are a binary file with weights and biases and an XML file that describes the network topology. The IR format is optimized for fast inference and is supported by the OpenVINO toolkit.

Now, once you have downloaded the intel_images_cnn or/and the intel_images_mobileNetV2 saved model directory.  Execute the following command to convert the model to IR format:

```
mo --use_legacy_frontend --saved_model_dir /intel_image_cnn --input_shape=[1,150,150,3] 
```

```
mo --use_legacy_frontend --saved_model_dir /intel_image_mobileNetV2 --input_shape=[1,224,224,3]  
```

Note: If you want to convert the model to FP16 precision, you can add the `----compress_to_fp16=True` argument to the command. If the original model has FP32 weights or biases, they are compressed to FP16. All intermediate data is kept in original precision. 

The model will be converted to IR format and saved in the current directory as `saved_model.xml` and `saved_model.bin`. Then, rename the files to `intel_image_cnn.xml` and `intel_image_cnn.bin`, `intel_image_mobileNetV2.xml` and `intel_image_mobileNetV2.bin`, then, copy them to the `image_classification/resources/models` folder.

## 3. Running the image classification notebook
You can find the notebook for this section in [image_classification_openvino_inference.ipynb](image_classification/image_classification_openvino_inference.ipynb). This notebook contains the code to perform image classification using the OpenVINO inference engine with the custom model that we converted to IR format.

------
## Exercises
### 1. Run the inference on different images
### 2. Run the inference with the intel_images_mobilenetV2 model
### 3. Measure the inference time for different models and devices

------

In this section we have learned how to use the OpenVINO Model Optimizer to convert a custom model to the Intermediate Representation format. Then, we have learned how to use the OpenVINO inference engine to perform image classification.