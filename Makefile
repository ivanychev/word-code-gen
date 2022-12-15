format:
	isort wordcodegen
	pycln wordcodegen
	pyupgrade --py310-plus `find wordcodegen -name "*.py"` || true
	black wordcodegen