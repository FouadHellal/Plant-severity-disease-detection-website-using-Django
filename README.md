# ZYRAI

- [![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/django-5.0.6-blue)](https://www.djangoproject.com/download/)
- [![rembg](https://img.shields.io/badge/rembg-2.0.28-blue)](https://pypi.org/project/rembg/)
- [Google AI Studio API Key](https://aistudio.google.com/app/apikey)


ZYRAI is an AI-powered leaf disease detection platform built with Django. It aims to revolutionize farming practices by providing farmers with an efficient and accurate tool to diagnose and manage plant health issues. By leveraging advanced machine learning algorithms, ZyrAI offers instant disease severity predictions and identifies disease zones in leaf images using U-NET architecture for image segmentation.
![image](https://github.com/FouadHellal/Plant-severity-disease-detection-website-using-Django/assets/113594352/f3952152-8385-4681-94bb-16e9cd0a9c84)

## Features

- **Leaf Disease Detection**: ZyrAI utilizes state-of-the-art deep learning models to accurately identify and classify diseases affecting plant leaves. This enables farmers to swiftly identify potential threats to crop health and take proactive measures to mitigate them.

- **U-NET Image Segmentation**: The platform employs U-NET, a convolutional neural network architecture designed for biomedical image segmentation tasks. This allows ZyrAI to generate precise disease masks, outlining the areas of the leaf affected by diseases with high granularity.
  
  **Check it out on my other Repo here :**
[![Repository U-net for plant segmentation](https://img.shields.io/badge/UNet-purple)](https://github.com/FouadHellal/U-net-for-plant-segmentation.git)
or clone it from here :
  ```bash
     https://github.com/FouadHellal/U-net-for-plant-segmentation.git
  ```

  **Examples :**
  
![56](https://github.com/FouadHellal/Plant-severity-disease-detection-website-using-Django/assets/113594352/fbab854d-ca7d-4f1f-b113-70bb1c00e863)
![mask_malade_56](https://github.com/FouadHellal/Plant-severity-disease-detection-website-using-Django/assets/113594352/be1d4f6a-f0e1-42b4-9a40-89464a02cf8e)

- **User-Friendly Interface**: ZyrAI features an intuitive and user-friendly interface, making it accessible to farmers of all technical backgrounds. The platform's simple yet powerful design ensures ease of use, allowing users to upload leaf images effortlessly and obtain accurate diagnostic results.
  

- **Chatbots Integration**: ZyrAI incorporates chatbot functionality to provide users with additional support and assistance. Through interactive chat interfaces, users can ask questions, seek advice on plant care practices, and receive real-time responses from the system.

![image](https://github.com/FouadHellal/Plant-severity-disease-detection-website-using-Django/assets/113594352/fc8d0d22-3af1-49b7-9a4c-da9a6f6921a0)

## Installation

Follow these steps to set up LeafAI-Django locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/username/[Plant-severity-disease-detection-website-using-Django.git]/
    ```

2. Navigate to the project directory:
    ```bash
    cd Plant-severity-disease-detection-website-using-Django
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run Plant-severity-disease-detection-website-using-Django.git locally, follow these steps:

1. Navigate to the project directory if you haven't already.
2. Run the Django development server:
    ```bash
    python manage.py runserver
    ```
3. Access the application by visiting `http://localhost:8000` in your web browser.

## How It Works

1. **Image Upload**: Users upload images of plant leaves suspected to be affected by diseases to the ZyrAI platform.

2. **Image Processing**: The uploaded images are processed using advanced computer vision techniques to extract relevant features and identify disease patterns.

3. **Machine Learning Analysis**: ZyrAI employs machine learning algorithms trained on extensive datasets of labeled leaf images to analyze and classify diseases accurately and generates the mask that shows the diseased zones.

4. **Result Presentation**: The platform presents users with comprehensive diagnostic reports, including disease severity predictions, disease zone delineations, and recommended actions for disease management.

## Benefits

- **Precision Agriculture**: ZyrAI facilitates precision agriculture by enabling farmers to target interventions only where they are needed, reducing the use of pesticides and other agrochemicals.

- **Early Disease Detection**: By detecting diseases at early stages of development, ZyrAI helps prevent crop losses and ensures optimal plant health and yield.

- **Cost-Effective Solutions**: The platform offers cost-effective solutions for disease management, allowing farmers to optimize resource allocation and maximize profitability.

- **Data-Driven Decision Making**: ZyrAI empowers farmers with data-driven insights, enabling informed decision-making and better crop management practices.

## Future Enhancements

- **Expanded Disease Database**: Continuously expanding the platform's disease database to encompass a wider range of plant diseases and variations.

- **Integration with IoT Devices**: Integrating ZyrAI with IoT devices and sensors to enable real-time monitoring of crop health parameters in the field.

- **Localized Recommendations**: Providing region-specific recommendations tailored to local climate, soil conditions, and prevalent diseases.

## Contribution

Contributions to ZyrAI are welcome! Whether you're interested in improving the user interface, enhancing machine learning models, or adding new features, feel free to contribute to the project by forking the repository, making your changes, and submitting a pull request.

## Technical Tasks

- **Improve Model Accuracy**: Continuously train and fine-tune the deep learning models to improve disease detection accuracy and reduce false positives.

- **Optimize Performance**: Implement optimizations to enhance the platform's performance, such as parallel processing for image analysis and caching frequently accessed data.

- **Enhance User Experience**: Conduct user testing and gather feedback to identify areas for improvement in the user interface and overall user experience.

- **Security Measures**: Implement robust security measures to protect user data and prevent unauthorized access to the platform.

- **Documentation**: Maintain comprehensive documentation for the project, including installation instructions, usage guidelines, and developer documentation.


## Contributing

We welcome contributions from the community. If you'd like to contribute to LeafAI-Django, please fork the repository, make your changes, and submit a pull request !

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


