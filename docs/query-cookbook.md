# Query Cookbook

Recipes for querying the library programmatically. Everything here was run and verified against the repo (July 2026). Needs `jq` (any version) and/or `python3`; run from the repo root.

The three queryable layers:

| File(s) | What it knows |
| --- | --- |
| `papers/papers.json` | catalog: title/authors/venue/tags, PDF provenance, status, page counts |
| `papers/extracts/*.json` | per-paper structured extracts: tasks, datasets (with roles), models, theories (with usage), headline results, findings, limitations |
| `data/datasets.json` | dataset catalog: contents, source, license, size, vendored status, paper cross-refs |

Plus the full text itself in `papers/md/<key>/<key>.md` — plain grep works great.

## Extract schema quick reference

Each `papers/extracts/<key>.json` has: `key`, `ref` (guide number like `#3`), `title`, `authors`, `year`, `venue`, `paper_types`, `research_questions`, `tasks`, `humor_domains`, `modalities`, `languages`, `datasets_used` (`{name, role, size}` — role is `introduced` / `evaluated-on` / `trained-on` / `analyzed` / `source-material`), `models_evaluated` (strings), `methods_proposed`, `humor_theories` (`{theory, usage, detail}` — usage is `operationalized` / `motivation`), `evaluation_methods`, `headline_results` (`{finding, metric, value, dataset, best_system}`), `key_findings`, `limitations`, `safety_ethics_notes`, `artifacts` (`{code_url, data_url, other}`).

## Papers by dataset / theory / model / task

**Which papers used a given dataset (any role):**

```bash
jq -r 'select([.datasets_used[]?.name] | index("Oogiri-GO")) | .ref + "  " + .title' papers/extracts/*.json
```

**…restricted to a role** (e.g. actually evaluated on it, not just cited it):

```bash
jq -r 'select([.datasets_used[]? | select(.role == "evaluated-on") | .name] | index("Oogiri-GO")) | .ref + "  " + .title' papers/extracts/*.json
```

**Which papers operationalized a theory** (vs merely citing it as motivation):

```bash
jq -r 'select([.humor_theories[]? | select(.usage == "operationalized") | .theory] | index("GTVH")) | .ref + "  " + .title' papers/extracts/*.json
```

Theory names are constrained to a fixed vocabulary (see `HUMOR_THEORIES` in `scripts/extract_papers.py`): SSTH, GTVH, incongruity-resolution, appropriate incongruity, benign violation, superiority, relief, surprise theory, frame-shifting, humor styles, other, none.

**Model census — which models the field actually runs:**

```bash
jq -r '.models_evaluated[]?' papers/extracts/*.json | sort | uniq -c | sort -rn | head -20
```

Caveat: model strings are as-written in each paper (`GPT-4o` vs `gpt-4o` vs `GPT-4o-mini` are separate rows). `scripts/build_analysis.py` has a `normalize_model()` that folds variants — copy it for anything serious.

**Headline results involving a model:**

```bash
jq -r '.headline_results[]? | select(.best_system // "" | test("GPT-4o")) | .finding' papers/extracts/*.json
```

**Fuzzy task search** (tasks are free-text, so match loosely):

```bash
jq -r 'select([.tasks[]?] | any(test("pun"; "i"))) | .ref + "  " + (.tasks | join("; "))' papers/extracts/*.json
```

## Catalog queries

**Papers not in the library (and why):**

```bash
jq -r '.papers[] | select(.status != "converted") | .ref + "  " + .title + "  (" + (.note // .status) + ")"' papers/papers.json
```

**Everything in one guide section:**

```bash
jq -r '.papers[] | select(.section | test("Part 4")) | .ref + "  " + .title' papers/papers.json
```

**Vendored datasets with local paths / blocked datasets with reasons:**

```bash
jq -r '.datasets[] | select(.status == "downloaded") | .key + "  " + .approx_size' data/datasets.json
jq -r '.datasets[] | select(.status != "downloaded") | .key + "  [" + .status + "]  " + (.note // "")' data/datasets.json
```

**Which datasets came from a given paper:**

```bash
jq -r '.datasets[] | select(.paper_keys | index("03-humorbench")) | .key' data/datasets.json
```

## Full-text search

**Which papers discuss a concept anywhere in their full text:**

```bash
grep -rli "benign violation" papers/md --include="*.md" | grep -v /pages/ | sed 's|papers/md/\([^/]*\)/.*|\1|'
```

**Then jump to the one-pager:** `papers/summaries/<key>.md`.

## Python, for joins across layers

```python
import json, glob

extracts = {e["key"]: e for f in glob.glob("papers/extracts/*.json")
            for e in [json.load(open(f))]}
datasets = json.load(open("data/datasets.json"))["datasets"]
vendored = {d["name"]: d["key"] for d in datasets if d["status"] == "downloaded"}

# e.g. papers whose evaluation data we actually have on disk
for key, e in sorted(extracts.items()):
    have = [d["name"] for d in e["datasets_used"]
            if d["role"] == "evaluated-on" and d["name"] in vendored]
    if have:
        print(e["ref"], "→", ", ".join(have))
```

Dataset `name` strings in extracts were normalized against `data/datasets.json` at extraction time, so exact-match joins like the above are reliable (unlike model names).
