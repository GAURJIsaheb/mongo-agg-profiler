"""
mongo_agg_profiler - MongoDB aggregation profiler that explains pipelines and suggests indexing improvements.
"""

__version__ = "0.1.0"

from .run_and_parse_aggregate_explai import MongoAggProfiler
from .types import MongoAggProfilerOptions, MongoAggProfilerResult
from .exceptions import MongoAggProfilerError, ConfigurationError, ValidationError

__all__ = [
    "MongoAggProfiler",
    "MongoAggProfilerOptions",
    "MongoAggProfilerResult",
    "MongoAggProfilerError",
    "ConfigurationError",
    "ValidationError",
]
