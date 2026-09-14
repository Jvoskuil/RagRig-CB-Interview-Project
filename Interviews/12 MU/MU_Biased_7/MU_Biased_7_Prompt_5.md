You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the incident, not in second-guessing the outcome. Everything's confidential and used for training and research purposes only. You're an Assistant Mine Manager at the site, correct?

**Participant:** That's right. I've been in that role about three years, twenty years underground total, mostly hard rock.

**Interviewer:** Good. Let's start broad — can you walk me through what was happening in Stope 14 East during that shift?

**Participant:** Sure. We were running a stope on the 950 level, standard longhole retreat mining. We'd had three microseismic events overnight — moderate magnitude, above what the array normally logs for that block over a rolling thirty-day average. No visible damage reported by the night shift, though. At the same time, we were two days behind on the monthly tonnage target, so there was some pressure from the production side to keep things moving.

**Interviewer:** What was your main objective going into that morning?

**Participant:** Keep the crew safe, obviously, but also not create a stoppage we couldn't justify. We'd had false alarms before — events that looked concerning on paper but turned out to be nothing. You don't want to shut a stope every time the array blips, or the crew starts tuning out the real warnings.

**Interviewer:** Take me through what you actually decided that morning.

**Participant:** The ground support plan for that stope had been signed off about four months earlier, and nothing had changed structurally since then — no fall of ground, nothing visible. So my read was that the plan was still sound, and I didn't see a reason to hold the crew back. We had options — pause entry and get an unscheduled inspection, or drop crew numbers until someone looked at it — but honestly, revising an approved plan on the back of three events felt like more disruption than the situation called for. We let day shift go in and start drilling as scheduled.

**Interviewer:** Did anything happen during that shift that stood out?

**Participant:** A bit of loose rock came off a rib wall mid-shift. Crew scaled it down, logged it as routine. Nothing that changed my thinking at that point.

**Interviewer:** Let's move to later that day — you mentioned a hazard rating came in.

**Participant:** Yes, our geotech support is remote most of the week — the engineer's only on-site two days. The model came back with a 2.3 on their five-point scale, tagged "moderate but manageable." The Stope 9 situation was actually the first thing that came to mind — it had come up on the shift handover just a few days earlier, almost the exact same rating and event cluster, and it had resolved completely fine, no incident. Between the number and that memory, I felt reasonably comfortable.

**Interviewer:** Were there other options at that point?

**Participant:** We could have asked for an updated rating that accounted for the blind spot near the intersection — the array doesn't read well there — or just held the blast until the engineer was back on-site the next day. I didn't go pull the broader run of comparable events across other stopes to see how those had generally played out; Stope 9 was just the one that was fresh in my head, so that's what I went with. The 2.3 read as solid enough, and Stope 9 had gone fine under similar numbers, so I authorized the afternoon blast clearance.

**Interviewer:** How much weight did that number carry versus other considerations?

**Participant:** A fair amount. It came from the model, and it was specific and official-looking, which made it easy to treat as settled rather than something to test against the blind spot we already knew was there.

**Interviewer:** What happened after the blast was cleared?

**Participant:** About two hours later there was a second event, larger than the first three, and outside what the model's confidence range would have predicted.

**Interviewer:** Let's talk about what happened next — the cracking.

**Participant:** Right, after the blast, the shift supervisor flagged some hairline cracking in the shotcrete on one rib. Around the same time a junior inspector — one of the geotech contractor's people — sent an email recommending we re-support before doing any more blasting. But two other crew members separately told me it looked like typical post-blast settling, nothing unusual.

**Interviewer:** How did you weigh those two views?

**Participant:** I leaned toward the crew's read. We'd seen a very similar crack pattern in Stope 9 previously that never led anywhere. So when the reporting went up to the production superintendent, I passed along the crew's "typical settling" assessments. The inspector's note got filed — I didn't raise it on the shift call, mostly because it felt like it would just muddy a picture that already seemed clear enough from the people who were actually standing there.

**Interviewer:** Was there a version of that decision where the inspector's note carried equal weight?

**Participant:** Looking back, sure — we could have treated the cracking as inconclusive and brought in an independent check rather than leaning on precedent and the on-the-ground opinions. At the time it didn't feel necessary because the Stope 9 comparison made the pattern seem like something we already understood.

**Interviewer:** Let's get to the final decision point — the next scheduled blast.

**Participant:** Right before that decision, one of the array nodes had sensor lag, so we didn't have confirmed magnitude data for recent ground movement. Then a small rock fall happened near the access drift — no injuries, minor. The superintendent was pushing to keep the blast on schedule to hit the month-end number.

**Interviewer:** What went into your call there?

**Participant:** Honestly, that rock fall didn't worry me much. I've personally been through plenty of similar events over twenty years underground, and they almost never escalate. If anything, it read to me as consistent with what we'd already been seeing — minor settling, nothing structural. I authorized the blast.

**Interviewer:** Were you uncertain at all in that moment?

**Participant:** There was a gap, sure — we didn't have the sensor confirmation we'd normally want. But I was confident in the call. Twenty years gives you a feel for these things that a delayed sensor reading doesn't necessarily add to.

**Interviewer:** Could you have suspended the blast pending that data, or escalated to the engineer for a fresh look?

**Participant:** Both were on the table. I just didn't think either was warranted given how the shift had gone.

**Interviewer:** What happened afterward?

**Participant:** The blast went fine. Ground stayed stable through the rest of the shift. We did schedule a post-shift review, though the underlying ground support plan wasn't actually revised.

**Interviewer:** Stepping back — if the geotechnical engineer had been on-site the whole time rather than remote, would anything have gone differently?

**Participant:** Possibly. Having someone physically there to look at the cracking directly, rather than relying on an email and crew impressions, might have changed how that got weighted.

**Interviewer:** And if the hazard rating had come back at 3.5 instead of 2.3?

**Participant:** That would have stopped me. A 3.5 doesn't let you lean on a comfortable memory the way a 2.3 does.

**Interviewer:** Looking back, would you make the same call on continuing under the existing support plan that first morning?

**Participant:** I'd probably want more of a structured comparison next time — actually laying the new seismic readings against the plan's original assumptions, rather than just defaulting to "nothing's changed, so we haven't changed anything." At the time, though, it felt like the obvious choice.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MU_Biased_7}}",
  "occupational_domain": "{{Mining and underground industrial operations}}",
  "role": "{{Underground Mine Manager / Assistant Mine Manager}}"
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
