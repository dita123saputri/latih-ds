from flask import Flask, request, jsonify

import joblib

# Inisiasi aplikasi Flask
app = Flask(__name__)

# Memuat model yang telah disimpan