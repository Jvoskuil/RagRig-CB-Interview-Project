You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about your decision-making during the last refueling outage, not a performance review. Everything you share is for process improvement. Can you tell me your role and roughly how long you've been doing outage coordination?

Participant: Sure, happy to walk through it. I'm the maintenance planner and outage coordinator for the unit — been doing this specific role about six years, plus four years as a planner before that. My main job during the outage is to sequence work orders against the critical path, allocate craft-hours, and make sure everything closes out before we hit the mode change hold points.

Interviewer: What made this particular outage stand out from a routine one?

Participant: Honestly, the sheer volume — we had around 140 concurrent work orders competing for a fixed 21-day window, and craft-hours were tighter than usual because two contractor crews got pulled to another site mid-cycle. So there was a lot of juggling. The item that ended up taking more of my attention than I expected was FW-IV-204, one of our feedwater isolation valves.

Interviewer: Take me through the sequence of events, from initial scoping to final return to service.

Participant: At the start of scoping, FW-IV-204 had a minor packing weep — nothing new, it had shown up in two prior outage condition reports, both closed as acceptable-as-found. No trend showing it was getting worse. But right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework. Then, once we got into execution, craft-hours were running thin one afternoon and I had to lock in a crew configuration fast for the valve job — Outage Manager wanted it settled within the hour. I went with the first configuration that cleared the minimum schedule and safety requirements. Later in the outage, during post-maintenance testing, we saw a mild vibration anomaly on the pump bearing right next to FW-IV-204. My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service.

Interviewer: Let's slow down and reconstruct the timeline in more detail. When exactly did FW-IV-204 first come onto your radar for this outage?

Participant: Right at the outset of scoping, maybe day one or two of pre-outage planning. It was already on the work list from the prior cycle's CR, so it wasn't a surprise. What changed was how I ranked it relative to everything else.

Interviewer: And the vibration anomaly — when did that surface relative to the valve work?

Participant: That was maybe day fourteen, after the valve rework was already complete and we were running post-maintenance functional tests on the adjacent feedwater pump.

Interviewer: Let's go through each of those decision points one at a time. First — the priority ranking. What information did you actually have in front of you when you made that call?

Participant: I had the two prior CRs, both closed, no adverse trend on leak rate. I also had the backlog of other work orders, some with comparable or even higher CR severity ratings. Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list.

Interviewer: So what tipped it to top-tier?

Participant: The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up.

Interviewer: Did you go back and re-check the trend data before finalizing that ranking?

Participant: No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to.

Interviewer: Understood. Second decision point — the crew configuration under the tight craft-hour window. Walk me through that.

Participant: We were maybe two-thirds through the day's craft-hour budget, and I had several configurations that would technically work — different mixes of overtime, different sequencing with other jobs. The Outage Manager wanted a decision inside the hour to protect the critical path. I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in.

Interviewer: Did you consider comparing the other options more fully?

Participant: I thought about it, but comparing all the variables — overtime cost, fatigue limits, downstream sequencing — for three or four configurations would have eaten time I didn't have. So I went with what worked and moved to the next fire.

Interviewer: What happened as a result?

Participant: It created a minor sequencing conflict later with an unrelated pump job — nothing that blew the schedule, but craft had to shuffle around it. When we reviewed it afterward, there was a configuration that would have avoided that friction. Marginally better, not dramatically.

Interviewer: Third decision point — the vibration anomaly. What was your first working theory?

Participant: Residual misalignment from the valve rework. It made sense sequentially — we'd just had hands in that area, and a little post-maintenance vibration isn't unheard of.

Interviewer: What data did you pull to check that theory?

Participant: I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis.

Interviewer: Was there other data available that you didn't request at that point?

Participant: In hindsight, yes. There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched.

Interviewer: What about the full trend history for that bearing?

Participant: Also didn't pull that at the time. The system engineer reviewed it later, after the fact.

Interviewer: Last decision point — the final return-to-service call. What was your basis for concurring?

Participant: By that point, all the CRs on the valve and the adjacent pump were formally closed, the system engineer had given written concurrence, and I did the walkdown myself with operations. Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service. I did weigh the earlier vibration discussion against that documentation, but everything on paper and everything I saw in the field lined up, so I didn't see a basis to hold it further.

Interviewer: Did you consider requesting extra monitoring time before mode change?

Participant: I did think about it briefly, given the anomaly earlier in the outage, but with the engineering concurrence and a clean walkdown, holding the unit longer without a specific technical reason didn't seem justified.

Interviewer: How much time pressure were you under across these decisions, generally?

Participant: Constant, honestly, but it spiked hardest around the crew assignment call — that was the one hour deadline. The priority ranking and the vibration call had a bit more breathing room, even if it didn't always feel that way in the moment.

Interviewer: If the lubrication log had been sitting on your desk when the vibration anomaly came up, do you think it would have changed your review?

Participant: Possibly. If it had shown something inconsistent with misalignment, I probably would have widened the investigation. It just wasn't something I went looking for at the time.

Interviewer: Looking back, is there a point where a different call on FW-IV-204's priority might have changed how things unfolded?

Participant: Maybe. If I'd ranked it purely on the documented trend, it might have sat lower in the queue, and I'd have had more craft-hours free for other jobs earlier. Hard to say if that changes anything meaningfully, since the valve work itself went fine.

Interviewer: Anything you'd tell a newer planner based on this outage?

Participant: Mainly to keep coming back to the actual trend data, even when a recent story or a tight clock makes a different path feel more urgent. It's not that those instincts are wrong, just that they're easy to lean on more than the numbers warrant.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{NP_Biased_3}}",
  "occupational_domain": "{{Nuclear power and Process-control operations}}",
  "role": "{{Maintenance Planner / Outage Coordinator}}"
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
