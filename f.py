from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    data = request.get_json()
    zip_code = data.get('zipCode')
    demographic_type = data.get('demographicType')


    graph_filename = f"{demographic_type}_{zip_code}.png"
    script_name = 'generate_demographic_graph.py'
    
    subprocess.run(['python', script_name, zip_code, demographic_type, f'static/graphs/{graph_filename}'])

    return jsonify(success=True, graphFilename=graph_filename)

if __name__ == '__main__':
    app.run(debug=True)
