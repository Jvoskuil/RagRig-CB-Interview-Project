You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down with me. Just to confirm, you're okay with this being recorded for training analysis, no names attached?

Participant: Yes, that's fine.

Interviewer: Could you give me a quick sense of your background?

Participant: Sixteen years piloting on this river system, mostly deep-draft container and bulk carriers. I've taken vessels the size of the Kalliopi up to Berth 7 probably a hundred times.

Interviewer: Let's talk through this particular transit. What did you know before boarding?

Participant: It was a fully loaded container ship, about 300 meters, drawing 14.2 meters. Port control had sent the passage plan that morning built around the tide table, giving roughly 1.2 meters of under-keel clearance at our planned transit time. That's tight but workable for that stretch under normal conditions. We had a closing tidal window, maybe ninety minutes, two tugs assigned, and wind forecast around 15 knots picking up through the afternoon.

Interviewer: What made this one feel nonroutine?

Participant: A few things stacked up together. A barge was moored tighter to the bend than charted, one of our tugs got delayed at the pilot station, and the wind ended up running hotter than forecast. Individually those are manageable. Together, they meant I was reassessing constantly instead of just running the plan as written.

Interviewer: Walk me through what happened after you boarded.

Participant: I went up to the conning position, confirmed the plan with the master, checked the draft survey again, and we got underway close to schedule. Shortly after, an outbound pilot radioed a fresh echo sounder sweep from near kilometer four, reporting less water than expected, closer to 0.7 meters instead of the 1.2 we'd planned around. Around the same time, VTS mentioned the tide gauge was reading a slower rise than the table predicted.

Interviewer: How did things develop from there?

Participant: Approaching the bend, VTS told us the barge hadn't moved despite requests, so I adjusted our track. Then the wind picked up faster than forecast right as we were down to one tug made fast, with the second still twenty minutes out. Near the berth, a cross-current pushed us off line during final approach, and we corrected with the tugs we had by then.

Interviewer: Let's take these one at a time. Starting with the clearance question after the outbound pilot's report — what were you actually weighing?

Participant: I had the morning tide table figure, and now a fresh sounding plus a tide gauge trend running slower than predicted. I didn't want to just discount either one. I asked the master to run our own echo sounder sweep as we approached that stretch to see what we were actually reading under our own hull, since the outbound vessel's trim and draft weren't identical to ours. That came back closer to the outbound pilot's number than the original table, maybe 0.8 to 0.9 meters once I accounted for our squat at the speed we were making.

Interviewer: So how did that change your plan?

Participant: I cut speed to reduce squat and shifted our track toward the deeper water on the outer edge of that stretch. Combined, cutting speed and hugging the deeper line got our effective margin back to something I was comfortable with, without needing to blow the tidal window with a full delay.

Interviewer: Did you consider just holding the original timing, or delaying instead?

Participant: Both were on the table. Holding the original timing didn't sit right once we had two independent readings pointing the same direction. A full forty-minute delay was the safer extreme, but I judged that speed and track adjustment addressed the actual shortfall without sacrificing the window. It was closer than I like, honestly, maybe a six out of ten on confidence, but it was based on our own numbers, not just the forecast.

Interviewer: Moving to the barge near the bend, what options did you weigh?

Participant: Push VTS harder for an emergency move, slow down and favor the wider side, or hold position until it cleared. I went with slowing and shifting track because waiting would have eaten into the window we'd already tightened up, and pushing VTS wasn't going to move the barge fast enough anyway.

Interviewer: How much time did you have to decide?

Participant: A couple of minutes. Enough to make a deliberate call, not enough to sit and debate it.

Interviewer: Next, the tug situation with rising wind.

Participant: With only one tug fast and the second still well out, and gusts running above forecast, I didn't want to rely purely on the bow thruster given our draft. When I heard a harbor tug not originally assigned was nearby, I requested that one instead of waiting on our delayed second tug. Getting help sooner mattered more than sticking with the original assignment.

Interviewer: Was waiting ever seriously on the table?

Participant: Briefly, yes, but the wind was trending the wrong way, and bringing in help early felt like the safer bet.

Interviewer: And the final approach, with the cross-current?

Participant: By then both tugs were fast. I chose a graduated correction rather than aborting, applying tug and thruster power progressively and watching the response. If that hadn't taken hold quickly, I would have aborted and circled. It ended up tighter to the neighboring berth than I'd like, but within what the berth operator confirmed was workable.

Interviewer: What made continuing feel safer than aborting?

Participant: The initial response to tug power told me we had steerage and margin. That's really the deciding factor in the moment, how she responds to the first correction.

Interviewer: Looking back, if the echo sounder report had reached you before you even left the pilot station, would your approach have changed?

Participant: Possibly less improvisation involved. I'd have built the speed reduction and track shift into the plan from the start rather than adjusting mid-transit. The outcome likely would have been similar, just calculated earlier with more margin to plan around.

Interviewer: If the second tug had arrived on schedule, would the bend or the berthing approach have gone differently?

Participant: The bend, not much, that was about the barge and speed. The berthing correction might have felt less tight, since we'd have had both tugs from the start rather than bringing in a substitute.

Interviewer: Anything you'd have wanted to know sooner?

Participant: I'd have liked our own sounding data earlier rather than relying on someone else's reading first. That's really a sequencing issue, not a judgment one.

Interviewer: What would you tell a less experienced pilot about a transit like this?

Participant: Don't treat any single number, old or new, as final. Cross-check it against your own instruments when the margin is tight enough to matter, and build your track and speed decisions around what you can verify yourself.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MO_Vocab_Control_1}}",
  "occupational_domain": "{{Maritime Operations}}",
  "role": "{{Harbor Pilot / Marine Pilot}}"
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
