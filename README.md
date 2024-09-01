# ProtiCalc

ProtiCalc is a comprehensive bioinformatics application for protein sequence analysis. Built with Python and Kivy, this app provides a user-friendly interface for calculating various protein parameters and visualizing protein composition.

## Features

- **Protein Sequence Analysis**: Enter any protein sequence to calculate key parameters.
- **Amino Acid Composition**: Visualizes the amino acid composition using a custom-built bar chart.
- **Atomic Composition**: Calculates and displays the atomic composition of the protein.
- **Physico-Chemical Parameters**: Calculates properties like molecular weight, isoelectric point, GRAVY, and more.
- **Secondary Structure Prediction**: Estimates the fractions of helix, turn, and sheet structures.
- **Molecular Descriptors**: Provides detailed molecular descriptors for comprehensive analysis.

## Installation

ProtiCalc is available as an Android APK. You can download it directly from [Here](https://mega.nz/file/ES02jQZA#gQxUdfkN-3p81gqiXVF4CoCUs26FprJEDTtygVb-PqM).

To build from source:

1. Clone the repository:
   ```
   git clone https://github.com/OuchenTech/ProtiCalc.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python main.py
   ```

## Usage

1. Launch the ProtiCalc app on your device.
2. Tap the "Start" button to navigate to Protein Analysis Screen.
3. Enter or paste a protein sequence in the input field.
4. Tap the "Compute Parameters" button.
5. View the results in the various sections below.

## Screen Shots:

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_1.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_2.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_3.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_4.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_5.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_6.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_7.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_8.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_9.jpg)

![](https://github.com/OuchenTech/ProtiCalc-0.1/blob/main/screenshots/Screenshot_10.jpg)

## Technologies Used

- Python
- Kivy
- KivyMD
- Biopython
- Peptides
- kivygradient
- Our Custom Bar Chart. [Link](https://github.com/OuchenTech/Kivy-Charts)

## Building the APK

This project uses GitHub Actions to automatically build the Android APK. The workflow is defined in `.github/workflows/build.yml`.

## Contributing

Contributions to ProtiCalc are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Kivy and KivyMD teams for their excellent frameworks.
- The Biopython and Peptides libraries for their comprehensive protein analysis tools.

## Contact

If you have any questions or feedback, please open an issue on this GitHub repository.

---

Happy protein analysis with ProtiCalc!
