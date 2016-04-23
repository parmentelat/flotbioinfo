BINS = nw_c_like nw_boost nw_boost_rect

all: $(BINS)
clean:
	rm -f $(BINS)

define cxx_target
$(1):
	g++ -std=c++11 -DNDEBUG -DBOOST_UBLAS_NDEBUG -O2 -o $(1) $(1).cxx
endef

$(foreach bin,$(BINS),$(eval $(call cxx_target,$(bin))))
