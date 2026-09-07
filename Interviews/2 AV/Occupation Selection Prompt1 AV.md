You are designing the occupation roster for a controlled benchmark of cognitive task analysis interviews.

The benchmark will evaluate whether an AI system can identify cognitive biases embedded in realistic descriptions of professional reasoning and decision-making.

Your task is to take one broad occupational domain and generate a balanced, realistic, and varied list of occupations within that domain. Do not generate interview transcripts. Do not embed cognitive biases yet. Produce a structured occupation-and-scenario inventory that can later be passed to separate prompts for scenario design, interview generation, and independent validation.

INPUTS

Occupational domain:
[Aviation]

Number of occupations required:
[12]

Geographic scope:
[NONE]

Industry scope:
[“MIXED”]

Target workforce:
[MIXED]

Required diversity constraints:
[“USE DEFAULT BALANCING RULES”]

Cognitive biases that may later be embedded:
[Information bias, Omitting subjectivity, Plan Continuation, Substitution bias, Anchoring Bias, Apophenia/Correlation Bias, Authority Bias, Automaticity/Automation Bias, Bias Blind Spot, Confirmation Bias, Experience Bias/Trusting expert intuition, Illusion of validity, Normalcy Bias, Optimism, Overconfidence, Representativeness, and Sunk Cost]

Existing occupations already used:
[NONE]

Existing scenarios already used:
[NONE]

GENERAL OBJECTIVE

Generate occupations that are genuinely distinct in the work they perform, not merely different titles for the same job.

The roster should provide enough variation to support a database of cognitive task analysis interviews with:
- Different decision types.
- Different levels of expertise.
- Different information environments.
- Different consequences of error.
- Different degrees of time pressure.
- Different levels of procedural structure.
- Different social and organizational settings.
- Different combinations of human, technical, financial, physical, and regulatory constraints.

Use real occupations or clearly recognizable occupational roles. Avoid fictional roles unless explicitly requested.

DEFAULT BALANCING RULES

Unless the input specifies otherwise, distribute the occupations across the following dimensions:

1. Work setting
   - Office or administrative.
   - Field or outdoor.
   - Clinical or care-oriented.
   - Industrial, laboratory, or technical.
   - Public-facing or service-oriented.
   - Remote, digital, or distributed.
   - High-reliability or safety-critical.

2. Decision type
   - Diagnosis or classification.
   - Planning or prioritization.
   - Monitoring or anomaly detection.
   - Resource allocation.
   - Risk assessment.
   - Negotiation or persuasion.
   - Troubleshooting or repair.
   - Emergency response.
   - Compliance or adjudication.
   - Design or creative judgment.
   - Personnel or team management.
   - Forecasting or prediction.

3. Information environment
   - Rich, structured, and quantified.
   - Incomplete or ambiguous.
   - Rapidly changing.
   - Conflicting across sources.
   - Primarily experiential or perceptual.
   - Socially mediated.
   - Data-heavy and software-mediated.
   - Regulated and documentation-heavy.

4. Operational pressure
   - Low time pressure.
   - Moderate time pressure.
   - High time pressure.
   - Interruption-heavy.
   - Resource-constrained.
   - High consequence of error.
   - Reputational or political pressure.
   - Conflicting stakeholder demands.

5. Expertise level
   - Developing practitioner.
   - Independent professional.
   - Senior practitioner.
   - Specialist or technical expert.
   - Supervisor or manager.
   - Strategist, investigator, or decision authority.

6. Primary interaction pattern
   - Individual work with tools or systems.
   - One-to-one client or patient interaction.
   - Team coordination.
   - Multi-party negotiation.
   - Supervision and delegation.
   - Public or stakeholder interaction.
   - Human-machine collaboration.

7. Consequence profile
   - Financial.
   - Health or welfare.
   - Safety.
   - Legal or regulatory.
   - Operational continuity.
   - Environmental.
   - Educational or developmental.
   - Reputational or political.

ROSTER REQUIREMENTS

For every proposed occupation:

- Use a specific occupational title.
- State whether it is a recognized occupation, specialization, or role.
- Explain why it belongs in the domain.
- Identify the primary work setting.
- Identify the typical level of expertise.
- Describe three to five realistic tasks.
- Identify two to four high-value decision points.
- Identify the information and cues available to the worker.
- Identify plausible alternatives the worker might consider.
- Describe the main constraints and pressures.
- Describe the consequences of error or delay.
- Identify the most natural CTA scenario type.
- Identify cognitive biases that could plausibly be embedded later.
- Identify biases that would be difficult or unnatural to embed in this occupation.
- State whether the occupation is suitable for a vocabulary control.
- State whether it is suitable for a counterfactual causal-evidence interview.
- Assign a diversity category to each balancing dimension.

OCCUPATIONAL DISTINCTIVENESS

Do not include multiple occupations that would produce essentially the same interview.

For example, do not list several roles whose core work is:
- Reviewing the same type of financial report.
- Diagnosing the same type of medical case.
- Supervising the same operational process.
- Performing nearly identical software troubleshooting.
- Conducting the same regulatory inspection.

If two roles are similar, retain both only if they differ materially in:
- Decision authority.
- Information access.
- Time pressure.
- Stakeholder relationships.
- Consequences of error.
- Tools or technologies.
- Degree of ambiguity.
- Accountability or regulatory exposure.

SCENARIO SUITABILITY

For each occupation, propose one primary scenario archetype and two alternative scenario archetypes.

A scenario archetype should describe a realistic decision episode, not a generic task.

Good example:
- “A hospital pharmacist notices a discrepancy between a medication reconciliation record and an urgent prescription while the prescribing physician is unavailable.”

Weak example:
- “The pharmacist makes a medication decision.”

Each scenario archetype must include:
- Triggering event.
- Decision point.
- Available evidence.
- Competing interpretations.
- Action options.
- Relevant constraints.
- Possible outcomes.
- Potential counterfactual change.

BIAS COMPATIBILITY

If a bias list is provided, classify each requested bias for each occupation as:

- NATURAL: can be embedded plausibly without distorting the scenario.
- POSSIBLE: can be embedded, but requires careful design.
- UNSUITABLE: likely to feel artificial or overlap with another mechanism.

Do not force every bias into every occupation. Explain the reasoning.

For each NATURAL or POSSIBLE bias, identify:
- The likely decision episode.
- The reasoning mechanism.
- The evidence that would reveal it.
- The main neighboring bias to avoid.
- The type of control condition that would be needed.

BALANCE AND COVERAGE

After generating the occupation list, calculate and report coverage across:

- Work setting.
- Decision type.
- Information environment.
- Operational pressure.
- Expertise level.
- Interaction pattern.
- Consequence profile.

Avoid having more than [INSERT MAXIMUM, DEFAULT 25%] of the occupations share the same primary category unless the domain naturally requires it.

If the requested number of occupations is too small to cover all categories, prioritize:
1. Distinct decision types.
2. Distinct information environments.
3. Distinct consequences of error.
4. Distinct work settings.
5. Distinct expertise levels.

QUALITY CONTROLS

Check for:

- Duplicate or near-duplicate occupations.
- Occupations that are too generic.
- Roles outside the stated domain.
- Roles that lack a meaningful decision episode.
- Scenarios that depend on rare or implausible events.
- Scenarios that are too similar to existing scenarios.
- Occupations where bias embedding would be forced.
- Excessive concentration in one work setting.
- Excessive concentration in one decision type.
- Hidden dependence on a particular country or regulatory system.
- Occupational claims that require current external verification.

When an occupation depends on country-specific rules, clearly mark it as:
- Country-specific.
- Regionally adaptable.
- Broadly transferable.

OUTPUT FORMAT

Return exactly the following sections.

## 1. Domain interpretation

Provide:

- Domain definition.
- Included occupations.
- Excluded occupations.
- Geographic and industry assumptions.
- Any important ambiguity.

## 2. Recommended occupation roster

Use a table with these columns:

| ID | Occupation | Role type | Work setting | Expertise level | Primary decision type | Information environment | Consequence profile | Scenario suitability | Bias compatibility |

Do not generate interview transcripts.
Do not embed any cognitive biases in an actual interview.
Do not use fictional occupations unless explicitly requested.
