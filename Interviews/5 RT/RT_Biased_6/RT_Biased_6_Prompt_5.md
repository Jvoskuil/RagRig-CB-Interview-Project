You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations research file — nothing here goes into a disciplinary record, and you can decline any question. Are you good to proceed?

**Participant:** Yeah, that's fine. I figured I'd get a call about this run eventually.

**Interviewer:** Can you start by telling me your role and roughly what a normal night looks like on this route?

**Participant:** Sure. I'm the engineer, so I'm running the power, handling speed and braking, working the radio with the dispatcher. I've had this territory for about eleven years now. It's single track most of the way, so timing matters — you've got meets scheduled at sidings, and if you're late getting into the hole, you can back up traffic for an hour or more. That night I had a loaded manifest train, mixed freight, heading toward a meet at a siding we needed to clear before an opposing train showed up.

**Interviewer:** Walk me through what happened that night, from the top.

**Participant:** Everything was normal to start. Light rain, some fog building up later, but nothing unusual for that time of year. We were running close to on time. About forty minutes in, we passed a wayside detector and got the automated call — hot bearing alarm, didn't specify which axle exactly, just flagged the train. Now, that particular detector, I want to say it's given us grief before. I know of at least two times in the last six months it flagged something in wet weather that turned out to be nothing — sensor drift, is what maintenance called it. So when I heard the alarm, my first thought was, here we go again, same detector, same kind of weather.

**Interviewer:** What did you do at that point?

**Participant:** I looked for anything from the cab — smoke, sparks, smell — didn't see or smell a thing. Told the dispatcher we copied the alarm, and honestly, I treated it as almost certainly another false trip. I kept the train moving at track speed.

**Interviewer:** Did you consider asking the dispatcher or the car department to check which car or axle had triggered it?

**Participant:** I could have. The information's usually gettable if you push for it. I just didn't think it would've changed anything in the moment — no visible symptoms, detector's flaky in the rain, so I didn't request the breakdown. Dispatcher didn't have it handy either when I asked in passing.

**Interviewer:** Let's move ahead. What happened as you approached the meet window?

**Participant:** So now I'm coming up on the point where I either need to get moving to make the siding in time, or I lose the slot and sit. No further alarms since the first one. My normal practice on this run, when nothing's confirmed wrong, is to just keep the plan as built — that's what I did. I kept us on the standing plan, didn't change speed or add a stop.

**Interviewer:** Was there anything else going on around that time?

**Participant:** The conductor mentioned the ride felt a little rough through one stretch, but he chalked it up to rail joints — we've got some known joint conditions in that section, nothing new. I did have him do a rolling check from his side window at the next spot where visibility was decent, just to cover myself on that first alarm. Didn't see anything.

**Interviewer:** Why the rolling check specifically, rather than, say, slowing down more broadly or calling the car department?

**Participant:** It felt like the right-sized response. It let me say I'd actually looked at something, rather than just sitting on the alarm and hoping. Once he told me there was no smoke, no sparks, nothing glowing on that car, I figured whatever the immediate danger was, it was covered — even though, strictly speaking, the original alarm itself was never actually resolved one way or the other. Slowing the whole train down or getting into it with the car department over the radio — that's a bigger step, and I didn't think the situation called for it yet.

**Interviewer:** Did you make the meet?

**Participant:** Yeah, cleared it with a few minutes to spare.

**Interviewer:** Then the second detector came into play. Tell me about that.

**Participant:** About twenty-two miles further on, second detector, independent from the first, flags a hot bearing alarm again — and this one specified roughly the same car position as before. Fog's thicker by then. Around the same time, dispatcher radios that the corridor's on-time numbers have been under review this month, so there's that in the back of my mind too.

**Interviewer:** How did you interpret the second alarm?

**Participant:** Honestly, I leaned on what I've seen over the years. In eleven years running this territory, almost every hot-box call from these wet-weather detectors has turned out to be nothing. So two alarms from detectors with that reputation — to me that still read as consistent with the pattern I already knew, not as something new and urgent. I didn't weight it much differently than the first one.

**Interviewer:** What did you decide to do?

**Participant:** Kept going to the next station stop rather than calling for an inspection right then.

**Interviewer:** Looking back, why do you think you didn't stop after that second alarm?

**Participant:** If I'm honest, I felt kind of boxed in that night — the dispatcher had just brought up the on-time scrutiny, and a full walking inspection eats twenty, thirty minutes easy, plus coordination, and on top of that these detectors just aren't reliable in this weather, that's well known on this line. Between the schedule sitting on me and detectors that cry wolf, it didn't feel like there was much room to do anything different. I guess if I really think about it, I did also just go with my own read that it probably wasn't anything, and I didn't push back on that read the way I maybe could have.

**Interviewer:** What happened next?

**Participant:** About eight miles past that second alarm, conductor calls up and says he's smelling something acrid from the trailing end of the train. That got my attention right away.

**Interviewer:** What did you do?

**Participant:** Made an emergency radio call to the dispatcher, requested an unscheduled stop immediately.

**Interviewer:** At that point, what was going through your mind — what made you decide to stop when you did?

**Participant:** The smell, mainly. That's a real, physical thing happening right then, not an automated call that might be a sensor glitch. That's what pushed me to stop.

**Interviewer:** By the time the smell came in, had the two earlier alarms already sort of faded from your mind, just because they'd happened a while back?

**Participant:** Yeah, honestly, kind of. They were still in there somewhere, but they'd happened miles ago at that point and nothing had come of them yet, so they weren't really front and center anymore. The smell was just what was right in front of me at that moment.

**Interviewer:** How much did the two earlier alarms factor into that decision, compared to the smell?

**Participant:** They were there, sure, in the back of my head. But honestly the smell is what did it. The alarms were a ways back by then, and like I said, they hadn't led anywhere before.

**Interviewer:** What did the inspection find?

**Participant:** Car department found an overheated wheel bearing on the flagged car — hadn't failed, but it needed to be set out right there. Turned out it had actually been logged as a watch item at the previous terminal, but that flag never got relayed to us.

**Interviewer:** If the second detector hadn't gone off at all, do you think you'd have handled the rest of the trip differently?

**Participant:** Probably not that differently, honestly. Without a second alarm, I likely would've just kept going the same way I did after the first one, until something more obvious showed up.

**Interviewer:** Looking back now, how would you weigh the two alarms against the smell, in terms of what actually mattered?

**Participant:** I still think the smell was the deciding piece. The alarms gave some warning, I'll grant that, but they'd cried wolf enough times before that I didn't put much stock in them until there was something undeniable.

**Interviewer:** If schedule pressure hadn't been part of the picture that night, do you think your decisions after the second alarm would have gone differently?

**Participant:** Maybe. Without the on-time conversation with the dispatcher sitting there, I might've been quicker to call for a look. But that pressure was real, and it's a normal part of the job on this territory.

**Interviewer:** Anything else you'd want a fresh crew to know if they saw this same pattern of alarms come up?

**Participant:** Just that these detectors do throw false alarms in wet weather, so I get why people read it that way. But I'd tell them two hits on the same car position is worth more than we probably gave it credit for that night.

**Interviewer:** That's helpful. I think that covers what I need — thanks for walking through it in this much detail.

**Participant:** No problem. Glad it didn't end up worse than a set-out.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{RT_Biased_6}}",
  "occupational_domain": "{{Rail Transportation}}",
  "role": "{{Locomotive Engineer / Train Driver}}"
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
