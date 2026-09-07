You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, just to confirm — this is a routine debrief for our operational learning file, not a disciplinary review, and you're free to skip anything you'd rather not detail. Can you tell me your role and how long you've been dispatching?

Participant: Sure, no problem. I'm a Flight Operations Officer, licensed dispatcher, coming up on nine years now, mostly widebody long-haul. I hold joint responsibility with the captain for the flight release, so I'm in it from planning through landing.

Interviewer: Good. Let's start broad — walk me through the flight and what your objective was going in.

Participant: This was an overnight JFK to Lisbon rotation, widebody twin. My job was to build a release that was compliant and reasonably efficient — right fuel, right alternate, nothing wasteful, but enough margin to cover the weather picture. Going into the shift I already knew the aircraft had an APU write-up, deferred under the MEL, so anywhere we might divert needed ground power support, not just a runway. That constraint shaped everything downstream.

Interviewer: What was the weather picture at that point?

Participant: The 0300Z TAF for Lisbon showed some morning visibility restriction, fairly typical coastal fog, but forecast to lift comfortably before our arrival window. Porto looked like the natural alternate — good runway, and their ground power unit was listed as available until 0500 local, which covered our arrival plus buffer. I built the release off that TAF: standard alternate fuel, contingency, reserve. It matched policy, so I didn't see a reason to load extra gas or chase a second alternate. I remember thinking the numbers were clean and moving on to the next release in the queue — it was a busy overnight bank.

Interviewer: Once the flight departed, how did things unfold?

Participant: Fairly normal until a few hours in. An amended TAF came through showing the fog setting in about two hours earlier than the original forecast had it. I pulled up the model guidance to sanity-check it. One run still showed the improving trend consistent with what I'd already briefed the crew. Another run, plus a PIREP from an aircraft that had landed there not long before, pointed to a slower burn-off, worse than forecast. Then later, closer to descent, the crew asked me directly for a fresh read on continue-versus-divert risk, and I answered that using the fuel picture. Finally at top of descent, with visibility sitting right at minima and the Porto GPU window closing, I gave a continue recommendation. There was a short hold near the bottom before it worked out, but we landed at Lisbon without further incident.

Interviewer: Let's rebuild that chronologically. What information did you have at each stage, in order?

Participant: Release time: early TAF, MEL constraint, alternate fuel policy. A couple hours later: amended TAF plus two competing model runs and a PIREP. Later still, maybe ninety minutes from arrival: extended satellite imagery, more METARs from stations around Lisbon, current fuel state, and updated word on the Porto GPU cutoff. Then at top of descent: live visibility trend, the closing GPU window, and the crew wanting a straight answer.

Interviewer: Let's take the first decision — building the release. What alternatives did you weigh?

Participant: Really it was between releasing on the minimum required fuel and alternate per the early TAF, or padding it — extra fuel, maybe a second alternate with round-the-clock power, given there was a fog signature in the picture at all.

Interviewer: What made you go with the minimum?

Participant: The TAF I had in front of me supported it, and Porto's GPU window comfortably covered our ETA. Once that release was built, honestly, that became my working number for the rest of the watch — the later checks I did were more about confirming that figure still held rather than starting over and asking whether a completely different fuel or alternate plan made more sense from scratch.

Interviewer: When the amended TAF and the conflicting model/PIREP data came in, how did you handle that?

Participant: I looked at both. The model that lined up with the trend I'd already briefed felt more current and more consistent with what we'd been seeing on other flights that shift, so I leaned on that one. The PIREP was useful, but a single pilot report felt like one data point against a fuller model picture, so I passed the update to the crew framed around the improving trend, noting the other read existed but wasn't the lead story.

Interviewer: Did you consider weighting the PIREP and the slower-recovery model more heavily?

Participant: I considered it, yeah. It just didn't feel like enough on its own to justify walking back guidance I'd already given the crew.

Interviewer: Move to the point where the crew asked for a fresh risk read. What did you do with the imagery and extra METARs?

Participant: I went through the extended satellite loop pretty carefully, plus the nearby METARs, spent real time on it. It gave me a fuller picture and I felt more settled afterward. Looking back, I think I was treating the sheer amount of data as if working through more of it would settle the call on its own — but the extra loop and those additional METARs were really just repeating the same broad trend I already had, and there wasn't a specific reading in any of them that was ever going to flip the recommendation one way or the other.

Interviewer: And how did you answer their risk question specifically?

Participant: They'd asked something broader — basically, is continuing to Lisbon versus setting up for Porto still the right call given the MEL and the visibility trend. I answered mostly with the fuel numbers — we had healthy reserves, well above minimums, comfortable margin to hold if needed. That's a real and necessary part of the answer. Whether I fully separated out the visibility-and-GPU-window piece as its own question, distinct from just "do we have gas," I'm less sure about now.

Interviewer: Last decision — top of descent, visibility near minima, GPU window closing. What tipped you to continue rather than divert?

Participant: The remaining fuel and time margin still looked workable, and the plan all along had been Lisbon with Porto as backup if things really fell apart. Diverting felt like abandoning a plan that had held up reasonably well to that point, and the numbers on paper still supported continuing. I recommended continue.

Interviewer: How confident were you at that moment?

Participant: Genuinely, moderately confident, not fully. There was real uncertainty in that visibility trend.

Interviewer: How did that get reflected afterward, say in the operations log?

Participant: I wrote it up fairly cleanly — noted that conditions supported continuing to Lisbon and that the fuel plan held throughout. Reading it back now, it reads a bit more settled than it actually felt in the moment.

Interviewer: If the PIREP and slower model had arrived before you finalized the release, would anything have changed?

Participant: Possibly the alternate fuel load, yes. Hard to say for certain.

Interviewer: If the GPU cutoff had been flagged an hour earlier than it was, what would you have done differently at top of descent?

Participant: That probably shifts the divert case earlier — that window was really the tightest constraint in the whole picture.

Interviewer: Anything you'd tell a newer dispatcher about a night like this?

Participant: Keep re-asking the actual question being asked, not just the easiest piece of it, and don't let your first number quietly become the only number you're checking against.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{AV_Biased_6}}",
  "occupational_domain": "{{Aviation}}",
  "role": "{{Flight Dispatcher / Flight Operations Officer}}"
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
