format:
	isort wordcodegen
	pycln wordcodegen
	pyupgrade --py311-plus `find wordcodegen -name "*.py"` || true
	black wordcodegen
