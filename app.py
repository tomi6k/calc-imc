# altura = float(input("ALTURA: "))
# peso = float(input("PESO: "))

# alturaD =  altura * altura
# imc = peso / float(alturaD)


# print("TU IMC ES IGUAL A: ", imc)

# if imc > 24.9:
#     print("TIENE SOBREPESO")
# elif imc < 18.5:
#     print("ESTA CON BAJO PESO")
# else:
#     print("SU PESO ES NORMAL")


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/action")
def calcular():
    if  request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])

        alturaD = altura * altura
        imc = peso / float(alturaD) 

        print("TU IMC ES IGUAL A: ", imc)

        if imc > 24.9:
            print("TIENE SOBREPESO")
        elif imc < 18.5:
            print("ESTA CON BAJO PESO")
        else:
            print("SU PESO ES NORMAL")



if __name__ == "__main__":
    app.run(port = 5000, debug = True)