This confirms strong grounding for software architects/engineers with sunk cost bias and technical debt decisions. Now I have enough to build the full allocation for this HCI/IS domain.

## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Product Manager (Digital Platform) | Deciding whether to adopt a competitor's newly launched feature after seeing multiple peer companies adopt similar features; herding in following industry movement rather than independent analysis | 100% | 3 | High | Adds product strategy, market-signal-driven, individual decision-making context | APPROVED |
| 2 | 2 | Software Engineering Team Lead | Deciding whether to continue a failing microservices migration after months of setbacks and negative team feedback; irrational escalation in continuing investment, negativity bias in overweighting recent failures | 100% | 6 | High | Adds technical/engineering, team leadership, resource-continuation context | APPROVED |
| 3 | 3 | UX Researcher | Running a usability study where participants react against a mandated new interface pattern; reactance in interpreting user pushback, priming effect from the study's introductory framing, cognitive dissonance in reconciling design team commitment with negative findings | 100% | 9 | High | Adds human-subjects research, perceptual/experiential, individual-with-participants context | APPROVED |
| 4 | 4 | UX/Product Designer | Designing a subscription pricing page with multiple tier options; decoy effect in tier structuring, halo effect from a polished visual mockup, illusion of control in A/B test interpretation, sunk cost bias in defending an existing design direction | 100% | 12 | High | Adds visual/interaction design, creative judgment, individual-with-tools context | APPROVED |
| 5 | 5 | Enterprise IT Systems Administrator | Deciding whether to migrate a legacy internal system to a new platform after years of stable operation; status quo bias in maintaining the legacy system, framing bias in how migration risk is presented, bandwagon effect from other departments' adoption, overconfidence in migration timeline, availability bias from a recent outage memory | 100% | 15 | High | Adds infrastructure/operations, technical/administrative, organizational-risk context | APPROVED |
| 6 | 6 | Software Architect | Choosing between two competing architectural patterns for a new system after initial team discussion and early technical spikes; anchoring on the first proposed architecture, confirmation bias in evaluating spike results, herding toward the industry-popular pattern, irrational escalation in defending the chosen pattern, negativity bias from one failed spike, reactance to mandated architecture review board feedback | 100% | 18 | High | Adds senior technical decision-making, design/creative judgment, high-consequence architectural context | APPROVED |
| 7 | 7 | Interaction Designer (Design Systems Lead) | Redesigning a core design-system component after being primed by a competitor's redesign and encountering resistance to abandoning a legacy component; priming effect from competitor exposure, cognitive dissonance after public commitment to the legacy pattern, decoy effect in presenting component variants to stakeholders, halo effect from a well-received prototype, illusion of control in rollout timeline, sunk cost bias in defending prior design investment, status quo bias in resisting full replacement | 86% | 19 | Moderate-High | Adds design-systems governance, cross-team stakeholder, long-horizon design context | APPROVED_WITH_CAVEATS (Priming Effect requires an explicit, isolable priming event distinct from ordinary competitive awareness) |

***

## 2. Candidate occupation matrix

### Interview 1 (Herding)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Product Manager (Digital Platform) | 1 (Herding) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (multi-phase feature decision) | High (change competitor adoption outcome) | High | High (adds product strategy, market-signal context) | 0.88 |
| Software Architect | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.76 |
| UX Designer | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.58 |
| IT Systems Administrator | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.55 |
| Engineering Team Lead | 0 | 0 | 1 | 0 | 25% | Low | High | High | High | Low (overlaps with Interview 2) | 0.45 |

**Selected:** Product Manager (Digital Platform) (best coverage, distinctness, diversity fit; herding is the natural core mechanism of competitive feature-parity decisions).

***

### Interview 2 (Irrational Escalation, Negativity Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Software Engineering Team Lead | 2 (Irrational Escalation, Negativity Bias) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (multi-month migration project phases) | High (change actual migration recoverability) | High | High (adds technical/engineering leadership context) | 0.90 |
| Software Architect | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 6) | 0.72 |
| Product Manager | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.65 |
| IT Systems Administrator | 1 | 1 | 0 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.62 |
| Interaction Designer | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 7) | 0.50 |

**Selected:** Software Engineering Team Lead (best coverage, distinctness, diversity fit; well-grounded in software engineering sunk-cost/escalation literature). [bura.brunel.ac](https://bura.brunel.ac.uk/bitstream/2438/14977/5/FullText.pdf)

***

### Interview 3 (Reactance, Priming Effect, Cognitive Dissonance)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| UX Researcher | 3 (Reactance, Priming, Cognitive Dissonance) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (study design, data collection, interpretation phases) | High (change study framing/introduction) | High | High (adds human-subjects research, perceptual context) | 0.92 |
| Interaction Designer | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 7) | 0.78 |
| UX/Product Designer | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.72 |
| Product Manager | 1 | 2 | 0 | 0 | 83% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.65 |
| Software Engineering Team Lead | 1 | 1 | 1 | 0 | 67% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.55 |

**Selected:** UX Researcher (best coverage, distinctness, diversity fit; introduces the domain's core human-subjects research role).

***

### Interview 4 (Decoy Effect, Halo Effect, Illusion of Control, Sunk Cost Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| UX/Product Designer | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (pricing page design, testing, iteration phases) | High (change A/B test data validity) | High | High (adds visual/interaction design, creative judgment context) | 0.94 |
| Interaction Designer | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.80 |
| Product Manager | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 1) | 0.76 |
| Software Architect | 2 | 2 | 0 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.68 |
| Engineering Team Lead | 2 | 1 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.62 |

**Selected:** UX/Product Designer (best coverage, distinctness, diversity fit).

***

### Interview 5 (Status Quo Bias, Framing Bias, Bandwagon Effect, Overconfidence Bias, Availability Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Enterprise IT Systems Administrator | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (migration decision phases, organizational stakeholders) | High (change migration timeline accuracy) | High | High (adds infrastructure/operations, organizational-risk context) | 0.95 |
| Software Architect | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 6) | 0.82 |
| Engineering Team Lead | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 2) | 0.74 |
| Product Manager | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.68 |
| Interaction Designer | 2 | 2 | 1 | 0 | 80% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.62 |

**Selected:** Enterprise IT Systems Administrator (best coverage, distinctness, scenario richness).

***

### Interview 6 (Anchoring Bias, Confirmation Bias, Herding, Irrational Escalation, Negativity Bias, Reactance)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Software Architect | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms across design phases) | High (architecture selection, spike, review phases) | High (change spike test data reliability) | High | High (adds senior technical decision-making, architectural context) | 0.96 |
| Engineering Team Lead | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Low (overlaps with Interview 2) | 0.82 |
| Product Manager | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 1) | 0.74 |
| IT Systems Administrator | 4 | 1 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.70 |
| UX Researcher | 3 | 2 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.66 |

**Selected:** Software Architect (best coverage, distinctness, diversity fit; all six biases map cleanly onto distinct stages of architectural decision-making, well-grounded in technical-debt bias literature). [arxiv](https://arxiv.org/abs/2309.14175)

***

### Interview 7 (Priming Effect, Cognitive Dissonance, Decoy Effect, Halo Effect, Illusion of Control, Sunk Cost Bias, Status Quo Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Interaction Designer (Design Systems Lead) | 5 (Cognitive Dissonance, Decoy, Halo, Sunk Cost, Status Quo) | 2 (Priming, Illusion of Control) | 0 | 0 | 100% | Moderate-High (Priming Effect requires an isolable event) | High (redesign phases, stakeholder presentation) | High (change prototype reception accuracy) | High | High (adds design-systems governance, cross-team stakeholder context) | 0.88 |
| UX/Product Designer | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.78 |
| Software Architect | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.76 |
| UX Researcher | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.72 |
| Product Manager | 3 | 2 | 2 | 0 | 71% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.65 |

**Selected:** Interaction Designer (Design Systems Lead) (best diversity fit, adds design-systems governance context; Priming Effect requires an isolable, distinct exposure event).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Herding
- **Selected occupation:** Product Manager (Digital Platform)
- **Role and setting:** Product management role at a digital platform or SaaS company; sets product roadmap priorities, monitors competitor moves and market trends, makes feature-adoption decisions that balance differentiation against competitive parity.
- **Why this occupation fits the bias list:** Product managers routinely observe competitor and industry moves before deciding whether to adopt a similar feature. Herding — following the observed behavior of multiple peers rather than independently analyzing the feature's merit for one's own product — is a natural, distinct mechanism in this competitive-signal-driven decision context.
- **Primary CTA scenario:** Deciding whether to adopt a competitor's newly launched feature after seeing multiple peer companies adopt similar features; herding in following industry movement rather than independent analysis.
- **Triggering event:** Within a few weeks, three competing platforms in the same market segment launch a similar new feature (e.g., an AI-assisted onboarding flow), and the product manager must decide whether to fast-track a comparable feature for the upcoming roadmap.
- **Decision episodes:**
  1. Initial observation of competitor launches and internal team reaction to the pattern.
  2. Review of available (limited) internal user data on whether the feature addresses a genuine need for this product's specific user base.
  3. Discussion with stakeholders about prioritizing the feature against other roadmap items.
  4. Final roadmap decision and resource commitment.
- **Available cues and evidence:** Competitor launch announcements and marketing materials, internal user research (if any) on the underlying need, current roadmap priorities and their own supporting evidence, team and stakeholder reactions to the competitive pattern.
- **Competing interpretations:** The multiple competitor launches indicate a genuine market need vs. reflect competitors independently misjudging demand or copying each other; the feature is right for this specific product vs. right for the competitors' different user bases.
- **Plausible actions:** Fast-track the feature onto the roadmap; commission targeted user research before deciding; deprioritize in favor of an existing roadmap item with stronger internal evidence; adopt a scaled-down version to test demand first.
- **Constraints and pressures:** Competitive pressure and fear of appearing behind, limited time to conduct independent research before the next roadmap cycle, sales and stakeholder pressure referencing competitor moves.
- **Consequences of error:** Diverting engineering resources to a feature that doesn't fit this product's actual user needs, or missing a genuinely valuable feature by resisting the pattern too skeptically.
- **Counterfactual causal variable:** Actual underlying user need for the feature within this product's specific user base (later found to differ substantially from the competitors' user bases).
- **Expected interview structure:** Opening (PM role context), Episode 1 (competitor observation), Episode 2 (internal evidence review), Episode 3 (stakeholder discussion and decision), Closing (reflection on how the competitive pattern shaped the decision).
- **Natural biases:** Herding.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Software Architect (would overlap with Interview 6; herding is plausible in technology-choice contexts but reserved for the more complex six-bias architectural scenario).
- **Rejected alternative occupation 2:** UX/Product Designer (overlaps with Interview 4; herding is less naturally isolated from the four other mechanisms already assigned there).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Irrational Escalation, Negativity Bias
- **Selected occupation:** Software Engineering Team Lead
- **Role and setting:** Technical leadership role managing a software engineering team; oversees a multi-month system migration or refactoring project, makes continue/abandon decisions on technical initiatives, balances team morale against sunk technical investment.
- **Why this occupation fits the bias list:** Engineering leads are extensively documented in the software-engineering bias literature as prone to irrational escalation (continuing to invest in a failing migration because of prior investment) and negativity bias (overweighting recent setbacks relative to the project's full track record) when deciding whether to continue or abandon a technical initiative. [bura.brunel.ac](https://bura.brunel.ac.uk/bitstream/2438/14977/5/FullText.pdf)
- **Primary CTA scenario:** Deciding whether to continue a failing microservices migration after months of setbacks and negative team feedback; irrational escalation in continuing investment, negativity bias in overweighting recent failures.
- **Triggering event:** Six months into a microservices migration, the team lead faces a decision point after the third consecutive sprint with significant setbacks, while the migration has also delivered some solid, less visible progress earlier in the project.
- **Decision episodes:**
  1. Initial review of the current sprint's setbacks and their proximate causes.
  2. Consideration of the total time and resources already invested in the migration.
  3. Weighing of recent negative outcomes against the project's fuller track record, including earlier successes.
  4. Final decision on whether to continue, pause, or abandon the migration.
- **Available cues and evidence:** Sprint retrospectives and setback details, cumulative time and budget invested, earlier project milestones and their outcomes, team morale indicators, alternative technical paths not yet explored.
- **Competing interpretations:** The recent setbacks indicate the migration approach is fundamentally flawed vs. reflect normal, resolvable friction in a complex undertaking; the investment already made justifies continuing vs. should be irrelevant to the forward-looking decision; the most recent sprints are most representative of the project's trajectory vs. the full history should be weighted more evenly.
- **Plausible actions:** Continue the migration with the current approach; pause to reassess the technical strategy; abandon the migration and revert to the prior architecture; bring in outside technical review before deciding.
- **Constraints and pressures:** Budget and timeline already committed, team morale and sense of investment, stakeholder expectations set at project outset, opportunity cost of continuing versus other initiatives.
- **Consequences of error:** Continued investment in a genuinely failing approach, compounding technical debt and cost, or premature abandonment of a recoverable project due to recent-setback overweighting.
- **Counterfactual causal variable:** Actual root cause of the recent setbacks (later found to be an isolated, fixable configuration issue rather than a fundamental flaw in the migration approach).
- **Expected interview structure:** Opening (team lead role context), Episode 1 (setback review), Episode 2 (investment consideration), Episode 3 (weighing recent vs. full history), Closing (reflection on the continue/abandon decision).
- **Natural biases:** Irrational Escalation, Negativity Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Software Architect (overlaps with Interview 6; irrational escalation already assigned there in a more complex six-bias architecture-selection context).
- **Rejected alternative occupation 2:** Enterprise IT Systems Administrator (overlaps with Interview 5; negativity bias is plausible in operational contexts but less naturally tied to an active development-project continuation decision).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Reactance, Priming Effect, Cognitive Dissonance
- **Selected occupation:** UX Researcher
- **Role and setting:** Human-subjects research role within a product organization; designs and conducts usability studies, interprets participant behavior and feedback, works individually with study participants and reports findings to design and product stakeholders.
- **Why this occupation fits the bias list:** UX researchers directly observe and must interpret participant reactions in studies, making reactance (participants or the researcher interpreting pushback against a mandated design as resistance rather than genuine feedback), priming effect (the study's introductory framing shaping subsequent participant or researcher interpretation), and cognitive dissonance (reconciling the design team's prior public commitment to a pattern with negative study findings) all natural and distinct mechanisms in this research-interpretation context.
- **Primary CTA scenario:** Running a usability study where participants react against a mandated new interface pattern; reactance in interpreting user pushback, priming effect from the study's introductory framing, cognitive dissonance in reconciling design team commitment with negative findings.
- **Triggering event:** A UX researcher runs a usability study on a new interface pattern that the design team has already publicly committed to shipping; the study's introductory script frames the pattern positively, and several participants react negatively, explicitly resisting the change.
- **Decision episodes:**
  1. Initial study design, including the introductory framing given to participants.
  2. Observation of participant reactions during the sessions, including explicit resistance from some participants.
  3. Interpretation of the resistance: genuine usability problem versus resistance to any change.
  4. Reconciliation of the findings with the design team's prior public commitment, and final reporting decision.
- **Available cues and evidence:** The study's introductory script and framing, participant verbal and behavioral reactions, task completion and error data, the design team's prior public commitment and stated rationale, comparable data from the previous interface pattern.
- **Competing interpretations:** Participant pushback reflects genuine usability problems with the new pattern vs. reflects reactance to being asked to change a familiar way of working; the positive introductory framing appropriately oriented participants vs. primed them toward a biased initial reaction; the findings should lead to reconsidering the shipped commitment vs. should be reconciled with it through reframing.
- **Plausible actions:** Report the findings as indicating a genuine usability problem requiring redesign; report the findings as reactance, recommending the launch proceed with change-management support; revise the study framing and re-test; present both interpretations to stakeholders without resolving them.
- **Constraints and pressures:** The design team's public commitment and launch timeline, researcher's relationship with the design team, limited number of study sessions, stakeholder expectations for a clear recommendation.
- **Consequences of error:** Shipping a genuinely flawed pattern because pushback was dismissed as mere reactance, or unnecessarily reversing a sound design decision because normal resistance-to-change was misread as a usability defect.
- **Counterfactual causal variable:** Actual source of participant resistance (later found to stem from a specific, fixable interaction flaw rather than general resistance to change).
- **Expected interview structure:** Opening (researcher role context), Episode 1 (study design and framing), Episode 2 (observation of reactions), Episode 3 (interpretation), Episode 4 (reconciliation with prior commitment), Closing (reflection on how framing and prior commitment shaped interpretation).
- **Natural biases:** Reactance, Priming Effect, Cognitive Dissonance.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Interaction Designer (overlaps with Interview 7; cognitive dissonance and priming effect are plausible there but reserved for the more complex seven-bias design-systems scenario).
- **Rejected alternative occupation 2:** UX/Product Designer (overlaps with Interview 4; reactance is less naturally embedded in a design-execution role compared to a research-interpretation role).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Decoy Effect, Halo Effect, Illusion of Control, Sunk Cost Bias
- **Selected occupation:** UX/Product Designer
- **Role and setting:** Design role responsible for the visual and interaction design of product surfaces, including pricing and conversion-critical pages; iterates on designs based on stakeholder feedback and A/B test results, works with design tools and collaborates with product and engineering.
- **Why this occupation fits the bias list:** Designers working on pricing and conversion surfaces routinely structure options using decoy effect (a deliberately less attractive tier that makes another tier look better), are subject to halo effect (a polished visual mockup making the underlying design logic seem sounder than it is), illusion of control (overestimating the designer's ability to predict A/B test outcomes from design intuition alone), and sunk cost bias (defending an existing design direction because of the time already invested in it). These four mechanisms map cleanly onto distinct stages of the design and testing process.
- **Primary CTA scenario:** Designing a subscription pricing page with multiple tier options; decoy effect in tier structuring, halo effect from a polished visual mockup, illusion of control in A/B test interpretation, sunk cost bias in defending an existing design direction.
- **Triggering event:** A designer has spent several weeks refining a pricing page design with three tiers, including one tier deliberately structured to make the middle tier look more attractive by comparison; an A/B test of the polished mockup against a simpler alternative returns ambiguous early results.
- **Decision episodes:**
  1. Initial tier structuring, including the deliberate decoy tier design.
  2. Stakeholder review of the polished visual mockup and its perceived quality.
  3. Interpretation of early A/B test results and confidence in predicting the final outcome.
  4. Final decision on whether to ship, iterate, or abandon the current direction given the time already invested.
- **Available cues and evidence:** The three tier structures and their relative pricing/features, the polished mockup's visual quality, early A/B test data (statistically ambiguous), the weeks of design time already invested, alternative simpler designs not fully explored.
- **Competing interpretations:** The decoy tier structure genuinely improves conversion vs. is a manipulation that may not hold up under real user behavior; the polished mockup's visual quality indicates the underlying design logic is sound vs. is unrelated to actual conversion effectiveness; the early A/B data is confidently predictive of the final outcome vs. is too ambiguous to draw conclusions; the time invested justifies continuing to refine this direction vs. should not factor into the forward-looking decision.
- **Plausible actions:** Ship the current design as tested; continue testing to gather more data before deciding; pivot to the simpler alternative design; revise the tier structure based on stakeholder input.
- **Constraints and pressures:** Launch deadline, stakeholder investment in the polished design, limited A/B testing traffic/time, sunk design effort.
- **Consequences of error:** Shipping a manipulative decoy structure that damages user trust and long-term retention, or abandoning a genuinely effective design due to premature or overconfident interpretation of ambiguous data.
- **Counterfactual causal variable:** Actual statistical significance of the A/B test once fully run (later found to show no meaningful difference between the polished and simpler designs, contrary to the designer's confident early read).
- **Expected interview structure:** Opening (designer role context), Episode 1 (tier structuring), Episode 2 (mockup review), Episode 3 (A/B interpretation), Episode 4 (final decision), Closing (reflection on the role of visual polish and prior investment).
- **Natural biases:** Decoy Effect, Halo Effect, Illusion of Control, Sunk Cost Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Interaction Designer (overlaps with Interview 7; would create redundancy in the decoy-effect/halo-effect/sunk-cost mechanisms already assigned there in a design-systems rather than conversion-page context).
- **Rejected alternative occupation 2:** Product Manager (overlaps with Interview 1; illusion of control is plausible in roadmap decisions but less naturally tied to hands-on visual design execution).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Status Quo Bias, Framing Bias, Bandwagon Effect, Overconfidence Bias, Availability Bias
- **Selected occupation:** Enterprise IT Systems Administrator
- **Role and setting:** Infrastructure and operations role within an enterprise IT department; manages legacy and current systems, evaluates migration and modernization proposals, presents risk assessments to management, works within organizational budget and change-management processes.
- **Why this occupation fits the bias list:** IT administrators managing long-running legacy systems face status quo bias (preferring to maintain a stable legacy system), framing bias (how migration risk is presented to management shaping the decision), bandwagon effect (other departments' adoption of a new platform influencing the decision independent of this system's specific fit), overconfidence bias (in estimating migration timelines), and availability bias (a recent, memorable outage disproportionately shaping risk perception). All five mechanisms are well-documented in enterprise technology-adoption and legacy-system literature. [medium](https://medium.com/thethursdaythought/technical-debt-is-anchored-in-psychological-and-organisational-debt-29ac0e51c35b)
- **Primary CTA scenario:** Deciding whether to migrate a legacy internal system to a new platform after years of stable operation; status quo bias in maintaining the legacy system, framing bias in how migration risk is presented, bandwagon effect from other departments' adoption, overconfidence in migration timeline, availability bias from a recent outage memory.
- **Triggering event:** An enterprise IT administrator is asked to evaluate migrating a stable, years-old internal system to a new platform, following two other departments' recent adoption of the new platform and a memorable outage on the legacy system three months earlier.
- **Decision episodes:**
  1. Initial risk assessment of the legacy system's continued operation versus migration.
  2. Consideration of the other departments' adoption pattern as a signal for this system's migration.
  3. Estimation of the migration timeline and resource requirements.
  4. Final recommendation and framing of the risk assessment presented to management.
- **Available cues and evidence:** Legacy system's operational history and stability record, the two other departments' migration experiences (which may differ in system complexity), the recent outage's actual cause and representativeness, migration timeline estimates from similar past projects, current budget and staffing constraints.
- **Competing interpretations:** The legacy system's long stability indicates low migration urgency vs. status quo comfort obscures accumulating risk; other departments' successful adoption indicates this system should follow vs. their systems differ materially in complexity; the migration timeline estimate is realistic vs. underestimates integration complexity; the recent outage is representative of ongoing risk vs. was an isolated, already-remediated incident.
- **Plausible actions:** Recommend migration on the estimated timeline; recommend maintaining the legacy system with additional monitoring; recommend a phased migration with contingency buffers; commission an independent risk assessment before deciding.
- **Constraints and pressures:** Budget cycle timing, management's awareness of the other departments' adoption and the recent outage, staffing availability for a migration project, organizational risk tolerance.
- **Consequences of error:** Continued operation of an increasingly risky legacy system, or a poorly planned migration that disrupts operations due to overconfident timeline estimation.
- **Counterfactual causal variable:** Actual cause and representativeness of the recent outage (later found to be a one-time configuration error unrelated to the system's underlying architecture, contrary to how it was framed in the risk assessment).
- **Expected interview structure:** Opening (administrator role context), Episode 1 (risk assessment), Episode 2 (peer-adoption consideration), Episode 3 (timeline estimation), Episode 4 (framing and recommendation), Closing (reflection on how the outage memory and peer signal shaped the decision).
- **Natural biases:** Status Quo Bias, Framing Bias, Bandwagon Effect, Overconfidence Bias, Availability Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Software Architect (overlaps with Interview 6; status quo bias and overconfidence are plausible there but reserved for the six-bias architecture-selection scenario to preserve distinct decision archetypes).
- **Rejected alternative occupation 2:** Engineering Team Lead (overlaps with Interview 2; availability bias is plausible in operational contexts but bandwagon effect is less naturally tied to an active development-project role).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Anchoring Bias, Confirmation Bias, Herding, Irrational Escalation, Negativity Bias, Reactance
- **Selected occupation:** Software Architect
- **Role and setting:** Senior technical decision-making role responsible for selecting system architecture patterns for new or evolving systems; conducts technical spikes and proof-of-concept work, presents architectural decisions to a review board, balances industry trends against project-specific requirements.
- **Why this occupation fits the bias list:** Software architects make high-consequence, difficult-to-reverse technology choices under genuine uncertainty, and the technical-debt bias literature specifically documents architects as prone to anchoring on an initially proposed pattern, confirmation bias in evaluating spike/proof-of-concept results, herding toward an industry-popular pattern, irrational escalation in defending a chosen pattern once committed, negativity bias from a single failed spike, and reactance to a mandated architecture review board's feedback. All six mechanisms map cleanly onto distinct stages of the architecture-selection workflow. [arxiv](https://arxiv.org/abs/2309.14175)
- **Primary CTA scenario:** Choosing between two competing architectural patterns for a new system after initial team discussion and early technical spikes; anchoring on the first proposed architecture, confirmation bias in evaluating spike results, herding toward the industry-popular pattern, irrational escalation in defending the chosen pattern, negativity bias from one failed spike, reactance to mandated architecture review board feedback.
- **Triggering event:** A software architect proposes an initial architectural pattern early in a design discussion (an industry-popular microservices approach), the team runs technical spikes on both this pattern and an alternative, one spike for the alternative fails due to a fixable configuration issue, and the mandated architecture review board later raises concerns requiring the architect to defend the chosen direction.
- **Decision episodes:**
  1. Initial architecture proposal and team discussion, anchored on the first-presented pattern.
  2. Technical spike execution and interpretation of results for both patterns.
  3. Reaction to the alternative pattern's failed spike and to the industry-popular pattern's associated momentum.
  4. Response to the architecture review board's feedback and final architectural commitment.
  5. (Optional continuation) Defense of the chosen pattern as implementation proceeds and further evidence emerges.
- **Available cues and evidence:** The initially proposed pattern and its rationale, spike results for both patterns, the failed spike's root cause, industry adoption trends for the popular pattern, the review board's specific concerns, implementation progress data.
- **Competing interpretations:** The initially proposed pattern remains the strongest choice vs. was simply the first anchor and deserves re-evaluation; the failed spike indicates a fundamental flaw in the alternative vs. a fixable configuration issue; industry popularity indicates genuine technical merit for this project vs. reflects trends not specific to this project's needs; the review board's feedback reflects a valid concern vs. an unwelcome constraint on the architect's autonomy.
- **Plausible actions:** Proceed with the initially proposed, industry-popular pattern; switch to the alternative pattern after fixing the spike's configuration issue; commission additional spikes before deciding; revise the architecture in response to the review board's feedback.
- **Constraints and pressures:** Project timeline pressure to commit to an architecture, the architect's professional investment in the initial proposal, review board authority and process requirements, industry trend visibility.
- **Consequences of error:** Committing to an architecture poorly suited to the project's actual requirements due to anchoring, herding, or defensive escalation, with significant downstream cost to change once implementation is underway.
- **Counterfactual causal variable:** Actual root cause of the alternative pattern's failed spike (later found to be a fixable configuration issue unrelated to the pattern's fundamental suitability).
- **Expected interview structure:** Opening (architect role context), Episode 1 (initial proposal and anchor), Episode 2 (spike interpretation), Episode 3 (reaction to failure and industry momentum), Episode 4 (review board response and commitment), Closing (reflection on the six-mechanism decision process).
- **Natural biases:** Anchoring Bias, Confirmation Bias, Herding, Irrational Escalation, Negativity Bias, Reactance.
- **Plausible but difficult biases:** None outright, but six biases require distribution across the four-to-five distinct decision episodes to avoid compression into a single point.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Engineering Team Lead (overlaps with Interview 2; irrational escalation and negativity bias already assigned there in a migration-continuation rather than architecture-selection context).
- **Rejected alternative occupation 2:** Product Manager (overlaps with Interview 1; herding already assigned there in a feature-adoption rather than technical-architecture context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Priming Effect, Cognitive Dissonance, Decoy Effect, Halo Effect, Illusion of Control, Sunk Cost Bias, Status Quo Bias
- **Selected occupation:** Interaction Designer (Design Systems Lead)
- **Role and setting:** Senior design role responsible for a shared design-system component library used across multiple product teams; leads redesign initiatives for core components, presents variants to cross-functional stakeholders, manages the tension between design consistency and evolving user needs.
- **Role and setting (continued):** Works with long design-review cycles, governance processes, and significant organizational visibility for design-system changes.
- **Why this occupation fits the bias list:** Design-systems leads redesign long-standing, widely-used components under conditions where priming effect (recent exposure to a competitor's redesign shaping the lead's initial framing), cognitive dissonance (reconciling a prior public commitment to the legacy pattern with evidence favoring change), decoy effect (presenting component variants to stakeholders in a way that steers preference toward one option), halo effect (a well-received prototype demo coloring the perceived quality of the underlying design), illusion of control (overestimating the ability to manage a smooth cross-team rollout), sunk cost bias (defending prior design investment in the legacy component), and status quo bias (resisting full replacement of an established pattern) are all plausible, though priming effect requires an isolable, distinct exposure event to avoid being conflated with ordinary competitive awareness.
- **Primary CTA scenario:** Redesigning a core design-system component after being primed by a competitor's redesign and encountering resistance to abandoning a legacy component; priming effect from competitor exposure, cognitive dissonance after public commitment to the legacy pattern, decoy effect in presenting component variants to stakeholders, halo effect from a well-received prototype, illusion of control in rollout timeline, sunk cost bias in defending prior design investment, status quo bias in resisting full replacement.
- **Triggering event:** Shortly after attending a conference talk showcasing a competitor's redesigned component, a design-systems lead — who has publicly defended the current component pattern in past design reviews — is tasked with proposing an update; the lead presents three variants to stakeholders, one deliberately weaker to steer preference, and a well-received prototype demo shapes stakeholder enthusiasm ahead of a cross-team rollout.
- **Decision episodes:**
  1. Initial framing of the redesign problem shortly after the competitor exposure at the conference.
  2. Reconciliation of the lead's own prior public defense of the legacy pattern with the case for change.
  3. Presentation of three component variants to stakeholders, including the deliberately weaker option.
  4. Prototype demo and stakeholder reaction, followed by rollout timeline planning across multiple dependent product teams.
- **Available cues and evidence:** The competitor's redesign and the conference exposure, the lead's own prior review comments defending the legacy pattern, the three variants and their relative strengths, the prototype demo's reception, the actual complexity of coordinating rollout across dependent teams, time and effort already invested in the legacy component's original design.
- **Competing interpretations:** The competitor's redesign indicates a genuine improvement opportunity vs. is being over-weighted simply due to recent, vivid exposure; the case for change is well-supported vs. the lead's discomfort with contradicting their own prior stated position is shaping the framing; the preferred variant is genuinely superior vs. was made to look superior by the weaker comparison option; the prototype's positive reception indicates rollout will be smooth vs. does not reflect the actual cross-team coordination complexity; the legacy component's design investment is a sunk cost vs. still has ongoing value that should factor into the decision.
- **Plausible actions:** Proceed with full replacement on an aggressive rollout timeline; propose an incremental, lower-risk transition preserving parts of the legacy pattern; present all variants neutrally and let stakeholders decide without a steered comparison; commission independent cross-team impact assessment before committing to a timeline.
- **Constraints and pressures:** Cross-team dependency complexity, the lead's own prior public position, governance review cycle timing, stakeholder enthusiasm following the demo, organizational visibility of design-system changes.
- **Consequences of error:** A rushed, poorly coordinated rollout disrupting multiple dependent product teams, or continued reliance on the legacy component despite compelling evidence for change, due to sunk cost and status quo pressures.
- **Counterfactual causal variable:** Actual cross-team rollout complexity (later found to require significantly more coordination than the lead estimated, contrary to confidence following the well-received prototype demo).
- **Expected interview structure:** Opening (design-systems lead role context), Episode 1 (post-conference framing), Episode 2 (reconciling prior position), Episode 3 (variant presentation), Episode 4 (demo reaction and rollout planning), Closing (reflection on competitor exposure, prior commitment, and rollout confidence).
- **Natural biases:** Cognitive Dissonance, Decoy Effect, Halo Effect, Sunk Cost Bias, Status Quo Bias.
- **Plausible but difficult biases:** Priming Effect (requires the conference exposure to be clearly isolated as the priming event, distinct from general professional awareness of industry trends), Illusion of Control (requires the rollout-complexity gap to be explicit and attributable to overestimated control rather than simple optimism).
- **Biases that should not be forced:** None outright, but Priming Effect must not be inferred merely from the lead having seen a competitor's product, which is ordinary professional awareness rather than a priming mechanism.
- **Rejected alternative occupation 1:** UX/Product Designer (overlaps with Interview 4; decoy effect, halo effect, and sunk cost bias already assigned there in a pricing-page rather than design-systems context).
- **Rejected alternative occupation 2:** Software Architect (overlaps with Interview 6; status quo bias and related mechanisms already assigned there in a technical architecture rather than design-systems context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Priming Effect requires an explicit, isolable priming event distinct from ordinary competitive awareness; Illusion of Control requires an explicit rollout-complexity gap)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (product manager, engineering team lead, UX researcher, UX/product designer, IT systems administrator, software architect, interaction designer) | None | None | None | None needed |
| Work setting | Product strategy/office (1), Technical/engineering (2, 6), Research/perceptual (3), Design/creative (4, 7), Infrastructure/operations (5) | Technical/engineering (2/7: 2, 6) | Technical/engineering | Field-based, public-facing | None critical; reflects the domain's inherently technical/design/research composition, and Interviews 2 and 6 differ materially in decision authority and consequence horizon |
| Decision type | Resource allocation/adoption (1), Troubleshooting/continuation (2), Diagnosis/interpretation (3), Design/creative judgment (4, 7), Risk assessment (5), Design/creative judgment + architecture (6) | Design/creative judgment (3/7: 4, 6, 7) | Design/creative judgment | Negotiation, Compliance/adjudication | None critical; design/creative judgment is the natural core of much of this domain, but each instance differs materially in artifact type (pricing page, architecture, design system) |
| Information environment | Socially-mediated/market signals (1), Data-heavy/technical (2, 6), Perceptual/experiential (3), Data-heavy/quantified (4), Organizational/socially-mediated (5), Cross-team/socially-mediated (7) | Data-heavy (2/7: 2, 6) | Balanced | Regulated/documentation-heavy as primary driver | None critical |
| Time pressure | Moderate (1, 3, 4), High (2, 6), Moderate-high (5, 7) | Moderate (3/7) | Moderate | Low | None critical |
| Consequence of error | Resource/strategic (1), Financial/technical debt (2), Product quality/reputational (3, 4), Operational/organizational risk (5), High-consequence/technical debt (6), Cross-team/organizational (7) | Technical debt-related (2/7: 2, 6) | Balanced | Legal/regulatory, environmental | None critical; reflects the domain's technical and product consequence profile |
| Expertise level | Independent professional (1, 3, 4), Senior practitioner/team lead (2), Senior practitioner/decision authority (5, 6), Senior practitioner/lead (7) | Senior practitioner (4/7: 2, 5, 6, 7) | Senior practitioner | Developing practitioner | None critical; reflects that consequential, bias-rich decisions in this domain often sit with more senior roles, though Interviews 1, 3, and 4 provide independent-professional contrast |
| Stakeholder pattern | Individual with market signals (1), Team leadership (2), Individual with research participants (3), Individual with tools (4), Individual with organizational stakeholders (5), Team with review board (6), Individual with cross-team stakeholders (7) | None significant | None | Multi-party negotiation | None critical |
| Scenario archetype | Feature-adoption decision (1), Migration continuation (2), Usability study interpretation (3), Pricing-page design (4), Legacy-system migration (5), Architecture selection (6), Design-system redesign (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Competitor user-base fit (1), Setback root cause (2), Resistance source (3), A/B test significance (4), Outage representativeness (5), Spike failure cause (6), Rollout complexity (7) | None significant | None | Equipment/technical hardware failure as primary variable | None critical; all seven turn on a distinct, plausible causal fact appropriate to the domain |

**Overall assessment:** Strong diversity across occupations, settings, and decision types, spanning product strategy, engineering leadership, research, design execution, infrastructure operations, architecture, and design-systems governance. Design/creative judgment and technical-debt-adjacent decisions recur across a few interviews, which is expected given the domain's inherent focus on design and engineering decision-making, but each instance differs materially in artifact, stakeholder configuration, and causal structure. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Herding (clear mechanism: following observed peer behavior over independent analysis) | None | Herding (risk of being read as simply "followed the trend and it was wrong") | None | None | None | Show the PM explicitly observing multiple competitors before deciding, not just making a similar feature independently; probe the reasoning for following the pattern, not just the outcome |
| 2 | Irrational Escalation (continued investment due to prior investment), Negativity Bias (recent-setback overweighting) | Irrational Escalation and Sunk Cost Bias (closely related; irrational escalation is the behavioral continuation, sunk cost bias the underlying valuation of past investment) | None | None | None | None | Show the team lead explicitly citing the amount already invested as a reason to continue, distinct from a reasoned assessment of future viability; separate the recent-setback weighting from the total-investment reasoning |
| 3 | Reactance (resistance interpretation), Priming Effect (introductory framing influence), Cognitive Dissonance (prior-commitment reconciliation) | Reactance and Cognitive Dissonance (both can involve resistance to change, though reactance concerns participant/researcher interpretation of pushback and cognitive dissonance concerns reconciling one's own prior commitment) | None | None | Priming Effect (the introductory framing's influence must be explicit and shown to shape interpretation, not just mentioned) | Priming Effect | Show the introductory script's specific framing language and its demonstrable effect on interpretation; separate the researcher's own dissonance (about the design team's commitment) from participants' reactance |
| 4 | Decoy Effect (tier structuring), Halo Effect (visual-polish influence), Illusion of Control (test-outcome overconfidence), Sunk Cost Bias (design-investment defense) | Halo Effect and Illusion of Control (both involve overestimating quality/predictability from a positive surface impression) | None | None | None | None | Show the decoy tier's deliberate structuring explicitly; separate the mockup's visual quality assessment from the statistical confidence judgment about the A/B test |
| 5 | Status Quo Bias, Framing Bias, Bandwagon Effect, Overconfidence Bias, Availability Bias (five distinct) | Bandwagon Effect and Herding (closely related; bandwagon in this list concerns organizational peer-adoption, herding in Interview 1/6 concerns market/technical trend-following) | None | None | Framing Bias (must show explicit alternative framings of the same risk to isolate this from simple risk communication) | Framing Bias | Show two different ways the same migration risk could have been framed, and which one was chosen and why; separate the outage-memory availability bias from the peer-adoption bandwagon effect as distinct cues |
| 6 | Anchoring Bias, Confirmation Bias, Herding, Irrational Escalation, Negativity Bias, Reactance (six distinct mechanisms across decision phases) | Anchoring Bias and Herding (both involve an external reference point, though anchoring concerns the first-proposed option and herding concerns industry-wide adoption patterns), Irrational Escalation and Confirmation Bias (both involve resistance to disconfirming evidence after commitment) | None | None | Reactance (must show an explicit negative reaction to the review board's authority, not just disagreement with its content) | Reactance | Distribute the six biases across the four-to-five distinct episodes; show the architect's specific negative reaction to being told what to do by the review board (reactance) as distinct from simply disagreeing with the feedback's technical content |
| 7 | Cognitive Dissonance, Decoy Effect, Halo Effect, Sunk Cost Bias, Status Quo Bias (five cleanly distinguishable); Priming Effect, Illusion of Control (require careful framing) | Sunk Cost Bias and Status Quo Bias (closely related; sunk cost concerns past investment justification, status quo concerns preference for the current state independent of investment), Priming Effect and ordinary competitive awareness (risk of conflation) | None | None | Priming Effect (competitor exposure must be shown as a specific, isolable event with a demonstrable framing effect), Illusion of Control (rollout confidence must be shown as exceeding the actual, articulable complexity) | Priming Effect, Illusion of Control | Mark the conference exposure as a specific, dated event with an explicit before/after framing shift; show the rollout complexity gap explicitly (e.g., a specific dependency the lead did not account for) rather than inferring illusion of control from general optimism |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interview 6, distribute all six biases across distinct decision phases and ensure Reactance is grounded in a negative reaction to authority/process rather than simple technical disagreement. For Interview 7, ensure Priming Effect is tied to a specific, dated exposure event with a demonstrable framing shift, and Illusion of Control is tied to an explicit, articulable complexity gap rather than general confidence. For Interviews 2 and 6, keep Irrational Escalation/Confirmation Bias distinct from Sunk Cost Bias/Negativity Bias by showing the specific reasoning pattern (continuation-due-to-investment vs. recent-event overweighting) rather than a single blended justification.
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, with particular attention to distinguishing closely related neighboring pairs identified above (Bandwagon/Herding across Interviews 1, 5, 6; Sunk Cost/Status Quo in Interview 7; Anchoring/Herding in Interview 6). Flag any bias supported only by the case's ultimate outcome rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules.
