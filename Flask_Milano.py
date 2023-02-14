from flask import Flask, render_template #restituisce il file html creato
app = Flask(__name__) #sempre

@app.route('/')
def benvenuto():
    return render_template('home_page.html') 

@app.route('/immagini')
def immagini():
    return render_template('immagini.html') 

@app.route('/duomo')
def duomo():
    return render_template('duomo.html')

@app.route('/basilica')
def basilica():
    return render_template('basilica.html')

@app.route('/galleria')
def galleria():
    return render_template('galleria.html')

@app.route('/santamaria')
def santamaria():
    return render_template('santamaria.html')

if __name__ == '__main__': #sempre
  app.run(host='0.0.0.0', port=3245, debug=True) #sempre

#Esercizio:
#realizzare un server web con flask che offra le seguenti funzionalità.
#1. homepage deve fornire una breve descrizione delle caratteristiche della città di milano
#2. al link <nome sito>/immagini deve essere visualizzate le immagini di 4 monumenti di milano (controllare sul sito del prof come si fa a mettere le immagini)
#3. fare in modo che cliccando sull'immagine si venga mandati ad un brevo testo descrittivo del monumento (sito prof)
