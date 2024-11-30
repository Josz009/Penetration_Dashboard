
from flask import render_template, request, jsonify
from app.services.nmap_service import run_nmap_scan
from app.services.metasploit_service import run_metasploit_exploit
from app.services.report_service import export_csv, export_pdf
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/run_scan", methods=["POST"])
def run_scan():
    data = request.json
    target = data.get("target")
    options = data.get("options", "-sV")

    try:
        results = run_nmap_scan(target, options)
        return jsonify({"status": "success", "data": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/run_exploit", methods=["POST"])
def run_exploit():
    data = request.json
    module = data.get("module")
    target = data.get("target")
    payload = data.get("payload")

    try:
        results = run_metasploit_exploit(module, target, payload)
        return jsonify({"status": "success", "data": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/export_csv", methods=["GET"])
def export_csv_endpoint():
    file_path = export_csv()
    return jsonify({"status": "success", "file_path": file_path})

@app.route("/api/export_pdf", methods=["GET"])
def export_pdf_endpoint():
    file_path = export_pdf()
    return jsonify({"status": "success", "file_path": file_path})
