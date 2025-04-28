from flask import Flask, render_template, send_file
import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import io

# Load the dataset
df = pd.read_feather('sample_dataset.feather')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html') 

@app.route('/data')
def Load_and_Send():
    table = pa.Table.from_pandas(df)
    buffer = io.BytesIO()
    feather.write_feather(table, buffer)
    buffer.seek(0)
    return send_file(
    buffer,
    mimetype='application/vnd.apache.arrow.file',
    as_attachment=False
    )

if __name__ == '__main__':
    app.run(debug=True)