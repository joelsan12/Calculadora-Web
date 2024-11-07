from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        op = int(request.form['opcion'])
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        resultado = None

        if op == 1:
            resultado = n1 + n2
            operacion = "Suma"
        elif op == 2:
            resultado = n1 - n2
            operacion = "Resta"
        elif op == 3:
            resultado = n1 * n2
            operacion = "Multiplicación"
        elif op == 4:
            if n2 != 0:
                resultado = n1 / n2
                operacion = "División"
            else:
                flash("No se puede dividir entre cero.")
                return redirect(url_for('index'))

        return render_template('index.html', resultado=resultado, operacion=operacion)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
