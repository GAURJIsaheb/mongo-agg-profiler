#!/usr/bin/env python3
"""Basic usage example for mongo_agg_profiler."""

from mongo_agg_profiler import MongoAggProfiler, MongoAggProfilerOptions


def main() -> None:
    # Create with default options
    instance = MongoAggProfiler()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = MongoAggProfilerOptions(verbose=True)
    instance = MongoAggProfiler(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
