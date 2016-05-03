CBINS = nw_c
CXXBINS = nw_naive nw_rect nw_c_like
PYS = nw_naive nw_rect nw_naive_range nw_dict_tuple

### pypy has no numpy installed
BASE_PYS = naive naive2 naive3 naive3_comp naive_flat naive_np naive2_np naive3_np dict_tuple
BASE_PYPYS = $(filter-out %_np,$(BASE_PYS))

##########
BINS = $(CBINS) $(CXXBINS)

TIME_CBINS = $(foreach bin,$(CBINS),$(bin).bin.time)
TIMES += $(TIME_CBINS)
TIME_CXXBINS = $(foreach bin,$(CXXBINS),$(bin).bin.time)
TIMES += $(TIME_CXXBINS)
TIME_PYS = $(foreach py,$(PYS),$(py).py.time)
TIMES += $(TIME_PYS)
TIME_PYPYS = $(foreach py,$(PYS),$(py).pypy.time)
TIMES += $(TIME_PYPYS)
#
TIME_BASE_PYS = $(foreach py,$(BASE_PYS),base_$(py).py.time)
TIMES += $(TIME_BASE_PYS)
TIME_BASE_PYPYS = $(foreach py,$(BASE_PYPYS),base_$(py).pypy.time)
TIMES += $(TIME_BASE_PYPYS)
TIME_BASE3_PYS = $(foreach py,$(BASE_PYS),base_$(py).py3.time)
TIMES += $(TIME_BASE3_PYS)

all: $(BINS)

time: $(TIMES)
time_bin: $(TIME_CBINS) $(TIME_CXXBINS)
py time_py: $(TIME_PYS)
pypy time_pypy: $(TIME_PYPYS)
time_nw: $(TIME_CBINS) $(TIME_CXXBINS) $(TIME_PYS) $(TIME_PYPYS)
# 
base time_base: $(TIME_BASE_PYS)
base3 time_base3: $(TIME_BASE3_PYS)
pypy time_pypy: $(TIME_BASE_PYPYS)
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
$(1).bin.time: $(1)
	{ time $(1) ; } 2>&1 | tee $(1).bin.time
endef

define py_time_target
$(1).py.time: $(1).py
	{ time python2 $(1).py ; } 2>&1 | tee $(1).py.time
$(1).py3.time: $(1).py
	{ time python3 $(1).py ; } 2>&1 | tee $(1).py3.time3
$(1).pypy.time: $(1).py
	{ time pypy $(1).py ; } 2>&1 | tee $(1).pypy.time
endef

define base_py_time_target
base_$(1).py.time: base.py
	{ time python2 base.py $(1) ; } 2>&1 | tee base_$(1).py.time
base_$(1).py3.time: base.py
	{ time python3 base.py $(1) ; } 2>&1 | tee base_$(1).py3.time
base_$(1).pypy.time: base.py
	{ time pypy base.py $(1) ; } 2>&1 | tee base_$(1).pypy.time
endef

####################
$(foreach bin,$(CBINS),$(eval $(call c_target,$(bin))))
$(foreach bin,$(CXXBINS),$(eval $(call cxx_target,$(bin))))
$(foreach bin,$(CBINS) $(CXXBINS),$(eval $(call bin_time_target,$(bin))))
$(foreach py,$(PYS),$(eval $(call py_time_target,$(py))))
$(foreach py,$(BASE_PYS),$(eval $(call base_py_time_target,$(py))))

####################
outline:
	grep real nw_{naive,rect}.[a-z]*.time
