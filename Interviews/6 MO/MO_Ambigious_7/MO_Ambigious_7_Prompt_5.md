You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making the time. This is a confidential debrief on the cargo transfer job alongside the platform, purely to understand the reasoning behind decisions on the day — not a disciplinary review. Comfortable proceeding?

Participant: Yes, go ahead.

Interviewer: Can you start with your role that day?

Participant: I was DPO on watch, running DP2 station-keeping during a scheduled cargo transfer — deck cargo and some bulk — to the platform. Normal job in most respects. Hold position off the leg, crane operator takes the lifts, we maintain the watch circle.

Interviewer: What made this one non-routine?

Participant: The forecast weather was closing in a bit faster than the morning brief suggested. Roughly a four-hour window before sea state would exceed the platform crane's limit. So there was schedule pressure, but nothing outside what we train for.

Interviewer: Walk me through what happened, start to finish.

Participant: On final approach I picked up a 1.7-meter discrepancy between HPR and the two DGPS units, which were agreeing with each other closely. The system had auto-weighted the DGPS pair and was showing green. I also remembered that HPR had an intermittent fault logged from a previous voyage — cleared, but never formally re-certified after that. Given that history, I treated the DGPS pair as the more trustworthy read and logged the discrepancy as unresolved rather than fully explained, and continued the approach. We got alongside, transfer went smoothly through the first several lifts. About halfway — 55% of cargo across — Thruster 3 raised a yellow caution, reduced power available. Consequence analysis still showed adequate capability, but with less margin than we'd started with. I also knew that switching to a more conservative configuration at that point would cost us something like twenty to twenty-five minutes we didn't have much room for against the weather window, so I weighed that against the capability numbers and kept going at the same pace. On the second-to-last lift, there was a wind shift that changed the footprint recommendation on the DP plot. I was on the crane boom display at that point, which is standard procedure during an active lift, and my co-operator was mid-exchange on the radio confirming rigging for the next lift, so neither of us picked up the footprint change immediately. The Master noticed the vessel's attitude shift a short time after and flagged it. For the final lift, OIM asked whether we could finish or should stand off. I checked both the time estimate — eight to ten minutes — and the separation and capability readout, which still looked adequate for that duration, and told him we could finish. Partway through, our separation closed faster than either figure had suggested it would, and we suspended early and backed off. No contact, stayed inside the watch circle, but it was closer than planned.

Interviewer: Let's go back through that in order. What were you tracking at each stage?

Participant: Early on, reference systems and DP status, which is standard for closing distance. Once we were alongside, it split across the crane display, thruster status, and periodic environmental checks. During the final lift specifically, the crane display gets priority per procedure, and whoever's free on the bridge picks up secondary monitoring — that shifted around a bit depending on what else was happening at the time.

Interviewer: On the reference discrepancy — talk me through the reasoning there.

Participant: DGPS1 and DGPS2 agreed tightly. HPR was off by 1.7 meters, and it had that fault history from a prior voyage — nothing currently logged against it, but nothing re-certifying it as fully sound either. Given a choice between two fresh, agreeing units and one with an open question mark over it, I leaned toward the DGPS pair. I didn't call it settled — I noted it as something to keep an eye on rather than a solved problem.

Interviewer: Did you consider pausing to pull HPR's diagnostic log before continuing?

Participant: I thought about it. It would have meant holding the approach for a few minutes with no clear guarantee it would tell us anything conclusive, since the fault history was intermittent by nature. I judged the DGPS agreement plus HPR's own track record gave enough basis to proceed, but I'll be honest, it wasn't a fully closed question either way.

Interviewer: Now the thruster caution — what went into continuing there?

Participant: The consequence analysis still cleared us, just with a smaller cushion than before. I also had a rough number for what a mode change would cost us time-wise against a window that was already tight. It came down to margin against time cost, and the margin figure won out. I can see an argument either way on that one.

Interviewer: Did the amount of cargo already moved factor into it?

Participant: No — the cargo already across was just where we happened to be in the sequence, not something I weighed. The actual comparison was the consequence-analysis margin against the projected delay from reconfiguring, and the margin held up well enough to justify continuing at that point.

Interviewer: Move to the final lift and the footprint change. What was happening with attention at that point?

Participant: Standard procedure has the crane display as priority during an active lift. My co-operator was tied up confirming rigging on the radio for the next lift, which is a legitimate concurrent task, not something either of us could have dropped without creating a different problem. So the footprint change sat for a short while before either of us caught it.

Interviewer: Would reassigning that monitoring in the moment have been realistic?

Participant: Possibly, but it would have meant interrupting a rigging confirmation that also affects safety on the next lift. It's a genuine trade-off, not an obvious call either way.

Interviewer: Last one — the OIM's question about the final lift.

Participant: I looked at both numbers I had — time to finish and the current separation and capability readout — and both supported finishing at that moment. The margin just closed faster than either had indicated it would once we were actually maneuvering.

Interviewer: If the margin readout had shown a tighter number at that moment, would that have changed your answer?

Participant: Probably, yes — if the readout itself had been less favorable I'd have told him to stand off. The issue wasn't which number I used, it's that the number moved faster than expected.

Interviewer: Looking back at the whole sequence, does it seem like there were earlier signs of how close things got, or does it read that way mainly because of how it ended?

Participant: Honestly, I go back and forth on that. Individually, none of those things — the discrepancy, the caution, the workload split — crossed a line that demanded a different call. Whether they add up to something predictable in hindsight, or whether it just came together unluckily at the end, I'm genuinely not sure.

Interviewer: What would you tell a newer DPO facing something similar?

Participant: Don't treat any single reading in isolation, and keep checking whether your trade-offs still hold as conditions shift, not just at the point you first made them.

Interviewer: Anything you'd do differently?

Participant: Maybe build in a fixed re-check of the margin figures rather than relying on the initial assessment holding steady. Otherwise I think the calls were reasonable given what was in front of me at each point.

Interviewer: Appreciate you walking through this in detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MO_Ambigious_7}}",
  "occupational_domain": "{{Maritime Operations}}",
  "role": "{{Dynamic Positioning Operator (Offshore Support Vessel)}}"
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
