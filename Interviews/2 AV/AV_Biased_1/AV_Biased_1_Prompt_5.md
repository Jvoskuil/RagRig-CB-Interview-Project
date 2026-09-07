You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for an internal reliability-process review, not a safety investigation into you personally — we're trying to understand how these calls actually get made in practice. That okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and how this particular case landed on your desk?

Participant: Sure. I'm a reliability engineer in Maintenance Control. Part of my job is watching for repetitive write-ups across the fleet and deciding when something crosses from "normal noise" into something that needs a formal corrective action. This one came up because tail 738 logged a third APU bleed air valve write-up inside 45 flight days. Two earlier ones had been closed out as operational check normal, no parts changed, which is pretty typical — a lot of these clear on the bench.

Interviewer: Walk me through the incident from the beginning, in your own words.

Participant: So the third write-up on 738 is what actually got my attention, because three in that short a window is unusual even though our fleet-wide removal rate for that valve was still sitting inside the OEM's published MTBUR. Nothing screamed "fleet problem" yet — it looked like it could just be a stubborn individual aircraft. I opened a focused review on that tail rather than calling it a fleet issue outright, and I put a flag on it so I'd get pinged if anything similar showed up elsewhere. Two days later it did — tail 712 logged a lower-severity version of basically the same complaint. That's when line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility we had an intermittent fault that ground checks weren't catching. At that point I pulled the two tails' component histories together and found they shared the same valve batch lot number. That felt like a real thread to pull.

Interviewer: What did you do with that lot-number connection?

Participant: Company policy is we don't like repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had had an actual in-flight consequence; both faults were caught on the ground. So grounding both outright felt like more than the evidence supported at that point. I put an interim restriction on — one leg of MEL carryover maximum, then it has to be addressed — on both tails, and opened a formal root-cause investigation tied to that lot number.

Interviewer: What came back from that investigation?

Participant: The vendor quality engineer confirmed that lot had a documented seal-material change about six months earlier. That's a real, traceable cause — not a guess. And our in-house teardown of the valve we'd pulled off 738 showed seal degradation that was consistent with exactly that material change. So by that point I had two independent lines — vendor documentation and physical teardown — pointing at the same thing.

Interviewer: Let's slow down on that moment, because I want to understand what happened next. What were you weighing?

Participant: Right, so this is the part before I finalized anything for the Reliability Control Board. I had ten days to the RCB deadline. The vendor's lot documentation and our own teardown already lined up on the seal material as the cause, and honestly I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had.

Interviewer: And what did you decide?

Participant: I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway.

Interviewer: At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended?

Participant: Not really, no. The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself.

Interviewer: What happened with the deadline?

Participant: We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it.

Interviewer: Let's move to the final decision — what you actually recommended once everything was in.

Participant: Once the root cause was locked down, the OEM tech rep raised the idea of a broader design review of the valve seal spec generally, as a longer-term option. But that's a slow, separate track. What I had in front of me was a specific, bounded problem: one vendor lot, identifiable serial ranges. I wrote the corrective action request to replace valves from that lot specifically, not a fleet-wide swap of every valve regardless of lot, and not just deferring to wait on the OEM's broader review.

Interviewer: Why bounded to the lot rather than fleet-wide?

Participant: Because a fleet-wide replacement would have pulled serviceable, unaffected valves for no reason — that's cost and downtime with no reliability benefit. The evidence pointed specifically at that lot, so that's what I scoped the action to.

Interviewer: What happened after you submitted it?

Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review got pushed into a separate long-term study, which is still open as far as I know.

Interviewer: Looking back at the whole sequence — is there a point where, with hindsight, you'd handle it differently?

Participant: The one thing I go back and forth on is the external lab. I already knew the recommendation wasn't going to move based on what it found — I'd have submitted the same lot-based request either way. Knowing that now, I probably should have just submitted on the original ten-day timeline using the vendor and teardown evidence and let the RCB approve on that, rather than holding the whole submission for a test that was only ever going to restate what I already had.

Interviewer: If the assay had come back showing something different from the vendor's account — a different degradation mechanism, say — what would you have done?

Participant: I'd have flagged it and opened a separate follow-up investigation into whether the lot-based campaign needed a second look. But that would've come after the fact — I wasn't planning to hold up this submission on that possibility, since I'd already committed to the lot-based recommendation before the assay went out.

Interviewer: And if this exact pattern showed up again on a different fleet type — same lot-based signature, same timeline pressure — would you send it out for independent lab work again?

Participant: Probably not on the same timeline, honestly. I think I'd ask myself earlier on whether the extra data was likely to change the recommendation I'd already reached or just make the file look better, and weigh that against the deadline more explicitly than I did this time.

Interviewer: That's a good place to stop. Thanks for the detail — this is exactly the kind of reconstruction we needed.

Participant: No problem. Happy to follow up if anything else comes to mind.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{AV_Biased_1}}",
  "occupational_domain": "{{Aviation}}",
  "role": "{{Aviation Maintenance Planner / Reliability Engineer}}"
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
