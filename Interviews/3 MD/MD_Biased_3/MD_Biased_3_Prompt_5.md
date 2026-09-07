You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a cognitive task analysis study, not for any evaluation of your performance or record. You can decline to answer anything. Are you okay to proceed?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and what your responsibilities were that night?

Participant: I was the Battle Captain on the night shift at the JOC, so I'm the watch officer responsible for the common operational picture, coordinating sensor and ISR tasking, and making the call on escalation — QRF alerts, higher headquarters notifications, that kind of thing. That night we were short an intel analyst, so the S2 shop was thinner than usual, and we only had one UAV available for the whole sector.

Interviewer: Walk me through what happened, starting from the first indication something was off.

Participant: Around 0215 a perimeter sensor near NAI-7, up on the northern boundary, logged a motion alert. Single sensor, no visual confirmation, and the weather that night — some ground fog — was already degrading sensor reliability. We didn't have any HUMINT or SIGINT corroborating it yet. Normally that's the kind of thing you'd log and keep an eye on. But I'll be honest, that specific sensor and that specific stretch of perimeter rang a bell for me. About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.

Interviewer: What exactly about the current alert reminded you of that earlier incident?

Participant: Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way.

Interviewer: Okay. What happened next?

Participant: I had the S2 analyst start pulling historical activity for the sector while I looked at tasking the UAV. That's where things got tight, because we only had the one asset and there were competing requests elsewhere in the sector that night.

Interviewer: Let's stay on that first call for a second — classifying the alert as elevated. What alternatives did you consider?

Participant: I could've left it routine and waited for more data, or reached out to the adjacent unit for corroboration before deciding priority. Comms with them were spotty that night, intermittent SATCOM, so that would've cost time. I went with elevating it based on what I already knew.

Interviewer: How confident were you in that classification at the time?

Participant: Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event.

Interviewer: Understood. So then you moved to the ISR tasking decision — walk me through that.

Participant: Right, with only one UAV, I had to justify diverting it to NAI-7 over the other requests. To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.

Interviewer: Were there other sources you could have checked?

Participant: Sure, there's the adjacent-unit SIGACT log and a sector-wide pattern-of-life database that tracks things like livestock movement and civilian traffic patterns near the perimeter. Both were accessible that night despite the comms issue — the pattern-of-life database is stored locally, actually.

Interviewer: Did you look at those before tasking the UAV?

Participant: No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later.

Interviewer: What made you stick with just the own-sector feed?

Participant: Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes.

Interviewer: What did the UAV feed show once it arrived on station?

Participant: Ambiguous thermal signatures. Could've been a small dismounted element, could've been livestock — genuinely hard to tell from the imagery alone. No weapons visible, no confirmed hostile indicators.

Interviewer: What did you do with that information?

Participant: I put the QRF on 15-minute alert status.

Interviewer: What alternatives were on the table at that point?

Participant: I could've held the current posture and requested more UAV dwell time to get a clearer picture, or asked the adjacent unit to send a ground patrol to verify visually before touching QRF readiness at all.

Interviewer: What tipped you toward alerting QRF instead of those options?

Participant: We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time.

Interviewer: Did the thermal evidence itself favor the ambush interpretation over livestock?

Participant: Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other.

Interviewer: What happened after QRF went to alert status?

Participant: Additional analyst review came back later and assessed the signatures as most consistent with livestock movement, based on movement speed and clustering patterns. QRF was never launched, just held at readiness.

Interviewer: How did you handle the final reporting for shift change?

Participant: I wrote it up as a genuinely mixed picture — noted the initial elevation, the QRF alert, and then the follow-up analyst assessment leaning non-hostile. I didn't want to call it a clean false alarm because the imagery was ambiguous enough that I couldn't rule out the dismounted-element read. I also didn't want to overstate it as an ongoing threat given what the analyst found. Higher headquarters ended up asking for a follow-up clarification the next day, which is pretty normal for anything left open like that.

Interviewer: Was there a point where you considered recommending a sensor review for NAI-7 instead?

Participant: I mentioned it as a secondary note, since that spot generates a fair number of ambiguous alerts, but I didn't want to bury the main SITREP under an infrastructure recommendation when the operational question was still open.

Interviewer: Stepping back — if the alert had come in during a quiet stretch with no recent similar incident in your memory, do you think you'd have classified it the same way?

Participant: Probably not as quickly to elevated. I think I'd have waited for the S2 pull before deciding priority.

Interviewer: If you'd checked the adjacent-unit and pattern-of-life data first, before your own-sector feed, do you think the tasking decision changes?

Participant: The UAV probably still goes to NAI-7 — that part of the call felt justified regardless. But I think how I framed the justification would've been different, maybe more grounded in actual cross-referenced history instead of just what was in front of me.

Interviewer: And if you hadn't run that ambush rehearsal in training recently, would you have read the thermal imagery differently?

Participant: Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way.

Interviewer: Last question — looking back with everything you know now, what would you change?

Participant: Honestly, probably slow down at each of those first three points and force myself to check the wider data before trusting my first read. None of the individual calls were unreasonable given what I had in front of me, but I can see now where I leaned on what came to mind fastest instead of what was actually available.

Interviewer: That's really helpful. Thanks for walking through it in that much detail.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MD_Biased_3}}",
  "occupational_domain": "{{Military and defense operations}}",
  "role": "{{Joint Operations Center (JOC) Watch Officer / Battle Captain}}"
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
