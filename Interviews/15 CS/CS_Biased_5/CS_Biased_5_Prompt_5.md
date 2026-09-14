You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a retrospective walkthrough of a specific vulnerability case you handled, purely for process review — nothing about individual performance evaluation. Can you tell me your role and how long you've been doing vulnerability management?

Participant: Sure, no problem. I'm a Vulnerability Management Analyst, I've been in this seat about three years now, before that I did general SOC monitoring. Right now I own triage and remediation tracking for our internet-facing assets, so patch coordination, compensating controls, closing out tickets against our SLA.

Interviewer: Great. Walk me through how this particular case started and what you were trying to accomplish.

Participant: So this began when our threat intel feed flagged a new CVE, critical, 9.8 on CVSS, and it had confirmed exploitation already happening in the wild. It hit the web framework running underneath our legacy order-processing gateway — that's the system customers hit when they check out, so it's tagged Tier-1 criticality, internet-facing, revenue-generating. My objective was straightforward on paper: get this closed within our 30-day SLA without taking the gateway down during a peak sales stretch. The complication is that gateway is old, it needs vendor coordination to patch, and we had a partial change freeze coming up in about ten days, so the runway to actually get a maintenance window was shrinking fast. On top of that I had two other high-severity tickets open at the same time, so this wasn't the only thing on my plate.

Interviewer: Given all that, how did the incident actually unfold, in order?

Participant: Day one, the alert comes in, I do initial triage and decide to push for an emergency change board session instead of waiting for the normal 21-day cycle. That gets approved, but it's only a two-hour window, not enough for full regression testing. So around day three, we deploy a WAF rule as an interim compensating control instead of the real patch. While I'm watching the dashboard for that, I notice there's also some odd outbound DNS traffic from the same host, but it's not part of what I'm tracking for this ticket. About a week in, IT Ops points out there's now a vendor SIEM correlation rule available for this CVE family, versus the detection script I'd built myself months earlier, and I decide how to handle that overlap. Then by day 27, with the SLA clock running out and the actual patch still not deployed, I make the call on whether to close the ticket as mitigated.

Interviewer: Let's slow down on the first one — the decision to escalate. What made you push for the emergency CAB slot instead of the standard cycle?

Participant: Honestly, the exploit-in-the-wild status was the trigger, that's usually a hard line for us. But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days.

Interviewer: Did you weigh that against the cost of disrupting the gateway with an emergency patch attempt?

Participant: A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that.

Interviewer: Understood. Second decision point — once you had the WAF rule in place, how did you handle the DNS anomaly you mentioned?

Participant: Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as "anomalous, monitor" and moved on. My focus was really on validating the compensating control against the threat we knew about.

Interviewer: Was there a reason you didn't open a parallel look into the DNS traffic at that point?

Participant: I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something. At the time, though, it just wasn't where my attention was.

Interviewer: Third decision — the detection tooling. What happened there?

Participant: Right, so I'd written a detection script for this six months back, tuned it myself against our traffic. When the vendor's SIEM correlation rule came out covering multiple payload variants, IT Ops suggested we just standardize on that instead. I kept my script as the primary and put the vendor rule in a secondary, lower-priority slot.

Interviewer: What was the reasoning behind keeping yours in the lead role, given the vendor rule had broader coverage?

Participant: I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well.

Interviewer: Did that decision have downstream effects?

Participant: About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap.

Interviewer: Last decision point — closing the ticket at day 27. Walk me through that.

Participant: At that point we still didn't have the actual vendor patch deployed, just the WAF rule and my script running as compensating controls. The SLA clock was almost out. I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup. There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.

Interviewer: How much of that closure decision was based on the specific residual-risk data for this ticket versus that broader context?

Participant: Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have.

Interviewer: Was there uncertainty at that point about whether the controls were fully sufficient?

Participant: Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it.

Interviewer: If you'd had another week before the SLA deadline, would anything have gone differently?

Participant: Probably would have chased down the DNS anomaly properly and maybe pushed harder for the actual vendor patch instead of leaning on compensating controls that long.

Interviewer: If that ransomware story hadn't been in the news that week, do you think the closure decision changes?

Participant: Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then.

Interviewer: And if the vendor SIEM rule had existed from day one, would you have built your own script at all?

Participant: Hard to say — probably still would have, honestly, just because I like understanding exactly what's under the hood. Though maybe I'd have made it secondary from the start instead of the other way around.

Interviewer: Looking back across the whole case, is there a point where you think you gave one piece of evidence more weight than it really deserved?

Participant: Probably the closure call. Between my own confidence in the controls I'd built and everything going on in the news that week, I think I leaned on those more than the actual open items on the ticket.

Interviewer: That's really helpful, thank you for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Biased_5}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{Vulnerability Management Analyst}}"
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
