# Alphabet Recognition Model

This project implements a Convolutional Neural Network (CNN) model using Keras for recognizing alphabets. Below is a brief overview of the project components and their functionalities:

## Model Architecture

The model architecture is as follows:
- Input Layer: Accepts grayscale images of size 80x80 pixels.
- Convolutional Layer 1: 64 filters of size 3x3 with ReLU activation.
- Max Pooling Layer 1: Pool size of 2x2.
- Convolutional Layer 2: 64 filters of size 3x3 with ReLU activation.
- Max Pooling Layer 2: Pool size of 2x2.
- Flatten Layer: Flattens the output for input to fully connected layers.
- Fully Connected Layer 1: 100 neurons with softmax activation.
- Dropout Layer: Dropout rate of 50%.
- Fully Connected Layer 2 (Output Layer): 35 neurons with softmax activation, representing the classes (alphabets).

The model is compiled using the Adam optimizer with categorical crossentropy loss function and accuracy metric.

## Data Preprocessing

Image data generators are used for both training and testing data. The images are resized to 80x80 pixels and converted to grayscale. Data augmentation techniques such as rescaling, shear, and zoom are applied to the training set.

## Training and Evaluation

The model is trained using the fit_generator method with the training data generator. It is trained for 326 epochs with validation data to monitor for overfitting. After training, the model is evaluated on the test set using the predict_generator method. Metrics such as accuracy, confusion matrix, and classification report are computed to assess the model's performance.

## Prediction

The trained model can be used to predict the class label of new images. An example image is read and preprocessed using OpenCV and Keras preprocessing functions. The model predicts the class label of the image.

## Usage

1. Ensure the required libraries (Keras, NumPy, Pandas, OpenCV) are installed.
2. Prepare the training and testing datasets.
3. Run the script to train the model and evaluate its performance.
4. Use the trained model to make predictions on new images.

Feel free to customize the model architecture, data preprocessing, and training parameters based on your specific requirements.

