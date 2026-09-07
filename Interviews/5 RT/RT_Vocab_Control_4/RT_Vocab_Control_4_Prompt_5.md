You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. This is being recorded for internal process review, not a performance evaluation — I'm interested in how you worked through the situation. Okay to proceed?

Participant: Sure, no problem.

Interviewer: Can you tell me your role and how long you've been in it?

Participant: Division Superintendent, six years in this role, twenty years on the railroad overall, most of it on this same subdivision as a trainmaster and roadmaster before that.

Interviewer: Walk me through what first came to your attention that morning regarding milepost 214.

Participant: Our track inspector called around 7 a.m. He'd run the ultrasonic test on the curve as part of the regular cycle, and it came back at 4 millimeters on an internal transverse defect. That same spot had been logged at 2 millimeters three weeks earlier. He called me directly instead of just filing the report because the jump stood out to him.

Interviewer: What was your objective for the shift once that came in?

Participant: Keep the operation safe, but also be realistic about the schedule. We had Q-119, one of our priority intermodal trains, due through that territory later in the day, and there's a contractual on-time window — past two hours late and we take a penalty. On top of that we had a cold front coming that night, about a 25-degree drop, which matters for rail integrity on continuous welded rail. So I'm weighing the defect information against the operational picture, not just one or the other.

Interviewer: What happened right after the ultrasonic results came in?

Participant: I pulled the defect history for that curve. There'd been small flaws there before, mostly on bolted rail nearby, that had stayed flat and never developed into anything. But what stood out this time wasn't just the 4-millimeter reading, it was the rate — doubling in three weeks is faster than anything in that log. I treated that rate as the key new piece of information. Instead of keeping the standard two-week retest, I moved it to an elevated-monitor status with a one-week retest.

Interviewer: What made you decide the growth rate itself should change the interval?

Participant: Two millimeters isn't much on its own, but the speed of the change is what a static reading doesn't tell you. If it had gone from 2 to 2.5, I'd probably have left the interval alone. Doubling in three weeks felt like something that needed a closer look sooner.

Interviewer: What information did you have at the moment you made that call?

Participant: The two readings, the inspector's comparison to the historical log, the current 60 mile-an-hour track class rating, and his statement that the rate was faster than what we'd typically seen. Nothing pointed to imminent failure, but the trend was enough to justify tightening the interval.

Interviewer: Let's move to later that morning. What led into the next decision?

Participant: The inspector called back to flag that this stretch is continuous welded rail, laid about five years ago, different from most of the bolted-rail spots in our comparison cases. He also mentioned tonnage on that curve is up around 15 percent year over year. Both came up before I made the next call.

Interviewer: How did you weigh those details against what you'd seen in similar cases before?

Participant: I've handled a lot of flaw reports over the years, and my instinct was that this looked like ones that had resolved fine. But the inspector's point about the CWR and tonnage was legitimate — those aren't small distinctions, especially with the cold snap coming. So rather than going with full track speed because it reminded me of past cases, or swinging all the way to a full slow order, I put a targeted, moderate speed restriction on that curve specifically, to hold until the one-week retest.

Interviewer: What alternatives did you rule out there, and why?

Participant: Full track speed leaned too much on pattern-matching without accounting for the differences the inspector raised. A full slow order across the segment felt heavier than the data supported — we didn't have evidence of anything beyond the flagged growth rate. The moderate restriction on just that curve matched the actual risk picture.

Interviewer: Let's go to the afternoon call about Q-119.

Participant: As we got closer to Q-119's window, the chief dispatcher, trainmaster, and road foreman got on a call with me to decide whether to release the train through 214 under the interim restriction, hold it for a reroute, or wait for more data.

Interviewer: What was everyone's position going in?

Participant: The trainmaster had texted beforehand that it was probably fine but he was a little nervous. The road foreman said he was leaning toward releasing it but wouldn't mind a slow order. So there was some caution on the table already.

Interviewer: How did the group's view compare to where people started?

Participant: It didn't move much, honestly. We talked through the restriction already in place, the penalty exposure if we held the train, and the retest timeline, and the road foreman asked partway through whether the restriction we had was enough given the CWR concern. We talked that through for a minute before agreeing to release under the existing restriction rather than removing it. The call ran close to fifteen minutes.

Interviewer: Did anyone push for a more extreme option, either direction?

Participant: Not really. Nobody argued for pulling the restriction, and nobody argued for a full reroute either. We landed close to where people already were.

Interviewer: After Q-119 went through, what happened?

Participant: A following local crew radioed in an unusual sound at the wheel-rail interface near that stretch — no visible damage, nothing measurable. That triggered a debrief before shift change.

Interviewer: Who was in that debrief?

Participant: Myself, the trainmaster, and the chief dispatcher initially. Our assistant engineer from track engineering asked to join to raise concerns about the classification and the speed decision. The meeting was originally set for fifteen minutes before shift change, but the chief dispatcher pushed it back to bring him in once we heard he wanted to weigh in.

Interviewer: What was discussed once he joined?

Participant: We went through the wheel-rail sound — the read was that it was probably unrelated, likely debris or a joint bar, but nobody stated that with certainty. We confirmed we'd keep the interim restriction in place until the retest, and we logged his specific concerns to revisit at that retest rather than closing them out.

Interviewer: Was there any disagreement in the room?

Participant: A bit. He wasn't fully convinced the sound was unrelated, and he wanted the retest moved up further. We didn't move the date, but we agreed to note his concern formally and treat it as open rather than resolved.

Interviewer: What alternatives did you consider in that meeting?

Participant: Closing it out quickly without him, which is basically what almost happened before the schedule got adjusted. Or escalating straight to the chief engineer that same day. We didn't think escalation was warranted yet, but documenting it as open with a defined follow-up felt like the right middle ground.

Interviewer: How much time pressure did you feel across these four moments?

Participant: The release call and the debrief were the tightest, tied to the two-hour window and the shift change. The morning classification had more room — that was mainly me and the inspector working through the numbers.

Interviewer: If the retest interval had stayed at two weeks, would anything about your classification have changed?

Participant: If it had stayed at two weeks, we'd have been relying longer on a single fast-growth data point without a closer check, which is part of why I didn't want to leave it standard.

Interviewer: If the assistant engineer had been on the original conference call, do you think the release decision would have gone differently?

Participant: Maybe the discussion would have taken a bit longer, but I don't think the restriction itself would have changed much, since we'd already built it in based on his earlier input about the CWR and tonnage.

Interviewer: Looking back, anything about the debrief you'd have handled differently given the time constraints?

Participant: I'd have looped him in before the meeting was even scheduled, rather than adjusting on the fly once he asked.

Interviewer: Last one — if this flaw had shown up on a curve you hadn't worked before, would your approach have been different?

Participant: Probably similar, since the restriction came out of the specific data points rather than familiarity with the location. I might have leaned on the inspector's judgment even more, since I wouldn't have my own history with that curve to cross-check against.

Interviewer: That's very helpful, thank you.

Participant: Sure thing.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{RT_Biased_4}}",
  "occupational_domain": "{{Rail Transportation}}",
  "role": "{{Division Superintendent / Operations Manager}}"
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
