## NEURAL STYLE TRANSFER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: Keerthi K

*INTERN ID*: CT06DG2158

*DOMAIN*: Artificial Intelligence

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

---

## Project Overview

This project implements a Neural Style Transfer tool that blends the content of one image with the artistic style of another using a pre-trained deep learning model from TensorFlow Hub. Built on the concept of convolutional neural networks, this tool enables creative image generation by applying artistic transformations to photographs.

The goal of this project is to demonstrate how pre-trained transformer-based vision models can be used to generate stylized visual content. The project helps explore the intersection of deep learning and art, making it applicable to design tools, content creation, and image-based AI applications.

---

## Tools & Technologies Used

| **Tool/Library**            | **Purpose**                                  |
| --------------------------- | -------------------------------------------- |
| Python                      | Main programming language                    |
| TensorFlow + TensorFlow Hub | Load pre-trained neural style transfer model |
| NumPy & Matplotlib          | Image handling and visualization             |
| OpenCV                      | Image saving and BGR to RGB conversion       |
| Git + GitHub                | Version control and code hosting             |

---

## How the Project Works (Architecture)

1. Image Input
The user provides a content image (e.g., img.jpg) and a style image (e.g., monet.jpg).

2. Preprocessing
Images are resized and converted into a format compatible with the model (float32 tensors of shape (1, height, width, 3)).

3. Style Transfer
Using the TensorFlow Hub model:

- Content and style images are passed to the pre-trained neural network.

- The model returns a new stylized image that combines the structure of the content image and the texture/colors of the style image.

4. Output Display
The resulting stylized image is displayed using Matplotlib and saved locally using OpenCV.

---

## Future Improvements
- Add UI for real-time style selection (via Gradio/Streamlit)

- Allow users to adjust style intensity or blend ratio

- Support higher-resolution image generation

- Add custom style training option

- Provide downloadable output with quality control options

## Output

Stylized Image: generated_img.jpg
<img width="796" height="677" alt="Image" src="https://github.com/user-attachments/assets/afc7678f-7247-452e-8c67-9ed55f8dbd3a" />
