# Academic review 07: computational reproducibility and provenance

**Recommendation:** Moderate revisions to the provenance guarantees and reproduction workflow. The historical measurements examined are internally traceable; I found no evidence of changed or fabricated response data. The findings below identify gaps in enforcing future reproducibility, rather than demonstrated numerical errors in the paper.

Reviewed independently on 9 September 2026. Scope: the historical paper's nine frozen exports (20-capital pilot, three original 50-capital conditions, five matched 50-capital language conditions), source history, collection records, and paper build workflow. Later 100-capital results are a separate extension and are not inputs to this manuscript. Base revision: `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`; the workspace also contained concurrent, uncommitted schema and documentation changes. Findings below also apply to the historical implementation unless stated otherwise.

Manuscript SHA-256: `5f48fffc573f56005f8074bdb7e73514e3fc1671575de2be6b379b3622eb7fa4`.

## Findings

### 1. [P2, moderate] Analysis identity does not capture every input that determines its output

**Evidence:** `atlas/analysis.py:61–66` derives the analysis identifier from response rows, seed/bootstrap settings, and Python source contents. It returns an existing result immediately when that identifier exists. The map input is read separately from `public/data/world.json` at line 74, without its hash entering the identifier. Analysis-time dependency versions are also absent from the analysis parameters. The `software` field in `atlas/experiment.py:61–62` describes experiment creation, which can precede analysis or reanalysis.

**Consequence:** With identical observations and Python source, changing the coastline file or numerical environment leaves the analysis ID unchanged. An existing cache then returns the old output; a fresh reconstruction may produce different geometry under the same nominal ID. The immutable export check at `atlas/analysis.py:160–162` would reject differing output on publication, which is useful protection, but does not give the new calculation an adequate identity. This matters particularly for a study whose central artifact includes deformed geography and numerical optimization.

**Requested revision:** Include hashes of external geometry and all relevant input artifacts, the actual analysis runtime/dependency lock, and solver settings in an analysis manifest before computing its ID. Record an analysis source revision as well as a content hash. Document numerical tolerance versus byte-for-byte reproducibility. Add a check that changing a coastline input or analysis environment produces a distinct analysis identity.

**Limit:** No changed coastline input or historical solver mismatch was observed in this review.

### 2. [P2, moderate] Collection provenance records HEAD, but does not establish which source executed every attempt

**Evidence:** `atlas/experiment.py:47–60` records `git rev-parse HEAD` at condition creation. It neither detects dirty tracked files nor records the collection source contents. `atlas/runner.py:67–85` validates the condition, places, and pairs on resume, but does not verify the currently executing collector against that revision. Attempt fields at `atlas/runner.py:22–25` contain no collector version or source hash.

**Consequence:** An edited adapter or parser, or resumption after a code update, can produce attempts within one experiment while its single `code_revision` remains unchanged. Exact prompts and provider responses help reconstruct what happened, but a revision alone should not be described as proof of the executed collection implementation. This is particularly relevant when adding an output-schema protocol: storing the schema as a distinct condition is necessary, and preserving the collector version across resumes is a separate requirement.

**Requested revision:** Record a collection source snapshot hash and dirty-state information, and either enforce that snapshot on resume or record execution version changes per attempt/session. Archive the relevant source or diff so a content hash is recoverable. Keep historical manifests unchanged; describe any remaining provenance limits explicitly.

**Limit:** I did not establish that the historical runs used unrecorded source changes. Their recorded revisions exist in Git, and the saved prompts and payloads pass the checks below.

### 3. [P2, moderate] The default paper rebuild refreshes provenance instead of enforcing a fixed input checksum contract

**Evidence:** `paper/experiment-index.json` pins export IDs and paths, but not result hashes. `paper/scripts/build_assets.py:44–65` reads those paths, calculates current hashes, and overwrites `paper/results/provenance.json`. It does not first compare them with a frozen expected manifest. `paper/Makefile:6–13` runs this asset generator as part of the default build. The language analysis similarly calculates new source hashes at `paper/scripts/check_language_differences.py:46–58`. In contrast, `paper/scripts/local_language.py:59–61` correctly checks input bytes against recorded hashes before proceeding.

**Consequence:** The fixed index successfully prevents the later 100-capital cohort from entering the paper. It does not, by itself, prevent replacement of bytes at a historical path from being accepted and re-certified by a rebuild. The model geographic-signal audit also lacks the source/script hashes present in the two language audits (`paper/scripts/check_distance_structure.py:49–70`). Git history preserves the old files, and existing tests catch several forms of drift, but the reproduction command should fail at the input boundary rather than regenerate the expected evidence.

**Requested revision:** Freeze a separate release manifest covering all raw inputs, result files, and analysis scripts. Verify it before any paper-generation writes. Make updating that manifest an explicit new release operation, and give the model geographic-signal audit the same source/script hash checks as the language audits. Preserve the useful separation between the historical paper index and the growing website index.

**Limit:** All nine current result hashes match the committed paper provenance. This is a workflow vulnerability, not evidence that the paper currently uses mismatched files.

## Checks completed and strengths

- Independently validated all nine experiment IDs against their manifests; all dataset hashes and regenerated WGS84 pair files passed `validate_inputs`.
- Recomputed every historical analysis ID from its saved response rows and analysis parameters. All nine matched. Every `result.json` hash matched `paper/results/provenance.json`, and each exported manifest matched the manifest embedded in its result.
- Checked all **99,904 recorded attempts**, comprising **99,900 saved successful-provider payloads** and four attempts without a payload, across the pilot and eight 50-capital runs. For every saved payload, extracted non-thought text, returned model version, and finish reason matched their CSV fields. This is a consistency audit of saved evidence, not independent authentication by Google.
- Matched every saved analysis-source hash to recoverable Git trees: pilot `f5b85dd`; original model analyses `14cd1e2`/`f08a138`; language analyses `287272b` and later commits with the same `atlas` source. Thus the source-hash recovery gap is addressable for these particular historical exports.
- Ran `tests/test_paper.py`, `tests/test_integrity.py`, and `tests/test_languages.py`: **21 passed**. These include exact prompt/parser audits, raw CSV-to-summary consistency, retry retention, manifest/pair tamper detection, and paper source/script hash checks.
- The frozen paper index, complete raw response retention, terminal invalid-content policy, per-attempt checkpoints, seeded numerical analyses, locked environment instructions, and explicit warning that a provider alias is not a fixed weight checkpoint are meaningful strengths. The manuscript correctly distinguishes reproducing saved-data calculations from reproducing future API behavior (`paper/main.tex:199`).

## Review limits

No paid API calls were made. I did not rerun the full permutation/bootstrap suites, all reconstructions, or the PDF build; other numerical and geometry reviews should cover those. I did not modify source, observations, generated paper assets, or the manuscript. This review does not authenticate the provider's hidden implementation, prove request independence, or replace independent human peer review. Storage format itself is not a research contribution; the relevant research properties are traceability, recoverability, and explicit experimental conditions.
