Claude Sonnet Thinking - Prompt 5 - Task Taxonomy Classification

You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about how you handled a specific case, purely for internal review of decision-making processes—not a quality complaint or formal chart audit. Is that okay to proceed?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you set the scene—what was going on in the department that evening?

Participant: It was a Thursday evening shift, and we were slammed. We had four boarders in hallway beds waiting for inpatient rooms, so our actual bed capacity was maybe 70% of normal. I was covering two acute patients already—a possible stroke workup and a kid with a fracture—when this new patient came in with chest pain. My resident, a second-year, picked it up initially.

Interviewer: What was your first impression when you got involved?

Participant: 52-year-old, otherwise healthy, came in with pleuritic chest pain—worse with deep breaths. Vitals were reassuring: oxygen at 97%, heart rate 88. On exam, I found reproducible tenderness over the chest wall when I pressed on it, which is pretty classic for costochondritis. He mentioned he'd been moving furniture two days earlier. That fit nicely. He also mentioned, almost in passing, that he'd flown back from a trip about a week before, and that his calf had been a little sore, but nobody had actually looked at the leg yet.

Interviewer: How did you weigh those different pieces of information?

Participant: Honestly, the chest wall tenderness was the dominant finding for me. It's a strong, reproducible sign, and combined with the lifting history, it painted a clean picture. The flight and the calf thing felt like background noise—people mention all kinds of things when you ask an open history. I didn't chase it further at that point; I told the resident we were looking at a musculoskeletal strain and started wrapping up that part of the visit.

Interviewer: Did you consider formally working through something like a Wells score at that stage?

Participant: Not really, no. It felt like overkill given how clean the exam finding was. In my head, the case was basically settled—strain, reassurance, maybe some ibuprofen.

Interviewer: What happened next?

Participant: About twenty minutes later, the nurse rechecked him and noted his left calf was mildly swollen—something that hadn't been documented before. That's when the resident, who'd already sent a D-dimer per our chest pain protocol, told me it came back mildly elevated, just barely over the cutoff.

Interviewer: Walk me through your reasoning at that point. What were the options?

Participant: Two directions, really. One was to slow down and actually redo the risk stratification—recalculate the Wells score properly now that we had the calf finding, maybe apply PERC, and decide whether the elevated D-dimer even mattered much given his pretest probability. The other option was to just get the CTPA immediately and settle it.

Interviewer: Which did you choose, and why?

Participant: I sent him straight for the CTPA. Scanner had a 40-minute queue already because of a trauma case, charge nurse was on me to move patients since we had boarders stacking up, and I had maybe two hours before handoff. I remember thinking, let's just get the scan and have a real answer instead of going back and forth on scoring systems. It felt like the more decisive move—stop deliberating, get imaging, know for sure.

Interviewer: Did you go back and recalculate the risk score before ordering it?

Participant: No, not formally. I probably could have, and in retrospect the numbers might have supported watching him a bit longer instead. But at the time, ordering the scan felt like the productive thing to do rather than sitting on an ambiguous number.

Interviewer: What came back?

Participant: CTPA was negative for PE, which was reassuring. But it picked up a small lung nodule that needs outpatient follow-up, and then he had a mild contrast reaction—flushing, some itching—that needed monitoring. That ate up another 45 minutes we didn't really have.

Interviewer: Around this time, I understand there was also a conversation about a colleague's case. Can you tell me about that?

Participant: Right, while we were waiting on the CTPA, the charge nurse mentioned that Dr. B had a very similar-looking patient the week before—pleuritic pain, moderate risk—and discharged him without any imaging at all. She said the patient did fine, no issues since.

Interviewer: What was your reaction to hearing that?

Participant: My first thought was that Dr. B made a good call there—clearly the right decision, since nothing bad happened. I said something like that to the resident, actually, that Dr. B read the situation correctly.

Interviewer: At that point, did you know what specific findings or scoring Dr. B had used to make that decision?

Participant: No, I didn't know any of that. I was just going off the fact that it turned out fine.

Interviewer: Did that change later?

Participant: It did, actually. Later in the conversation, my resident mentioned that Dr. B had documented a formal low Wells score and a negative PERC result before discharging that patient—so there was actual structured reasoning behind it, not just a gut call that happened to work out.

Interviewer: Looking back, does that additional detail change how you'd frame your initial reaction?

Participant: I suppose it does add something. I was reacting more to the fact that it ended well than to what Dr. B actually knew going in. If it had gone badly, I probably would've had a very different first reaction, even with the same underlying reasoning on his part.

Interviewer: Let's move to the end of the shift. What was the situation with your patient at that point?

Participant: PE was ruled out, the nodule was noted for follow-up, and he'd recovered from the contrast reaction and was stable. The hospitalist I called wasn't thrilled about admitting someone with a negative PE workup—said there wasn't an inpatient indication. Meanwhile the patient and his wife were anxious and wanted to go home, and handoff was coming up fast.

Interviewer: What did you decide, and how did you get there?

Participant: I actually went back and forth on that one. Part of me wanted to admit him overnight just because the visit had been eventful—the contrast reaction, the nodule, the whole thing. But clinically, there wasn't a strong reason to keep him; he was stable, PE was excluded, and the nodule needed outpatient workup, not inpatient care. I ended up discharging him with pulmonology follow-up scheduled within a week and clear return precautions, but I wasn't fully settled on it—I remember telling the resident it could reasonably go either way.

Interviewer: What ultimately tipped it toward discharge?

Participant: Mostly that admission wouldn't have changed his management overnight, and the follow-up was arranged quickly. But I'll be honest, boarding pressure was part of the calculus too. I don't think it was the deciding factor, but it was in the room.

Interviewer: If the department had been quiet that night, do you think you'd have handled the D-dimer result differently?

Participant: Possibly. With more breathing room, I might have redone the scoring before jumping to the scanner. Whether that would've changed the outcome, I don't know—he might have needed the scan anyway.

Interviewer: And if you'd learned about Dr. B's Wells score and PERC result before hearing how the case turned out, do you think your initial reaction would have been different?

Participant: Probably calmer, less about vindication and more about the actual process. I think I would've evaluated it the same way I'd want someone to evaluate mine—based on what was known at the time, not just how the dice landed.

Interviewer: Looking back at the whole case, is there a point where you'd have paused longer before deciding?

Participant: The D-dimer moment, honestly. That's where I moved fastest, and where slowing down might have mattered most.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HC_Biased_3}}",
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
