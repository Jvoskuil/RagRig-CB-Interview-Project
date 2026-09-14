You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for talking with me. This is for a plan-review case study, it's voluntary, and you can skip anything you'd rather not go into. Can you tell me about your role and how the Meridian Tower conversion came to you?

Participant: Happy to. I'm a plan review official in the building and fire division—permitting and life-safety sign-off, mainly. Meridian Tower was an adaptive reuse, a 22-story former office tower going to mixed-use residential and retail. The complication was the atrium, a large central void running most of the building height. It didn't fit the prescriptive smoke control provisions in our code, so the design team came in with a performance-based alternative instead.

Interviewer: What was your objective going in?

Participant: Get the review done correctly within our statutory window. We had a 30-day clock, the department was short-staffed that quarter, and there was pressure from the city to keep housing projects moving. All of that mattered, but the core job was still making sure the building would actually perform the way the code intends if there's a fire.

Interviewer: Walk me through what happened, from the start.

Participant: The engineer of record was Halkirk & Vance, a regional firm with a lot of atrium experience—dozens of approved performance-based designs, and a neighboring jurisdiction had approved something similar from them the year before. They submitted a CFD-based smoke control model in place of the prescriptive system. We didn't have budget for an outside peer review that cycle, so I went through the documentation myself. One assumption stood out—how the model handled stack effect if a door were left partially open during an event—and I wasn't satisfied it was addressed clearly enough, so I sent that back to them in writing before finalizing anything. After that we moved into commissioning planning, where we had to choose between two verification protocols. Construction got underway, and about six weeks in, our inspector flagged fire-rated door deficiencies on three floors. Later, as we were approaching occupancy, the developer requested an early certificate before full integration testing was complete. Near the end of construction there was a small trash-chute fire—sprinklers handled it, no injuries—which led us to take another look at the atrium system, though it turned out to be a separate issue.

Interviewer: Let's put the order together more precisely. What did you know before the first major decision, and what came in after?

Participant: Before approving the design, I had the CFD report, the firm's general track record, and the neighboring jurisdiction's approval. After I sent back the question on the stack-effect assumption, they responded with additional documentation, and I approved based on that exchange. Then came the commissioning protocol decision. After that, construction started, and the door issue came up. The occupancy request was near the end, and the trash-chute fire happened after that decision was made, not before.

Interviewer: Let's take the first decision—approving the performance-based design. What carried the most weight?

Participant: The firm's documentation carried real weight, and so did the neighboring jurisdiction's approval—that told me the overall modeling approach had held up under scrutiny elsewhere. But I still went through the assumptions myself, and the stack-effect piece wasn't fully addressed for our specific geometry. I asked for a written clarification on that point specifically rather than taking the package at face value or sending the whole thing out for a full outside review, which would have added about three weeks.

Interviewer: Was a full peer review ever seriously on the table?

Participant: It was one of the options, yes. I decided a targeted clarification on the one assumption that mattered most for egress got me most of the benefit without the full delay.

Interviewer: Second decision—the commissioning protocol. What were you weighing?

Participant: Two options. Option A was a newer risk-informed test, better matched to this atrium's geometry according to the guidance, but its thresholds were only partly and qualitatively defined. Option B was the older prescriptive smoke test—clean binary pass-fail, but less sensitive to some of the failure modes this atrium could actually have.

Interviewer: Which did you choose, and why?

Participant: Option A, but not without addressing the enforcement problem. I built in defined interim checkpoints and documentation standards so the qualitative thresholds would still be auditable if anyone questioned the sign-off later. I didn't want to trade technical fit for administrative convenience, but I also didn't want a protocol I couldn't defend.

Interviewer: Third decision—the door deficiencies. What did you see, and how did you respond?

Participant: The inspector found bad fire-door installations on floors 8, 11, and 14. My first instinct was to wonder if we had a specific crew problem. But crews were rotated randomly across the building, and it was three deficiencies out of roughly 150 doors checked at that point—which is within the range you'd expect from ordinary variation on a project this size. So I kept the original random-sample inspection plan across all floors rather than concentrating just on those three.

Interviewer: What did the rest of the inspection show?

Participant: The building-wide sample came back with a defect rate consistent with what we'd already seen—nothing suggesting those three floors were actually worse than the rest.

Interviewer: Fourth decision—the temporary occupancy request. What was your basis?

Participant: The developer had a financing deadline, and full integration testing on the alarm and smoke systems was still about three weeks out. The contractor had a good record on other city jobs, and a colleague mentioned a nearby building that had gotten early partial occupancy without incident. But our own five-year data show something like a 15 percent rework rate on these atrium integration tests citywide, and that number is specific to the exact system we hadn't tested yet. So I granted occupancy only for the floors that didn't depend on the untested atrium system, and held back the rest until testing was done.

Interviewer: What would have made you grant broader occupancy at that point?

Participant: A completed, passed integration test, basically. Nothing short of that for the floors relying on that system.

Interviewer: How much uncertainty did you feel across these decisions?

Participant: Fairly consistent, honestly. The door situation had some ambiguity until the wider sample came back. The occupancy call had the most riding on it, which is part of why I drew the line where I did rather than treating the contractor's general history as settling the question.

Interviewer: Looking back now, after the trash-chute fire, how do you view the original design approval?

Participant: It held up fine, as it turned out—the fire was in the chute enclosure, unrelated to the atrium system. If anything, it reinforced that the clarification I'd asked for on the stack-effect assumption was worth pursuing at the time, though I wouldn't say the fire proved anything either way about that decision.

Interviewer: If you had to make the temporary occupancy call again with the same information, would you do anything differently?

Participant: No, I think I'd draw the same line. The rework rate was too specific to ignore just because of a good general track record elsewhere.

Interviewer: Last question—what would you tell a newer reviewer facing a similar submittal?

Participant: Don't let a strong firm's name stand in for checking the one assumption that actually matters for your building, and don't let a small pattern in early data override what a proper sample tells you.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Vocab_Control_6}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Building/Fire Code Official (Plan Review and Permitting)}}"
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
