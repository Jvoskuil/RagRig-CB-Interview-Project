## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | High School Classroom Teacher | Grading a large stack of end-of-term essays and settling on scores that cluster toward the middle of the rubric range; averaging bias in combining multiple assignment scores into a final grade | 100% | 3 | High | Adds individual grading task, rubric-based, moderate time pressure context | APPROVED |
| 2 | 2 | Curriculum Coordinator / Instructional Coach | Reviewing a new teaching method proposal that challenges the coordinator's own long-used approach; biased assimilation in evaluating supporting vs. contradicting evidence, egocentric bias in favoring self-authored materials | 100% | 6 | High | Adds evidence-evaluation, peer-review, moderate procedural structure context | APPROVED |
| 3 | 3 | Special Education Caseworker / IEP Coordinator | Assessing a student's progress on an Individualized Education Program after a difficult first-quarter interaction; group attribution error toward the student's demographic group, present bias in short-term behavior weighting, horn effect from an early negative impression | 100% | 9 | High | Adds one-to-one student relationship, longitudinal case management context | APPROVED |
| 4 | 4 | School Principal / Building Administrator | Deciding whether to approve a teacher's request for a new intervention program based on a persuasive but thin proposal; bounded rationality in limited review time, coherence-based reasoning in constructing a supportive narrative, illusion of understanding of the program's mechanism, self-enhancement bias in taking credit for the decision | 100% | 12 | High | Adds administrative decision authority, resource allocation, moderate time pressure context | APPROVED |
| 5 | 5 | University Admissions Officer | Evaluating a borderline applicant file where an early strong personal statement colors the reading of later academic records; belief perseverance and attitude polarization after committing to an initial impression, fundamental attribution bias in explaining a low grade, halo effect from one outstanding recommendation letter, ingroup favoritism toward applicants from the officer's own alma mater, ambiguity aversion toward an unconventional transcript | 100% | 15 | High | Adds high-stakes gatekeeping, document-based, individual review context | APPROVED |
| 6 | 6 | School District Curriculum Committee Member | Participating in a committee meeting to select a new districtwide reading program; bandwagon effect as colleagues voice early support, groupthink in committee consensus, availability bias from a recently attended vendor demonstration, anchoring bias on the first program presented, confirmation bias in evaluating pilot data, averaging bias in combining committee members' ratings | 100% | 18 | High | Adds team decision-making, multi-stakeholder, resource allocation context | APPROVED |
| 7 | 7 | Academic Department Chair (Higher Education) | Reviewing a junior faculty member's tenure case file after a strong initial impression from their job talk years earlier; biased assimilation in evaluating mixed teaching evaluations, egocentric bias in weighting the chair's own mentorship contribution, group attribution error toward the candidate's subfield, present bias in weighting recent publication output, horn effect from one negative student comment, bounded rationality in reviewing a large case file under deadline, coherence-based reasoning in constructing a case narrative | 86% | 19 | Moderate-High | Adds high-stakes personnel evaluation, document-heavy, committee-adjacent context | APPROVED_WITH_CAVEATS (Egocentric Bias requires careful framing distinct from ordinary self-attribution) |

***

## 2. Candidate occupation matrix

### Interview 1 (Averaging Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| High School Classroom Teacher | 1 (Averaging Bias) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (grading phases across multiple assignments) | High (change one component score's weight/validity) | High | High (adds individual grading, rubric-based context) | 0.88 |
| Curriculum Committee Member | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.76 |
| University Admissions Officer | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.60 |
| Instructional Coach | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.55 |
| Department Chair | 0 | 0 | 1 | 0 | 25% | Low | High | High | High | Low (overlaps with Interview 7) | 0.45 |

**Selected:** High School Classroom Teacher (best coverage, distinctness, diversity fit; grounded directly in the teacher grading-bias literature). [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S004727272200175X)

***

### Interview 2 (Biased Assimilation, Egocentric Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Curriculum Coordinator / Instructional Coach | 2 (Biased Assimilation, Egocentric) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (evidence review, peer proposal evaluation) | High (change quality of the new method's supporting data) | High | High (adds evidence-evaluation, peer-review context) | 0.90 |
| Department Chair | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 7) | 0.72 |
| Admissions Officer | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.65 |
| Classroom Teacher | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.50 |
| Principal | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.62 |

**Selected:** Curriculum Coordinator / Instructional Coach (best coverage, distinctness, diversity fit; introduces a peer-evidence-evaluation role distinct from direct student assessment).

***

### Interview 3 (Group Attribution Error, Present Bias, Horn Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Special Education Caseworker / IEP Coordinator | 3 (Group Attribution Error, Present Bias, Horn Effect) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (longitudinal case review, one-to-one relationship) | High (change the first-interaction context) | High | High (adds longitudinal case management, one-to-one context) | 0.92 |
| Classroom Teacher | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 1) | 0.76 |
| School Counselor | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Medium | 0.72 |
| Department Chair | 1 | 2 | 0 | 0 | 83% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.65 |
| Admissions Officer | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.58 |

**Selected:** Special Education Caseworker / IEP Coordinator (best coverage, distinctness, diversity fit).

***

### Interview 4 (Bounded Rationality, Coherence-based Reasoning, Illusion of Understanding, Self-Enhancement Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| School Principal / Building Administrator | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (proposal review, resource allocation decision) | High (change proposal evidence quality) | High | High (adds administrative authority, resource allocation context) | 0.94 |
| Department Chair | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.80 |
| Curriculum Coordinator | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 2) | 0.70 |
| Admissions Officer | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.62 |
| Committee Member | 2 | 1 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.58 |

**Selected:** School Principal / Building Administrator (best coverage, distinctness, scenario richness).

***

### Interview 5 (Belief Perseverance/Attitude Polarisation, Fundamental Attribution Bias, Halo Effect, Ingroup Favoritism, Ambiguity Aversion)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| University Admissions Officer | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (multi-document file review phases) | High (change the reliability of one document) | High | High (adds high-stakes gatekeeping, document-based context) | 0.95 |
| Department Chair | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.80 |
| Principal | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 4) | 0.74 |
| IEP Coordinator | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.68 |
| Classroom Teacher | 2 | 2 | 1 | 0 | 80% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.62 |

**Selected:** University Admissions Officer (best coverage, distinctness, diversity fit).

***

### Interview 6 (Bandwagon Effect, Groupthink, Availability Bias, Anchoring Bias, Confirmation Bias, Averaging Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| School District Curriculum Committee Member | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms across meeting phases) | High (multi-phase committee meeting, multiple stakeholders) | High (change pilot data accuracy) | High | High (adds team decision-making, multi-stakeholder context) | 0.96 |
| Principal | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Low (overlaps with Interview 4) | 0.82 |
| Department Chair | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 7) | 0.74 |
| Classroom Teacher | 3 | 2 | 1 | 0 | 83% | Moderate-High | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.62 |
| Instructional Coach | 4 | 1 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.68 |

**Selected:** School District Curriculum Committee Member (best coverage, distinctness, diversity fit).

***

### Interview 7 (Biased Assimilation, Egocentric Bias, Group Attribution Error, Present Bias, Horn Effect, Bounded Rationality, Coherence-based Reasoning)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Academic Department Chair (Higher Education) | 5 (Biased Assimilation, Group Attribution Error, Present Bias, Horn Effect, Bounded Rationality, Coherence-based Reasoning) | 2 (Egocentric Bias) | 0 | 0 | 100% | Moderate-High (Egocentric Bias requires careful framing) | High (tenure case review phases, multiple document types) | High (change one teaching evaluation's context) | High | High (adds high-stakes personnel evaluation, document-heavy context) | 0.88 |
| Principal | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.78 |
| Admissions Officer | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.76 |
| IEP Coordinator | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.72 |
| Curriculum Coordinator | 3 | 3 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.70 |

**Selected:** Academic Department Chair (Higher Education) (best diversity fit, adds personnel-evaluation/tenure-review context; Egocentric Bias requires careful design distinct from ordinary self-attribution).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Averaging Bias
- **Selected occupation:** High School Classroom Teacher
- **Role and setting:** Classroom-based instructional role; grades assignments, tests, and projects against a rubric, combines multiple component scores into term grades, works largely individually under grading-period deadlines.
- **Why this occupation fits the bias list:** Teachers routinely combine several distinct pieces of evidence (a strong project, a weak quiz, a middling essay) into a single overall grade. Averaging bias — treating each component as equally informative and blending them toward the middle rather than weighting the most diagnostic evidence appropriately — is a well-documented mechanism in teacher grade-determination research, particularly around "cusp grade" decisions. [digitalcommons.georgefox](https://digitalcommons.georgefox.edu/edd/179/)
- **Primary CTA scenario:** Grading a large stack of end-of-term essays and settling on scores that cluster toward the middle of the rubric range; averaging bias in combining multiple assignment scores into a final grade.
- **Triggering event:** A teacher is finalizing term grades for a student whose component scores are unusually spread — one exceptional project, two average quizzes, and one poor exam — and must decide on a single term grade before the deadline.
- **Decision episodes:**
  1. Initial review of each component score in isolation.
  2. Combination of the components into a preliminary overall impression.
  3. Consideration of whether the most recent or most diagnostic piece of evidence should carry more weight than a simple average.
  4. Final grade determination and decision on whether to note a discrepancy for the student/parent.
- **Available cues and evidence:** The four component scores and their dates, the rubric's stated weighting scheme, the student's overall pattern of engagement, prior term grades for context.
- **Competing interpretations:** All four components are equally informative of the student's mastery vs. the exceptional project or the poor exam is more diagnostic of true understanding; a simple average is fair vs. understates or overstates actual mastery.
- **Plausible actions:** Assign a grade close to the simple average of all components; weight the most recent assessment more heavily; weight the strongest demonstration of mastery more heavily; consult the rubric's stated weighting rules strictly.
- **Constraints and pressures:** Grading-period deadline, rubric policy constraints, parent/student expectations for consistency, workload from grading many students simultaneously.
- **Consequences of error:** A term grade that under- or overstates the student's actual mastery, affecting placement, eligibility, or the student's own self-assessment.
- **Counterfactual causal variable:** Actual diagnosticity of the poor exam score (later found to reflect a testing-day illness rather than a genuine gap in mastery).
- **Expected interview structure:** Opening (teacher role context), Episode 1 (component review), Episode 2 (combination into overall impression), Episode 3 (weighting consideration), Closing (reflection on how the components were combined).
- **Natural biases:** Averaging Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** School District Curriculum Committee Member (would overlap with Interview 6's more team-based averaging-of-ratings mechanism).
- **Rejected alternative occupation 2:** University Admissions Officer (overlaps with Interview 5; averaging bias is plausible in file review but less naturally isolated from the five other mechanisms already assigned there).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Biased Assimilation, Egocentric Bias
- **Selected occupation:** Curriculum Coordinator / Instructional Coach
- **Role and setting:** District or school-level instructional support role; evaluates new teaching methods, materials, or programs proposed by teachers or vendors, often against the coordinator's own established approach that they may have authored or long championed.
- **Why this occupation fits the bias list:** Curriculum coordinators frequently review evidence (pilot data, research studies, teacher testimonials) for new methods that compete with an approach the coordinator has personally invested in. Biased assimilation — interpreting mixed or ambiguous evidence as supporting one's prior position — and egocentric bias — overweighting one's own contribution or authored materials relative to their actual merit — are both natural and distinct mechanisms in this evidence-evaluation context.
- **Primary CTA scenario:** Reviewing a new teaching method proposal that challenges the coordinator's own long-used approach; biased assimilation in evaluating supporting vs. contradicting evidence, egocentric bias in favoring self-authored materials.
- **Triggering event:** A teacher proposes adopting a new reading intervention method, presenting pilot data that is genuinely mixed (strong results in one cohort, weak in another), while the coordinator has spent several years developing and promoting the current districtwide approach.
- **Decision episodes:**
  1. Initial review of the new method's pilot data alongside the coordinator's own approach's track record.
  2. Interpretation of the mixed pilot results in light of prior commitment to the current approach.
  3. Comparison of the two approaches' materials, including the coordinator's self-authored resources.
  4. Final recommendation on whether to pilot, adopt, or reject the new method districtwide.
- **Available cues and evidence:** New method's pilot data (mixed results), coordinator's own approach's historical outcome data, self-authored training materials and their usage records, teacher feedback on both approaches.
- **Competing interpretations:** The mixed pilot results indicate the new method is not yet proven vs. indicate genuine promise obscured by implementation variability; the coordinator's self-authored materials are effective because of their content vs. because of the effort invested in creating them.
- **Plausible actions:** Recommend continuing with the current approach; recommend a broader pilot of the new method; recommend a hybrid approach; commission an independent evaluation of both.
- **Constraints and pressures:** Professional investment in the current approach, budget for new materials, teacher buy-in considerations, district timeline for curriculum review cycles.
- **Consequences of error:** Continued use of a less effective method due to attachment to prior work, or premature abandonment of an effective established approach based on weak new evidence.
- **Counterfactual causal variable:** Actual cause of the pilot's mixed results (later found to stem from inconsistent implementation fidelity in the weak cohort, not the method itself).
- **Expected interview structure:** Opening (coordinator role context), Episode 1 (data review), Episode 2 (interpretation of mixed results), Episode 3 (materials comparison), Closing (reflection on the role of prior investment in the recommendation).
- **Natural biases:** Biased Assimilation, Egocentric Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Academic Department Chair (overlaps with Interview 7; both mechanisms are plausible there but reserved for the more complex seven-bias tenure-review scenario).
- **Rejected alternative occupation 2:** School Principal (overlaps with Interview 4; egocentric bias is plausible in administrative decisions but less naturally tied to evidence-evaluation of competing methods).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Group Attribution Error, Present Bias, Horn Effect
- **Selected occupation:** Special Education Caseworker / IEP Coordinator
- **Role and setting:** Student-support role managing Individualized Education Programs (IEPs); conducts ongoing progress reviews, documents behavioral and academic observations over an extended relationship with each student, coordinates with teachers, parents, and specialists.
- **Why this occupation fits the bias list:** IEP coordinators form impressions of individual students partly shaped by group-level assumptions (group attribution error — attributing a student's behavior to characteristics of their demographic or disability group rather than individual circumstances), by recent short-term behavior rather than longer developmental trajectory (present bias), and by an early negative interaction that colors subsequent interpretation (horn effect). These are well-documented in longitudinal case-management and student-assessment literature. [resources.depaul](https://resources.depaul.edu/teaching-commons/teaching-guides/feedback-grading/Pages/assessment-and-bias.aspx)
- **Primary CTA scenario:** Assessing a student's progress on an Individualized Education Program after a difficult first-quarter interaction; group attribution error toward the student's demographic group, present bias in short-term behavior weighting, horn effect from an early negative impression.
- **Triggering event:** A caseworker is preparing a quarterly IEP progress review for a student who had a disruptive first interaction months ago; the current quarter's data shows substantial improvement, but the caseworker's initial impression and general assumptions about students with similar backgrounds shape the review.
- **Decision episodes:**
  1. Initial recall of the difficult first interaction and its lasting impression.
  2. Review of the current quarter's behavioral and academic data.
  3. Interpretation of the data in light of assumptions about the student's demographic or disability group.
  4. Final progress determination and recommendation for the IEP team meeting.
- **Available cues and evidence:** First-quarter incident notes, current-quarter behavioral and academic records, teacher observations across the full period, general patterns the caseworker has observed among students with similar backgrounds.
- **Competing interpretations:** The student's early behavior reflects their true underlying tendencies vs. was situational and has genuinely changed; broader group-level patterns are informative for this student vs. this student's individual trajectory should be assessed independently; recent data is most representative vs. the full longitudinal record should carry equal weight.
- **Plausible actions:** Report substantial progress based on current data; report continued concern based on the lasting first impression; recommend continued monitoring without a clear determination; request additional input from other teachers to counterbalance the caseworker's own impression.
- **Constraints and pressures:** IEP review deadlines, parent and team expectations, caseload size limiting individualized attention, the caseworker's own accumulated impressions across many similar cases.
- **Consequences of error:** Under-recognition of genuine progress delaying appropriate service reduction, or premature service reduction based on outdated impressions.
- **Counterfactual causal variable:** Actual cause of the first-quarter incident (later found to be an unrelated, temporary family disruption rather than an indicator of the student's typical behavior).
- **Expected interview structure:** Opening (caseworker role context), Episode 1 (recall of first impression), Episode 2 (current data review), Episode 3 (interpretation and determination), Closing (reflection on how the early interaction shaped the review).
- **Natural biases:** Group Attribution Error, Present Bias, Horn Effect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Classroom Teacher (overlaps with Interview 1; horn effect and present bias are plausible in daily grading but less naturally tied to the longitudinal case-management structure needed for group attribution error).
- **Rejected alternative occupation 2:** Academic Department Chair (overlaps with Interview 7; group attribution error and horn effect already assigned there in a tenure-review rather than student-relationship context).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Bounded Rationality, Coherence-based Reasoning or Rationalisation, Illusion of Understanding, Self-Enhancement or Self-serving Bias
- **Selected occupation:** School Principal / Building Administrator
- **Role and setting:** School-level administrative leadership role; reviews and approves teacher proposals for new programs or interventions, allocates limited school resources, makes decisions under significant time constraints across many competing demands.
- **Why this occupation fits the bias list:** Principals must evaluate proposals with limited time and imperfect information (bounded rationality), often construct an internally consistent supportive narrative once inclined toward a decision (coherence-based reasoning), may believe they understand a program's mechanism of action better than the evidence warrants (illusion of understanding), and may later attribute a successful outcome disproportionately to their own decision-making (self-enhancement bias). These four mechanisms map cleanly onto distinct stages of administrative decision-making.
- **Primary CTA scenario:** Deciding whether to approve a teacher's request for a new intervention program based on a persuasive but thin proposal; bounded rationality in limited review time, coherence-based reasoning in constructing a supportive narrative, illusion of understanding of the program's mechanism, self-enhancement bias in taking credit for the decision.
- **Triggering event:** A teacher submits a persuasive proposal for a new classroom intervention program, citing a compelling but thin evidence base, during a week when the principal has limited time due to competing budget and staffing demands.
- **Decision episodes:**
  1. Initial rapid review of the proposal under severe time constraints.
  2. Construction of a supportive rationale for why the program should work, filling gaps in the thin evidence with plausible-sounding mechanism explanations.
  3. Approval decision and resource allocation.
  4. Later reflection (e.g., at a staff meeting) on the outcome and the principal's role in the decision.
- **Available cues and evidence:** The proposal document, the teacher's verbal pitch, the principal's competing time demands, the program's actual (thin) evidence base, other similar programs' documented outcomes elsewhere.
- **Competing interpretations:** The proposal's compelling narrative reflects genuine likely effectiveness vs. thin evidence that hasn't been adequately scrutinized; the principal's understanding of why the program should work is accurate vs. an oversimplified or incorrect mental model; a successful outcome should be attributed to the program and staff execution vs. to the principal's approval decision specifically.
- **Plausible actions:** Approve the proposal as presented; request additional evidence before deciding; approve with modified scope or a trial period; decline and suggest revision.
- **Constraints and pressures:** Severe time limitations from competing demands, budget constraints, staff morale considerations, the principal's own accountability for school outcomes.
- **Consequences of error:** Approval of an ineffective program diverting scarce resources, or rejection of a genuinely promising program due to insufficient review time.
- **Counterfactual causal variable:** Actual mechanism by which the program affects student outcomes (later found to work through a different pathway than the principal's understanding, with implications for how it should be implemented).
- **Expected interview structure:** Opening (principal role context), Episode 1 (rapid review), Episode 2 (rationale construction), Episode 3 (approval decision), Episode 4 (later reflection on outcome), Closing (reflection on time constraints and understanding).
- **Natural biases:** Bounded Rationality, Coherence-based Reasoning or Rationalisation, Illusion of Understanding, Self-Enhancement or Self-serving Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Academic Department Chair (overlaps with Interview 7; bounded rationality and coherence-based reasoning already assigned there in a tenure-review rather than program-approval context).
- **Rejected alternative occupation 2:** Curriculum Coordinator (overlaps with Interview 2; illusion of understanding is plausible but self-enhancement bias is less naturally tied to a non-decision-authority evaluative role).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Belief Perseverance and Attitude Polarisation, Fundamental Attribution Bias, Halo Effect, Ingroup Favoritism or In-group Bias, Ambiguity Aversion
- **Selected occupation:** University Admissions Officer
- **Role and setting:** Higher-education admissions role; reviews complete applicant files (transcripts, personal statements, recommendation letters, test scores) to make or recommend admission decisions, often working individually within a broader committee process, under application-cycle deadlines.
- **Why this occupation fits the bias list:** Admissions officers read multi-document files in a sequence that can create belief perseverance and attitude polarization (an early strong impression from one document hardening rather than updating with later information), make dispositional judgments about an applicant's circumstances (fundamental attribution bias — attributing a low grade to the applicant's ability rather than situational factors), let one outstanding element halo the assessment of the whole file (halo effect), favor applicants who share the officer's own background or institution (ingroup favoritism), and are less comfortable admitting applicants with unconventional or hard-to-categorize records (ambiguity aversion). All five mechanisms are well-documented in admissions and file-review research and map onto distinct stages of file review. [education-ni.gov](https://www.education-ni.gov.uk/sites/default/files/2026-06/June%202026%20Newsletter%20-%20Cognitive%20Biases_0.PDF)
- **Primary CTA scenario:** Evaluating a borderline applicant file where an early strong personal statement colors the reading of later academic records; belief perseverance and attitude polarization after committing to an initial impression, fundamental attribution bias in explaining a low grade, halo effect from one outstanding recommendation letter, ingroup favoritism toward applicants from the officer's own alma mater, ambiguity aversion toward an unconventional transcript.
- **Triggering event:** An admissions officer reads a borderline applicant's exceptionally strong personal statement first, forms a positive initial impression, and then encounters a low grade in one course, an outstanding recommendation letter, an unconventional transcript pattern (a gap year with nontraditional coursework), and the fact that the applicant attended the officer's own undergraduate institution.
- **Decision episodes:**
  1. Initial reading of the personal statement and formation of a strong positive impression.
  2. Encounter with the low grade and explanation of its cause.
  3. Encounter with the outstanding recommendation letter and the applicant's shared alma mater.
  4. Encounter with the unconventional transcript and final admission recommendation.
- **Available cues and evidence:** Personal statement content, full transcript including the low grade, recommendation letters, applicant's undergraduate institution, standardized test scores, the unconventional gap-year coursework pattern.
- **Competing interpretations:** The low grade reflects the applicant's genuine ability limitation vs. a situational circumstance (illness, family crisis) unrelated to ability; the outstanding letter reflects the applicant's true qualities vs. one recommender's generous style; shared alma mater is irrelevant to merit vs. provides genuine insight into fit; the unconventional transcript indicates risk vs. reflects valuable nontraditional experience.
- **Plausible actions:** Recommend admission based on the strong initial impression; recommend denial based on the low grade and unconventional pattern; request additional information (an interview or further documentation); refer the file to committee for a second read.
- **Constraints and pressures:** Application-cycle deadlines, institutional enrollment targets, committee review norms, the officer's own educational background and institutional loyalty.
- **Consequences of error:** Admission of an applicant whose file was favorably distorted by early impression and shared background, or denial of a genuinely qualified applicant due to an unconventional record or an unexplained low grade.
- **Counterfactual causal variable:** Actual cause of the low grade (later found to result from a documented family emergency during that term, unrelated to the applicant's ability).
- **Expected interview structure:** Opening (admissions officer role context), Episode 1 (personal statement reading), Episode 2 (grade encounter), Episode 3 (letter and alma mater encounter), Episode 4 (transcript and final decision), Closing (reflection on how document order and background shaped the read).
- **Natural biases:** Belief Perseverance and Attitude Polarisation, Fundamental Attribution Bias, Halo Effect, Ingroup Favoritism or In-group Bias, Ambiguity Aversion.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Academic Department Chair (overlaps with Interview 7; halo effect and belief perseverance are plausible there but reserved for the tenure-review context to preserve distinct scenario archetypes).
- **Rejected alternative occupation 2:** School Principal (overlaps with Interview 4; ambiguity aversion is plausible in program decisions but the five-bias combination is less naturally tied to a document-based file-review task).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Bandwagon Effect, Groupthink, Availability Bias, Anchoring Bias, Confirmation Bias, Averaging Bias
- **Selected occupation:** School District Curriculum Committee Member
- **Role and setting:** Team-based decision-making role; participates in a multi-member district committee (teachers, coordinators, administrators) tasked with selecting instructional materials or programs for districtwide adoption, working through structured meetings with vendor presentations and pilot data review.
- **Why this occupation fits the bias list:** Committee-based curriculum selection is a naturally team-based, multi-phase process where bandwagon effect (adopting a position because colleagues have voiced early support), groupthink (converging on consensus without adequately probing dissent), availability bias (overweighting a vivid, recently attended vendor demonstration), anchoring bias (the first program presented setting a reference point for evaluating subsequent options), confirmation bias (interpreting pilot data as it relates to a preferred program), and averaging bias (combining individual committee members' ratings into a group score without appropriate weighting) can all be embedded as distinct mechanisms across the meeting's phases.
- **Primary CTA scenario:** Participating in a committee meeting to select a new districtwide reading program; bandwagon effect as colleagues voice early support, groupthink in committee consensus, availability bias from a recently attended vendor demonstration, anchoring bias on the first program presented, confirmation bias in evaluating pilot data, averaging bias in combining committee members' ratings.
- **Triggering event:** A district curriculum committee convenes to select among four reading program candidates; the first program presented sets an initial reference point, one committee member recently attended a vivid vendor demonstration for a different program, and two vocal members voice early support for a third option.
- **Decision episodes:**
  1. Initial presentation of the first program and formation of a reference point for comparison.
  2. Discussion phase where early vocal support for one option shapes the room's momentum, and the vivid vendor demonstration disproportionately influences one member's input.
  3. Review of pilot data for each program, interpreted in light of the emerging preference.
  4. Final scoring, where individual members' ratings are averaged into a single committee recommendation.
- **Available cues and evidence:** Presentation materials for all four programs, pilot outcome data for each, the vivid vendor demonstration experience, individual committee members' private ratings, the order of presentation.
- **Competing interpretations:** The first program presented is genuinely strongest vs. simply anchored the comparison; the vocal early support reflects sound judgment vs. shapes the room's momentum disproportionately; the pilot data supports the emerging preference vs. is being read selectively; a simple average of ratings reflects the committee's collective judgment vs. obscures a strong minority dissent.
- **Plausible actions:** Recommend the program with the highest averaged score; recommend further piloting before a final decision; explicitly solicit and document dissenting views before finalizing; reorder the review process for a fresh comparison.
- **Constraints and pressures:** Meeting time limits, vendor sales pressure, budget cycle deadlines, committee members' desire for consensus and collegiality.
- **Consequences of error:** Districtwide adoption of a program that underperforms for the reasons overlooked in the biased review process, at significant cost and disruption to reverse.
- **Counterfactual causal variable:** Actual comparative effectiveness of the four programs (later found that the program presented last, and given least attention due to anchoring, had the strongest independent evidence base).
- **Expected interview structure:** Opening (committee member role context), Episode 1 (first presentation and anchor), Episode 2 (discussion and momentum), Episode 3 (pilot data review), Episode 4 (scoring and averaging), Closing (reflection on group dynamics and the averaging process).
- **Natural biases:** Bandwagon Effect, Groupthink, Availability Bias, Anchoring Bias, Confirmation Bias, Averaging Bias.
- **Plausible but difficult biases:** None outright, but six biases require distribution across the four distinct meeting phases to avoid compression into a single decision point.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** School Principal (overlaps with Interview 4; would create redundancy in the bounded-rationality/decision-authority mechanism already assigned there in an individual rather than team context).
- **Rejected alternative occupation 2:** Classroom Teacher (overlaps with Interview 1; averaging bias already assigned there in an individual grading rather than team-rating context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Biased Assimilation, Egocentric Bias, Group Attribution Error, Present Bias, Horn Effect, Bounded Rationality, Coherence-based Reasoning or Rationalisation
- **Selected occupation:** Academic Department Chair (Higher Education)
- **Role and setting:** Senior academic leadership role in a university department; leads the review of a junior faculty member's tenure case file, synthesizing teaching evaluations, research output, service records, and letters into a case narrative and recommendation, working under significant time pressure with a large, document-heavy file.
- **Why this occupation fits the bias list:** Department chairs review complex, multi-source tenure files where biased assimilation (interpreting mixed teaching evaluations in light of a prior view of the candidate), egocentric bias (overweighting the chair's own mentorship contribution to the candidate's success), group attribution error (attributing patterns to the candidate's subfield or department culture), present bias (overweighting recent publication output relative to the full record), horn effect (one negative student comment disproportionately coloring the overall assessment), bounded rationality (reviewing a large file under deadline with necessarily limited depth), and coherence-based reasoning (constructing an internally consistent narrative for the case) are all well-documented in tenure and promotion review contexts, though egocentric bias requires careful framing to distinguish it from ordinary, legitimate acknowledgment of mentorship.
- **Primary CTA scenario:** Reviewing a junior faculty member's tenure case file after a strong initial impression from their job talk years earlier; biased assimilation in evaluating mixed teaching evaluations, egocentric bias in weighting the chair's own mentorship contribution, group attribution error toward the candidate's subfield, present bias in weighting recent publication output, horn effect from one negative student comment, bounded rationality in reviewing a large case file under deadline, coherence-based reasoning in constructing a case narrative.
- **Triggering event:** A department chair begins reviewing a junior faculty member's tenure case file under a tight committee deadline; the chair recalls a strong initial impression from the candidate's job talk years earlier and has personally mentored the candidate, while the file contains mixed teaching evaluations, one sharply negative student comment, a strong recent publication record, and a subfield the chair associates with certain departmental patterns.
- **Decision episodes:**
  1. Initial recall of the job-talk impression and the chair's own mentorship investment as framing for the review.
  2. Review of mixed teaching evaluations, interpreted in light of the prior favorable impression.
  3. Encounter with the single negative student comment and its effect on the overall teaching assessment.
  4. Review of the publication record with emphasis on recent output, and construction of a coherent case narrative under time pressure before the deadline.
- **Available cues and evidence:** Job-talk recollection, the chair's own mentorship record with the candidate, full teaching evaluation set (mixed), the one negative comment, full publication record across the review period, subfield-level departmental patterns the chair has observed, committee deadline.
- **Competing interpretations:** The mixed teaching evaluations reflect genuinely uneven teaching vs. are consistent with the strong impression from years ago; the chair's mentorship explains the candidate's success vs. the candidate's own independent work is primarily responsible; the negative comment reflects a real teaching weakness vs. an outlier unrepresentative of the full evaluation set; recent publication output is most indicative of future trajectory vs. the full record should carry equal weight; subfield-level patterns are informative for this candidate vs. this candidate's case should be assessed independently of subfield generalizations.
- **Plausible actions:** Write a strongly positive case narrative; write a case narrative flagging teaching concerns; request additional teaching evaluation data or a classroom observation; extend the review timeline despite the deadline.
- **Constraints and pressures:** Committee submission deadline, the chair's personal and professional investment in the candidate's success, departmental norms around subfields, large file volume relative to available review time.
- **Consequences of error:** A tenure recommendation that overstates or understates the candidate's actual record due to prior impressions, mentorship investment, or an outlier comment, with career-defining consequences for the candidate.
- **Counterfactual causal variable:** Actual representativeness of the single negative student comment (later found to be an outlier from a single difficult semester, contradicted by consistently strong evaluations in all other terms).
- **Expected interview structure:** Opening (chair role context), Episode 1 (initial framing), Episode 2 (teaching evaluation review), Episode 3 (negative comment encounter), Episode 4 (publication review and narrative construction), Closing (reflection on time pressure and personal investment).
- **Natural biases:** Biased Assimilation, Group Attribution Error, Present Bias, Horn Effect, Bounded Rationality, Coherence-based Reasoning or Rationalisation.
- **Plausible but difficult biases:** Egocentric Bias (requires careful framing — the chair's mentorship contribution must be shown as inflating the chair's own causal role in the outcome, not merely as accurate credit-taking for legitimate mentorship).
- **Biases that should not be forced:** None outright, but Egocentric Bias must be clearly distinguished from ordinary, warranted acknowledgment of mentorship to avoid feeling artificial.
- **Rejected alternative occupation 1:** University Admissions Officer (overlaps with Interview 5; biased assimilation and halo-adjacent mechanisms already assigned there in an applicant-file rather than personnel-file context).
- **Rejected alternative occupation 2:** School Principal (overlaps with Interview 4; bounded rationality and coherence-based reasoning already assigned there in a program-approval rather than personnel-evaluation context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Egocentric Bias requires careful framing distinct from ordinary, legitimate self-attribution of mentorship credit)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (classroom teacher, curriculum coordinator, IEP coordinator, principal, admissions officer, committee member, department chair) | None | None | None | None needed |
| Work setting | Classroom/individual (1), Instructional support (2), Student-relationship/casework (3), School administration (4), Higher-ed admissions office (5), Team meeting (6), Department leadership (7) | None significant | None | Field-based, remote/distributed | None critical; education domain is inherently office/classroom/administrative weighted |
| Decision type | Grading/classification (1), Evidence evaluation (2), Diagnosis/progress assessment (3), Resource allocation/approval (4), Compliance/adjudication (5), Team resource allocation (6), Personnel evaluation (7) | None significant | None | Emergency response, Negotiation | None critical |
| Information environment | Rich/structured (1), Evidence-based/mixed (2), Longitudinal/socially-mediated (3), Time-constrained/thin evidence (4), Document-heavy/sequential (5), Team/socially-mediated (6), Document-heavy/large-file (7) | Document-heavy (2/7: 5, 7) | Balanced | Rapidly-changing as primary driver | None critical; reflects education's inherently document- and evidence-based decision structure |
| Time pressure | Moderate (1, 2, 3, 5), High (4, 6, 7) | Moderate (4/7) | Moderate | Low | None critical |
| Consequence of error | Educational/developmental (1, 3), Operational/resource (2, 4, 6), Legal/gatekeeping (5), Career/reputational (7) | None significant | None | Financial-only, environmental | None critical; reflects education's developmental and gatekeeping consequence profile |
| Expertise level | Independent professional (1, 2, 3), Decision authority (4), Specialist/gatekeeper (5), Team/mixed expertise (6), Senior practitioner/decision authority (7) | None significant | None | Developing practitioner | None critical |
| Stakeholder pattern | Individual (1, 5), One-to-one relationship (2, 3), Individual with authority (4), Team (6), Individual with committee-adjacent stakes (7) | Individual (3/7: 1, 4, 5) | Individual work | Multi-party negotiation, public-facing | None critical; Interview 6 provides the needed team-based contrast |
| Scenario archetype | Grading (1), Method evaluation (2), Progress review (3), Program approval (4), File review (5), Committee selection (6), Tenure review (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Component score diagnosticity (1), Pilot data cause (2), First-interaction cause (3), Program mechanism (4), Grade cause (5), Comparative program effectiveness (6), Comment representativeness (7) | None significant | None | Equipment/technical failure as primary variable | None critical; all seven turn on a distinct, plausible causal fact appropriate to the education domain |

**Overall assessment:** Strong diversity across occupations, settings, decision types, and consequence profiles, spanning K-12 and higher education, individual and team decision-making, and student-facing, peer-facing, and personnel-facing contexts. Document-heavy review is present in two interviews (5, 7) but differs materially in stakeholder stakes (admissions gatekeeping vs. tenure/personnel) and causal structure. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Averaging Bias (clear mechanism: equal-weighting of unequally diagnostic components) | None | Averaging Bias (risk of being read as simply "graded imperfectly") | None | None | None | Show explicit component-by-component reasoning before the final grade; probe why weighting wasn't adjusted, not just the final number |
| 2 | Biased Assimilation (interpreting mixed evidence toward prior view), Egocentric Bias (overweighting self-authored materials) | Biased Assimilation and Confirmation Bias (closely related; biased assimilation specifically concerns interpretation of genuinely mixed/ambiguous evidence) | None | None | None | None | Ensure the pilot data is genuinely mixed, not one-sided, to isolate biased assimilation from simple confirmation bias; show explicit comparison between self-authored and alternative materials |
| 3 | Group Attribution Error (group-level inference), Present Bias (short-term weighting), Horn Effect (early-impression coloring) | Horn Effect and Belief Perseverance (both involve resistance to updating an early impression) | None | None | Group Attribution Error (must show explicit group-level reasoning, not just individual stereotyping) | Group Attribution Error | Show the caseworker explicitly invoking a pattern observed "among students like this" to distinguish group attribution error from simple horn effect; separate the recency of current-quarter data from the group-level inference |
| 4 | Bounded Rationality (time/information limits), Coherence-based Reasoning (narrative construction), Illusion of Understanding (overestimated mechanism knowledge), Self-Enhancement Bias (outcome credit-taking) | Illusion of Understanding and Coherence-based Reasoning (both involve constructing an account that feels more solid than the evidence supports) | Self-Enhancement Bias (risk of being read as simply "took credit for a good outcome") | None | Illusion of Understanding (must show an explicit, articulable but flawed mechanism explanation) | Illusion of Understanding | Show the principal explicitly articulating (and getting wrong) how the program is supposed to work, not just expressing confidence; separate the approval-stage reasoning from the later outcome-attribution episode |
| 5 | Belief Perseverance and Attitude Polarisation, Fundamental Attribution Bias, Halo Effect, Ingroup Favoritism, Ambiguity Aversion (five distinct) | Halo Effect and Belief Perseverance (both involve one strong element coloring the whole), Fundamental Attribution Bias and Horn Effect (both involve dispositional inference from a single data point, though in opposite valence) | None | None | Ambiguity Aversion (must show explicit discomfort with the unconventional pattern, not just a negative conclusion about it) | Ambiguity Aversion | Present the five cues (personal statement, low grade, letter, alma mater, unconventional transcript) in a fixed order with explicit officer reasoning at each step; separate the file-order-driven belief perseverance from the single-document halo effect |
| 6 | Bandwagon Effect, Groupthink, Availability Bias, Anchoring Bias, Confirmation Bias, Averaging Bias (six distinct mechanisms across meeting phases) | Bandwagon Effect and Groupthink (closely related — bandwagon is the individual-level mechanism, groupthink the group-level outcome), Anchoring Bias and Availability Bias (both involve overweighting a specific, vivid reference point) | None | None | Groupthink (dissent-suppression must be explicit, not just consensus) | Groupthink | Distribute the six biases across the four distinct meeting phases; show at least one committee member's dissenting view being discounted to distinguish groupthink from ordinary bandwagon-driven agreement; show the averaging step as a distinct final calculation separate from the discussion-phase biases |
| 7 | Biased Assimilation, Group Attribution Error, Present Bias, Horn Effect, Bounded Rationality, Coherence-based Reasoning (six cleanly distinguishable); Egocentric Bias (requires careful framing) | Biased Assimilation and Horn Effect (both involve interpretation shaped by an anchor point, though biased assimilation concerns ongoing mixed evidence and horn effect a single negative element), Bounded Rationality and Coherence-based Reasoning (time pressure driving narrative-gap-filling) | None | None | Egocentric Bias (mentorship-credit cue must clearly show inflated causal attribution, not legitimate credit) | Egocentric Bias | Show the chair explicitly overstating their own causal role in the candidate's success relative to the candidate's independent contributions; separate the job-talk recollection (framing) from the mentorship-credit reasoning (egocentric bias) as distinct cues |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interview 6, distribute all six biases across the four distinct meeting phases rather than compressing them into a single discussion moment; explicitly show a discounted dissenting view for Groupthink. For Interview 7, ensure Egocentric Bias is grounded in an explicit overstatement of causal contribution rather than legitimate, accurate credit for mentorship — this is the bias most at risk of feeling forced in this occupation. For Interviews 3 and 5, ensure early-impression biases (Horn Effect, Belief Perseverance) are clearly separated from group-level or single-document biases (Group Attribution Error, Halo Effect) via distinct cues at different points in the narrative.
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, with particular attention to distinguishing closely related neighboring pairs identified above (Bandwagon/Groupthink in Interview 6; Biased Assimilation/Horn Effect in Interview 7; Halo Effect/Belief Perseverance in Interview 5). Flag any bias supported only by the case's ultimate outcome rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules.
