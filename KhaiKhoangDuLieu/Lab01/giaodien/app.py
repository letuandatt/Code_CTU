import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file, flash
import joblib
from io import BytesIO  # Import BytesIO for in-memory file handling
from models.train import process_input, get_data_and_process
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

# Load các model đã huấn luyện
model_paths = {
    'KNN': 'models/KNN_iris.joblib',
    'NaiveBayes': 'models/NaiveBayes_iris.joblib',
    'DecisionTree': 'models/DecisionTree_iris.joblib',
    'RandomForest': 'models/RandomForest_iris.joblib',
    'SVM': 'models/SVM_iris.joblib',
    'MLP': 'models/MLP_iris.joblib',
}

# Load file chuẩn hóa
scaler_path = 'models/scaler.joblib'

# Lưu tên các loại hoa
predictions = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

# Lịch sử dự đoán
prediction_history = []

# Load model
def load_model(model_name):
    model_path = model_paths.get(model_name)
    if model_path:
        return joblib.load(model_path)
    else:
        raise ValueError(f"Model {model_name} not found!")

@app.route('/')
def index():
    return render_template('index.html', history=prediction_history)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        selected_model = request.form['model']
        model = load_model(selected_model)

        # Kiểm tra phương thức nhập liệu
        input_method = request.form.get('input_method')

        # Nếu nhập liệu thủ công
        if input_method == 'manual':
            # Lấy dữ liệu từ form
            feature1 = float(request.form['sepal.length'])
            feature2 = float(request.form['sepal.width'])
            feature3 = float(request.form['petal.length'])
            feature4 = float(request.form['petal.width'])

            # Chuẩn bị dữ liệu để dự đoán (dùng numpy để tạo mảng 2D)
            input_data = process_input([[feature1, feature2, feature3, feature4]], scaler_path)

            # Dự đoán
            prediction = model.predict(input_data)[0]

            # Thêm vào lịch sử dự đoán
            prediction_history.append({
                'model': selected_model,
                'sepal_length': feature1,
                'sepal_width': feature2,
                'petal_length': feature3,
                'petal_width': feature4,
                'prediction': predictions[prediction]
            })

            return redirect(url_for('index'))

        # Nếu người dùng chọn tải lên file csv
        elif input_method == 'file':
            file = request.files.get('file')
            if not file:
                raise ValueError("No file uploaded!")

            # Đọc file csv
            df = pd.read_csv(file)
            print(df)
            if not all(col in df.columns for col in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']):
                raise ValueError("Missing required columns in the CSV file!")

            # Chuẩn bị dữ liệu từ file CSV
            input_data = process_input(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']], scaler_path)

            # Dự đoán từng hàng
            predictions_from_file = model.predict(input_data)

            # Tạo DataFrame kết quả dự đoán
            df['prediction'] = [predictions[p] for p in predictions_from_file]

            # Lưu kết quả vào file CSV
            output_filename = "prediction.csv"
            df.to_csv(output_filename, index=False)

            # Trả file CSV về cho người dùng
            return (
                send_file(output_filename, as_attachment=True, download_name=output_filename),
                redirect(url_for('index'))
            )

    except Exception as e:
        return render_template('index.html', error=str(e))


@app.route('/clear_history', methods=['POST'])
def clear_history():
    """API to clear the prediction history"""
    prediction_history.clear()  # Clear the history list
    return jsonify({"status": "success"})


@app.route('/delete_prediction/<int:index>', methods=['POST'])
def delete_prediction(index):
    """API to delete a specific prediction based on index"""
    if 0 <= index < len(prediction_history):
        del prediction_history[index]
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Index out of range"}), 400


@app.route('/download_history', methods=['GET'])
def download_history():
    # Check if there is history to download
    if not prediction_history:
        flash("No prediction history to download.", "error")
        return redirect(url_for('index'))  # Redirect back to the main page

    df = pd.DataFrame(prediction_history)
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return send_file(output, mimetype='text/csv', as_attachment=True, download_name='prediction_history.csv')

if __name__ == '__main__':
    app.run(debug=True)
