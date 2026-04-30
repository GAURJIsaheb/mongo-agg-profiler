"""Type definitions for mongo_agg_profiler."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class MongoAggProfilerOptions:
    """Configuration options for MongoAggProfiler.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Run and parse aggregate() explain plans into readable summaries
        feature_2: Configuration for: Detect common pipeline anti-patterns (unbounded $lookup, $sort after $group)
        feature_3: Configuration for: Index suggestion engine based on match/sort stages and winning plan
        feature_4: Configuration for: Compare before/after explains and output a diff report
        feature_5: Configuration for: Export reports as JSON/Markdown for PR reviews
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None
    feature_5: Optional[dict[str, Any]] = None


@dataclass
class MongoAggProfilerResult:
    """Result returned by MongoAggProfiler operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
