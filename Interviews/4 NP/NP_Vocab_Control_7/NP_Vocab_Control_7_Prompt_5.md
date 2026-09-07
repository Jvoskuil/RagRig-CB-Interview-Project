You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for sitting down with me. This is for our operations learning file, not a disciplinary review — nothing here goes in your personnel record. Can you tell me your role and background?

Participant: Sure. I'm a process control operator on the catalytic reforming unit, six years on this board, eleven at the refinery overall. I run the DCS console — feed rates, heater duty, reactor temps, that side of things.

Interviewer: Good. Let's start broad — walk me through the incident from the beginning.

Participant: It kicked off right at shift handover, early morning. I'd just settled in when the high-temperature alarm came up on the feed heater outlet. Annunciator lit up, tone sounded. That specific point has been noisy lately — I want to say it tripped something like eleven times over the past month, all logged as instrument drift. But before I acknowledged it, I pulled up the pressure-differential trend on the adjacent screen too, since that's a habit of mine with recurring alarms — you want to see if anything else is moving with it. That trend had been creeping upward for a couple hours, slower and less obvious than the alarm itself, but it was there. Seeing both together made me less comfortable calling it a pure nuisance trip like the others had been, so I got the field operator moving to verify the thermocouple directly rather than just silencing it and continuing on.

Interviewer: What did the field check turn up?

Participant: Confirmed the outlet reading was accurate — not an instrument fault. So now I've got a real alarm and a real trend, and I flagged both for closer attention going into handover.

Interviewer: Walk me through the handover conversation.

Participant: Night operator said things had been "stable, unremarkable" for his last four hours, which matched what I was seeing on the immediate trend. But there was an older note in the board log, a few days back, about a slow upward drift in heater duty that had been flagged and never formally closed out. Rather than just assume it had resolved itself because the recent hours looked clean, I asked him directly whether that drift had actually been corrected or just stopped showing up in the short-term data. He wasn't sure — said it hadn't come up again, but nobody had gone back and verified the root cause.

Interviewer: How did that affect what you did next?

Participant: Production wanted the feed rate bumped to bank throughput before our regeneration window, about six hours out at that point. Given the alarm, the trend, and the unresolved drift note, I didn't just run the standard increase sequence the way I normally would. I ramped it more conservatively than usual and kept a closer eye on outlet temperature through the whole move, rather than treating it as routine.

Interviewer: What happened after that?

Participant: Temperature climbed some, as expected with any increase, but then the field operator called in from a walkdown and mentioned heat shimmer near the firebox — visually distinct, not something he'd normally flag. That raised the stakes.

Interviewer: Let's go back and unpack the first decision — cross-checking the pressure trend before acknowledging. What information did you actually have at that point?

Participant: The alarm, the recent trip history, and that pressure trend, which I made a point of looking at before doing anything else.

Interviewer: What alternatives did you weigh?

Participant: I could've just silenced it like the last eleven times — would've been the fast option. Or dispatched the field guy without checking the trend first. I did a version of both, but in a specific order: checked the trend, saw it didn't look like the earlier isolated trips, then sent the field operator to verify independently rather than assuming it was drift again.

Interviewer: How confident were you in that read at the time?

Participant: Moderately. I wasn't certain something was wrong, but the combination was enough that I didn't want to treat it as routine.

Interviewer: Moving to the feed increase decision — what alternatives were on the table?

Participant: Full delay and a deep dive into the multi-day trend log, looping in the engineer before touching setpoints, or proceeding as planned. I landed somewhere in the middle — proceeded, but modified, with tighter monitoring, specifically because the drift note hadn't been confirmed resolved.

Interviewer: Was that a deliberate call, or did you default to the usual procedure?

Participant: Deliberate. I actually thought about skipping the modification since the last four hours looked fine, but the unresolved log entry bothered me enough that I didn't want to run it exactly like every other routine bump.

Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind?

Participant: The pattern — alarm, temperature climb, shimmer — had some resemblance to a compressor surge event I'd handled about a year and a half ago on a similar unit. There's also a tube-rupture incident from a couple years back that people still bring up in briefings, more dramatic, shut the unit down for weeks. Both crossed my mind. But instead of just running with either, I checked specifically for the vibration signature that had shown up in the surge event — wasn't present here at all. And I asked the engineer whether the current data showed any of the specific markers tied to the tube-rupture failure mode. It didn't match either one cleanly.

Interviewer: What did you do given that neither precedent matched?

Participant: Treated it as its own case. Pulled fresh heater-specific diagnostic data and requested an independent instrument check rather than forcing it into either historical bucket.

Interviewer: Final decision — regeneration window closing in.

Participant: Under ninety minutes left. Temps and pressure still climbing, not at trip setpoints yet. I had a short checklist of standard corrective actions. Full engineer consultation would've eaten twenty to thirty minutes I didn't have to spare, but I also didn't want to just grab the first option on the list.

Interviewer: How did you choose?

Participant: I compared the top two or three checklist options against what the diagnostic data was actually showing, picked the one that matched the pattern best, not just the first one listed, and briefed the engineer by radio while I implemented it so he could flag anything I'd missed in real time.

Interviewer: What was the outcome?

Participant: Stabilized the trend. Later review said the comparison held up reasonably well given the time we had, though the full underlying cause took longer to pin down completely.

Interviewer: If the alarm's history had been clean instead of noisy, would you have handled that first moment differently?

Participant: Probably would've moved even faster to dispatch the field operator — less hesitation about whether it was worth the disruption. The noisy history didn't stop me from checking, but it's fair to say it added a beat of consideration before I did.

Interviewer: What single piece of information, if you'd had it sooner, would have changed the most?

Participant: Confirmation on whether that multi-day drift had genuinely resolved. I was operating on an unanswered question there, and if I'd known definitively either way, the feed-increase decision would've been more clear-cut.

Interviewer: And with more time before the regeneration window?

Participant: I'd have gotten the full engineer consultation rather than the quick radio brief. The comparison I did was reasonable, but a full conversation would've added confidence.

Interviewer: Anything else stand out looking back?

Participant: Just that none of these calls were obvious in the moment. Each one had a real alternative I seriously considered, and I don't think the outcome tells you definitively whether any single step was the right one — it worked out, but there was real uncertainty the whole way through.

Interviewer: That's a good place to stop. Thanks for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{NP_Vocab_Control_7}}",
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
