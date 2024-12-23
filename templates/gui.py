import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QWidget, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import requests


class CropRecommendationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Recommendation System")
        self.setGeometry(100, 100, 600, 700)  # Ukuran jendela GUI
        self.initUI()

    def initUI(self):
        # Font default
        title_font = QFont("Poppins", 20, QFont.Bold)
        label_font = QFont("Poppins", 12)

        # Layout utama
        main_layout = QVBoxLayout()

        # Judul aplikasi
        self.title = QLabel("🌱 Crop Recommendation System 🌱")
        self.title.setFont(title_font)
        self.title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title)

        # Form input
        form_layout = QFormLayout()
        form_layout.setVerticalSpacing(15)

        self.nitrogen_input = self.create_input(form_layout, "Nitrogen (N):", label_font)
        self.phosphorus_input = self.create_input(form_layout, "Phosphorus (P):", label_font)
        self.potassium_input = self.create_input(form_layout, "Potassium (K):", label_font)
        self.temperature_input = self.create_input(form_layout, "Temperature (°C):", label_font)
        self.humidity_input = self.create_input(form_layout, "Humidity (%):", label_font)
        self.ph_input = self.create_input(form_layout, "pH Level:", label_font)
        self.rainfall_input = self.create_input(form_layout, "Rainfall (mm):", label_font)

        main_layout.addLayout(form_layout)

        # Tombol Prediksi
        self.predict_button = QPushButton("Get Recommendation For Your Future Crop!")
        self.predict_button.setFont(QFont("Poppins", 14))
        self.predict_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        self.predict_button.clicked.connect(self.predict_crop)
        main_layout.addWidget(self.predict_button)

        # Hasil prediksi
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Poppins", 16))
        self.result_label.setStyleSheet("color: #4CAF50; text-align: center;")
        self.result_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def create_input(self, form_layout, label_text, label_font):
        label = QLabel(label_text)
        label.setFont(label_font)
        input_field = QLineEdit()
        input_field.setStyleSheet("padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-size: 14px;")
        form_layout.addRow(label, input_field)
        return input_field

    def predict_crop(self):
        try:
            # Ambil input dari field
            data = {
                "nitrogen": float(self.nitrogen_input.text()),
                "phosphorus": float(self.phosphorus_input.text()),
                "potassium": float(self.potassium_input.text()),
                "temperature": float(self.temperature_input.text()),
                "humidity": float(self.humidity_input.text()),
                "ph": float(self.ph_input.text()),
                "rainfall": float(self.rainfall_input.text()),
            }

            # Kirim data ke server Flask
            url = "http://127.0.0.1:5000/predict"
            response = requests.post(url, data=data)

            if response.status_code == 200:
                result = response.json()
                if "recommendation" in result:
                    self.result_label.setText(f"Recommended Crop: {result['recommendation']}")
                elif "error" in result:
                    self.show_error(f"Error: {result['error']}")
            else:
                self.show_error("Failed to connect to the server. Please try again.")
        except ValueError:
            self.show_error("Please fill in all fields with valid numbers.")
        except Exception as e:
            self.show_error(f"Unexpected error: {str(e)}")

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CropRecommendationApp()
    window.show()
    sys.exit(app.exec_())
