# mongo_agg_profiler

MongoDB aggregation profiler that explains pipelines and suggests indexing improvements.

## Installation

```bash
pip install mongo_agg_profiler
```

## Quick Start

```python
from mongo_agg_profiler import MongoAggProfiler

instance = MongoAggProfiler()
result = instance.run()
print(result)
```

## Features

- Run and parse aggregate() explain plans into readable summaries
- Detect common pipeline anti-patterns (unbounded $lookup, $sort after $group)
- Index suggestion engine based on match/sort stages and winning plan
- Compare before/after explains and output a diff report
- Export reports as JSON/Markdown for PR reviews

## API Reference

### `MongoAggProfiler`

#### Constructor

```python
MongoAggProfiler(options: MongoAggProfilerOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `MongoAggProfilerResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/mongo_agg_profiler/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
