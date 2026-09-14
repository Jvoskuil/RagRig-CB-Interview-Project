You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm — this is a voluntary conversation about how you handled the EDR replacement evaluation earlier this year, purely for internal process review. Nothing here affects performance evaluation. You're the Security Product/Vendor Evaluation Manager on that project, correct?

Participant: That's right. I led the vendor evaluation from shortlist through to the board recommendation.

Interviewer: Good. Let's start broad — what triggered this whole evaluation?

Participant: We had a near-miss in Q1. An affiliate's endpoint got hit with what looked like early-stage ransomware staging — lateral movement, some encrypted command-and-control traffic that our incumbent EDR didn't flag until a threat hunter noticed anomalous SMB activity manually. We contained it before encryption, but the incident review was blunt: our detection had real gaps. Our contract with the incumbent was also up for renewal in about ninety days, so leadership decided this was the moment to replace rather than renew.

Interviewer: What was the objective you were given, and what constraints came with it?

Participant: Close the detection gaps — specifically lateral movement and encrypted C2 — before the board's remediation deadline, and do it within budget. The CISO wanted a shortlist within two weeks because ninety days isn't much runway once you factor in procurement and implementation. We also run on a fairly integrated cloud and SIEM stack, so anything we picked needed to plug into that without a lot of custom engineering. And our red-team capacity was thin — maybe two weeks of testing bandwidth total across everything.

Interviewer: Walk me through what happened first.

Participant: Almost immediately, our SIEM vendor's account rep reached out — they'd heard about the incident through the account team — and proposed we evaluate their three "certified integration partner" EDR products alongside our incumbent. He framed it as saving us weeks of integration testing since those three were pre-validated against our stack. Given the two-week shortlist deadline, that was appealing. I brought it to the CISO, we agreed it made sense, and that became our shortlist: incumbent plus those three.

Interviewer: Did you look at anything outside that list?

Participant: Not formally, no. I skimmed a couple of analyst write-ups just to sanity-check the names, but I didn't commission an independent RFI or request-for-information process. Honestly, the two-week clock was the driving factor — running a broader market scan across eight or ten vendors would have eaten most of that window just on paperwork and calls.

Interviewer: What made you confident that list was sufficient, versus, say, expanding it by even one or two names?

Participant: The integration angle was real — those three had documented connectors into our logging pipeline already, which meant our engineers wouldn't be building anything from scratch. Time was tight, and I weighted that heavily. I didn't do a deep comparison against vendors outside that set because, frankly, the clock made that feel like a luxury we didn't have.

Interviewer: Did you learn anything afterward about vendors that weren't on that list?

Participant: Yeah — a bit later, procurement was doing some contract-comparison work and flagged two other EDR vendors with higher published MITRE ATT&CK technique coverage scores than any of the three we'd tested. They'd never come up because they weren't in the sales rep's bundle. Separately, a CISO at a peer firm mentioned they'd run a much wider search for a similar replacement. Neither of those changed our timeline, but it did make me wonder what we might have missed.

Interviewer: Let's move to the next phase — the proof-of-concept process. How did you decide to evaluate the shortlisted vendors?

Participant: Each vendor offered a POC window, and they also offered their own third-party benchmark reports as a shortcut — essentially, "trust our numbers." I decided against relying on those and instead ran a standardized red-team simulation, same attack playbook, against all three plus the incumbent. Our testing bandwidth was tight, but I thought it was worth spending it on a controlled, apples-to-apples comparison rather than vendor-marketed numbers.

Interviewer: What tipped you toward the in-house simulation over the benchmark reports?

Participant: One vendor's benchmark report claimed near-perfect detection on lateral movement, but when we actually ran our simulation, their live results were noticeably weaker than advertised. That gap alone justified the extra effort. I'd rather have a smaller but trustworthy dataset than a larger one I can't verify.

Interviewer: That makes sense. Let's get into the tier and pricing decision — what happened there?

Participant: The leading vendor after POC testing had two tiers: a standard tier and a premium threat-hunting tier. POC results confirmed the standard tier met our documented detection SLA — it closed the lateral-movement and C2 gaps we cared about. But during the sales presentation, they walked us through a risk exposure calculator projecting the average breach cost we'd avoid — something like several million dollars — if we went with the premium tier instead. The premium tier was about 40% over our budgeted amount.

Interviewer: When you were putting together your recommendation, what evidence carried the most weight?

Participant: If I'm honest, that avoided-cost number stuck with me the most. It was concrete, it was framed around what happens if we don't act — another incident, but worse, uncontained — and given we'd just come out of a near-miss, that scenario felt very real to the board and to me. The standard tier's SLA compliance was in the POC report, sure, but it didn't have an equivalent dollar figure attached to it — nobody had built out what the efficiency or analyst-time savings from the cheaper option would look like in the same terms. So the premium tier's case was just more vivid.

Interviewer: Did anyone push back on the budget variance?

Participant: Finance flagged it — the premium tier exceeded our pre-approved variance threshold — and I had to get an exception signed off. I justified it by pointing to the exposure figure. Later, procurement went back and built a comparable savings case for the standard tier plus a phased upgrade path, and it turned out that route would have met the same SLA at meaningfully lower cost. That wasn't available to me at the time I made the call, though.

Interviewer: What information, if it had existed at that point, might have changed your recommendation?

Participant: Probably that phased-upgrade ROI figure. If I'd had a dollar-for-dollar efficiency case sitting next to the exposure calculator, I think the comparison would have felt more balanced. Instead, one option had a scary number and the other didn't have a number at all.

Interviewer: Last decision point — the rollout recommendation to the board. What happened there?

Participant: We had two paths: full production rollout within sixty days to lock the vendor's renewal pricing, or a thirty-day extended pilot to validate some outstanding false-positive concerns from the POC before committing fully. I recommended the full rollout. The pricing was only guaranteed if we signed within thirty days, and the board wanted a remediation update before the old contract lapsed.

Interviewer: Any uncertainty in that call?

Participant: Some. The false-positive tuning wasn't fully validated yet. But weighing the schedule risk against the pricing lock and the board's deadline, I felt the full rollout was the more defensible path, with a commitment to tune aggressively post-launch.

Interviewer: How did that play out?

Participant: We did see a higher false-positive rate than expected in early production, which took extra tuning cycles. The board asked for a follow-up review at ninety days. Not ideal, but manageable.

Interviewer: Looking back across the whole process, if you'd had an extra month and no budget constraint, would anything have gone differently?

Participant: Probably the shortlist. I'd have liked to run a proper market scan rather than starting from a vendor-curated list. I still think the POC methodology and the rollout timing were sound calls given what I knew.

Interviewer: And if a colleague had challenged the tier decision directly — what do you think that conversation would have looked like?

Participant: They'd probably have asked why we didn't build out the same kind of savings case for the cheaper tier. I don't have a great answer beyond that the exposure number was already sitting in front of us and the other side of the ledger wasn't.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Biased_2}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{Security Product/Vendor Evaluation Manager}}"
}

TAXONOMY

This taxonomy distinguishes three aspects of work:

1. Task content: what the worker does.
2. Work methods: how the work is organised.
3. Tools: what machinery or technology is used.

Classify only categories supported by observable evidence. Multiple categories may be present. Select one primary content category and any defensible secondary categories. Do not force a category when evidence is insufficient.

A. TASK CONTENT — WHAT THE WORKER DOES

A1. PHYSICAL TASKS

A1.1 Strength
The worker exerts physical force or effort, handles loads, pushes, pulls, lifts, carries, restrains, or uses bodily strength as a meaningful part of the task.

A1.2 Dexterity
The worker performs precise, coordinated, or fine-grained physical movements, manipulates objects or instruments, assembles, repairs, operates controls manually, or uses hand-eye coordination as a meaningful part of the task.

A1.3 Navigation
The worker physically moves through or around an environment, routes people or objects, or maintains orientation and position in a spatial setting as a meaningful part of the task.

A2. INTELLECTUAL TASKS

A2.1 Uncodified visual or auditory information processing
The worker interprets visual, auditory, or other perceptual information that is difficult to reduce to a fully explicit rule, including recognizing patterns, anomalies, conditions, or signals.

A2.2 Literacy
The worker reads, writes, composes, edits, interprets, or communicates using written language as a meaningful part of the task.

A2.3 Numeracy
The worker calculates, quantifies, estimates, compares numerical values, interprets numerical information, or reasons about proportions, probabilities, measurements, or financial quantities.

A2.4 Information search, retrieval, gathering, and evaluation
The worker seeks, retrieves, gathers, compares, verifies, filters, or evaluates information from records, people, systems, documents, observations, or other sources.

A2.5 Conceptualisation, learning, and abstraction
The worker forms concepts, learns from experience, generalises, diagnoses, explains relationships, builds mental models, applies abstract principles, or understands a system beyond the immediate facts.

A2.6 Creativity, planning, and resolution
The worker generates, designs, or adapts solutions to a problem; develops and compares possible courses of action; plans their implementation; anticipates dependencies or consequences; or resolves a novel, non-routine situation by combining information in an original or context-sensitive way. Planning counts when it involves organising a sequence of actions, timing, resources, contingencies, or dependencies toward a goal—not merely selecting or carrying out a routine next step.

A3. SOCIAL TASKS

A3.1 Serving and attending
The worker responds to another person's immediate needs, provides a service, receives requests, attends to a customer, patient, client, user, colleague, or member of the public, or manages an interaction aimed at assistance.

A3.2 Teaching, training, and coaching
The worker explains, instructs, demonstrates, trains, develops, mentors, or coaches another person.

A3.3 Selling and influencing
The worker persuades, negotiates, recommends, markets, advocates, manages expectations, seeks agreement, or attempts to influence another person's decision or behaviour.

A3.4 Managing and coordinating
The worker allocates work, coordinates people or activities, manages dependencies, sets priorities, resolves organisational conflicts, supervises, or aligns multiple stakeholders.

A3.5 Caring
The worker provides emotional, personal, health-related, protective, or welfare-oriented support in which attention to another person's condition or well-being is central.

B. WORK METHODS — HOW THE WORK IS ORGANISED

B1. AUTONOMY

B1.1 Latitude
The worker has discretion over objectives, priorities, timing, sequence, methods, or decisions. Classify low, moderate, or high only when the interview provides evidence about the worker's discretion.

B1.2 Control and monitoring
The worker's work is supervised, measured, audited, monitored, reviewed, or constrained by another person, policy, procedure, system, target, or formal approval process. Classify low, moderate, or high based on the strength and frequency of such control.

B2. TEAMWORK

Direct collaboration with co-workers or other actors to accomplish a shared task, exchange information, coordinate actions, hand off work, or reach a joint decision. Classify low, moderate, or high based on the worker's dependence on collaboration in the described episode.

B3. ROUTINE

B3.1 Repetitiveness
The same or highly similar actions, inputs, decisions, or outputs recur frequently.

B3.2 Standardisation
The task follows prescribed procedures, scripts, checklists, templates, rules, or consistent sequences.

B3.3 Certainty and response to unforeseen situations
Certainty refers to how predictable the relevant inputs, conditions, and consequences are. Response to unforeseen situations refers to how much the worker must handle exceptions, novelty, ambiguity, disruptions, or unexpected developments.

For this dimension, report both:
- certainty: low, moderate, high, or not_observable;
- unforeseen_response_requirement: low, moderate, high, or not_observable.

C. TOOLS — MACHINERY AND TECHNOLOGY USED

C1. Non-digital machinery
Analog or mechanical devices and machinery without meaningful digital control, sensing, computing, or networked information processing.

C2. Digitally enabled machinery
Machinery or equipment using digital control, sensors, software, automation, robotics, or networked digital systems. Classify the most specific supported subtype:

C2.1 Autonomous machinery or robots
The equipment performs meaningful operations with limited direct human control after initiation.

C2.2 Non-autonomous digitally enabled machinery
The worker directly operates or controls digitally enabled physical equipment.

C2.3 Basic ICT
Routine use of computers, smartphones, email, office software, standard databases, or basic digital communication and information systems.

C2.4 Advanced ICT or programming
Programming, data analysis, modelling, system configuration, advanced computational tools, or complex software-based information processing.

C2.5 Specialised ICT
Special-purpose professional software or digital systems used for a particular occupation or work process, where the system is more specialised than ordinary office or communication software.

C2.6 Other digitally enabled tools
Digital tools that clearly matter to the work but do not fit the preceding subcategories.

CLASSIFICATION RULES

1. Classify the described episode, not the entire occupation.
2. A category must have textual evidence. Do not infer it from the role title.
3. Assign one primary task-content category: the category most central to the operational objective and decision episode.
4. Assign secondary content categories only when they are substantively involved, not merely mentioned.
5. Content categories may come from different families. For example, an interview may contain intellectual information evaluation as primary content and social influencing as secondary content.
6. Methods and tools are separate from content. Do not label a task intellectual merely because it uses a computer, or social merely because other people are mentioned.
7. Distinguish information search/evaluation from conceptualisation: the former concerns obtaining and assessing information; the latter concerns forming models, diagnoses, abstractions, or generalisations.
8. Distinguish creativity/resolution from ordinary choice: creativity requires adaptation, novel solution generation, or non-routine problem resolution.
9. Distinguish serving/attending from selling/influencing: assistance and responsiveness are not necessarily persuasion or negotiation.
10. Distinguish managing/coordinating from teamwork: teamwork is collaboration; managing/coordinating involves organising dependencies, priorities, people, or activities.
11. Do not infer strength, dexterity, navigation, or caring without direct evidence.
12. For autonomy, monitoring, teamwork, repetitiveness, standardisation, and certainty, use `not_observable` when the interview does not support a reliable level.
13. Multiple tools may be present. Record only tools that play a meaningful role in the episode.
14. If a classification is ambiguous, record the competing categories and explain the ambiguity.
15. Do not treat the participant's cognitive bias, if any, as a task category.
16. Do not use external web research. The supplied taxonomy is the authority for this annotation.

EVIDENCE REQUIREMENTS

For every assigned content category, method level, and tool category, provide:
- a short quotation or faithful text span;
- the location, such as opening, timeline, decision point, or participant turn;
- an explanation of why the evidence supports the category;
- confidence from 0 to 100.

For categories not observed but potentially plausible, do not list them as present. Place them in `not_observed_or_insufficient` only if doing so helps explain a material ambiguity.

COVERAGE STATUS

Set `coverage_status` as follows:
- `complete`: the interview contains enough evidence to classify content, methods, and tools;
- `partial`: at least one major dimension is not observable;
- `ambiguous`: competing categories cannot be resolved from the text;
- `insufficient`: the interview does not contain a sufficiently identifiable work episode.

OUTPUT SCHEMA

{
  "taxonomy_version": "Fernandez-Macias_Bisello_2021",
  "interview_id": "...",
  "occupational_domain": "...",
  "role": "...",
  "classification_confidence": 0,
  "coverage_status": "complete|partial|ambiguous|insufficient",
  "content": {
    "primary_category": {
      "family": "physical|intellectual|social|unknown",
      "subcategory": "...",
      "confidence": 0,
      "evidence": [
        {
          "location": "...",
          "quote": "...",
          "explanation": "..."
        }
      ]
    },
    "secondary_categories": [
      {
        "family": "physical|intellectual|social",
        "subcategory": "...",
        "confidence": 0,
        "evidence": [
          {
            "location": "...",
            "quote": "...",
            "explanation": "..."
          }
        ]
      }
    ],
    "all_observed_categories": [],
    "not_observed_or_insufficient": [],
    "ambiguities": []
  },
  "methods": {
    "autonomy": {
      "latitude": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "control_monitoring": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      }
    },
    "teamwork": {
      "level": "low|moderate|high|not_observable",
      "confidence": 0,
      "evidence": []
    },
    "routine": {
      "repetitiveness": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "standardisation": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "certainty": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "unforeseen_response_requirement": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      }
    }
  },
  "tools": [
    {
      "category": "non_digital_machinery|autonomous_machinery_or_robot|non_autonomous_digitally_enabled_machinery|basic_ict|advanced_ict_or_programming|specialised_ict|other_digitally_enabled_tool",
      "role_in_task": "...",
      "confidence": 0,
      "evidence": [
        {
          "location": "...",
          "quote": "...",
          "explanation": "..."
        }
      ]
    }
  ],
  "task_anchors": [
    {
      "location": "...",
      "task_description": "...",
      "taxonomy_labels": [],
      "confidence": 0
    }
  ],
  "decision_point_task_map": [
    {
      "decision_point": 1,
      "dominant_task_categories": [],
      "methods_relevant": [],
      "tools_relevant": [],
      "evidence": []
    }
  ],
  "classification_quality": {
    "occupation_inference_risk": "low|moderate|high",
    "stereotype_risk": "low|moderate|high",
    "taxonomy_ambiguity": "low|moderate|high",
    "missing_evidence": [],
    "manual_review_recommended": false
  },
  "coverage_flags": {
    "physical_content_observed": false,
    "intellectual_content_observed": false,
    "social_content_observed": false,
    "methods_observed": false,
    "tools_observed": false,
    "all_major_dimensions_observable": false
  },
  "recommended_dataset_action": "retain|retain_with_low_confidence|sample_more|manual_review|exclude"
}

FINAL CHECK

Before returning JSON, verify that:
- Every present category has textual evidence.
- The primary category is central to the episode, not merely the most frequently mentioned word.
- Secondary categories are substantively involved.
- Method and tool labels are supported independently from content labels.
- `not_observable` is used where appropriate.
- Confidence reflects evidence quality, not certainty from the occupation or role.
- No cognitive-bias labels appear as task categories.
- No external sources or unstated occupational assumptions were used.
- The result is valid JSON and contains no prose outside the JSON object.
