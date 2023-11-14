<h2 align="center">  <b>Transferring Intelligence to the Edge:</b> Modeling, Optimization, and Deployment of Computer Vision Models for Embedded Systems </h2>

<img title="" alt="Alt text" src="images/logos.png">

<p align='right'><i>  Updated: November 14th, 2023 </i></p> <div align="center">
  <a href="#Abstract"><b>Abstract</b></a> |
  <a href="#Contents"><b>Slides</b></a> |
  <a href="#Contents"><b>Tutorial</b></a> |
  <a href="#Results"><b>Resources</b></a> 
</div>


# Abstract 

Patterns recognized by deep learning models from visual information have reached unprecedented precision levels in diverse fields. However, most of the state-of-the-art computer vision systems require high computing resources, which in turn makes them need high bandwidth for image or video transferring to central servers. Recently, the significant improvements in GPU, TPU, and CPU components on diverse embedded devices have opened opportunities for new real-time applications of computer vision . Nevertheless, inference near where the data is collected still requires strategies to cope with constrained resources to function without delays. Moreover, efficient systems at the edge must be designed considering power and memory monitoring and estimation. In this tutorial, new opportunities, tools, strategies, and challenges for the deployment of computer vision systems will be explored. Specifically, we will delve into Edge-AI in practice through the OpenVino Framework. The in-person version of this workshop also utilizes the computing units of the Intel Neural Computer Stick and OAK-D.

# Slides 
TO BE INCLUDED HERE

# Tutorial 

OpenVino and TensorRT are two toolkits that stood out for the deployment of deep learning models on low-cost edge devices. While TensorRT is one of the first choices for projects that count on Nvidia graphics processing units (GPUs), OpenVino optimizes models for devices that only have Intel-based CPUs/GPUs. Additionally, the best deep learning frameworks also count with packages for model optimization when deployed: TensorFlow Lite (for TensorFlow) and JIT (for PyTorch). In this opportunity, we will see complete OpenVino examples to optimize and deploy models for object detection and classification on edge devices. 

1. [Installing dependencies](01-insalling-dependencies.md)
2. [OpenVino Model Zoo for object detection](02-model-zoo-for-object-detection.md)
3. [Image clasification with OpenVino](03-image-classification-with-openvino.md)

# Resources

- [Tutorial website](http://www.micai.org/2023/t7.php)
- [OpenVino Documentation](https://docs.openvino.ai/2023.1/home.html)