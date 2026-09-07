You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the procurement network reporting incident from earlier this year in detail, including your own decision-making, and that this is for internal process review rather than any kind of performance evaluation.

Participant: Yeah, that's fine. I figured we'd get to that one eventually.

Interviewer: Can you give me your role and a quick sense of what this incident was?

Participant: I'm a reports officer, I also handle collection management for our part of the station. This case was a walk-in who showed up claiming to know about a shipment tied to a procurement network we'd been chasing for months. It turned into a pretty compressed reporting cycle because we had a policy briefing coming up fast.

Interviewer: Let's start with the incident itself. Walk me through how it began.

Participant: So this network had been frustrating us for a while — lots of partial reporting, nothing that let us really nail down how they were moving material. Then out of nowhere, a walk-in comes into the local office claiming direct knowledge of an imminent shipment. He had a handwritten fragment that looked like part of a manifest, and a photo of a shipping container. Honestly, my first reaction was that this looked like exactly the pattern we'd been building toward — the container markings, the paper trail, it all lined up with what we expected this network's shipments to look like. I remember telling my deputy it was almost a textbook match.

Interviewer: What did the documents actually show, as best you recall?

Participant: The manifest fragment was partial — some numbers, an abbreviated destination code, nothing complete. The photo was a standard container, generic markings, could've been thousands of containers at that port. But given everything we'd already built on this target, it read to me as clearly consistent. I didn't really entertain that it could just as easily be a routine shipment.

Interviewer: How did you feel at that point, beyond the analytical read?

Participant: If I'm honest, there was relief. We'd put months into this with basically nothing to show, and here's someone walking in with exactly the kind of specificity we'd been missing. I remember thinking, finally, this is the break. That colored how quickly I moved to request expedited document validation instead of sitting with the uncertainty a bit longer.

Interviewer: Let's reconstruct the timeline from there. What happened after the walk-in session?

Participant: I drafted debrief notes describing him as consistent with the network hypothesis and pushed for expedited validation. Around the same time, we had a coordination call with technical collection folks, and that's when a colleague flagged that their data showed activity at a different port than the one the walk-in named. Then I spent the next stretch drafting the report itself, and the final hours before the briefing were spent finalizing language and setting up follow-on tasking.

Interviewer: Let's go back to that first decision — accepting the walk-in's material as consistent with the network hypothesis versus treating him as fully unvetted. What were your alternatives?

Participant: Technically I had three options: treat him as an unvetted contact needing full standard validation before any tasking, treat the material as a strong match and move to tasking right away, or defer any assessment twenty-four hours for basic authentication. I went with the middle path, more or less.

Interviewer: What made the middle path more compelling than waiting for authentication?

Participant: The pattern fit was strong enough that I didn't feel authentication would tell me anything I didn't already believe. Looking back, that's probably generous — the physical evidence itself wasn't that specific. But it matched the shape of what we expected, and given how long we'd been at this, waiting felt like it was leaving value on the table.

Interviewer: Second decision point — reconciling the walk-in's account with the technical collection discrepancy about the port. What did you weigh there?

Participant: The walk-in claimed he'd had a prior logistics role, which would explain how he'd know shipment details. That struck me as the kind of detail a real insider would know, not something you'd fabricate. So I leaned toward treating his account as substantially credible on that basis. Honestly, the claim on its own didn't prove he knew anything about this particular shipment — it just made the story fit together the way I already expected it to, so I let it stand as enough. If that same claimed logistics background had come attached to an account that pointed away from the network we'd been building the case on, I probably would have wanted a lot more before accepting it. Meanwhile the port discrepancy from technical collection was sitting there, and my colleague raised it directly on the call.

Interviewer: How did that discrepancy factor into the draft?

Participant: It went into a footnote. The corroborating sub-source reporting and the walk-in's account got the bulk of the narrative treatment. I didn't have a strong evidentiary reason to downgrade the technical flag — if anything it deserved more scrutiny — but it just didn't get the same space in my head at that point.

Interviewer: What was driving that imbalance in attention, would you say?

Participant: Partly deadline pressure. Partly that the corroborating material fit the story we were already building, so it took less effort to write up. The port discrepancy would have required unwinding something, and I didn't have time to unwind it properly.

Interviewer: Third decision point — how you described the uncertainty in the report itself, and how you scheduled the follow-on work. Walk me through that.

Participant: The shipment timing estimate had real uncertainty in it. I could have written it either way — emphasizing what we didn't know and what might undercut the assessment, or emphasizing the probability that the network would move soon. I went with language that stressed the chance of imminent action. It read as more useful for a policy audience with fourteen hours to go.

Interviewer: Just to pin that down — was the actual underlying estimate any different depending on which way you phrased it, or was it the same number either way?

Participant: Same number, same underlying picture. Nothing in the estimate itself changed. But writing it as "likely to move soon" instead of "not confirmed to move imminently" made the whole thing feel more actionable to me as I was drafting it — like it justified moving forward with fewer qualifiers than I probably would have used if I'd framed it the other way.

Interviewer: And the follow-on tasking timeline?

Participant: I set meetings and validation steps assuming everything would line up — interpreter availability, safehouse access, sub-source cooperation, all on a fast track. We'd run similar validation sequences before and they'd almost always taken longer than planned, but I didn't build that history into the schedule this time. The deadline was right there, so I planned for the version where things went smoothly.

Interviewer: Fourth decision point — the branch chief's push to disseminate. What happened?

Participant: My chief reviewed the draft and wanted it out the door as-is, minimal additional caveats, given the deadline. The port discrepancy was still unresolved at that point. I'd seen him make calls like this before in ambiguous situations, and he'd usually been right. So I didn't push back or request the extra caveat language I probably could have asked for.

Interviewer: What was the deciding factor in not pushing back?

Participant: Honestly, his track record and seniority carried a lot of weight for me in that moment. I didn't go back and independently re-examine the discrepancy myself before agreeing — I mostly deferred to his read of the situation.

Interviewer: What happened after dissemination?

Participant: The product went out largely as he wanted. Afterward, the observed shipment activity didn't line up with the timing we'd put in the report.

Interviewer: If the port discrepancy had surfaced earlier, before your first read of the walk-in, do you think your draft would have looked different?

Participant: Maybe. I'd like to think I'd have weighed it more evenly from the start rather than treating it as something to explain away later.

Interviewer: If your chief hadn't expressed a preference on dissemination, would you have handled the caveats differently?

Participant: Possibly stronger caveats, or at least a harder look at the discrepancy before signing off. Hard to say for certain.

Interviewer: Looking back, is there a point where you'd have wanted more time, regardless of the deadline?

Participant: The very first read of the documents. I moved to expedited validation pretty fast instead of sitting with the ambiguity.

Interviewer: Last one — if this kind of walk-in situation happened again, what would you want in place beforehand?

Participant: Probably a standing rule to get an independent second read on ambiguous physical evidence before it shapes the rest of the reporting cycle, and more discipline about building historical timelines into follow-on scheduling instead of assuming best case.

Interviewer: That's really helpful context. Thank you for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IA_Biased_7}}",
  "occupational_domain": "{{Intelligence analysis and information-intensive analytic work}}",
  "role": "{{Human Intelligence (HUMINT) Collection Manager/Reports Officer}}"
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
