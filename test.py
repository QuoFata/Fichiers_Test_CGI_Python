#!C:\laragon\bin\python\python-3.6.1\python.exe

# Envoi d'un entête (header) dans le message 'réponse'
print("Content-Type: text/html; charset=ISO-8859-15")

# Envoi d'une ligne vide de séparation de la zone d'entêtes et de 'body' du message 'réponse'
print()

# Envoi du contenu du 'body' du message 'réponse'
print ("""
<!DOCTYPE html>
<html lang="fr-fr">
	<head>

		<meta charset="ISO-8859-15">
		<title>NSI-TestWebServeur-CGI-Python</title>
		<meta content="Jean-Michel HAROUY" name="author">
		<meta content="Fichier HTML destin&eacute; &agrave; tester le fonctionnement d'un serveur web local" name="description">
		<style>
			h1,h2{	text-align: center;
					font-family: Berlin Sans FB;
					font-weight: normal;
			}
			h2{	color: rgb(153, 51, 153);
			}
			hr{	height: 2px;
				width: 80%;
			}
			.succes{	color:#FF0000;
			}
			.nomFichier{	text-align: center;
							font-family: Verdana;
							font-weight: bold;
			}
			.placeFichier{	text-align: center;
							font-family: Helvetica,Arial,sans-serif;
							font-size:0.9em;
							font-weight: normal;
			}
			.zoneBouton{	margin: 10px;
							text-align: center;
			}
			button{	font-size: 12px;
					width: 150px;
					height: 40px;
					font-family: Verdana;
					color: rgb(204, 0, 0);
			}
			.auteur, .licence{	text-align: center;
								padding: 10px;
								font-size: 10px;
								font-family: Helvetica,Arial,sans-serif;
								color: rgb(102, 102, 102);
			}
		</style>
	</head> 
	
	<body>

		<h1>Num&eacute;riques et Sciences Informatiques</h1>
		<hr>
		<h2>Monter un serveur web local Apache avec interface cgi pour scripts python</h2>
		<p class="nomFichier">Fichier de &nbsp;test : test.py</p>
		<p class="placeFichier">Ce fichier doit &ecirc;tre plac&eacute; &agrave; dans le répertoire 'cgi-bin' du serveur</p>
		<hr>
		<h1 class="succes">Test Réussi !</h1>
		<hr>
		<div class="zoneBouton">
				<a href="../index.html">
					<button name="essai" type="button">Retour</button>
				</a>
		</div>
		<div class="auteur">R&eacute;alis&eacute; par :&nbsp; 
			<a href="https://ent.sapiensjmh.top/svt/?page_id=10120">Jean-Michel HAROUY</a>
		</div>
		<div class="licence">
			<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/fr/">
				<img alt="Licence Creative Commons" style="border-width: 0pt;" src="https://i.creativecommons.org/l/by-nc-sa/3.0/fr/88x31.png">
			</a>
			<br>
			Ce fichier est mis &agrave; disposition selon les termes de la 
				<a style="color: rgb(102, 102, 102);" rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/fr/">
					Licence Creative Commons Attribution - Pas d&rsquo;Utilisation Commerciale - Partage dans les M&ecirc;mes Conditions 3.0 France.&gt;
				</a>
		</div>
	</body>
</html>
""")