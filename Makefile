FOCUS = w?

all: norm

# run nbnorm on all notebooks
norm normalize: normalize-notebook

# add the --sign option only on Thierry's macos to reduce noise-only changes
NORM = tools/nbnorm.py
NORM_OPTIONS = --author "Thierry Parmentelat" --author "François Rechenmann" --version 1.0

# -type f : we need to skip symlinks
normalize-nb normalize-notebook: force
	git ls-files $(FOCUS) | grep '\.ipynb$' | xargs $(NORM) $(NORM_OPTIONS)

.PHONY: norm normalize normalize-nb normalize-notebook

