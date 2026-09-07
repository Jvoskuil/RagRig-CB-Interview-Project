You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable having this conversation recorded and used for training analysis purposes only, no names attached to the write-up.

Participant: Yeah, that's fine, I've done these debriefs before.

Interviewer: Great. Can you tell me a bit about your background as a harbor pilot?

Participant: Sixteen years piloting on this river system, mostly deep-draft container and bulk carriers. I've taken vessels the size of the Kalliopi up to Berth 7 probably a hundred times.

Interviewer: Let's talk about this particular transit. Can you walk me through what you knew before you even boarded?

Participant: Sure. It was a fully loaded container ship, about 300 meters, drawing 14.2 meters. Port control had sent over the passage plan that morning built around the tide table, which gave us roughly 1.2 meters of under-keel clearance at our planned transit time. That's tight, but it's within what we consider workable for that stretch. We had a closing tidal window, maybe ninety minutes to get up to the berth before the margin got too thin. Two tugs were assigned, wind was forecast around 15 knots picking up through the afternoon.

Interviewer: What made this one feel nonroutine compared to a typical run up that channel?

Participant: A few things stacked up. There was a barge moored tighter to the bend than charted, one of our tugs got delayed at the pilot station, and the wind ended up running a bit hotter than forecast. None of those alone would worry me much, but together they made it a transit where I was managing multiple moving pieces instead of just following the plan.

Interviewer: Let's reconstruct the sequence. What happened right after you boarded?

Participant: I went up to the conning position, confirmed the passage plan with the master, checked the draft survey again, and we started the transit close to the planned time. Not long after we got underway, an outbound pilot radioed in a fresh echo sounder sweep from near kilometer four, saying he was seeing less water than expected there, something closer to 0.7 meters of clearance instead of the 1.2 we'd planned around. Around the same time, VTS mentioned the tide gauge was reading a slightly slower rise than the table predicted.

Interviewer: How did that develop as you continued?

Participant: We kept going. Then approaching the bend, VTS told us the barge hadn't moved despite requests, so I had to adjust our track. After that, the wind picked up faster than forecast right as we were down to one tug made fast, with the second one still twenty minutes out. Near the berth, a cross-current pushed us off line during the final approach, and we had to correct with the tugs we had by then.

Interviewer: Let's go through each of those in turn. Starting with the clearance question after the outbound pilot's report — what were you weighing at that moment?

Participant: I had the morning tide table figure in hand, which I trust because it comes from the same source we use every day and it's usually solid. Then I had this one radio report from another pilot's sounding. My read was that a single sweep from someone else's vessel isn't necessarily apples to apples with our draft and trim, so I didn't see it as something that overrode the passage plan. The tide gauge lag was a few centimeters, not dramatic on its own.

Interviewer: What alternatives did you actually consider there?

Participant: Delaying about forty minutes to let the tide build more before we hit that stretch, or slowing down and shifting toward the deeper side of the channel. Both were on the table. I chose to hold our timing and proceed as planned, treating the 1.2 as still the number that mattered.

Interviewer: What made you settle on that instead of recalculating with the new sounding and the slower tide rise together?

Participant: Honestly, the original number felt like the anchor point for the whole plan, it had already been checked by port control, and one radio call didn't feel like enough to unwind that. In hindsight I probably could have asked for a second sounding or run our own check before committing, but at the time it felt like the tide table was the more reliable reference.

Interviewer: How confident were you in that judgment in the moment?

Participant: Reasonably confident, maybe seven out of ten. Not fully certain, but confident enough not to change course.

Interviewer: Moving to the barge near the bend — what options did you weigh there?

Participant: I could push VTS harder for an emergency move, slow down and favor the wider side, or hold position until it cleared. I went with slowing down and shifting track because waiting would have eaten into our tidal window, and pushing VTS wasn't going to get the barge moved fast enough anyway.

Interviewer: How much time did you have to decide?

Participant: A couple of minutes, maybe less. Enough to make a deliberate call but not to sit and debate it.

Interviewer: Next, the tug situation with rising wind. What was going through your mind?

Participant: With only one tug fast and the second still well out, and gusts running above forecast, I didn't like relying purely on the bow thruster given our draft. When I heard a harbor tug not originally assigned was nearby, I asked for that one instead of waiting on our delayed second tug. It came down to getting extra help sooner rather than sticking with the original assignment.

Interviewer: Was there a moment you considered just waiting it out?

Participant: Briefly, yes. But wind was trending the wrong direction, and I'd rather bring in help early than get caught short later.

Interviewer: And the final approach, with the cross-current pushing you off line?

Participant: By then we had both tugs fast. I chose a graduated correction rather than aborting, applying tug and thruster power progressively and watching how she responded. Aborting and circling was an option, but I judged we had enough room and control authority to correct in place.

Interviewer: What made continuing feel safer than aborting?

Participant: The response to the first pushes of tug power told me we had steerage and margin. If that correction hadn't taken hold quickly, I would have aborted. It ended up tighter to the neighboring berth than I'd like, but within what the berth operator confirmed was workable for mooring.

Interviewer: Looking back at the whole transit, if the echo sounder report had reached you before you left the pilot station instead of mid-transit, would your timing decision have gone differently?

Participant: Possibly. Getting it earlier, alongside the tide gauge lag, together rather than as two separate small inputs, might have pushed me toward the delay option. Mid-transit, each piece came in isolated and didn't feel like enough on its own to override a plan that was already running.

Interviewer: If the second tug had arrived on schedule, would the bend or berthing approach have gone differently?

Participant: The bend, not much, that was really about the barge and speed. The berthing correction might have felt less tight, since we'd have had both tugs earlier rather than picking up the harbor tug as a stand-in.

Interviewer: Is there a point where, in retrospect, you might have weighted new information more heavily?

Participant: Probably the clearance question early on. I leaned on the original figure because it had already been vetted, and I discounted the fresh sounding a bit more than I probably should have.

Interviewer: What would you tell a less experienced pilot to watch for in a transit like this?

Participant: Don't let the plan you walked in with carry more weight just because it came first. New readings, even partial ones, deserve a real second look, not just a quick mental check against what you already believe.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MO_Biased_1}}",
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
