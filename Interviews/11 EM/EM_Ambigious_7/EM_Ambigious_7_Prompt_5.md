You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for taking the time. Just to confirm, you're okay with this being recorded for after-action training purposes only, not for any personnel review?

Participant: Yeah, that's fine.

Interviewer: Can you describe your role and what you were responsible for when this incident began?

Participant: I'm the Situation Unit Analyst for the county EOC. During an activation, I build and maintain the Common Operating Picture — pulling together field reports, gauge data, weather updates, whatever's coming in — and I turn that into something the Branch Directors can actually act on. That night I was covering the flood side while also keeping half an eye on the fire branch, since Ridge Fire was still active and was interfering with some of our sensor and repeater coverage.

Interviewer: Walk me through how the incident began.

Participant: Around 9 PM we got a notice from the Twin Forks Reservoir Authority about a release tied to the incoming storm cell. The wording was pretty standard operational language — not alarmist, but not something I'd call reassuring either. Our downstream gauges were showing a gradual rise at that point, nothing that clearly told you how big this was going to get. The duty hydrologist was tied up on another call for at least ninety minutes, so I didn't have a technical read to lean on. Our flood Branch Director looked at it and said the pattern looked similar to releases he'd seen before, but he also flagged that the rainfall forecast for this particular storm cell was less certain than in past events — he wasn't fully reassuring, just giving me his honest read on both sides of it.

Interviewer: What did you do with that information?

Participant: I went with a monitor-and-prepare advisory rather than an immediate warning. It wasn't really one factor — it was the gradual gauge trend, the Director's qualified take, and the fact that jumping straight to a warning without more to go on has its own costs, in terms of credibility and resource strain if it turns out to be nothing. I documented specific thresholds that would trigger an upgrade if the gauges moved past them, so it wasn't an open-ended wait.

Interviewer: Did you consider seeking independent verification before finalizing that?

Participant: I did think about it, but with the hydrologist unavailable, the choice was really between acting on the best synthesis I had or delaying any messaging at all, which carries its own risk. I weighed the Director's read alongside the actual gauge numbers rather than just taking his word for it.

Interviewer: What happened next?

Participant: About ninety minutes later, the gauges spiked much faster than the early trend had suggested. The release turned out to be larger than what the gradual rise had implied.

Interviewer: Let's talk about the resource decision that followed.

Participant: Our field liaison started getting scattered water-rescue calls in two sub-neighborhoods, but the call intervals were irregular — hard to say if that was tapering off or about to surge. Around the same time, the weather service bumped up their estimate of how long the storm cell would sit over us, and a neighboring jurisdiction let us know their swift-water assets were available on a limited-time mutual-aid hold.

Interviewer: How did you decide what to request?

Participant: I went with a staged tier-2 mobilization instead of matching the confirmed calls exactly or going straight to tier-3. Part of it was the call pattern being ambiguous, part of it was the extended storm estimate, and part of it was that mutual-aid window — if I waited and needed more later, those assets might not be there. None of those three things alone would've pushed me to tier-2, but together they did.

Interviewer: Was there a specific past incident that shaped that call?

Participant: Not really one specific case I was drawing on. It was more just weighing what was in front of me that shift.

Interviewer: How did that play out?

Participant: Calls plateaued at a level that, looking back, either tier-1 or tier-2 could've handled. Some of the mutual-aid assets got used, some stayed in reserve. Hard to say in hindsight whether tier-1 would've been enough or whether we got lucky with tier-2.

Interviewer: Let's move to the evacuation decision.

Participant: This was the hardest one. Six of eight gauges were down from repeater damage tied to the Ridge Fire smoke, so I only had two reporting, both rising sharply over about twenty minutes. We do have a contingency protocol for this — when network coverage drops below half, there's a default evacuation radius around any gauge that crosses threshold. Field spotters were also seeing street flooding near one of the two working gauges, though nothing yet from the other sub-zones.

Interviewer: How did you apply that?

Participant: I followed the protocol and expanded evacuation to the zones adjacent to those two gauges. I was explicit with the team that the radius is a policy compromise — it's not a claim that we know what's happening in the unmonitored zones, it's just the standard response when coverage is this degraded. I didn't feel like I had enough to justify going wider than the protocol called for, and I also didn't think it was responsible to wait for full confirmation given the rate of rise.

Interviewer: Did you weigh expanding further than the protocol specified?

Participant: I considered it, honestly. Two gauges isn't much of the network. But going beyond what the protocol lays out felt like it would've been guessing past the point where I had a documented basis for the call.

Interviewer: What came out of that?

Participant: When backup gauges came back later, the adjacent zones matched the protocol's assumptions in some spots and not others. So it's genuinely mixed — the protocol got some of it right and missed some of it.

Interviewer: Let's talk about the hot-wash review of the initial advisory decision.

Participant: We used our standard after-action template, which forces you to separate what was known at the time from what's known now. Going through it point by point, some parts of the original advisory call still look reasonable to me given the gradual trend and the Director's qualified comment. Other parts — like the uncertain storm-duration forecast — in hindsight, maybe should've pushed us toward an earlier tier upgrade. It's not a clean verdict either way.

Interviewer: Do you think the outcome makes that decision look worse than it actually was?

Participant: That's the tension the template is designed to catch. I try to ask what a reasonable person would've concluded with only the 9 PM information, not what's obvious now that we know the release was bigger than expected. Some of it holds up under that test, some of it doesn't.

Interviewer: If the dam operator's notice had used clearly urgent language instead of standard language, would your initial call have changed?

Participant: Possibly, but it wouldn't have been the only thing driving it — I'd still have been weighing the actual gauge trend and the Director's forecast concerns alongside it.

Interviewer: And if all eight gauges had stayed online through the evacuation decision?

Participant: I'd have had a fuller picture to work with, which might have let us tighten or widen the radius with more confidence either way. Hard to say which direction it would've gone.

Interviewer: Looking back, how do you separate what was knowable in the moment from what only became clear afterward?

Participant: I lean on the template for that specifically, because otherwise it's easy to let the outcome color your memory of how clear things actually were at 9 PM. Some calls hold up, some don't, and I try not to flatten that into a single before-and-after story either way.

Interviewer: That's a good place to stop. Thanks for walking through this.

Participant: No problem.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Ambigious_7}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Emergency Operations Center (EOC) Situation Unit Analyst}}"
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
