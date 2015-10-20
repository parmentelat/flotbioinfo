all: norm v2

# work on one week at a time with FOCUS=w1
FOCUS     = $(wildcard w?)
NOTEBOOKS = $(shell git ls-files $(FOCUS) | grep '\.ipynb$$')

# for phony targets
force:

####################
# our notebooks now use format 4.0
# to downgrade one can run this

V2DIR = nbformat2
NOTEBOOKS_V2 = $(foreach notebook,$(NOTEBOOKS),$(V2DIR)/$(notebook))

v2: $(NOTEBOOKS_V2)

define v2_target
$(V2DIR)/$(1):
	@mkdir -p $(dir $(V2DIR)/$(1))
	jupyter nbconvert --to notebook --nbformat=2 --output=$(V2DIR)/$(1) $(1)
endef

$(foreach notebook,$(NOTEBOOKS),$(eval $(call v2_target,$(notebook))))

####################
# run nbnorm on all notebooks
norm normalize: normalize-notebook

# nbnorm.py now is python3 script
# it is not in the git repo for bioinfo so locate from PATH
NORM = nbnorm.py
NORM_OPTIONS = --author "Thierry Parmentelat" --author "François Rechenmann" --version 1.0 --sign

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
