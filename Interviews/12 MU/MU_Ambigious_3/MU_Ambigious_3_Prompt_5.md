You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down with me. This is a routine interview to reconstruct how you approached a specific blast round — it's not an evaluation of your performance, and everything stays with the study team. Okay to go ahead?

Participant: Sure, no problem.

Interviewer: Can you tell me about your role and what this round involved?

Participant: I'm the drill and blast engineer for the lower sublevels — I own the pattern design, sign off on charging, and coordinate with geology and ventilation before anything fires. This was a production round in Panel 14, sublevel open stope, about 450 meters down, right next to the service shaft, so vibration control is always part of the picture. Goal was simple on paper: fire on schedule, hit fragmentation targets for the mill, stay under our PPV limits near the shaft.

Interviewer: What was the situation going in?

Participant: We were a shift behind and the mill was low on feed, so there was real pressure to keep moving. A couple days out, geology mapped a minor fault trace crossing about a third of the panel, with some moisture along it. Not alarming on its own, but new enough that I didn't want to just wave it off either. A full geotechnical resurvey would've eaten the whole shift, which we didn't have, so I had the crew run a limited spot-check on a handful of holes near the trace instead — a middle option between doing nothing and doing everything.

Interviewer: Walk me through what happened as drilling and charging progressed.

Participant: The spot-check came back clean on the three holes we tested, but it didn't cover the entire fault-affected stretch — I was upfront with the crew about that limitation. Once full drilling wrapped, a few more holes near the trace logged wet, including two just outside where we'd spot-checked. The explosives technician flagged those specific holes and suggested decking them with emulsion instead of running full ANFO columns. I went with that for the flagged holes only, keeping ANFO for the rest of the panel — partly on his data, partly because I'd handled similar wet ground before without major issues. Then, while loading, one more hole outside the original flagged list turned up borderline wet too, which we hadn't caught. On timing, our two vibration sensors near the shaft disagreed a bit — one comfortably under limit, the other borderline — and the vendor guidance didn't clearly say which one to trust for our geometry. I went with the more conservative longer-interval sequence given that mismatch. After firing, the fault-zone section came out with some overbreak and coarser fragmentation, vibration stayed under limit on both sensors but with less margin than usual, and no complaints came in.

Interviewer: Let's go back to the pattern decision specifically. What was driving the choice to spot-check rather than resurvey or just proceed?

Participant: Honestly, it was a resource call as much as anything. A full resurvey was the safer option in theory, but it would've blown the schedule entirely, and the pattern's history in that ground gave me some confidence it probably wasn't a major issue. The spot-check felt like a reasonable middle ground — get some current data without stopping everything.

Interviewer: Did the fact that it only covered part of the zone concern you at the time?

Participant: A bit, yeah. I flagged it to the crew supervisor as a known gap, not something I was fully comfortable with, but I judged it acceptable given the time we had.

Interviewer: On the charging decision — how did you land on the mixed approach rather than going one way or the other?

Participant: The technician's data pointed pretty specifically at certain holes, and I didn't have a strong reason to extend that to the whole panel. At the same time, I've seen wet ground behave both ways — sometimes it's nothing, sometimes it needs real adjustment — so I wasn't relying purely on his numbers or purely on my own read. It felt like combining both was the more defensible call.

Interviewer: Did you consider treating the whole panel more conservatively given the borderline hole that turned up later?

Participant: In hindsight, sure, but at the time it hadn't been discovered yet — that came up during loading, after the charging plan was already largely set.

Interviewer: Moving to the timing call — the two sensors disagreeing seems like a genuinely tricky spot. How did you work through that?

Participant: It was tricky. Neither sensor was clearly wrong, and the vendor's guidance didn't settle it for our specific layout. I talked it through with the safety officer, and we agreed the conservative reading deserved more weight given we couldn't fully explain the gap between the two. So we went with the longer interval, accepting a bit less fragmentation efficiency for a wider vibration margin.

Interviewer: Was there time pressure to just default to the standard sequence instead?

Participant: A little, but not enough to skip that conversation. It felt like the kind of disagreement worth pausing on for ten minutes.

Interviewer: Last one — after the round, how did you approach explaining the overbreak to the mine manager?

Participant: That one I genuinely couldn't resolve on the spot. It looked similar to a fault-zone overbreak pattern I'd seen at a previous site, but this round also had real gaps — the spot-check didn't cover everything, and the charging was mixed rather than uniform. Either factor could explain what we saw, maybe both together. I told the manager that rather than picking one story, and asked the geologist to review the current instrumentation before we changed anything for the next round.

Interviewer: Was there pressure to give a cleaner answer than that?

Participant: A little — he wanted something actionable — but I didn't think I could honestly narrow it down yet without more review.

Interviewer: If the spot-check had covered the entire fault-affected zone, do you think the outcome would have been different?

Participant: Possibly. We might have caught those additional wet holes earlier and adjusted the charging more broadly. I can't say for certain it would've changed the overbreak, but it would've closed one of the gaps we're now unsure about.

Interviewer: And if the two vibration sensors had agreed with each other?

Participant: That would've made the timing call much simpler — less deliberation, less uncertainty about which reading to trust.

Interviewer: Looking back, is there a specific piece of information that could have resolved the overbreak question one way or the other?

Participant: Full coverage on the geotechnical side, honestly. Right now we've got two plausible explanations sitting side by side, and neither the deviation survey nor my own experience is enough on its own to settle which one mattered more.

Interviewer: That's a really thorough walkthrough — thank you.

Participant: Happy to clarify anything further if it helps.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MU_Ambigious_3}}",
  "occupational_domain": "{{Mining and underground industrial operations}}",
  "role": "{{Drill and Blast Engineer}}"
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
