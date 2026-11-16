# Raw Discovery Records

These files preserve unmodified primary metadata responses, source archives, and authoritative paper downloads used during Stage 1 on 2026-11-15. Extracted or converted working copies are under `research/working/fulltext/`; they are not substitutes for the preserved raw files.

## Metadata and search records

| File | Purpose | SHA-256 |
|---|---|---|
| `arxiv_seed_records_20261115.xml` | Initial 11-paper arXiv seed set | `4b3ad4ff2df682fababcc47e0acfdf31f0db694349d6b120b5c55280198e5c33` |
| `arxiv_elephant_search_20261115.xml` | Initial ELEPHANT search | `cc06b946d4e03ba180c7b122a8e109f4b2991f7c634ca66a3b2f71828f7c1db4` |
| `crossref_elephant_search_20261115.json` | Initial Crossref ELEPHANT search | `3ca132a881bd6e6d0ce83af111d074c5411ce6c72b246b037c54ddb14cf88561` |
| `arxiv_additional_metadata_20261115.xml` | Metadata for newly identified close papers | `9d26092cc2783def2041b206d7632e70cf77526d9e1c5eff6975aeffe77dbd9d` |
| `arxiv_recent_overlap_search_20261115.xml` | Recent SycoBench overlap search | `d7be0515e39db071cb7e7d0f8689a3959a326d0a9e52a8d1a2e2f341add5209d` |
| `arxiv_evidence_pressure_multiturn_20261115.xml` | Evidence + social pressure + multi-turn query | `da0f29a6797daa9efef0b9104bfc00344c9ead73b8e2bb83420e5dea2d96ed4b` |
| `arxiv_valid_invalid_feedback_20261115.xml` | Valid-correction / invalid-pressure query | `3aff2798baa6293965bd621cef950ed4b31e535bed35c8604a71def1db92afa9` |
| `arxiv_selective_updating_20261115.xml` | Selective-updating query | `abe52e689b1733f4cee76a2af0788247070ae45f5a59779b8be45953547d276c` |
| `arxiv_belief_revision_authority_20261115.xml` | Belief-revision + authority query | `a25e9ee1ff4e5ab96fd2840403d33cc848b69e4b19c082d1168cb5cce505d21d` |

## Source archives and authoritative downloads

| File | SHA-256 |
|---|---|
| `sources/2311.08596.src` | `40497f72cd6cfeb86e7d12d8aeea3a67987fe92bda77c358b158ae03d5f19a80` |
| `sources/2502.08177.src` | `4a95f4705f8817845be5b395c66e1433ac90bcd6430b81593878e03dae0b13d7` |
| `sources/2505.13995.src` | `aa38c1f9ef5625555b9b249d559acc3a3a8c3c49ff46bb9b37835f4af99d486e` |
| `sources/2505.23840.src` | `567bb9547a64b2e868a265513c46a827ec1e23887f5566c4bab45094d787f4ab` |
| `sources/2508.16846.src` | `76ac046ca9658ef6428241b7f11f0ae9de2c0a8a9f6fc8d7474bb04604f2c1ac` |
| `sources/2509.16533.src` | `c1009c42ff482f8852cc904880d539d35573d63dcb1cd199e3a298ead7b8260d` |
| `sources/2603.23848.src` | `e2b77321c66fb5a2bd8149dbae11e308d2798db2afcf231934dc74453c77d139` |
| `sources/2604.07749.src` | `61645c7819cf1615daa2c805cfce83849ba3d4336b338994b48a82f30f072613` |
| `sources/2604.16009.src` | `520d94b695901e1246341b80e461725a6a9f6db7092b9296548d10b01e6f364c` |
| `sources/2608.26511.src` | `8aa78814e8f90831aa4e6b500126654ab6604d823eae5fdfdd5b6cc592e78812` |
| `sources/2609.32867.src` | `d431727e703da07459c03764920ae4462fd4fb0ce218c61b78878e49a501c51d` |
| `sources/2609.11428.src` | `ef7ef1520eadc27df4dddf4fc6e4918b44439c397e232ce81d2f594e2eff05b4` |
| `sources/2610.15634.src` | `68ffa9240aac1f1965e632772c1a707002b7ead7a2d7260000127746fc138c12` |
| `sources/sycobench600_2026.findings-acl.1759.pdf` | `68c86f4644bab74e815c13249bccdcff9384bcfafb503d3d5f1dbbec3ffebdc3` |
| `sources/sycobench600_2026.findings-acl.1759.bib` | `29886c199daebe02fa74e5695f5399c7fb22df4bef35d6af017e989a9da20465` |

## Integrity notes

- Raw files must not be edited in place.
- Source archives use arXiv IDs as downloaded filenames; version binding should be inferred only from accompanying metadata, not from the filename alone.
- A verifier compared the initially extracted source trees with their archives and reported no content mismatch. This verifies extraction fidelity, not publication authenticity or empirical correctness.
- Numerical results have not been reproduced.
