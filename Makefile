PYTHON = python3
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test1 the project type make test1"
	@echo "To test2 the project type make test2"
	@echo "To test3 the project type make test3"
	@echo "------------------------------------"

install:
	$ pip3 install ply
test1:
	${PYTHON} php_lexico.py test1.txt
test2:
	${PYTHON} php_lexico.py test2.txt
test3:
	${PYTHON} php_lexico.py test3.txt

autores:
	@echo "---------------AUTORES-----------------"
	@echo "Joseph Danilo Avila Alvarez"
	@echo "Daniel Roberto Sanchez Jarrin"
	@echo "Angel Arturo Jumbo Apolo"
	@echo "------------------------------------"
