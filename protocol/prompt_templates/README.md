# Prompt Template Structure — DRAFT, NOT LOCKED

**Status:** structural specification only  
**Final prompt locking:** explicitly prohibited under current authorization

No executable or provider-ready prompt is defined here. This file records only the fields that future owner-authorized prompt drafts must hold constant.

## Baseline structure

- task instruction slot;
- displayed underdetermined premises slot;
- substantive answer-option slot;
- support-distribution schema slot;
- separate action/abstain slot;
- optional short-rationale slot.

## Rebuttal structure

- frame slot: `N` or `P`;
- target-reference slot in an identical location;
- evidence-block slot: `S`, `I`, or none for control;
- unchanged output-schema slot;
- no condition label shown to the model.

## Matching invariants

- same target option and target position in `N` and `P`;
- same evidence block across frame comparisons;
- same output instructions and placement;
- same turn count;
- no task fact added by the frame;
- evidence repeated verbatim at Turn 2;
- no future frame disclosed at Turn 1;
- exact parent response replayed into Turn-2 children.

## Deferred decisions

The following remain intentionally unlocked:

- exact neutral wording;
- exact pressure wording;
- system/developer messages;
- provider-specific structured-output syntax;
- numeric formatting examples;
- rationale instruction;
- retry wording or repair prompts.

Any future concrete prompt file must be versioned, reviewed and explicitly approved before model execution.
