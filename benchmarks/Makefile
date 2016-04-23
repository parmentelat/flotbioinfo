CBINS = nw_c
CXXBINS = nw_c_like nw_boost nw_boost_rect
PYS = nw_naive nw_naive_xrange nw_dict_tuple
BASE_PYS = naive naive2 naive3 npnaive npnaive2 npnaive3 dict_tuple

##########
BINS = $(CBINS) $(CXXBINS)

TIME_CBINS = $(foreach bin,$(CBINS),$(bin).time)
TIME_CXXBINS = $(foreach bin,$(CXXBINS),$(bin).time)
TIME_PYS = $(foreach py,$(PYS),$(py).time)
TIME_BASE_PYS = $(foreach py,$(BASE_PYS),base_$(py).time)
TIME_BASE3_PYS = $(foreach py,$(BASE_PYS),base_$(py).time3)
TIMES = $(TIME_CBINS) $(TIME_CXXBINS) $(TIME_PYS) $(TIME_BASE_PYS)

all: $(BINS)

time: $(TIMES)
time_bin: $(TIME_CBINS) $(TIME_CXXBINS)
py time_py: $(TIME_PYS) $(TIME_BASE_PYS)
base time_base: $(TIME_BASE_PYS)
base3 time_base3: $(TIME_BASE3_PYS)
clean:
	rm -f $(BINS) $(TIMES)

####################
define c_target
$(1):
	gcc -DNDEBUG -DBOOST_UBLAS_NDEBUG -O2 -o $(1) $(1).c
endef

define cxx_target
$(1):
	g++ -std=c++11 -DNDEBUG -DBOOST_UBLAS_NDEBUG -O2 -o $(1) $(1).cxx
endef

####################
define bin_time_target
$(1).time: $(1)
	{ time $(1) ; } 2>&1 | tee $(1).time
endef

define py_time_target
$(1).time: $(1).py
	{ time python2 $(1).py ; } 2>&1 | tee $(1).time
$(1).time3: $(1).py
	{ time python3 $(1).py ; } 2>&1 | tee $(1).time3
endef

define base_py_time_target
base_$(1).time: base.py
	{ time python2 base.py $(1) ; } 2>&1 | tee base_$(1).time
base_$(1).time3: base.py
	{ time python3 base.py $(1) ; } 2>&1 | tee base_$(1).time3
endef

####################
$(foreach bin,$(CBINS),$(eval $(call c_target,$(bin))))
$(foreach bin,$(CXXBINS),$(eval $(call cxx_target,$(bin))))
$(foreach bin,$(CBINS) $(CXXBINS),$(eval $(call bin_time_target,$(bin))))
$(foreach py,$(PYS),$(eval $(call py_time_target,$(py))))
$(foreach py,$(BASE_PYS),$(eval $(call base_py_time_target,$(py))))
