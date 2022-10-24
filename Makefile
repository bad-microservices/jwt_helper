checkfiles = jwt_helper/ doc/

help:
	@echo "jwt_helper Makefile"
	@echo "usage: make <target>"
	@echo "Targets:"
	@echo "    - doc       Build the documentation"
	@echo "    - package   Build jwt_helper as package"

deps:
	pipenv install --dev

doc: deps
	rm -fR ./build
	pipenv run sphinx-build -M html doc _build

package: deps
	rm -fR dist/
	pipenv run python -m build
