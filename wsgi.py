from flask import Flask
application = Flask(__name__)

@application.route("/")
def test():
print("Test de programme en Python dans OpenShift qui calcul si une année est bissextile ou non.")
annee = input ("Entrez une année : ")
annee = int(annee)
if(annee % 400 or (annee % 400 and annee % 100 != 0)) :
	return "L année saisie est bissextile."
else :
	return "L année saisie n'est pas bissextile."
#input('Appuyez sur ENTREE pour quitter')

if __name__ == "__main__":
    application.run()
