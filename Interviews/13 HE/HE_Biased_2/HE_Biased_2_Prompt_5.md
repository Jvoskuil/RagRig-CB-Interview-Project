You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down for this. This is voluntary, and I'm interested in your reasoning process, not in re-grading your final report. Can you give me your role and background?

Participant: Sure. Certified fire investigator, IAAI-CFI, eleven years doing origin and cause, mostly commercial buildings. Six years on suppression before that.

Interviewer: Good. Tell me about the incident. What did you see and hear when you first arrived?

Participant: Two-story mixed-use building—café downstairs, apartment above. Fire was already knocked down. The rear of the ground floor, dry storage plus part of the kitchen, had a partial ceiling collapse. The electrical panel sat on the wall maybe eight feet from the fryer exhaust duct. Suppression crew said they hit heavy smoke logging before they even got through the back door, so it had clearly been burning a while in low oxygen before anyone noticed. That matters because ventilation-limited burning smears your pattern reading—you don't get one clean V-pattern pointing at a single spot. The whole back room was charred fairly evenly, top to bottom, which made the visual read genuinely hard.

Interviewer: What was your objective going in?

Participant: Defensible origin and cause, NFPA 921 methodology, systematic elimination of ignition sources, all documented well enough to survive insurer and possibly legal scrutiny. And we had the clock running—48 hours before the demolition permit kicked in.

Interviewer: Walk me through the sequence, start to finish.

Participant: Scene photography and assessment first. Then excavation, starting in the rear zone since that's where the damage was worst. Within that zone I had to pick which side to dig into first, panel or fryer. Then witness statements came in and I had to fold those into a timeline that didn't quite match the dispatch log. Then a hard resource call—only one component could go out for full lab testing before demolition. And finally the report had to go out with whatever I had, on deadline.

Interviewer: Let's take the excavation order first. What led you to start where you did?

Participant: The panel breaker had visually severe heat damage, that's true. But honestly, what really settled it for me was that this whole setup—panel right next to a grease-heavy kitchen zone, older wiring—reminded me hard of a case I worked maybe four years back where a corroded panel connection took out a similar back-of-house area. That case stuck with me. So when I saw this layout, my gut said panel, and I went with the panel side first.

Interviewer: Even though the fryer wiring showed comparable damage and that zone had a higher fuel load and heavier daily use?

Participant: Yeah, and if you'd asked me to lay it out purely on the numbers—damage severity, fuel load, use frequency—it's closer than I probably made it sound at the time. But it felt like the same shape of fire I'd already solved once, so panel got my attention first. I'll grant that's not purely evidence-driven; it's partly this one felt familiar.

Interviewer: Let's move to the witness accounts. What exactly did the tenant tell you?

Participant: She said she smelled an electrical, burning-plastic odor about twenty minutes before she saw flame—and she also mentioned catching a flicker, like a spark, near where the panel is, before the smell really set in. That's a strong data point pointing at the panel.

Interviewer: I want to check that against what you told me earlier, when we first logged her statement—you described it then as smell only, no visual detail. Can you help me reconcile that?

Participant: Huh. You're right, that's how I noted it initially—smell only. I'm... now second-guessing whether she actually said "flicker" to me directly, or whether that's something I pieced together afterward from the panel damage and just started saying it as if she'd told me. It's possible I filled that in without meaning to. I don't think I did it on purpose, but sitting here, I can't swear the flicker detail came from her and not from my own read of the scene.

Interviewer: That's helpful to flag. How did the employee's account factor in?

Participant: He said the fryer had been left on, unattended, longer than usual before closing. Neither his estimate nor the tenant's matched the 911 log precisely—people misjudge time under stress, that's normal. I logged both as provisional. I didn't have a strong basis to fully trust one over the other independent of physical evidence.

Interviewer: Third decision point—the lab retention call, since you could only send one component out.

Participant: Right, demolition was scheduled, budget only covered one full forensic workup. Panel breaker or fryer control assembly. The utility inspector had given me an informal, not-yet-written read that leaned panel. I weighed that against the fryer component's condition, which was also degradable enough to still be informative. I picked the panel breaker. I considered asking for a deadline extension to save both, but the insurer pushed back hard, and waiting risked losing both to further collapse anyway.

Interviewer: What would have made you send the fryer assembly instead?

Participant: Clear independent radiating burn patterns from the appliance itself. It wasn't a toss-up, but it wasn't locked in either.

Interviewer: Last point—the final classification under deadline.

Participant: With no new evidence coming and the clock out, I had three options: determinate finding, undetermined pending lab results, or a conditional finding naming both with relative likelihood. I went conditional—panel fault primary, fryer malfunction as a documented secondary possibility. A hard determinate call felt premature since the fryer possibility wasn't eliminated, and "undetermined" felt like it undersold the direction the pattern evidence and the inspector's preliminary read were pointing.

Interviewer: What single piece of missing evidence would have most changed your confidence?

Participant: Independent lab results on both components. Losing the fryer assembly to demolition is the one thing I'd redo—push harder for even partial preservation.

Interviewer: If the witness timestamps had matched the dispatch log exactly, would your timeline weighting have differed?

Participant: Probably, yeah—I'd have leaned into whichever account lined up and trusted it more as an anchor point instead of treating both as soft.

Interviewer: How much of your final call would you attribute to prior cases versus this case's own evidence?

Participant: I'd like to say it was mostly this case. Looking back at how I've described a couple of these steps to you, though, I think the prior case did more work in my head than I'd have said if you'd asked me that on day one—especially early on, before the excavation even really got going.

Interviewer: Anything you'd flag for someone reviewing this file cold?

Participant: That the ambiguity was real, and that at least one detail I reported to you about the tenant's statement needs to be double-checked against her actual recorded interview before it goes in the file as fact.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Biased_2}}",
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
