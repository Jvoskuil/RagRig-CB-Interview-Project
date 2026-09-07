You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time. Just to confirm, this conversation is voluntary and for internal review of decision-making, not a formal chart audit. Okay to proceed?

Participant: Yeah, that's fine.

Interviewer: Can you set the scene—what was going on in the department that evening?

Participant: It was a Thursday night, pretty rough. We had four boarders in hallway beds waiting on inpatient rooms, so our effective capacity was well below normal. I was covering two other acute patients—a possible stroke and a kid with a fracture—when this chest pain patient came in. My second-year resident saw him first and then brought me in.

Interviewer: What was your first impression once you got involved?

Participant: 52-year-old man, generally healthy, pleuritic chest pain that was worse with deep breaths. Vitals were reassuring, sat 97%, heart rate 88. On exam I found reproducible tenderness over the chest wall, which does suggest something musculoskeletal, and he told me he'd been moving furniture two days earlier. That's a coherent story by itself. But he also mentioned, almost in passing, a 10-hour flight home from a trip about a week before, and a mild calf ache nobody had actually examined yet.

Interviewer: How did you weigh those pieces against each other?

Participant: The chest wall tenderness was a legitimate finding, so I wasn't going to dismiss it, but the flight and the calf comment gave me pause. Immobility plus a leg symptom is exactly the combination you don't want to explain away just because there's a tidier story sitting right in front of you. So I told the resident we'd hold off on a final impression until we actually looked at the leg directly.

Interviewer: What happened after that?

Participant: About twenty minutes later, the nurse rechecked him and confirmed mild swelling in the left calf, matching what he'd described. Around the same time, the resident came back with the D-dimer result—it had already been sent per our chest pain protocol—and it was mildly elevated, just above the assay cutoff.

Interviewer: Walk me through your thinking once you had that result.

Participant: A borderline D-dimer doesn't mean much on its own; it depends on the pretest probability going in. With the calf swelling now confirmed, I sat with the resident and we recalculated the Wells score properly, incorporating the leg finding this time rather than just the original picture. That pushed him into a range where imaging felt genuinely warranted, not just a reaction to one number.

Interviewer: How much did the scanner queue or bed pressure factor into that?

Participant: It was there in the background—40-minute queue behind trauma, charge nurse pushing to free up beds—but I didn't let that skip the reassessment step. I wanted the score redone first. Once that supported imaging, the practical pressure just meant asking radiology to prioritize him within their existing queue.

Interviewer: Tell me about the conversation regarding Dr. B's earlier patient.

Participant: While we were waiting on the CTPA, the charge nurse mentioned Dr. B had a similar-looking patient the week before—same kind of pleuritic pain—and discharged him without imaging. She said the patient did fine afterward.

Interviewer: What was your reaction to hearing that?

Participant: Honestly, my first thought was that I didn't know enough to judge it either way. Did he do a formal Wells score? Was it PERC-negative? A good outcome doesn't tell you whether the underlying reasoning was sound—some borderline calls work out fine by chance. I asked the resident to pull the chart before forming any real opinion.

Interviewer: What did you find?

Participant: Dr. B had documented a formal low-risk Wells score and a negative PERC before discharging that patient. So there was actual structure behind the decision, not just a guess that happened to land well.

Interviewer: Did that change your view?

Participant: It confirmed what I suspected—that it was a reasonable, defensible call given what he knew. If it had gone badly instead, with the same documented workup, I'd still call it reasonable. The outcome doesn't really tell you much about the quality of the reasoning behind it.

Interviewer: Let's get to the end of your shift. What was the situation with your patient by then?

Participant: PE was ruled out on the CTPA, though it picked up a small lung nodule needing outpatient follow-up, and he'd had a mild contrast reaction that took about 45 minutes to settle. By the time all that resolved, he was stable, but the visit had gotten more complicated than expected. The hospitalist I called wasn't eager to admit someone with a negative PE workup, and the patient and his wife were anxious to leave. Handoff was closing in.

Interviewer: How did you decide between admitting and discharging?

Participant: I genuinely went back and forth. Part of the pull toward admission was that the visit had been eventful—the reaction, the nodule—but eventful isn't the same as unsafe. Clinically, admission wouldn't have changed anything overnight; the nodule needed outpatient pulmonology, not inpatient care. I discharged him with a follow-up scheduled within the week and clear return precautions, but I told the resident honestly it could have gone either way.

Interviewer: What tipped it toward discharge in the end?

Participant: Mostly that nothing about his overnight risk profile had changed, and we had a real follow-up plan arranged quickly. The boarding pressure was present in the background, but I don't think it drove the decision. If anything, I spent more time on that disposition than I'd have liked given how busy we were.

Interviewer: What information, if it had been available earlier, would have changed how you handled the D-dimer result?

Participant: If the calf swelling had been documented at triage instead of found later, I probably would have gone straight to a formal risk score without the intermediate step of waiting on the nurse's recheck. It would have saved some time, though I don't think it would have changed the ultimate decision to image him.

Interviewer: If the department had been quiet that night, would you have handled things differently?

Participant: Not fundamentally—I still would have wanted the leg exam and the recalculated score before deciding on imaging. Busy or not, that step felt necessary once the calf came into the picture.

Interviewer: And if you'd learned about Dr. B's Wells score at the same time as the outcome, rather than afterward, would your reaction have been different?

Participant: No, I think I'd have asked the same question regardless of order—what did he actually know when he made the call. The outcome was almost beside the point for me.

Interviewer: Looking back, is there a moment you'd have handled differently?

Participant: Maybe I could have pushed radiology harder given how backed up we were. But on the clinical reasoning itself, I wouldn't change much. The disposition at the end is probably where I sat longest and still feel least certain—it was a genuinely close call, not an obvious one.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HC_Vocab_Control_3}}",
  "occupational_domain": "{{Healthcare}}",
  "role": "{{Emergency Medicine Attending Physician (community hospital, ~8 years post-residency experience)}}"
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
