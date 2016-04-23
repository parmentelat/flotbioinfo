BINS = nw_c_like nw_boost nw_boost_rect
PYS = nw_naive.py nw_dict_tuple.py

##########
TIME_BINS = $(foreach bin,$(BINS),$(bin).time)
TIME_PYS = $(foreach py,$(PYS),$(py).time)
TIMES = $(TIME_BINS) $(TIME_PYS)

all: $(BINS)
time: $(TIMES)
time_bin: $(TIME_BINS)
time_py: $(TIME_PYS)
clean:
	rm -f $(BINS) $(TIMES)

####################
define cxx_target
$(1):
	g++ -std=c++11 -DNDEBUG -DBOOST_UBLAS_NDEBUG -O2 -o $(1) $(1).cxx
$(1).time: $(1)
	time $(1) 2>&1 | tee $(1).time
endef

####################
define py_time_target
$(1).time: $(1)
	time python2 $(1) 2>&1 | tee $(1).time
$(1).time3: $(1)
	time python3 $(1) 2>&1 | tee $(1).time
endef

$(foreach bin,$(BINS),$(eval $(call cxx_target,$(bin))))
$(foreach py,$(PYS),$(eval $(call py_time_target,$(py))))
