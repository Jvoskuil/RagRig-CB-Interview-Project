You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and there's no evaluation of your performance attached to it — I'm strictly interested in how you thought through the situation. Sound okay?

Participant: Yeah, that's fine. I figured this was coming after the milepost 214 write-up.

Interviewer: Right. Can you start by telling me your role and roughly how long you've been in it?

Participant: I'm the Division Superintendent for the subdivision, been in this seat about six years, twenty years total with the railroad, most of it on this same territory as a trainmaster and roadmaster before I moved up.

Interviewer: Good. So walk me through what first came to your attention that morning regarding milepost 214.

Participant: I got a call from our track inspector around 7 a.m. He'd run the ultrasonic test on the curve as part of the regular cycle, and it came back showing an internal transverse defect at 4 millimeters. That segment had a flaw logged three weeks earlier at 2 millimeters, so it had grown. He flagged it to me directly instead of just filing it because he wanted me aware before the day got going.

Interviewer: What was your objective once that report came in?

Participant: Keep the railroad safe, obviously, but also keep things moving. We had Q-119, one of our priority intermodal trains, scheduled through that same territory later that day, and there's a contractual on-time window — if we blow past two hours late, we eat a penalty. So I'm balancing the defect against keeping that train on schedule, and we've also got a cold snap coming that night, temperatures dropping about 25 degrees, which matters for rail integrity in continuous welded rail.

Interviewer: What happened right after the ultrasonic results came in?

Participant: I pulled the defect log for that curve. It's had small flaws before — bolted rail sections nearby had similar-sized readings that just sat there and never went anywhere. My first read was, this looks like the kind of thing we've seen. I told the inspector I wanted to keep it classified as monitor status, retest in two weeks, standard for a flaw in that size range.

Interviewer: Did the inspector push back on that?

Participant: He mentioned the growth was faster than what we'd typically seen — doubling in three weeks is quicker than the other cases in the log, which had been pretty flat over a couple months. I heard him on that, but doubling from 2 to 4 millimeters is still a small number in absolute terms. It didn't strike me as enough to change the call. We'd retest in two weeks like normal.

Interviewer: What information did you have in front of you at the moment you made that classification?

Participant: The two readings, the growth comparison the inspector gave me verbally, the historical log showing similar flaws stabilizing, and the fact the segment's rated for 60 miles an hour under our current track class. Nothing in front of me suggested immediate failure, just a number that had gone up.

Interviewer: How certain were you about the growth rate at that point?

Participant: Fairly certain — the inspector's numbers are reliable. I just didn't weigh the rate itself as the deciding factor. I was weighing it against "we've handled dozens of these," and none of them ever became anything.

Interviewer: Let's move to later that morning. What led into the next decision?

Participant: The inspector called back to make sure I'd registered that this stretch is continuous welded rail, laid about five years ago — different from most of the bolted-rail spots where we'd seen flaws stabilize before. He also mentioned tonnage on that curve is up about 15 percent year over year. I heard both points.

Interviewer: What made you confident this flaw would behave like the earlier ones?

Participant: I've personally been through this scenario more times than I can count. I can think of three specific cases off the top of my head — one back around 2019, another maybe two years ago — where we had a flaw that size, kept it under monitor status, and it never amounted to anything. That's twenty years of pattern on this same stretch. When you've watched the same thing play out that many times, you trust what you've seen.

Interviewer: Did the CWR construction or the tonnage increase change your thinking?

Participant: I registered it, but those three cases felt close enough to this one that it didn't move me off keeping the curve at track speed. We held off on any interim slow order and left it at the two-week retest.

Interviewer: What alternatives did you consider?

Participant: Putting in an interim slow order just through that curve, or restricting it only for certain train types until the retest. I thought about the interim order, but given how those other cases went, it felt like overkill for what looked like the same pattern I already knew.

Interviewer: Let's go to the afternoon, the call about Q-119. What led up to that?

Participant: As we got closer to Q-119's window, the chief dispatcher, the trainmaster, and the road foreman got on a short call with me to decide whether to run it through at track speed, put a temporary slow order on it, or reroute it around the adjoining subdivision. Customer service had already flagged that a reroute or hold risked blowing our two-hour window with the customer.

Interviewer: What was everyone's position going into that call?

Participant: The trainmaster had texted beforehand saying it was probably fine but he was a little nervous. The road foreman said he was leaning toward running it but wouldn't mind a slow order. So people had some reservations, nothing dramatic.

Interviewer: How did the group's view change over the course of the call?

Participant: It moved pretty quickly. Once we started talking, everybody's confidence built on everybody else's. By the end we'd landed on releasing Q-119 at full track speed, no slow order at all — more decisive than where any of us individually started. The whole call took maybe six minutes. Nobody raised an objection at the end.

Interviewer: Does that six-minute timeframe feel fast for that kind of call, looking back?

Participant: In the moment it felt efficient. We all had the same information, everyone seemed to be arriving at the same place, so there wasn't a sense we needed to slow down and hash it out further.

Interviewer: After Q-119 went through, what happened?

Participant: A following local crew radioed in they'd noticed an unusual sound at the wheel-rail interface passing that same stretch — no visible damage, nothing measurable, just an odd noise. That prompted us to get a debrief together before shift change.

Interviewer: Who was in that debrief?

Participant: Myself, the trainmaster, and the chief dispatcher. Our assistant engineer from track engineering asked to sit in — he wanted to raise concerns about how we'd classified the defect and handled the speed decision — but the meeting was scheduled tight, fifteen minutes before shift change, and he wasn't looped in beforehand, so he ended up not joining. Between the three of us, we also figured he'd come in and push on the CWR classification again like he had before, and nobody was especially eager to reopen that discussion this late in the shift.

Interviewer: What was discussed, or not discussed, in that debrief?

Participant: We went through the wheel-rail sound, agreed pretty quickly it was unrelated to the flaw — probably debris or a joint bar, nothing tied to milepost 214 specifically. We didn't get into re-examining the retest interval or walking back through the earlier classification call. It felt like we'd already covered that ground, so there wasn't much appetite to go back over it again.

Interviewer: Was there any dissent in the room?

Participant: No, everybody agreed it was a non-event. The minutes just note we concluded the process worked as intended.

Interviewer: What alternatives did you weigh in that closing meeting?

Participant: We could have pulled the assistant engineer in after the fact, or kicked it up to the chief engineer for an independent look at the classification. Given how it played out with the sound being unrelated, it didn't feel necessary to extend the meeting further.

Interviewer: How much time pressure did you feel across these four moments — the morning classification, the track-speed call, the release decision, and the debrief?

Participant: The debrief and the release call were the tightest, shift change and the two-hour window respectively. The morning classification had the least pressure — that was just me and the inspector working through the numbers.

Interviewer: If the retest interval had been one week instead of two, would anything about your classification have changed?

Participant: Possibly. A tighter retest window would have given us another data point sooner, which might have shifted how I read the growth rate. As it stood, two weeks felt like standard practice.

Interviewer: If the assistant engineer had been on the original conference call about Q-119, do you think the release decision would have gone differently?

Participant: Hard to say for certain. He tends to be more conservative about CWR segments specifically, so it's possible his voice in that room would have slowed us down or gotten someone to push back on going full speed.

Interviewer: Looking back, is there a point where you'd have wanted a dissenting voice to speak up more forcefully?

Participant: Probably the debrief. He was asking to be included for a reason, and we didn't make room for that given the schedule. Might've been worth five more minutes.

Interviewer: Last one — if this same flaw had shown up on a curve you hadn't worked before, do you think your approach would have been different?

Participant: Yeah, honestly, probably. On unfamiliar territory I'd likely lean more on the inspector's read of the growth rate itself rather than my own sense of how these things usually go, since I wouldn't have twenty years of watching that particular stretch to fall back on.

Interviewer: That's helpful, thank you. I appreciate you walking through it in this much detail.

Participant: No problem. It's useful to talk it through, honestly — you don't always get the chance to go back over the reasoning like this.
}}

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
