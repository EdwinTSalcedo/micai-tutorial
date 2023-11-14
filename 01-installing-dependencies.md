# Installing Dependencies

This guide will take you through the necessary steps to install OpenVINO on your computer. OpenVINO is the tool we will use in this workshop to work on Computer Vision through Edge Computing.

## Prerequisites

Before you begin, make sure your computer meets the following requirements:

- Operating System: Windows 10+, Ubuntu 18.04 - 20.04 (recommended)
- [Git](https://git-scm.com/) (Windows: git bash)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Anaconda](https://www.anaconda.com/download) (Participants should know how to create virtual environments and install libraries)

## Installation Steps

### 1. Download and Install OpenVINO 2022.3.1

Visit the official OpenVINO website and download the version compatible with your operating system from the following links:

1. Installation of OpenVINO runtime from archives
    - Linux: [Instalation link](https://docs.openvino.ai/2022.3/openvino_docs_install_guides_installing_openvino_from_archive_linux.html)
    - Windows: [Instalation link](https://docs.openvino.ai/2022.3/openvino_docs_install_guides_installing_openvino_from_archive_windows.html)

### 2. Virtual Environment Setup

It is recommended to use [Anaconda](https://www.anaconda.com/download) to set up the virtual environment.

1. Execute the following command in the terminal or Anaconda Prompt:
    
    ```
    conda create -n micai-tutorial python=3.9
    ```
    
2. Activate the virtual environment:
    
    ```
    conda activate micai-tutorial
    
    # Para desactivar el ambiente virtual se usa:
    # conda deactivate
    ```
    
3. Update pip
    
    ```
    python -m pip install --upgrade pip
    ```

4. Install additional libraries
   
    ```
    pip install numpy
    pip install opencv-python
    pip install matplotlib
    pip install tensorflow

    ```

5. Install the development tools [Openvino-dev](https://docs.openvino.ai/2022.3/openvino_docs_install_guides_install_dev_tools.html#doxid-openvino-docs-install-guides-install-dev-tools)
    
    ```
    pip install openvino-dev
    ```

6. Test the installation by running the following command:
    
    
    ```
    mo -h
    ```

7. Everytime you need to use OpenVINO, you must activate the environment and initialize the environment variables:
   
   - Linux/MacOS:
       
        ```
        source <openvino_installation_dir>/setupvars.sh
        ```
    
    - Windows:
        
        ```
        <openvino_installation_dir>\setupvars.bat
        ```
    
8. Finally, execute the following Python script to check the installation; it should list the connected devices.
    
```python
# Load library Openvino API
from openvino.runtime import Core
# Instantiate the API
ie = Core()
# Query the available devices
print(ie.available_devices)
# Outputs ['CPU'], but this might list "MYRIAD" if NCS2 is connected. 
```

### 3. Additional Configuration for the Intel NCS2 (Linux Only)
Navigate to the install_dependencies folder in the OpenVINO installation directory:

```
cd <INSTALL_DIR>/install_dependencies
```

Then, run the following command:

```
sudo -E ./install_NCS_udev_rules.sh
```

If something fails, complete the following configuration steps on your operating system:

- [Configuration link](https://docs.openvino.ai/2022.3/openvino_docs_install_guides_configurations_for_ncs2.html#ncs-guide)

You can also refer to the following resource:

- [Addtional configuration resources](https://medium.com/openvino-toolkit/how-to-run-openvino-with-neural-compute-stick-2-on-linux-9ab1f185c920)

Execute the following Python script to check the installation; it should list the connected devices, and you should see a new MYRIAD device, which corresponds to the Intel NCS2.
    
```python
# Load library Openvino API
from openvino.runtime import Core
# Instantiate the API
ie = Core()
# Query the available devices
print(ie.available_devices)
```

You're all set! Now you have OpenVINO configured on your computer, and you're ready to explore the exciting world of Computer Vision through Edge Computing. Now, we will continue with the [Model Zoo for Object Detection](02-model-zoo-for-object-detection.md) section.
