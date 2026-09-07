You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for training purposes — we're reviewing your decision-making during the Kestrel Subdivision shift, not evaluating your performance. Is that alright with you?

Participant: Sure, no problem. I've done a few of these before.

Interviewer: Great. Can you start by telling me your role and what the board looked like that evening?

Participant: I was the sole dispatcher covering the Kestrel Sub, about 40 miles of single track for most of it. We had a maintenance possession scheduled from 6:40 to roughly 7:30 for tamping work near milepost 214, plus a mixed traffic evening — a manifest freight headed east and an intercity passenger train that was already running about 22 minutes behind schedule with a connection downstream. My main priority was keeping things moving safely through that one possession window without letting the passenger delay balloon further.

Interviewer: Walk me through how the incident actually unfolded.

Participant: About twenty minutes into my shift, the wayside hot-box detector near milepost 198 flagged the freight train — an axle bearing reading slightly above baseline, but well under the threshold that triggers an automatic stop. No abnormal noise reported by the crew, nothing visual. Not long after that, I started working the sequencing problem for the passenger train getting through the work zone at 214. Then, while I was juggling that, the foreman on-site radioed in something about a possible person near the right-of-way — the transmission was choppy, in and out, so I didn't get a clean picture of where exactly or how many. And near the tail end of the possession, the foreman asked for a 12-minute extension to finish the tamping work properly.

Interviewer: So four distinct things landed on you in a fairly short window.

Participant: Pretty much back to back, yeah. That's a normal night on that line, honestly — it's just a matter of which order you deal with them and what you're willing to let sit for a minute.

Interviewer: Let's reconstruct the order. What came first, and what did you do right after?

Participant: The hot-box alert came first. I checked the reading against the threshold table — it was elevated, but not near the automatic-stop number. The next detector was about 8 miles up the line. I authorized the crew to proceed at restricted speed to that next detector rather than stopping cold on the single track, since stopping there would've blocked everything behind it, including the passenger train's approach to the work zone. When the next reading came back, the temperature had actually stabilized rather than climbed, so that resolved fairly cleanly.

Interviewer: What was going through your mind when you made that call?

Participant: The number was below the mandatory stop point, so procedurally I had room to make that judgment. Stopping a train on that single track for a hands-on inspection is a big deal — it doesn't just hold up that train, it backs up the whole corridor behind it. Given no other symptoms from the crew, restricted speed to the next detector felt like the appropriate middle ground. I've made calls like that before and they've resolved fine most of the time.

Interviewer: How confident were you at that moment?

Participant: Reasonably. Not certain — you're never fully certain with a bearing reading — but confident enough given the threshold and the lack of other symptoms.

Interviewer: Let's move to the passenger train and the work zone. What were your options there?

Participant: Two real options. One, hold the passenger train for a short window — maybe four or five minutes — while the crew paused work, and let it through under standard flag protection, which is the setup they use routinely at that site. Two, reroute it entirely onto the alternate line, which avoids the work zone altogether but adds about 25 minutes and forces me to realign two other train slots later in the evening.

Interviewer: Which did you choose, and why?

Participant: I sent it around on the alternate line. I just didn't want that train anywhere near an active work zone that evening — I wanted it completely clear of that whole area rather than threading it through on a flag. Even though the flagging setup there is the standard one they use all the time, I'd rather eat the schedule hit than have any interaction with the work zone at all.

Interviewer: Was there something specific about that flag protection that made you distrust it?

Participant: Not really anything specific to that crew — it's the same setup used all over the subdivision. I think I just weighed it as, if I reroute, that risk is off the table entirely, full stop. The delay is a known, manageable cost. I didn't sit there and compare exactly how much risk the flagged window actually removes versus how much schedule damage the reroute causes — it was more that avoiding the zone altogether felt like the safer place to land.

Interviewer: Did the 25-minute cost and the two realigned slots factor into that comparison?

Participant: They were in the back of my mind, but honestly, once I decided I wanted the train out of that zone entirely, the size of the delay became secondary. It's not that I ignored it, I just didn't weigh it against how small the actual exposure through a flagged window normally is.

Interviewer: Let's go to the trespasser report. What did you actually hear?

Participant: It was garbled — "possible person near the right-of-way," something like that, no confirmed location, no headcount, and I couldn't tell if they'd already moved off or not. Reception near that stretch is spotty.

Interviewer: What were your options at that point?

Participant: Realistically both options started with getting a precaution in place right away — you don't leave a train unprotected on a report like that no matter which way you go next. So it was really a question of which precaution. I could issue the standard subdivision-wide restriction — ten minutes of restricted speed through the whole general area — which is the routine call for reports like this. Or I could put a shorter restriction on just the immediate approach while the foreman tried a callback, and then either lift it early or extend it once I actually knew what we were dealing with.

Interviewer: Which did you go with?

Participant: I went with the full ten-minute restriction across the whole area. It's the protocol I know — fixed length, fixed scope, everyone on the radio understands exactly what it means and when it ends. The tailored version might've actually cost the queued trains less time if the callback had come back clean, but I couldn't tell you up front how long that would run or how far the restriction would need to extend, so it felt like the harder thing to commit to in the moment.

Interviewer: Did you weigh what the report might actually mean — say, that it could be nothing, or could be something more serious than the standard protocol addresses — against the tailored option?

Participant: Not really as a probability question, no. It wasn't that I sat down and worked out how likely it was to be nothing versus something worse. It was more that the fixed protocol had a shape I could describe to everyone right away, and the tailored version was open-ended until the callback came through, so I defaulted to the one with the known edges.

Interviewer: Last decision — the possession extension.

Participant: The foreman asked for 12 more minutes to finish the tamping properly. I had two trains queued behind the work zone at that point. I granted it. Denying it risked leaving the work incomplete, which usually means scheduling a whole new possession later in the week — more disruption overall. The queued trains absorbed a modest additional delay, but the crew finished clean.

Interviewer: How did you land on that one?

Participant: That was more of a straightforward cost comparison — a short, bounded extension now versus a bigger disruption later. Fairly routine call.

Interviewer: If the detector reading had been just a bit higher, would your first decision have changed?

Participant: Yes, definitely — if it had been near the stop threshold I'd have held the train for a physical inspection, no question.

Interviewer: And if the foreman's report had come through clearly instead of garbled — say, confirmed as one person who'd already left the area?

Participant: If I'd had that, I probably would've gone with the tailored, shorter restriction from the start instead of the full ten-minute call. Knowing the person was already clear would've given me something definite to scope the response around, instead of having to lean on the fixed protocol just because it was the one thing I could describe with certainty in the moment.

Interviewer: Looking back, is there anything you'd handle differently with the same information you had at the time?

Participant: Maybe on the reroute — I might spend a bit more time actually comparing what the flagged window really costs in risk versus what the full reroute costs in delay, rather than just leaning toward whichever option felt more completely clear of the zone. But overall, given what I knew in the moment, I'd probably make the same calls again.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{RT_Biased_2}}",
  "occupational_domain": "{{Rail Transportation}}",
  "role": "{{Signal Maintainer / Signal Technician}}"
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
