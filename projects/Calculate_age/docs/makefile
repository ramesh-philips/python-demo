# Makefile for Sphinx documentation

# The path to the Sphinx source directory
SPHINXBUILD = sphinx-build
SPHINXOPTS = 
SPHINXDIR = source
BUILD_DIR = build

# The default target
all: html

# Build HTML documentation
html:
	$(SPHINXBUILD) -b html $(SPHINXDIR) $(BUILD_DIR)/html $(SPHINXOPTS)

# Build LaTeX documentation (if needed)
latex:
	$(SPHINXBUILD) -b latex $(SPHINXDIR) $(BUILD_DIR)/latex $(SPHINXOPTS)

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)
