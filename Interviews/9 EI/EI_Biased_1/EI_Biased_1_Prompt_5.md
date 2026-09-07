You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a workplace research project on how teachers make placement decisions, and you can decline to answer anything or stop at any point. Sound okay?

Participant: Yes, that's fine.

Interviewer: Great. Can you tell me a bit about your role and how long you've been teaching math here?

Participant: I've taught high school math for eleven years, the last six here. I mostly teach Algebra II and Geometry, and I'm usually the one who handles course placement questions when a student transfers in mid-year, since I know the sequencing best.

Interviewer: And walk me through, generally, what happens when a transfer student shows up without a complete academic record?

Participant: It varies. Sometimes the transcript is solid and we just slot them in. Other times, like this case, the transcript alone doesn't tell us enough, so we pull in a diagnostic test, maybe an observation, and go from there. The counselor coordinates logistics, but the placement call is mine, with my chair signing off.

Interviewer: Let's talk through the specific incident you had in mind. Can you give me the full account, start to finish?

Participant: Sure. A junior transferred in from out of state in early October. His transcript listed a "B+" in "Algebra II Honors," but the school wasn't one I recognized, and the counselor couldn't verify their grading scale or how rigorous that course actually was. We had about a week before the schedule locked, so I didn't have much runway. My first instinct was just to trust the transcript and drop him into Algebra II, but the ambiguity bothered me — I didn't want to either shortchange him with an easier class or set him up to fail in one that assumed skills he didn't have. So I asked my chair if we could hold off a few days and get a diagnostic test done, plus sit him in on one of my classes to see how he handled a formative assessment live. She agreed.

Interviewer: What happened next?

Participant: The diagnostic came back at the 72nd percentile against grade-level norms, which is solid. I also had his transcript GPA, which I converted to our 100-point scale as best I could — that conversion is always a little shaky since I don't actually know how their department curved things. Then I sat him in on a quiz during my third-period class, and he got a 78. On top of that, I had him fill out a short self-assessment where he rated his own algebra confidence, and he put himself at an 8 out of 10. So by the deadline I had four numbers in front of me.

Interviewer: How did you get from four numbers to a decision?

Participant: I converted everything to the same 100-point scale and averaged the four together. That gave me a composite right around 79, which cleared our department's cutoff of 75 for Algebra II placement, so I placed him there and my chair signed off on the figure.

Interviewer: Let's reconstruct the order things arrived in a bit more precisely. What came first?

Participant: The transcript came with his enrollment paperwork on day one. The diagnostic was scheduled for day three. The classroom observation happened day four, same day as the self-assessment survey, since I had him do both during that visit. I finalized everything by day five to make the deadline.

Interviewer: When each new piece came in, what did you do with it?

Participant: Mostly just logged it and waited until I had all four before doing anything with the numbers. I didn't want to prejudge based on one piece — that's actually why I asked for more data in the first place instead of just going with the transcript alone.

Interviewer: Going back to that first decision — holding off versus placing him immediately based on the transcript. What tipped you toward waiting?

Participant: The uncertainty around the prior school's rigor. A "B+" from a school I don't know isn't the same as a "B+" here. I've been burned before trusting an out-of-state label at face value, so I wanted more direct evidence before locking him in.

Interviewer: Once you had the diagnostic, transcript conversion, quiz grade, and self-report, which of those did you consider most important?

Participant: Honestly, I looked at them as four inputs into one number rather than ranking them. The goal was to get a composite score I could defend to my chair, something that wasn't just my gut feeling.

Interviewer: Did you consider treating any of them differently, given they came from pretty different sources?

Participant: I thought about it briefly, but averaging felt like the fairest way to combine them without me injecting extra subjectivity into which one mattered more. If I started picking and choosing weights, that's its own kind of judgment call, and I wanted the number to feel more objective than that.

Interviewer: Had you handled a composite score like this before?

Participant: A couple times, yes, and I've generally just averaged the available measures. It's quick, and it's easy to explain to a parent or administrator.

Interviewer: How much time pressure were you under at that point?

Participant: A fair amount — we were basically at the deadline day. I didn't have room to request another data point even if I'd wanted to.

Interviewer: How confident were you that all four numbers deserved equal footing in that calculation?

Participant: I didn't really stop to weigh that question at the time. I was focused on getting to a number that cleared or didn't clear the cutoff.

Interviewer: Moving to the third point — a few weeks in, he scored 55 on his first unit test, below the class median. What went through your mind?

Participant: That was concerning, but not alarming yet. His homework completion was strong and he still reported feeling confident. I've seen transfer students hit a rough patch adjusting to a new teacher's style and pacing before leveling out, so I didn't want to overreact to one test.

Interviewer: What alternatives did you weigh?

Participant: Move him down to standard track right away, or keep him in Algebra II with extra support and watch the trend. I chose the second option and set up twice-weekly tutoring.

Interviewer: What made you favor waiting over reassigning him immediately?

Participant: One test isn't the whole picture, and reassigning mid-quarter has real costs — transcript continuity, disruption, his own confidence. I wanted more evidence before making that call.

Interviewer: And the fourth point — end of quarter, he had a C-, with an upward trend the last three weeks. His parent asked in writing that he stay in Algebra II. What was your reasoning there?

Participant: The recent trend mattered a lot to me — it suggested the tutoring was working and he was catching up. The counselor also flagged that switching tracks mid-year could complicate his transcript. Combined with the parent's request, keeping him in with continued support seemed like the right call.

Interviewer: Looking back, is there anything you'd have wanted to know earlier that might have changed the placement decision?

Participant: Probably a second observation period. One 50-minute sit-in is a pretty thin slice of evidence, and I'd have liked a bit more before finalizing that composite number.

Interviewer: If the self-report survey had shown low confidence instead of high, do you think your composite score — and the placement — would have come out differently?

Participant: Yes, actually, since it was one of four numbers going into a straight average, a lower self-rating would have pulled the total down and possibly under the cutoff.

Interviewer: If only the diagnostic test had been available, without the other three measures, do you think you'd have placed him the same way?

Participant: Probably, since 72nd percentile alone is a reasonably strong signal. But I wouldn't have felt as comfortable relying on just one number for something this consequential.

Interviewer: Anything you'd do differently next time you face a similar composite decision?

Participant: I think I'd slow down and think harder about how the pieces relate to each other before just averaging them, especially when they're not really measuring the same thing with the same precision. At the time, though, it felt like the practical way to turn four different pieces of paper into one decision.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EI_Biased_1}}",
  "occupational_domain": "{{Education and instructional work}}",
  "role": "{{High School Classroom Teacher}}"
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
