"""Tests for mongo_agg_profiler."""

from mongo_agg_profiler import MongoAggProfiler, MongoAggProfilerOptions


class TestMongoAggProfiler:
    def test_create_instance_with_defaults(self) -> None:
        instance = MongoAggProfiler()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = MongoAggProfilerOptions(verbose=True)
        instance = MongoAggProfiler(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = MongoAggProfiler()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = MongoAggProfiler()
        result = instance.run()
        assert result.error is None
