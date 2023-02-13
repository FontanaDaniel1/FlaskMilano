from flask import Flask, render_template #restituisce il file html creato
app = Flask(__name__) #sempre

@app.route('/benvenuto')
def benvenuto():
    return render_template('benvenuto.html')

if __name__ == '__main__': #sempre
  app.run(host='0.0.0.0', port=3245, debug=True) #sempre