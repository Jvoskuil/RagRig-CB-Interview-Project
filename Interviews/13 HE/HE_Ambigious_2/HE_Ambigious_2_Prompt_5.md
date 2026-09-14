You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary cognitive task analysis session—I'm interested in how you actually reasoned through the case, not in evaluating your final report. You can decline to answer anything. Can you state your role and certification background briefly?

Participant: Sure. I'm a certified fire investigator, IAAI-CFI, been doing origin and cause work for about eleven years, mostly commercial and mixed-use structures. Before that I was on the suppression side for six years.

Interviewer: Good. Let's start with the incident itself. Walk me through what you saw and were told when you first arrived on scene.

Participant: This was a two-story building, café on the ground floor, an apartment above. Fire had been knocked down by the time I got there, moderate involvement, but the rear of the building—dry storage and part of the kitchen—had a partial ceiling collapse. The electrical panel was mounted on the wall right next to that storage room, maybe eight feet from the fryer exhaust duct. Suppression crew told me they'd hit heavy smoke logging before they even got through the back door, which tells you it had been burning a while in a low-oxygen environment before anyone noticed. That's important because ventilation-limited burning distorts your pattern reading—you don't get a clean V-pattern pointing straight at an origin. Everything in that back room was charred fairly evenly, high up and low down, which made the visual read ambiguous from the start.

Interviewer: What was your primary objective going in?

Participant: Get a defensible origin and cause determination that would hold up for the insurer and, if it came to it, in a legal setting. NFPA 921 methodology, systematic elimination of ignition sources, document everything. The complication here was the clock—insurer wanted the report inside 48 hours because a demolition permit was already queued.

Interviewer: Let's reconstruct the sequence. What happened first, and how did your thinking evolve?

Participant: First thing was scene assessment and photography before touching anything. Heaviest char and the collapse were both concentrated in that rear zone, so that's where excavation had to start—that part wasn't really a choice, that's just where the fire did its damage. Within that zone, though, I had two candidate sources sitting close together: the panel and the fryer. I made a call on which to excavate first. Then came witness statements, which didn't line up cleanly with each other or with the dispatch log. Then a resource constraint—I could only send one component out for full lab testing before the site got demolished. And finally, the report itself had to go out with the evidence I had, not the evidence I wished I had.

Interviewer: Let's slow down on each of those. Starting with the excavation sequence—what specific cues led you to start where you did?

Participant: I started at the panel side. The breaker for that circuit showed heat damage that looked more severe on initial visual than the fryer wiring, and panel failures are a common competent ignition source in older commercial buildings—I've seen it plenty. The alternative would have been starting at the fryer given it's a higher fuel-load area and gets heavy daily use, or splitting the crew to hit both zones at once, which we discussed and rejected because it would've thinned out documentation quality on both sides.

Interviewer: What made the panel side win out over the fryer side, given both were physically plausible?

Participant: Honestly, the visual severity tipped it, plus accessibility—the collapse debris made the fryer area harder to reach safely at that hour, so starting where we could actually work safely made practical sense too. I want to be clear, though: that sequencing decision doesn't by itself tell you which one caused the fire. Excavating one zone first is a logistics call, not a conclusion.

Interviewer: Understood. Now the witness statements. How did you weigh those against each other and against the dispatch log?

Participant: The upstairs tenant said she smelled something like burning plastic or an electrical smell roughly twenty minutes before she saw flame. The café employee said the fryer had been left on, unattended, longer than normal before closing. Neither timestamp matched the 911 log precisely—people are bad at estimating time under stress, that's just standard. I logged both accounts as provisional, flagged the discrepancy explicitly in my notes, and treated neither as more reliable than the other without physical corroboration. I didn't have a strong basis to prefer one witness's timeline over the other's at that point.

Interviewer: What would have changed that weighting for you?

Participant: If either estimate had matched the dispatch window closely, I'd have leaned into that account more. Since neither did, I kept both as soft data points, not anchors.

Interviewer: Third decision point—the lab retention call. Walk me through that.

Participant: This was the hard one. Demolition was scheduled, budget only covered forensic testing on one major component, and I had two candidates: the panel breaker or the fryer control and wiring assembly. The utility company's field inspector had looked at the panel and said, informally, that it looked consistent with an internal fault, but that wasn't a written finding yet, just his gut read on-site. I weighed that against the fryer component's condition, which was also degraded enough that lab testing could still be informative. I chose to retain the panel breaker.

Interviewer: What drove that specific choice over sending the fryer assembly instead?

Participant: A few things together—the visual severity from excavation, the utility inspector's preliminary read, and the fact that panel-related fires are something I've dealt with successfully identifying before, so I had a reasonably fast, defensible chain-of-custody process ready for that specific type of component. I did consider requesting a deadline extension to preserve both, but the insurer pushed back hard on timeline, and structurally, waiting risked losing both components to further collapse.

Interviewer: Is there a scenario where you'd have picked differently?

Participant: If the fryer had shown clearer independent ignition indicators—like burn patterns radiating from the appliance itself rather than the panel—I'd have sent that instead. It wasn't a coin flip, but it also wasn't airtight.

Interviewer: Last decision point—the final report classification under deadline.

Participant: With the clock running out and no new physical evidence expected, I had three options: issue a determinate finding, call it undetermined pending lab results, or issue a conditional finding naming both candidates with relative likelihood. I went with the conditional finding—electrical panel fault as the primary hypothesis, fryer malfunction as a documented secondary possibility—because the evidence genuinely supported more than one explanation and I didn't think forcing a single determinate answer was honest given what I actually had.

Interviewer: What alternative did you reject, and why?

Participant: I rejected calling it fully undetermined because that felt like it was underselling the pattern evidence and the inspector's preliminary read—there was more direction in the data than a blank "undetermined" would convey. I rejected a hard determinate call because the fryer possibility hadn't been eliminated, and NFPA 921 wants you to rule things out, not just pick a favorite.

Interviewer: Looking back, what single piece of missing evidence would have most changed your confidence?

Participant: Independent lab results on both components, honestly. Losing the fryer assembly to demolition is the piece I'd redo if I could—getting a deadline extension for preservation, even partial, would have mattered more than anything else.

Interviewer: How much of your final call would you attribute to prior cases versus the specifics of this one?

Participant: Mostly this case's own evidence. My experience shaped how fast I could process what I was seeing and gave me a working process for the panel component specifically, but the conditional finding came from what the debris and testimony actually showed, not from assuming this fire had to resemble something I'd seen before.

Interviewer: Anything you'd flag for someone reviewing this file cold?

Participant: Just that the ambiguity was real. Ventilation-limited burning, two plausible sources sitting close together, imperfect witness timing—none of that resolves cleanly, and I'd rather the file reflect that honestly than look more certain than the evidence actually was.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Ambigious_2}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Fire Investigator (Origin and Cause)}}"
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
