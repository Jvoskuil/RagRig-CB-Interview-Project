You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a review of decision-making processes during watch operations, not for any disciplinary purpose. Is that okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me a bit about your role and what you were responsible for monitoring that evening?

Participant: Sure. I was on console for the approach channel, so my job was traffic separation through the narrows — sequencing inbound and outbound vessels, keeping an eye on anything that didn't fit the normal pattern, and coordinating with pilots on larger transits. That evening we had a crude tanker inbound under pilotage, and it was right around dusk, so visibility was starting to get patchy with some fog banks rolling through. My main objective was just making sure the tanker had a clean run through the bend within its tidal window, since that channel doesn't give you much room to maneuver once you're committed.

Interviewer: Okay. Walk me through what happened, from when things started to become unusual.

Participant: About forty minutes before the tanker was due at the bend, I picked up a small contact near there — slow track, kind of wandering. AIS class B tagged it as a local fishing vessel, one that's licensed to work that area, so my first read was that it was probably setting or hauling gear. That's a pretty common sight in that spot, especially in the evening. The radar was showing some inconsistent course data on it, near-zero speed at some points, but with the sea state kicking up a bit of clutter, small-target tracking isn't always clean, so I didn't put much weight on that at first. No distress call, nothing on the radio suggesting trouble, so I logged it as routine and kept my main attention on the tanker's progress.

Interviewer: What happened after that?

Participant: About ten minutes later I noticed the track had drifted a bit further toward the centerline than I'd expect from a boat working gear in that area, and there was a short burst on the radio from around that frequency, but it was garbled — couldn't make out any content. Around then my shift supervisor came on for handover and looked at the display with me. He'd worked that stretch for years and said straight off that this looked typical for that vessel, that he'd seen this exact drift pattern before with boats working that bend. My colleague on the next console glanced over and mentioned the track looked a little off to her, but didn't push it further, and we moved on with finishing the handover log. Then, as the tanker got closer to the tidal cutoff, the supervisor turned to me and framed it as, essentially, are we going to lose the tide window over this or not. I proceeded with the transit as scheduled. Afterward, once the tanker had cleared and things settled, we found the fishing vessel was completely stationary and not answering hails, so I put out a general advisory. Turned out later it had a fouled propeller and needed a tow.

Interviewer: Let's reconstruct that a bit more carefully. Starting with your very first read on the contact — what specific cues led you to call it routine fishing activity?

Participant: Mainly the AIS tag. It came up as a class B unit registered to a fishing vessel we see in that area fairly often, so that matched what I'd expect to see there at that hour. I did notice the COG data wasn't fully consistent with active maneuvering, but I chalked that up to the clutter — that channel gets noisy on radar with any chop, and small targets bounce around in the plot all the time.

Interviewer: Did you go back and check the COG pattern again once you'd made that initial call?

Participant: Not specifically, no. Once I had a plausible explanation for it, my attention went back to the tanker's progress, since that was the higher-priority track at that point.

Interviewer: What alternatives did you consider at that moment?

Participant: I could have hailed the vessel directly on VHF to check status, or just flagged it for tighter radar tracking without contacting them. I didn't do either right away — with no distress call and the AIS type matching, it didn't seem urgent enough to prioritize over the tanker sequencing.

Interviewer: Moving to the handover — tell me more about that conversation with your supervisor and colleague.

Participant: He came on, looked at the plot, and said it looked like the same pattern he'd seen from that boat before — kind of a lazy drift while gear's out. He said it with a lot of confidence, and honestly that matched my own initial read too, so it didn't feel like there was much to question. My colleague said something like "that track looks a little odd" but didn't really elaborate, and nobody asked her to say more. We closed out the handover log with a "no action required" note on that contact.

Interviewer: Did anyone suggest getting an independent re-plot or double-checking the radar data before finalizing that note?

Participant: No, not really. It felt like a fairly settled read at that point, given his experience with that specific vessel.

Interviewer: When the tanker was about fifteen minutes from the bend, how did the decision to proceed take shape?

Participant: That's when my supervisor turned it into a scheduling question — asked whether holding for this would cost us the tide window. Once he framed it that way, the conversation was mostly about whether the delay was worth it, since missing that window would push the tanker's transit back a full cycle. Holding to confirm the fishing vessel's status would almost certainly have meant losing the window.

Interviewer: Was there a point where you weighed the safety margin on its own, separate from the schedule question?

Participant: I think I mostly folded it into the same conversation — the tide window was the thing driving the urgency, so that's the lens I was looking at it through. In hindsight I can see how that shaped which options felt realistic.

Interviewer: What alternatives were on the table there?

Participant: Holding the tanker outside the channel, advising the pilot to slow down and open up the CPA a bit while still proceeding, or just going ahead as scheduled. I went with proceeding as scheduled, given the tide constraint.

Interviewer: And the final decision, after the tanker had cleared and the fishing vessel was found stationary and not responding — how did you land on issuing the advisory?

Participant: At that point the immediate encounter was already resolved, but there was another inbound vessel due within the hour, so I weighed that residual risk against the fact that the current situation had cleared without incident. I decided the advisory was worth it given the upcoming traffic, even though nothing bad had actually happened yet.

Interviewer: How much time pressure did you feel across these decisions?

Participant: The tide window created real pressure during that middle stretch. The final advisory call felt calmer, more like a standard judgment call with time to think it through.

Interviewer: If you'd gotten a clean, confirmed COG reading right at the start, would anything have changed?

Participant: Probably — if it had clearly shown no active movement at all, I likely would've tried to raise them on the radio much earlier instead of letting it ride.

Interviewer: Looking back, if your colleague had pushed harder on that "looks odd" comment, do you think it would have changed the outcome?

Participant: Possibly. If she'd said more specifically what she was seeing, it might have prompted another look at the plot before we closed the handover.

Interviewer: And if the tide-window question had been framed differently — say, purely as a safety check rather than a scheduling one — do you think you'd have weighed the options differently?

Participant: That's a fair point. I might have leaned more toward slowing the pilot down or holding briefly, if the conversation had started from the risk side rather than the schedule side.

Interviewer: Anything you'd want to do differently if this came up again?

Participant: I'd probably push for a direct radio check earlier, before letting an initial read sit unchallenged for too long.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{MO_Biased_3}}",
  "occupational_domain": "{{Maritime Operations}}",
  "role": "{{Vessel Traffic Service (VTS) Operator}}"
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
