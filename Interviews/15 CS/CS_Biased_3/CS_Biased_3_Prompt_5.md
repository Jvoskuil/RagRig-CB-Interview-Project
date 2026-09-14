You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our incident-response learning archive, not a performance review — you can skip anything you're not comfortable discussing. Can you start by stating your role and how long you've been on the Tier 2 triage rotation?

Participant: Sure. I'm a Tier 2 SOC analyst, been doing log and alert triage for about two and a half years, most of that on the overnight rotation. This shift was a fairly typical Tuesday-into-Wednesday, except we had a scheduled vulnerability scan running against the 10.14.0.0/16 range.

Interviewer: Good, let's go through what happened. Walk me through what you saw when you first opened the alert queue that night.

Participant: I logged into the SIEM around 1 a.m. and the queue already had close to 300 new alerts in about twenty minutes, which is a lot even for us. Handoff notes from the day shift flagged that vuln management had an authenticated scan scheduled starting midnight, so I expected noise. When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see.

Interviewer: What was your primary goal in those first ten minutes?

Participant: Get through the noise fast so I wouldn't blow the 45-minute SLA on anything that actually mattered. With that volume, you can't eyeball every single alert individually — you triage by pattern.

Interviewer: Okay, let's reconstruct the rest of the shift chronologically, then we'll go back and dig into specific decisions. What came after that initial queue review?

Participant: I ran our saved scan-window filter to bulk-close the low-severity scan-tagged alerts, then almost immediately got pulled into a phishing cluster — a bunch of similar-looking emails landing in different inboxes. I spent maybe twenty minutes on that while the shift lead was pinging me for status. Then around 2:40, EDR kicked out an anomaly on a finance workstation, FIN-WK-114, with a process making periodic outbound connections. I looked at that, made a call, and moved on. About forty minutes later, a threat intel feed update came back and changed the picture on that same host, so I escalated to IR.

Interviewer: Let's slow down on the first decision — closing that initial batch. What information did you actually have in front of you at the moment you applied the filter?

Participant: The queue view, sorted by source subnet and severity. Almost everything was scan-subnet, low severity. There was one alert from FIN-WK-114 — a DNS query to a domain I didn't recognize — but it was sitting at low severity too, so visually it didn't distinguish itself from the rest of the batch.

Interviewer: What other options did you consider before bulk-closing?

Participant: I could have spot-checked a random sample of the low-severity ones outside the scan subnet before closing, or set a rule to pull out anything touching non-IT departments like finance for individual review. Honestly, with SLA pressure and that volume, the batch filter felt like the efficient move. I ran it across the whole set.

Interviewer: And the FIN-WK-114 alert — what happened to it specifically?

Participant: It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up. I didn't isolate it as a finance host outside 10.14.0.0/16 until I came back to it hours later.

Interviewer: What would have needed to be different for you to catch that at the time?

Participant: Probably if the queue view had color-coded by subnet instead of just severity, or if I'd run the spot-check option instead of the full batch close. In hindsight it was sitting right there.

Interviewer: Let's move to the phishing cluster. What made you confident that was contained?

Participant: I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately. Given how fast the visible queue cleared, I told the shift lead it looked contained.

Interviewer: Did you verify that against anything else — inbox delivery logs, a manual sample?

Participant: Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket.

Interviewer: Was there anything in the queue at that time that didn't fit that picture?

Participant: There was one variant with a slightly different sender domain that the rule wouldn't have matched — I didn't clock that until later. At the time I was reading the drop in volume as the rule working.

Interviewer: Understood. Now the EDR anomaly on FIN-WK-114 — what led you to the backup-agent explanation?

Participant: The connection pattern — periodic, roughly every 55 seconds — looked a lot like something we'd seen twice in the previous two shifts, both traced back to a misconfigured backup agent on other hosts. That was fresh in my mind since I'd closed both of those tickets myself within the last week.

Interviewer: Did the current alert have a direct signature match to that backup agent?

Participant: No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as "likely backup-agent artifact, monitor only" based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up.

Interviewer: Was pulling the process tree or checking the destination IP against threat intel an option at that point?

Participant: Yeah, it was, and normally I'd lean that way if I weren't juggling two things. Since the pattern matched what I'd just dealt with twice, it felt like a safe bet to downgrade it and keep an eye on it rather than treat it as new.

Interviewer: What told you it was "safe" specifically — the interval, or something else?

Participant: Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first.

Interviewer: Let's get to the fourth point — the escalation. What changed?

Participant: About forty minutes later, threat intel updated and flagged that destination IP as a known C2 rendezvous point, which directly contradicted the backup-agent call. By then the SLA on that alert had already lapsed by twelve minutes, and my shift lead was tied up on another incident call for the next twenty.

Interviewer: What were your options at that point?

Participant: Escalate straight to IR with what I had, wait for the shift lead to be free for sign-off, or go back and rebuild the evidence chain from the earlier alerts first. I chose to escalate immediately — the SLA was already blown and waiting felt riskier than moving fast with an incomplete write-up.

Interviewer: How did that play out?

Participant: IR picked it up and confirmed lateral movement attempts from FIN-WK-114, consistent with that original DNS alert from hours earlier — the one that got closed in the batch.

Interviewer: Looking back across the night, at what point were you least certain about your read of the situation?

Participant: Probably the beacon classification. I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch.

Interviewer: A couple of hypotheticals to close. If the scan window hadn't been running that night, do you think you'd have handled the FIN-WK-114 alert differently?

Participant: Almost certainly. Without 300 scan alerts flooding the queue, that single DNS alert would have stood out on its own and I'd have looked at it individually.

Interviewer: If you hadn't been the one who wrote the suppression rule, would you have checked phishing containment differently?

Participant: Maybe — I might have been more inclined to ask someone else to verify it rather than trust the count dropping.

Interviewer: And if the last two shifts hadn't involved backup-agent false positives, how might you have approached the beacon differently?

Participant: I think I'd have gone straight to the process tree and IP lookup instead of pattern-matching against recent history. That comparison was really the whole reason I felt comfortable downgrading it.

Interviewer: Last one — what single process change would have caught this earlier?

Participant: Separating subnet visibility from severity in the queue view, so a scan-window filter can't accidentally sweep up a host that was never actually part of the scan. That's the gap that mattered most here.

Interviewer: That's really helpful, thank you for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Biased_3}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{SOC Analyst (Tier 2, Log/Alert Triage)}}"
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
