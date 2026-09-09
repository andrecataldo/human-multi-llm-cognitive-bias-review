# Search Strategy — v0.2

## Search families

### Q1 — Cognitive Bias Core

```text
AI / LLM
AND
cognitive bias / confirmation / anchoring / automation bias
AND
secondary study
```

### Q2 — Trust / Reliance / Automation

```text
AI / LLM
AND
overreliance / appropriate reliance / trust calibration /
algorithm aversion / algorithm appreciation / automation bias
AND
secondary study
```

### Q3 — Human–AI Decision & Interaction

```text
AI
AND
human-AI interaction / collaboration / AI-assisted decision making
AND
secondary study
```

### Q4 — Human–LLM Interaction

```text
LLM / Generative AI
AND
human-LLM interaction / human factors / decision making /
trust / reliance
AND
secondary study
```

### Q5a — Multi-Agent / Agentic AI Landscape

```text
Multi-Agent LLM / Agentic AI
AND
LLM / Generative AI
AND
secondary study
```

### Q5b — Human–Multi-Agent Bridge

```text
Multi-Agent LLM / Agentic AI
AND
human / user / judgment / decision / trust / reliance /
cognitive bias / consensus / disagreement
AND
secondary study
```

## Search execution order

```text
Q1 → Q2 → Q3 → Q4 → Q5a → Q5b
```

## Pilot rules

For each query record:

- database;
- query_id;
- query_version;
- execution_date;
- publication period;
- searched fields;
- exact query;
- number of results;
- expected known-set;
- retrieved known-set;
- missed known-set;
- precision proxy based on a defined sample;
- notes and observed noise.

Do not refine a query merely because a known paper is missing. First assess whether that paper should actually be in scope and whether the miss reflects a genuine retrieval problem.

## Known-set principle

Calibration studies may be used to adjust query design.

Holdout studies must not be repeatedly used to tune the query. They are reserved for independent recall checking after a provisional freeze.

