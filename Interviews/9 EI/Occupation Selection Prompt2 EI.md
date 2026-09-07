You are designing a controlled cognitive task analysis interview dataset.

Your task is to take:
1. One occupational domain.
2. Seven predetermined interview-level cognitive-bias lists.
3. Optional constraints and previously used occupations.

You must recommend one realistic occupation and one realistic scenario for each of the seven interviews. The selected occupation should have the strongest plausible overlap with that interview’s complete bias list, while the seven selected interviews should remain meaningfully varied in occupational role, setting, decision type, information environment, and consequence profile.

Do not generate the final interview transcripts.
Do not write the hidden bias annotations yet.
Do not force a bias into an occupation where it would be artificial.
Produce an auditable occupation-and-scenario allocation that can later be passed to the interview-blueprint prompt.

INPUTS

Occupational domain:
[Education and instructional work]

Interview 1 bias list:
[Averaging Bias]

Interview 2 bias list:
[Biased Assimilation and Egocentric bias]

Interview 3 bias list:
[Group attribution error, Present Bias, and Horn Effect]

Interview 4 bias list:
[Bounded Rationality, Coherence-based reasoning or Rationalisation, Illusion of understanding, and Self-Enhancement or Self-serving Bias]

Interview 5 bias list:
[Belief Perserverence and Attitude Polarisation, Fundamental attribution Bias, Halo effect, Ingroup Favoritism or In-group bias, and Ambiguity Aversion]

Interview 6 bias list:
[Bandwagon effect, Groupthink, Availability Bias, Anchoring Bias, Confirmation bias, and Averaging Bias]

Interview 7 bias list:
[Biased Assimilation, Egocentric bias, Group attribution error, Present Bias, Horn Effect, Bounded Rationality, and Coherence-based reasoning or Rationalisation]

Geographic scope:
[NONE]

Industry scope:
[Mixed]

Target expertise level:
[MIXED]

Previously used occupations:
[NONE]

Previously used scenarios:
[NONE]

Required exclusions:
[NONE]

Additional diversity requirements:
[DEFAULT]

CORE OBJECTIVE

For each of the seven interviews:

- Recommend a realistic occupation within the specified domain.
- Recommend a specific scenario involving a consequential cognitive task or decision.
- Determine how naturally each requested bias can be embedded.
- Maximize the number of requested biases that can be embedded clearly and independently.
- Avoid relying on generic occupational stereotypes.
- Avoid assigning an occupation to a bias list merely because the job title sounds compatible.
- Preserve realistic causal, informational, and organizational conditions.
- Ensure the final seven-interview set has meaningful scenario diversity.

The occupation should be chosen based on the work actually performed, including:
- Tasks.
- Work activities.
- Decision points.
- Available cues.
- Information quality.
- Time pressure.
- Stakeholder dynamics.
- Consequences of error.
- Degree of discretion.
- Feedback and learning environment.

SCORING PRINCIPLE

For every interview-bias-list and occupation pairing, assess each bias independently as:

- NATURAL: The bias can be embedded realistically and distinctly.
- PLAUSIBLE: The bias can be embedded, but careful scenario design is required.
- WEAK: The connection is possible but likely to feel artificial or ambiguous.
- UNSUITABLE: The occupation does not provide a credible mechanism for embedding the bias.

Use the following numerical scores:

- NATURAL = 3
- PLAUSIBLE = 2
- WEAK = 1
- UNSUITABLE = 0

Calculate:

1. Raw overlap score:
   Sum of the bias-compatibility scores for the interview’s requested biases.

2. Coverage score:
   Percentage of requested biases rated NATURAL or PLAUSIBLE.

3. Distinctness score:
   How clearly the biases can be separated into different reasoning mechanisms.

4. Scenario richness score:
   Whether the occupation supports enough decision points, evidence, alternatives, and probes for a CTA interview.

5. Causal-counterfactual score:
   Whether a relevant causal fact can be changed while preserving the rest of the scenario.

6. Occupational realism score:
   Whether the scenario is realistic for the role and setting.

7. Dataset-diversity score:
   How much the proposed assignment adds variation relative to the other six assignments.

Use this default composite score:

- Bias compatibility: 40%.
- Bias distinctness: 15%.
- Scenario richness: 15%.
- Causal-counterfactual suitability: 10%.
- Occupational realism: 10%.
- Dataset diversity: 10%.

If a required constraint makes this weighting inappropriate, explain the adjustment.

BIAS EVALUATION RULES

Do not treat the following as sufficient evidence of a cognitive bias:

- A bad outcome.
- An incorrect decision.
- Confidence.
- Uncertainty.
- Time pressure.
- A memorable event.
- Use of a shortcut.
- Failure to consider every possible alternative.
- Organizational pressure.
- A factual misunderstanding without a reasoning pattern.

For each requested bias, identify:

- The relevant reasoning mechanism.
- The decision episode where it could appear.
- The information available to the worker.
- The alternative or contradictory evidence.
- The observable cues that would support the bias.
- The main neighboring biases that could be confused with it.
- The minimum evidence needed to distinguish it.
- Whether the bias would be natural, plausible, weak, or unsuitable.

If two requested biases overlap substantially, state whether:
- They can be embedded as distinct mechanisms.
- They should be embedded in separate decision episodes.
- One should be treated as a secondary label.
- The pairing should be rejected.

SCENARIO DESIGN REQUIREMENTS

Each recommended scenario must include:

- A specific triggering event.
- A realistic role and work setting.
- Three or four decision episodes or phases.
- A meaningful decision or judgment.
- At least two plausible alternatives.
- Information available at the time.
- Contradictory, incomplete, or competing evidence where relevant.
- A realistic action or intervention.
- A plausible outcome.
- A causal fact that can later be changed for a counterfactual version.
- Opportunities for neutral CTA interviewer probes.

Do not create a scenario whose only purpose is to display biases. It should first be a credible occupational decision episode.

DIVERSITY REQUIREMENTS ACROSS THE SEVEN INTERVIEWS

Maximize variation across:

- Specific occupation.
- Work setting.
- Decision type.
- Information environment.
- Time pressure.
- Consequence of error.
- Expertise level.
- Stakeholder configuration.
- Human-versus-technical information sources.
- Individual versus team decision-making.
- Degree of procedural structure.
- Level of causal observability.

Avoid assigning all seven interviews to:
- The same type of professional.
- Office-based analytical work.
- High-stakes emergency situations.
- Financial or medical examples.
- One recurring scenario pattern.
- One shared bias mechanism.

If one occupation is the best match for several bias lists, you may reuse it only if:
- The scenario is materially different.
- The decision episode is materially different.
- Reuse is necessary to preserve bias validity.
- You explain why using a different occupation would reduce ecological validity.

OCCUPATION-CANDIDATE GENERATION

Before selecting the final occupation for each interview:

1. Generate at least five plausible occupation candidates within the domain.
2. Score every candidate against the relevant bias list.
3. Remove candidates that are too similar to occupations already selected.
4. Remove candidates where one or more requested biases would be artificial.
5. Select the highest-quality candidate, not automatically the candidate with the highest raw overlap.
6. If the highest-scoring candidate creates excessive repetition across the seven interviews, select the best diverse alternative and explain the tradeoff.

For every interview, report at least:
- The selected occupation.
- Two rejected alternatives.
- Why the selected occupation is superior.
- Any bias that remains weak or uncertain.

OUTPUT FORMAT

Return exactly these sections.

## 1. Dataset allocation summary

Use a table:

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |

## 2. Candidate occupation matrix

For each interview, provide a table:

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |

## 3. Final occupation and scenario recommendations

For each interview, provide:

### Interview [number]

- Requested biases:
- Selected occupation:
- Role and setting:
- Why this occupation fits the bias list:
- Primary CTA scenario:
- Triggering event:
- Decision episodes:
- Available cues and evidence:
- Competing interpretations:
- Plausible actions:
- Constraints and pressures:
- Consequences of error:
- Counterfactual causal variable:
- Expected interview structure:
- Natural biases:
- Plausible but difficult biases:
- Biases that should not be forced:
- Rejected alternative occupation 1:
- Rejected alternative occupation 2:
- Recommendation status:

Recommendation status must be one of:
- APPROVED
- APPROVED_WITH_CAVEATS
- REQUIRES_REDESIGN

## 4. Cross-interview diversity audit

Assess variation in:

- Occupation.
- Work setting.
- Decision type.
- Information environment.
- Time pressure.
- Consequence of error.
- Expertise.
- Stakeholder pattern.
- Scenario archetype.
- Causal-counterfactual structure.

Identify:
- Repetitions.
- Overrepresented categories.
- Underrepresented categories.
- Recommended substitutions.

## 5. Bias-integrity audit

For every interview, identify:

- Biases that can be independently distinguished.
- Bias pairs that risk conflation.
- Biases that could accidentally become outcome bias.
- Biases that could accidentally become hindsight bias.
- Biases that would be supported only by one weak cue.
- Biases that require a stronger scenario.
- Recommended safeguards for Prompt 1 and Prompt 2.
