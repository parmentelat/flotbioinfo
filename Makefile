all: norm v2

HOME=$(shell pwd)

# work on one week at a time with FOCUS=w1
FOCUS     = $(wildcard w?)
NOTEBOOKS = $(shell git ls-files $(FOCUS) | grep '\.ipynb$$')
NOTEBASES = $(subst .ipynb,,$(NOTEBOOKS))

# for phony targets
force:

####################
# our notebooks now use format 4.0
# to downgrade one can run this

# notebase -> full path of v2 notebook
define v2_path
$(HOME)/nbformat2/$(1).ipynb
endef

NOTEBOOKS_V2 = $(foreach notebase,$(NOTEBASES),$(call v2_path,$(notebase)))

v2: $(NOTEBOOKS_V2)

define v2_target
$(call v2_path,$(1)): $(1).ipynb
	@mkdir -p $(dir $(call v2_path,$(1)))
	jupyter nbconvert --to notebook --nbformat=2 --output=$(call v2_path,$(1)) $(1).ipynb
endef

$(foreach notebase,$(NOTEBASES),$(eval $(call v2_target,$(notebase))))

.PHONY: v2
####################
# the notebooks saved in python format

# notebase -> full path of py module
define py_path
$(HOME)/modules/$(notdir $(subst -,_,$(1))).py
endef

NOTEBOOKS_PY = $(foreach notebase,$(NOTEBASES),$(call py_path,$(notebase)))

py: $(NOTEBOOKS_PY)
python: py

define py_target
$(call py_path,$(1)): $(1).ipynb
	@mkdir -p $(dir $(call py_path,$(1)))
	jupyter nbconvert --to python --output=$(call py_path,$(1)) $(1).ipynb
endef

$(foreach notebase,$(NOTEBASES),$(eval $(call py_target,$(notebase))))

####################
# run nbnorm on all notebooks
norm normalize: normalize-notebook

# nbnorm.py now is python3 script
# it is not in the git repo for bioinfo so locate from PATH
NORM = nbnorm.py
NORM_OPTIONS = --author "François Rechenmann" --author "Thierry Parmentelat" --version 1.0 --sign

# -type f : we need to skip symlinks
normalize-nb normalize-notebook: force
	 $(NORM) $(NORM_OPTIONS) $(NOTEBOOKS)

.PHONY: norm normalize normalize-nb normalize-notebook

#################### convenience, for debugging only
# make +foo : prints the value of $(foo)
# make ++foo : idem but verbose, i.e. foo=$(foo)
++%: varname=$(subst +,,$@)
++%:
	@echo "$(varname)=$($(varname))"
+%: varname=$(subst +,,$@)
+%:
	@echo "$($(varname))"
