You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations learning file, not a disciplinary review — anything you share is for process improvement. Can you state your role and how long you've been on this unit?

Participant: Sure. I'm a process control operator on the catalytic reforming unit, been on this board for about six years, refinery for eleven. I run the DCS console during my shift — feed rates, heater duty, reactor temps, that kind of thing.

Interviewer: Good. Let's start broad — walk me through the incident from the beginning.

Participant: It started right at shift handover, early morning. I'd just sat down at the console when the high-temperature alarm came up on the feed heater outlet. Annunciator panel lit up red, audible tone too. Honestly, my first thought was "here we go again" — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast. I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own. So I acknowledged it, silenced the tone, and kept going with handover.

Interviewer: Did you check anything else at that point?

Participant: Not right away, no. I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens, but it's a quieter kind of alarm, just a slow line drifting upward, no flashing, nothing urgent-looking. I didn't pull that screen up until later in the shift.

Interviewer: Okay, let's keep going chronologically. What happened during the handover conversation itself?

Participant: Night operator gave me the rundown — said the unit had been "stable, unremarkable" for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value. There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours. It felt like old news at that point since the recent hours looked clean.

Interviewer: And then?

Participant: Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.

Interviewer: What happened after the increase?

Participant: Outlet temperature climbed further than I expected. Then the field operator called in from a walkdown and mentioned some heat shimmer near the firebox — visually noticeable, he said, not normal. That's when it started feeling like more than a nuisance alarm.

Interviewer: Let's go back and unpack that first decision — acknowledging the alarm as nuisance. What information did you actually have in front of you at that moment?

Participant: The alarm itself, my memory of that alarm going off a lot recently, and that pressure trend I mentioned, which I hadn't really looked at yet.

Interviewer: What alternatives did you consider?

Participant: I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality.

Interviewer: How confident were you in that read?

Participant: Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head, even if I hadn't actually gone back through the log to confirm it.

Interviewer: Moving to the feed increase decision — what alternatives were on the table?

Participant: I could've delayed the increase and gone back through the multi-day trend log, or looped in the process engineer before touching setpoints. Neither felt necessary given how clean the last few hours looked.

Interviewer: When you ran the sequence, were you consciously deciding it was the right call, or was it more automatic?

Participant: If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump.

Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind?

Participant: The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template. At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.

Interviewer: Did the current data support either of those comparisons specifically?

Participant: Looking back, not entirely. The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.

Interviewer: What alternatives existed at that point?

Participant: I could've treated it as a new case entirely and pulled fresh heater-specific data before picking a diagnostic path, or requested an independent instrument check to compare against both remembered precedents.

Interviewer: Let's talk about the final decision, with the regeneration window closing in.

Participant: Under ninety minutes left. Temps and pressure still climbing but not at trip setpoints yet. I had the standard checklist for heater excursions, and I could've paused everything to escalate fully to the process engineer, but that's a twenty-to-thirty-minute conversation minimum, and the clock was working against us.

Interviewer: How did you decide?

Participant: I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.

Interviewer: What was the outcome?

Participant: It did stabilize the immediate trend, which was the priority. Root cause wasn't fully addressed though — a later review flagged another corrective step on that same checklist that probably would've hit the underlying issue better. Wasn't wrong exactly, just not the most complete answer.

Interviewer: If the alarm's history had been different — say, no prior nuisance trips at all — would you have handled that first moment the same way?

Participant: No, honestly no. If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise.

Interviewer: What single piece of information, if you'd had it earlier, would have changed the most for you?

Participant: Probably the pressure-differential trend, pulled up right alongside the alarm at the very start. That would've reframed the whole thing much sooner instead of it building quietly in the background.

Interviewer: And if you'd had more time before the regeneration window closed?

Participant: I'd have gone through more of the checklist options side by side, maybe gotten the engineer on the line even for ten minutes. It wasn't that I thought the first option was definitely best — it was available and it worked well enough given the clock.

Interviewer: Anything else stand out looking back?

Participant: Just that a lot of small, reasonable-feeling calls stacked up into something bigger than any one of them looked like at the time. Nothing felt like a wrong decision in the moment.

Interviewer: That's a good place to close. Thanks for walking through this in detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{NP_Biased_7}}",
  "occupational_domain": "{{Nuclear power and Process-control operations}}",
  "role": "{{Process Control Operator (Chemical/Petrochemical Refinery)}}"
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
