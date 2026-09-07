You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary interview about your clinical decision-making, it's being recorded for research purposes only, and you can skip anything you'd rather not discuss. Can you tell me a bit about your role?

Participant: Sure. I'm an outpatient physical therapist, mostly orthopedic caseload — a lot of post-surgical knees and shoulders. I've been doing this about nine years. Right now I see somewhere between eleven and fourteen patients a day.

Interviewer: I'd like to focus on one case that stands out to you — something nonroutine, where you had to make some real judgment calls. Can you walk me through it?

Participant: Yeah, there's one that's been on my mind. Adult patient, competitive amateur soccer player, hamstring autograft ACL reconstruction. She was highly motivated — wanted to be back for preseason, which gave us roughly a sixteen-week runway before her insurance authorization would expire. So there was a real clock running the whole time. Around week eight, we did a strength check — quad index came out to 78% of the uninvolved side. Threshold for moving into plyometric loading is usually cited around 80 to 85%, so she was close but technically under. No pain, no swelling, moving well. I actually had a case a couple years back — different patient entirely, similar timeline — who progressed into plyometrics early and re-tore her graft. That one stuck with me. So at that checkpoint, I held her at the current loading level rather than bumping her into closed-chain, modified plyo work, even though her numbers were close and she was symptom-free. I told her we'd reassess in two weeks.

Interviewer: What happened next?

Participant: The surgeon's clearance for advanced loading came through a few days later, no structural concerns noted. She was frustrated — she'd been comparing notes with a teammate who'd had a faster progression somewhere else. Then over the next couple weeks she had three really clean sessions of single-leg hopping — pain-free, form was improving each time, no swelling afterward. We had the isokinetic dynamometer booked for a hop-symmetry test that week, since it's only in clinic two days a week and slots go fast. But I remember thinking, three good sessions in a row is unusual for this stage — felt like we were due for something to give, so I pushed the test back a week rather than run it as scheduled.

Interviewer: And the week after?

Participant: Fourth session, also fine. No setback. But pushing the test back did eat into the authorization window a bit more than I'd have liked.

Interviewer: Let's go back to that first checkpoint, week eight. What information did you have in front of you at that moment?

Participant: The 78% index, no pain, no effusion, and clearance was pending but I fully expected it to come through. Objectively she was close to threshold and asymptomatic.

Interviewer: What alternatives did you weigh?

Participant: I could've progressed her into the modified plyo work right then, held her flat and reassessed in two weeks like I did, or split the difference with a reduced-intensity subset. I chose to hold.

Interviewer: What was the deciding factor?

Participant: Honestly, that prior patient's graft failure. I know it's a different case, different graft type technically, but it was vivid enough that it colored how I read this one. If I'm being fully honest, the current patient's actual numbers supported at least a partial progression.

Interviewer: How confident were you in that call at the time?

Participant: Moderately. I could have justified either choice on paper, but that memory tipped me toward the more conservative one.

Interviewer: Moving to the hop-test delay — what was your reasoning in the moment?

Participant: There was no clinical red flag — no fatigue report, no swelling, PROMs were stable. It was really just this sense that things had gone smoothly for long enough that a dip felt likely. In hindsight, each session doesn't really owe you anything based on what came before it.

Interviewer: Did time pressure factor into that decision?

Participant: A little, in the sense that delaying cost us a slot, but the reasoning driving it wasn't the schedule — it was that instinct about the streak.

Interviewer: Let's move to the third checkpoint. What was happening there?

Participant: Around week twelve, she'd hit about 85% of her interim milestones. Case manager wanted my recommendation — keep her in twice-weekly clinic visits or transition to a home program. Her numbers genuinely could've supported either path; it wasn't a clear-cut read.

Interviewer: How did you present the options?

Participant: I told the case manager and the patient that if we stopped clinic visits now, she'd risk losing the strength gains she'd built up. That's really the framing I led with. I didn't spend much time on the flip side — that a structured home program with check-ins could just as easily consolidate her progress and build her independence. Looking back, I leaned on the "you'll lose what you've gained" language more than the actual data probably warranted, and that's largely what drove the recommendation to keep her in clinic.

Interviewer: Did the patient respond to that?

Participant: She went along with it, but she mentioned afterward that the way I put it made her anxious about stopping, more than she felt the numbers alone would've justified.

Interviewer: Let's talk about discharge, around week sixteen. What did the picture look like then?

Participant: Strong. Hop symmetry index at 88%, quad index at 91%. Genuinely some of the best numbers I'd seen on my caseload that year. Surgeon wanted my recommendation on return-to-sport clearance.

Interviewer: What did you tell the patient?

Participant: I told her she was very likely to get back to competitive play injury-free — I said it pretty directly, based on how strong her numbers were compared to other patients I'd worked with. Looking back, I think I took "better than most patients I've seen" and turned it into "very likely injury-free" more firmly than those two scores alone could really back up for someone returning to a cutting-and-pivoting sport.

Interviewer: What alternatives did you consider at that point?

Participant: Full clearance outright, clearance with a structured sport-specific reconditioning phase and closer monitoring, or delaying for another functional movement screen. I went with full clearance.

Interviewer: She asked you something specific at that point, right?

Participant: Yeah, she asked what her actual chances were of re-injuring it once she got back to playing. I answered in terms of her numbers — how strong her hop symmetry and quad index were relative to threshold. I didn't really bring in anything about how often athletes in general re-injure after this kind of surgery when they go back to cutting and pivoting sports. In hindsight, that's relevant information I have some familiarity with, and I didn't raise it.

Interviewer: What would have needed to be different for you to answer that differently?

Participant: If she'd asked more pointedly, "compared to other patients in general," I probably would've brought in more of that broader picture. But she asked about her chances, and I answered about her.

Interviewer: Looking back across the whole case, if insurance had allowed unlimited visits, would anything have changed?

Participant: Probably the pacing at that third checkpoint — less pressure to frame things one way or another, more room to just let the home program idea breathe.

Interviewer: If this had been a recreational walker instead of a competitive athlete, would your discharge conversation have gone differently?

Participant: Almost certainly softer, less urgency, and I think I'd have been more inclined to caveat the outcome rather than state it so plainly.

Interviewer: Any final reflection you'd offer a colleague facing a similar case?

Participant: Just to keep checking whether what's driving a call is the patient in front of you, or something you're carrying in from somewhere else — a past case, a good run of sessions, whatever it is. It's not always obvious in the moment which one it is.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HC_Biased_5}}",
  "occupational_domain": "{{Healthcare}}",
  "role": "{{Physical Therapist with outpatients}}"
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
