# Image Color Palette Generator App
This project is a simple Flask web application that allows users to upload images and get the most prominent colors in the image. It uses Python libraries such as Flask, Pillow (PIL), NumPy, and collections for color extraction and processing.

---

## Features
* **Upload Images**: Users can upload images in various formats (PNG, JPG, JPEG, BMP, WEBP, SVG).
* **Extract Colors**: The application analyzes the uploaded image and extracts the top colors based on pixel frequency.
* **Display Results**: Displays the image alongside the extracted top colors in hexadecimal format.

---

## Requirements
To run the project locally, ensure that you have the following installed:
* Python 3.x
* Flask
* Pillow
* NumPy
* Flask-Bootstrap
* werkzeug 

### Installing dependencies
1. Clone the repository:
    ```commandline
    git clone https://github.com/shrabhay/Image-Color-Palette-Generator.git
    cd Image-Color-Palette-Generator
    ```

2. Install the required packages

---

## Usage
1. Run the Flask App:
    ```commandline
    python3 image_color_palette_generator.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`. You will be able to upload an image and view the top colors in the image.

### File Uploads
* Images are saved in the `static/uploads/` directory.
* The application only allows the following file formats: `png`, `jpg`, `jpeg`, `bmp`, `webp`, `svg`.

### Top Colors
* The top colors are extracted using pixel analysis and displayed in hexadecimal format.
* The application shows the top 10 most common colors by default, but this can be adjusted in the `get_top_colors` function.

---

## Folder Structure
```text
Image_Color_Palette_Generator/
│
├── image_color_palette_generator.py               # Main Flask application
├── static/
│   └── uploads/                                   # Directory for uploaded images
├── templates/
│   ├── index.html                                 # Homepage template
│   └── results.html                               # Template for displaying results
└── README.md                                      # Project documentation
```

---

## Contributing
If you have suggestions or improvements, feel free to fork this repository and submit a pull request. If you encounter any issues, please open an issue on GitHub.

---

## License
This project is licensed under the MIT License.