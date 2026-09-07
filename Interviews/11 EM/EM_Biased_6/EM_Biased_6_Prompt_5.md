You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief for our exercise-design case-study library — I'll be asking about a specific project you led, how the decisions actually unfolded, not whether they were "right" in hindsight. Everything stays de-identified. Sound okay?

Participant: Sure, happy to walk through it. This is the Riverbend Rising full-scale exercise, right? That one's still pretty fresh for me.

Interviewer: Exactly. Can you start by describing the assignment and what success would've looked like?

Participant: I was handed the FSE build in early spring — simulate a levee failure and flash-flood evacuation, get it HSEEP-compliant, and use it to validate EOC escalation procedures before the seasonal flood window opened. Success meant a full exercise day, a usable Controller-Evaluator handbook, and an AAR that actually told the Director something new about our capability gaps.

Interviewer: Give me the incident account — how did the project actually go, start to finish?

Participant: We'd run something similar back in 2019 — smaller footprint, two of us on it, and we mostly reused an existing scenario shell. That one took about six weeks start to finish. This time I was solo, and the scope was bigger: a brand-new levee-failure module built off updated Army Corps dam-break modeling, plus coordination across the regional EOC, the school district, and municipal police and fire. Deadline was fixed at ten weeks because of the flood-risk calendar. I scoped the build assuming it'd track pretty close to the 2019 timeline — figured I knew the process well enough to move fast. About four weeks in, I was still building the custom hydrology module and waiting on sign-off from three different agencies, and a status check showed we'd already slipped two weeks. From there it became a scramble — severity calibration with the advisory committee, a fight over which training injects we could actually finish, and a last push on the handbook right up against the deadline.

Interviewer: Let's reconstruct that chronologically. What did you know at each stage, and what changed as you learned more?

Participant: At kickoff I had the 2019 numbers in my head and the new Corps data in hand, but I hadn't yet mapped out how much longer three-agency coordination would take versus one shell reused solo. Once the schedule slipped, I knew severity calibration and the advisory committee conversation were coming up next, and I could already tell we wouldn't have time to fully build every kind of training material — so the inject decision became a resource fight. By the time I got to the handbook, the clock was the dominant fact.

Interviewer: Let's slow down on the first real decision — scoping the build timeline. Walk me through it.

Participant: Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much. I remember telling the Director I could deliver in the same general window even though I was down to one person and building the hydrology piece essentially from scratch.

Interviewer: What made you confident the compressed schedule would hold?

Participant: Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead.

Interviewer: What information would have changed that estimate?

Participant: If I'd actually broken out hours for three-agency sign-off separately instead of folding it into "coordination," I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up.

Interviewer: Still in that same phase — you also had a choice about which scenario format to build from. What drove that?

Participant: Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in.

Interviewer: Did you compare how the two formats actually performed for training outcomes?

Participant: Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure.

Interviewer: Let's move to the severity decision. What was on the table?

Participant: The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years. There was real pressure to keep the scenario grounded in something the community would find plausible.

Interviewer: How did you weigh the modeling against that history?

Participant: I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face.

Interviewer: Around that same time, you were part of an AAR review for a peer's exercise. What happened there?

Participant: Right, a planner in another county got flagged for an unrealistically mild scenario — didn't stress escalation procedures at all. In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time.

Interviewer: Did you apply the same scrutiny to your own severity choice that you applied to theirs?

Participant: Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard.

Interviewer: Third decision point — the training injects. What were the options?

Participant: We only had production time to fully build one category. Option one was photo and video clips of levee overtopping — dramatic, but slow to produce. Option two was the data packages — stream gauge readouts, GIS flow-rate shapefiles — less visually interesting but more specific for EOC modeling decisions.

Interviewer: Which did you prioritize, and why?

Participant: I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool.

Interviewer: Did you weigh how well each format supported the actual operational decisions evaluators would need to make?

Participant: Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them.

Interviewer: Last decision point — the Controller-Evaluator handbook. What went into that?

Participant: I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary.

Interviewer: Was there any indication a glossary might be needed?

Participant: There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left.

Interviewer: Looking back across all four decisions — if you'd had two more weeks, what would you have done differently?

Participant: Probably built in a real contingency buffer up front instead of assuming the old timeline would hold, and maybe split production time more evenly between the visual and data injects.

Interviewer: And if a different planner had taken over halfway through?

Participant: They might have pushed harder on the severity call, given the modeling was pretty clear. And they might not have carried the same assumptions I had about what "obvious" means in the handbook, since they wouldn't have fifteen years of the same habits behind them.

Interviewer: Anything you'd flag as uncertain even now?

Participant: Whether the milder scenario actually undercut the escalation testing, or whether it was just a rough exercise day for other reasons — I genuinely don't know. Same with the handbook; the scoring inconsistencies could've come from a dozen things, not just the shorthand.

Interviewer: That's a good place to stop. Thanks for the detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Biased_6}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Emergency Preparedness Curriculum Designer / Exercise Planner}}"
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
