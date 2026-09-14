You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{**Interviewer:** Thanks for making time this week. Just to confirm, this is a voluntary conversation about your recent work verifying the fire engineering package on the tower project—I'll be asking about a specific sequence of decisions, and there's no need to reference anything confidential like commercial terms. That work for you?

**Participant:** Sure, that's fine. I led the performance-based design verification on the 42-story mixed-use tower—office floors, residential above, and an assembly space at podium level. My job was to close out the fire strategy sign-off before the developer's occupancy certificate deadline.

**Interviewer:** Can you give me a general account of what happened in that final stretch?

**Participant:** It was a compressed week. We had four things converging: a late glazing substitution from the contractor, a smoke-control model that came back borderline, a punch list that wasn't fully closed, and a final egress run we needed clean before submission. Normally these would be spaced out, but the contract had liquidated damages tied to the occupancy date, so everything landed at once. The contractor proposed swapping the specified glazing for a cheaper product from another supplier—call them Vendor B—because the original product had a lead-time problem. Around the same time, our CFD smoke model for the atrium showed a visibility result at the escape stair door that was right at the edge of the tenability threshold. Then, with about two inspection days left, our QA reviewer flagged some open punch-list items across cladding fire-stopping, stair pressurization, and signage. And finally, we had to finalize the egress modeling parameters before submitting to building control.

**Interviewer:** Let's reconstruct that in order. What came first?

**Participant:** The glazing issue surfaced first, maybe ten days out. Vendor B sent their technical bulletin, and their rep followed up by email restating the same fire resistance figure, and then I found the same number again in their product brochure. The CFD result came in a few days later, right when we were prepping for fan commissioning. The punch-list conversation happened after that, once the QA reviewer did a walk-through. The egress modeling was the last piece, done in the final two days before submission.

**Interviewer:** Let's take the glazing decision first. What did you have in front of you?

**Participant:** The original spec had a UL-tested 90-minute integrity rating, properly documented. Vendor B's material said their product also achieved "90 minutes, independently verified." I saw that phrase in their bulletin, then again in the cover email, then again in their brochure.

**Interviewer:** What made you comfortable with that?

**Participant:** Honestly, seeing it stated the same way three times across three different documents gave me a level of confidence I probably wouldn't have had from just one. It felt corroborated—like it wasn't just marketing spin, because the same number kept showing up consistently.

**Interviewer:** Did you look at whether those three statements were drawing on the same underlying test?

**Participant:** Not at that stage, no. It didn't occur to me to check whether the bulletin, the email, and the brochure were all citing the same lab report versus separate testing. Building control asked for the raw report later, and that's when we found the mounting configuration in the original test didn't match our as-installed detail, which meant we needed a compatibility assessment. At the time, though, I provisionally accepted the substitution on the basis that it was consistently documented.

**Interviewer:** Moving to the CFD result—what were the options there?

**Participant:** The model showed visibility at the stair door getting close to the threshold around the six-minute mark. Our QA reviewer recommended re-running it with a revised HVAC shutdown sequence, which would've added about five working days. We had four days to the deadline. Fan commissioning was next on the critical path.

**Interviewer:** What did you decide, and why?

**Participant:** I authorized the commissioning to proceed. We were losing days, and holding the whole phase for a re-run felt like it would stall the entire program right when we needed to keep moving. I treated the re-run as something that could happen in parallel rather than as a gate before the next milestone.

**Interviewer:** Was there a technical basis for treating it as non-blocking, or was it mainly about the schedule?

**Participant:** If I'm honest, it was mostly about not wanting the project to stand still. The commissioning itself wasn't destructive, so proceeding felt like the safer, more productive choice compared to just waiting around for numbers we already suspected might come back tight. The re-run did eventually show the margin was narrower under a slightly different shutdown assumption, but by then commissioning had already passed its initial functional tests.

**Interviewer:** Let's talk about the punch-list reprioritization. What was on the list at that point?

**Participant:** Cladding fire-stopping, a pressurization deficiency on one of the lift-shaft fan doors, and some egress signage items. Two inspection days left.

**Interviewer:** How did you decide where to spend those two days?

**Participant:** There'd been that apartment-tower fire overseas about two weeks earlier—cladding-related, and the footage was everywhere. It stuck with me. Even though our cladding and compartmentation system is different and already well-documented, I put the remaining time into re-inspecting the cladding fire-stopping.

**Interviewer:** What about the pressurization fan-door deficiency?

**Participant:** It got pushed down the list. It had already been logged, so it felt like something we understood and could revisit later. The cladding felt like the one I needed to be extra sure about after watching that. In hindsight, a follow-up visit found the fan-door issue was more significant than we'd initially logged, and the cladding re-inspection didn't turn up anything new.

**Interviewer:** Did you use the standard risk matrix to rank those items?

**Participant:** Not formally at that point. It was more of a judgment call based on what felt most urgent to check again.

**Interviewer:** Last decision point—the egress modeling parameters.

**Participant:** Right, this was in the final two days. The software's default library has pre-movement times and flow rates calibrated for generic office occupancy. Our building's mixed-use—office, residential, assembly—so the population isn't quite the same. A colleague flagged that we actually had project-specific pre-movement survey data, plus some comparable mixed-use studies, that could refine those numbers.

**Interviewer:** Did you use that data?

**Participant:** We didn't, in the end. Recalibrating with the survey data would've meant extra runs and QA time we didn't have. The defaults are the standard starting point in that software, so I kept them for the final compliance run. I flagged in my notes that the calibration population wasn't a perfect match, but the run passed the required threshold, so we submitted it as is.

**Interviewer:** If recalibrating had taken less effort, would you have used the survey data instead?

**Participant:** Probably, yes. It wasn't that I thought the defaults were more accurate—it was more that changing them under that timeline felt like an unnecessary complication.

**Interviewer:** Looking back across all four decisions, what would have changed your approach on the glazing, if anything?

**Participant:** If the 90-minute claim had come from one document instead of three, I think I'd have pushed harder for the raw report before accepting it. Something about seeing it repeated made it feel more settled than it actually was.

**Interviewer:** And if there'd been no deadline pressure at all that week?

**Participant:** The CFD re-run probably would've been a hard hold point rather than something running in parallel. Without the schedule squeeze, I don't think I'd have authorized commissioning ahead of it.

**Interviewer:** Last one—if that overseas fire hadn't been in the news right before your punch-list decision, do you think the priority would have looked different?

**Participant:** Possibly. I'd like to think I'd have gone with the risk matrix from the start. But I can't fully separate how much of that reallocation was the news versus genuine caution.

**Interviewer:** That's a helpful place to stop. Thanks for walking through it in this much detail.

**Participant:** No problem. It's useful to go back over it, honestly.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Biased_4}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Structural Fire Engineer (Performance-Based Design)}}"
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
