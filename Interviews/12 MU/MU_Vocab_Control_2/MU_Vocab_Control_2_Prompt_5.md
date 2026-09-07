You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our internal learning review, not a disciplinary process — anything you share helps us understand decision-making under uncertainty, not to assign blame. Can you start by telling me your role and what you were responsible for during this incident?

**Participant:** Sure. I'm the ground control specialist for the site — geotech engineer by training. I cover support design, monitoring interpretation, and sign-off on ground conditions for active headings. During this shift I was working from the surface office but on call for anything flagged at the 4200 development face and the adjacent bolted heading next to it.

**Interviewer:** Good. Before we get into specifics, can you give me a general account of what happened, start to finish?

**Participant:** It started with a call from the shift boss — minor rib spalling near the 4200 face, right after a blast, with a bit of dust puffing off the wall. Nobody was hurt, the crew paused on their own. Our extensometer near that face had been down for about two days — the bolting rig had knocked the cable loose — so I didn't have fresh convergence numbers for that specific spot. That gap mattered to me; I flagged it as something we'd need to close before I could really trust any read on that area. I also had the 3800 panel in the back of my mind — a similar-looking spalling event about six months earlier that we'd traced to aggressive undercutting by the operator at the time. But I didn't want to lean on that too hard, since one analogy from a different crew and a different round doesn't tell you much about stress conditions here. I authorized continued mucking with a visual check, treating both the operator-technique angle and the possibility of something geological as open questions.

A bit later the scaling crew called in bigger slabs than first described, plus a hairline fracture pattern we hadn't logged. We're roughly fifteen to twenty meters from a mapped fault splay there, though the exact position is fuzzy. I ran our convergence model using the nearest working stations, which weren't right at the face. It came back with a low displacement forecast, but the technician reminded me the model's calibration came from a different rock mass domain, so I didn't take the number at face value — I discounted it and tied continuing the round to a specific follow-up scaling check afterward.

After the round, spalling showed up in the adjacent bolted heading too. The shift boss asked about mesh and bolts before the next rotation, and the mine manager flagged the schedule hit. I treated the second location as new information rather than just an extension of what I already believed, so I ordered spot bolts at the fracture and a targeted scaling check instead of either a full upgrade or a full deferral. A couple hours later a crack opened along a bolt row. The technician wanted immediate evacuation. I authorized a restricted, technician-accompanied entry instead of routine access, since I didn't think the crack could just be read as more of the same. Not long after, we had a larger fall in that section. No one was hurt — an unrelated alarm cleared people out just before it happened — but it could have gone differently.

**Interviewer:** Let's reconstruct the timeline a bit more precisely. What exactly did you know at the moment of that first call?

**Participant:** Just the spalling, the dust, no injuries, crew stopped on their own. And that our monitoring near that face was blind because of the extensometer outage — that was very much on my mind, not something I set aside.

**Interviewer:** And after the scaling crew's second report?

**Participant:** That's when the picture got more complicated — bigger slabs, a fracture pattern, and the fault splay proximity became more relevant. It pushed me to actually run the model rather than rely on judgment alone.

**Interviewer:** When did you first pull up the convergence model output, and what did you do with it?

**Participant:** Right after that second report. I wanted a second line of evidence, but I went in already expecting to have to adjust for the domain mismatch.

**Interviewer:** Walk me through the gap between finishing the round and the evacuation call.

**Participant:** Round finished, spalling in the adjacent heading came up, I ordered the spot check rather than closing the question either way, then the crack appeared maybe two hours later, and the technician pushed for evacuation almost immediately after that.

**Interviewer:** Let's go through the first decision — authorizing continued mucking. What alternatives did you weigh?

**Participant:** Stopping everything for a full inspection, or restricting a buffer zone and resequencing the round. I went with the visual-check option, but I didn't treat it as a closed case.

**Interviewer:** How did you weigh the 3800 comparison against the missing extensometer data?

**Participant:** I tried to hold both at once. The 3800 case gave me one plausible read, but the missing monitoring meant I genuinely didn't know what the ground was doing locally, and I didn't want that gap to just disappear because I had a tidier story available. I made a point of telling the shift boss I wanted that extensometer back online as soon as the rig work allowed.

**Interviewer:** Second decision — using the convergence model output to justify finishing the round. How did you decide how much weight to give it?

**Participant:** Given the domain mismatch the technician flagged, I didn't treat the low-displacement number as decisive on its own — more as one data point that shifted my confidence somewhat, conditional on a scaling check afterward. If that check had come back worse, I'd have stopped regardless of what the model said.

**Interviewer:** What was the technician's concern, specifically, and how did you incorporate it?

**Participant:** She said the model's calibration came from a different rock mass domain and might not transfer well this close to the fault splay. I built that into how much I let the forecast move my decision — I leaned on it less than I would have on a panel where I trusted the calibration fit.

**Interviewer:** Third decision — the adjacent heading. What led you to the spot-check option rather than a full upgrade or a full deferral?

**Participant:** The new location mattered to me — it wasn't just the same spalling showing up again, it was a second area behaving in a way the earlier forecast hadn't covered. A full deferral felt like ignoring that; a full upgrade felt premature without more specific data on where the fracture actually was. The spot bolts and scaling check were a way to act on the new information without overcommitting either direction.

**Interviewer:** What would have changed that decision?

**Participant:** Fresh convergence readings right at that heading, or if the crack had shown up before I made the call instead of after.

**Interviewer:** Fourth decision — allowing entry after the crack appeared. What was your reasoning?

**Participant:** The model hadn't been rerun with the crack data, so I didn't extend the earlier forecast to cover it — that felt like a different question. I authorized a restricted entry with the technician present rather than routine access, treating the crack as something we still needed to understand rather than something already explained by what we'd seen at the face.

**Interviewer:** How much did time pressure factor into that specific call?

**Participant:** A fair amount. The next crew was due within the hour, and a full lockout would have meant a second schedule hit in one shift. That pressure was real, but it's why I restricted the entry rather than just clearing it outright.

**Interviewer:** Looking back, if the extensometer had been working the entire time, do you think your decisions would have gone differently?

**Participant:** Probably at the first and third points especially. Real numbers instead of partial analogies and adjusted model output would have given me something firmer to act on earlier.

**Interviewer:** And if the 3800 investigation had reached a different conclusion — say it had been traced to stress redistribution near a geological structure instead of operator technique — do you think you'd have read this situation differently?

**Participant:** Maybe somewhat, but I'd hope I'd still have tried to treat it as one data point rather than the deciding factor, given how different the local conditions were here.

**Interviewer:** Last one — what would you do differently if a similar sequence came in again?

**Participant:** Push even harder to get monitoring restored before any round decision, and probably formalize the follow-up conditions I attach to model output, rather than keeping them informal in my own head.

**Interviewer:** That's really helpful detail. Thanks for walking through it so openly.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MU_Vocab_Control_2}}",
  "occupational_domain": "{{Mining and underground industrial operations}}",
  "role": "{{Geotechnical Engineer / Ground Control Specialist}}"
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
