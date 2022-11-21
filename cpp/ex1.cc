#ifdef USE_ATOMIC_N
#include <atomic>
#endif

class CountInstances {
public:
    CountInstances() {
        ++n_instances_;
    }

    ~CountInstances() {
        --n_instances_;
    }

    int nobjs() const {
        return n_instances_; // If using atomics, load could use a more relaxed
                             // memory order, such as memory_order_acquire
    }

private:
#ifdef USE_ATOMIC_N
    // Can be used in a multi-thread program
    static atomic<int> n_instances_;
#else
    // Using a bare int mean races if used in a multi-threaded context
    static int n_instances_;
#endif
};
