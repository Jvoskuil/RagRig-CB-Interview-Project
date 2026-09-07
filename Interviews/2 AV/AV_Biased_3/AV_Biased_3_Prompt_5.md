You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for taking the time. Just to confirm, this is a cognitive task analysis interview—I'll ask about a specific turnaround you handled, and I'd like you to walk me through your reasoning as it happened, not just the outcome. Nothing here is evaluative of your performance. Can you tell me your role and roughly how long you've been doing it?

Participant: Sure. I'm a load controller, been doing it about nine years now, mostly narrow-body combi ops. On a normal day I'm building load sheets, issuing loading instructions to the ramp, checking weight and balance against structural limits, and making sure the NOTOC is accurate before the captain gets it. This particular one was a standard 45-minute turnaround, nothing scheduled to be unusual about it.

Interviewer: Walk me through what happened, from when you first got involved.

Participant: I got the initial cargo manifest about an hour before departure. Mixed load—regular baggage, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what we usually put through, not on a pallet. Our load-control software generates an automatic load instruction—the ALI—and it put that machinery item into hold 3. The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated so they could start loading, because we were already tight on time. About twenty minutes later, after the ramp had loaded per that instruction, they called up and said the aircraft was sitting slightly tail-heavy on the jacks reading—not out of limits, just noticeably aft of where we'd expect for that load.

Interviewer: What did you do at that point?

Participant: I logged it and kept moving, because we still had the last-minute change to deal with. About that time, an LMC came in—roughly 380 kilos of mail plus six late bags that hadn't made the original manifest. The mail got assigned to hold 5, which is our aft bulk hold, smaller one. I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route—we'd had three similar ones, same ballpark, and none of those needed any redistribution. So I cleared it on that basis and moved to finalize the trim sheet.

Interviewer: And the trim sheet—what informed that?

Participant: I pulled up the dispatch log because I wanted a sanity check before signing off, given the tail-heavy reading from the ramp. I saw that the two previous flights on this same rotation—different tail numbers, one had gone to a different destination—had both needed aft trim adjustments. That, plus what the ramp had just told me, made me think the rotation itself was running tail-heavy that day, so I shifted some of the cargo distribution forward before finalizing, beyond what my own computed index actually called for.

Interviewer: Let's slow down and go through each of these moments individually. Starting with the ALI and the machinery item—what specifically told you it was fine to issue as generated?

Participant: Mainly just experience with the system. It's been accurate for months on this fleet, and we don't have time in a 45-minute turn to hand-check every ALI. I did register that the item was irregular, non-palletized, heavier than usual—that did cross my mind—but the system's had a good run, so I went with it.

Interviewer: Was there a manual limits chart you could have checked against for that item specifically?

Participant: There is one, for exactly this kind of non-standard cargo. I know it exists. I just didn't pull it that time.

Interviewer: What would have made you stop and check it?

Participant: If the system itself had flagged it somehow—like if it had kicked back a warning saying "verify manually," I'd have stopped. Since it didn't, I treated it the same as any other ALI.

Interviewer: Moving to the LMC decision—what exactly did you compare when the mail and bags came in?

Participant: Total weight against the week's pattern. That's the number I had readily in my head from the previous LMCs.

Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs had gone?

Participant: Not specifically, no. The earlier ones went into a forward hold, I believe—hold 2 typically. This one went aft into 5. I didn't run the index shift for that specific placement; I just used the weight comparison as my check.

Interviewer: What would it have taken to run that index calculation directly instead?

Participant: A couple of extra minutes with the trim computer, honestly. It wasn't unavailable—I just didn't feel it was necessary given how the weight lined up.

Interviewer: Let's talk about the trim sheet redistribution. What was your reasoning connecting the two previous flights to this one?

Participant: They were on the same rotation, back to back, both needed aft correction. Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift as a margin before I signed off.

Interviewer: At the time, what did your own calculated index for this flight actually show?

Participant: It was within the normal range on its own, forward of the aft limit with margin. The redistribution wasn't because my numbers were bad—it was more that I didn't fully trust that after seeing two prior aft trims.

Interviewer: Did you look into why those two prior flights ran tail-heavy?

Participant: Not at the time. I found out afterward one was a fuel imbalance and the other had extra catering loaded late. Different tails, different causes, nothing tying them to each other.

Interviewer: Last one—the final sign-off. What was the situation there?

Participant: Closeout figures were within limits, looked clean. But the ramp tally was one bag short of what the NOTOC and manifest showed. Small discrepancy, and we were right up against the slot.

Interviewer: What did you decide, and what were you weighing?

Participant: I signed and released with the figures as they stood. I weighed the delay risk—losing the slot—against a one-bag discrepancy that's usually a clerical miscount, not a safety issue on its own. It resolved itself afterward as a manifest correction; the weight and balance conclusion didn't change. I could see someone making the other call too, holding a few minutes to chase it down. It wasn't an easy one either way.

Interviewer: Looking back across the whole sequence, how confident were you in each of those calls at the time versus now?

Participant: The ALI and the LMC I was fairly confident on in the moment—maybe more than I'd be now, knowing how it played out. The trim redistribution I was less sure about even then; it felt more like caution than certainty. The final sign-off, I'm still not fully sure I made the "right" call, but I don't think it was wrong given what I had.

Interviewer: If the software had required a manual check for irregular cargo shapes before finalizing the ALI, do you think that changes how this played out?

Participant: Probably, yes. If it forced me to open the manual chart, I would have caught the hold 3 placement issue before the ramp ever loaded it.

Interviewer: And if the mail had gone into the usual forward hold instead of hold 5?

Participant: Then the weight comparison I used would have actually been a fair proxy, because placement wouldn't have mattered much. It was really the aft location that made the comparison misleading, not the comparison itself.

Interviewer: If you'd known upfront that the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way?

Participant: No, I don't think I would have. I'd have trusted my own numbers for this flight instead of layering in a correction based on what happened to two other tails.

Interviewer: Anything you'd do differently if this exact sequence happened again?

Participant: Pull the manual chart for anything irregular regardless of the system's history, and separate what the current flight's numbers say from what the last couple of flights did, unless I actually know there's a shared cause. The last-minute change is the one I'd still have to think about—weight alone clearly wasn't the full picture that day.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{AV_Biased_3}}",
  "occupational_domain": "{{Aviation}}",
  "role": "{{Load Controller / Loadmaster (Commercial)}}"
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
