You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay?

Participant: Sure, that's fine.

Interviewer: Can you tell me a bit about your role?

Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also work through our open findings backlog for compliance reporting, and I sit in on the weekly risk review with application owners.

Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened.

Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. There'd also been some industry news about a breach at another company the week before, though that wasn't really something I was thinking about directly when this came in — just background noise on the security channels, the kind of thing that's always circulating.

Interviewer: When the new CVE came in, what did you do first?

Participant: I read through the advisory, checked the CVSS score and the exposure — internet-facing, no compensating control in front of it, no WAF rule that would catch this pattern — and decided it needed to jump ahead of the backlog. The database finding is serious on paper, but at that point I didn't have a confirmed exploit path for it, just the privilege configuration itself and how long it had been sitting there. So it came down to weighing a confirmed critical exposure against an older, structurally risky one without fresh evidence of active exploitability.

Interviewer: How confident were you in that call?

Participant: Reasonably, but not completely. If I'd had time to pull a fresh risk assessment on the database server that morning, it's possible that would've changed the ordering. I didn't have that luxury, and honestly both items had a legitimate claim to going first.

Interviewer: Where did you route the new CVE?

Participant: Into our standard remediation workflow, tagged toward the web-facing application team, since it touches a customer-facing API and that team handles most of our external-facing patch coordination. It turned out to be more specifically an authentication-bypass issue in the API gateway rather than a typical injection bug, which meant a slightly different exploit chain than I'd first assumed, but the initial routing wasn't far off and the handoff to the right owner happened within the same day.

Interviewer: Walk me through what happened next, later that day.

Participant: While I was cross-referencing the CVE against our asset inventory, the SIEM threw an alert — "privilege escalation, low confidence" — on an internal host. I pulled up the log entry, saw a lateral-movement timestamp that looked a little off from the usual pattern, and there was also an outbound traffic flag on the same host in the same view.

Interviewer: What did you do with that?

Participant: I looked at both — the timestamp and the outbound entry — but neither one on its own had enough corroborating detail to justify pulling away from the CVE triage right then. No matching indicator from the threat intel feed, no other host showing similar activity, nothing in the ticket history suggesting a known campaign. I made a note to loop back once the CVE work was further along and kept going.

Interviewer: Two days later that outbound entry turned out to be linked to an actual low-level compromise. Looking back, do you read that decision differently?

Participant: It's hard to say. Given what I had at the time — a low-confidence label and a somewhat unusual but unconfirmed pattern — I don't think escalating immediately was obviously the right call either. It could've gone either way with the same information in front of me. I've seen similar-looking situations resolve as nothing more than a test process before, and I've also seen them turn out to matter, so I don't think this one particular case tells me much either way about how I generally handle it.

Interviewer: Let's talk about the change window request.

Participant: Patching the API gateway meant an emergency change window during business hours, about twenty minutes of disruption to customer transactions. IT ops needed a written justification to approve that instead of waiting for the weekend cycle.

Interviewer: What went into the justification?

Participant: I put in both the EPSS number — moderate probability, not exceptional — and what the exposure meant in practical terms: the contract implications, the audit angle, and the disruption window itself. I didn't deliberately lead with one over the other, honestly. It read as a fairly standard risk memo, the same format I use for most emergency requests.

Interviewer: Which part do you think actually got it approved?

Participant: I genuinely don't know. IT ops doesn't usually explain which line convinced them. Could've been the score, could've been the business language, could've been that the ask was only for twenty minutes rather than a longer outage. I couldn't tell you with confidence which one mattered most.

Interviewer: Did anything happen afterward that would clarify that?

Participant: Not really. No exploitation was observed against that CVE in the following week, but that doesn't tell me whether the request was overstated or exactly right — we patched it, so there was nothing left to observe either way. It's genuinely inconclusive from where I sit.

Interviewer: Last decision point — scoping which systems got patched.

Participant: The scanner's default view showed two hosts with the matching vulnerable library. Given the deadline, I scoped the ticket to those two, but I also flagged a follow-up sweep of the broader asset inventory for the next week, since I know that default view doesn't always capture everything depending on how assets are tagged in different categories.

Interviewer: One of three additional hosts under a different category turned out to still have the vulnerable library a week later.

Participant: Right, and that's a fair miss. I did build in the follow-up step, it just didn't happen fast enough given everything else on my plate that week. Whether a full manual cross-check up front versus a scheduled follow-up was the better trade-off given the deadline — I go back and forth on that even now.

Interviewer: If you'd had more time before the deadline, would any of these have gone differently?

Participant: Maybe the database server would've gotten a proper fresh look instead of being compared mostly on paper. And I might've pushed the manual inventory check earlier instead of scheduling it after the ticket closed. Hard to know for sure without actually having had that time.

Interviewer: If the scanner had shown five hosts instead of two, would scoping have changed?

Participant: I'd have patched what was in front of me either way, so probably not much different in terms of process — the follow-up sweep would just have had a shorter list left to check afterward.

Interviewer: Looking back, is there anything you'd weigh differently now?

Participant: Maybe how much weight I gave the SIEM alert without a corroborating signal. Not sure I'd act differently even now with the same information, but it's the one I think about.

Interviewer: If you had to write the change-window justification again, would you present it differently?

Participant: Possibly lead more with the numbers and less with the business language, just to see if it changes anything. I don't have strong evidence either framing actually mattered to the outcome.

Interviewer: That's really helpful, thank you for walking through it in detail.

Participant: No problem, glad to help.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Ambigious_6}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{Threat Intelligence Analyst}}"
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
