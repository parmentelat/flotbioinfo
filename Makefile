all: norm

# work on one week at a time with FOCUS=W2
FOCUS     = $(wildcard w?)

# for phony targets
force:

####################
# run nbnorm on all notebooks
norm normalize: normalize-notebook

# nbnorm.py now is python3 script
# it is not in the git repo for bioinfo so locate from PATH
NORM = nbnorm.py
NORM_OPTIONS = --author "Thierry Parmentelat" --author "François Rechenmann" --version 1.0 --sign

# -type f : we need to skip symlinks
normalize-nb normalize-notebook: force
	git ls-files $(FOCUS) | grep '\.ipynb$$' | xargs $(NORM) $(NORM_OPTIONS)

.PHONY: norm normalize normalize-nb normalize-notebook

