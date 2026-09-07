You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time. Just to confirm before we start—this is a voluntary cognitive task analysis session, recorded for internal research on how IA investigations get worked, not a disciplinary review. You can decline any question. That work for you?

Participant: Yeah, that's fine. I've sat through enough of these on the other side of the table.

Interviewer: Can you tell me your role and how long you've handled complaint reviews?

Participant: I've been in the Internal Affairs Bureau about five years, investigator rank. I handle use-of-force complaints, some policy violations, occasional off-duty stuff.

Interviewer: Let's start with the case itself. Can you walk me through what came in?

Participant: Sure. Complaint came in the morning after a traffic stop on Cedar Street—expired registration stop that turned into a takedown. Driver, a Mr. Alvarez, said Officer Marquez used excessive force, ended up with a wrist fracture. Marquez wrote it up as a compliant-turned-resistant subject, said the takedown was necessary once Alvarez pulled his arm away. His partner, Officer Chen, backed that account. I pulled the file—Marquez has nine years in, two prior complaints, both closed unfounded. Alvarez has a record, two priors including a resisting-arrest charge.

Interviewer: When you opened the file, what did you do first?

Participant: I wanted to know who I was dealing with on both sides, so I ran backgrounds. For Alvarez, I requested his full arrest history and looked for anything that might explain inconsistency in his statement—prior resisting charge stood out, so I flagged that for the interview. For Marquez, I already had the two priors in the system, both unfounded, so I treated his report as the operational starting point and built the review around confirming or contradicting it rather than opening a parallel background pull on him the same way.

Interviewer: Was there a reason you didn't request the same kind of independent verification for Marquez's account at that stage?

Participant: I mean, his report exists, it's the formal record, that's the baseline you work from. Alvarez's statement is what's being tested. I don't think I consciously decided to treat them differently—it's just how intake usually goes. Later, dispatch audio came back showing it was a routine expired-registration stop, not flagged high-risk, and the medical report showed the wrist fracture, which honestly could line up with either version.

Interviewer: Let's move to the footage. Take me through the BWC review.

Participant: Eighteen minutes total, minus a forty-second gap where his camera didn't reactivate right after the initial contact. The first part is pretty calm—verbal back and forth, Marquez asking for license and registration, nothing dramatic. Then the last ninety seconds, Alvarez pulls his arm back when Marquez tries to walk him to the cruiser, and Marquez takes him down. That's where the injury happens.

Interviewer: How did you weigh the earlier minutes against that final sequence when you were forming your assessment?

Participant: Honestly, the takedown is what matters for a force review—that's the moment the fracture occurred, so that's where I put most of my attention. I ended up running that last segment back three or four times to get the mechanics right, and by the time I moved on, it was just sitting closer to the front of my mind than anything from the first part of the stop. The earlier fifteen minutes felt like it had run its course without incident, so once I'd watched it through the first time, I didn't feel much pull to go back and sit with it again. My working read was built mainly around those last ninety seconds.

Interviewer: Did anything from earlier in the footage later become relevant?

Participant: Yeah, actually. A slowed-frame audio pass done later picked up Marquez raising his voice and stepping into Alvarez's space almost three minutes before the takedown—something neither report mentioned. A use-of-force consultant flagged that positioning as relevant to the reasonableness call. I hadn't weighted that part much the first time through.

Interviewer: What was your reaction to learning that?

Participant: A little uncomfortable, if I'm honest. It didn't fit cleanly into the picture I'd already been building around the final segment.

Interviewer: Let's talk about the case conference. Who was there and what happened?

Participant: Day six, me, the sergeant, and two peer investigators. The sergeant supervised Marquez for three years and opened by saying Marquez has "never been a problem," which set kind of a tone. One of the other investigators raised the forty-second BWC gap, said it was worth flagging before we went further.

Interviewer: How did the room respond to that?

Participant: We talked about it briefly, but the conversation moved pretty quickly toward the take that the force was likely justified given Chen's corroboration and the resisting motion on camera. We didn't formally table the gap as an open item. I drafted the preliminary summary along those lines within the forty-eight-hour window we had for the Deputy Chief.

Interviewer: Did the investigator who raised the gap seem satisfied with that?

Participant: Not entirely, as it turned out. She told me privately afterward she still had reservations but didn't push it once the room had settled on a direction. I didn't document that follow-up conversation in the file at the time.

Interviewer: What made you align with the room's direction rather than the concern she'd raised?

Participant: I think once the sergeant framed it that way and Chen's report backed it up, the momentum was already there. It felt like the sensible read given everyone's read of the tape. I didn't feel like there was a strong reason to hold it up.

Interviewer: Let's go to day ten. What happened with the eyewitness?

Participant: A civilian witness who'd called in initially but was hard to reach finally gave a statement. She said Marquez was "aggressive from the start," which conflicts with how I'd characterized the early footage as calm. That came five days after I'd already briefed the Deputy Chief that this was trending toward exonerated.

Interviewer: How did that statement affect your thinking?

Participant: It shifted things somewhat. It was the freshest account I had at that point, closer in my mind than the footage I'd reviewed back on day three, so it carried a lot of weight in the conversations we had finalizing language.

Interviewer: You mentioned a supplemental review. What did that find?

Participant: A second investigator confirmed she had an unobstructed view but was about thirty-five feet away. Command also asked whether the preliminary briefing still stood.

Interviewer: How did you resolve the tension between her account and what you'd already told the Deputy Chief?

Participant: I leaned toward treating her statement as less determinative—distance, lighting, that kind of thing—and kept the briefing largely as it was. I'll admit part of that was probably about not wanting to walk back something I'd already told command with some confidence. Revising it at that point would've meant explaining why my read had changed, and I didn't feel the new statement was strong enough on its own to justify that.

Interviewer: What's the part of this case you're least confident about, even now?

Participant: Probably whether the early three-minute positioning detail should have carried more weight from the start. I don't know that it changes the final call, but I didn't give it a fair look the first time around.

Interviewer: If the eyewitness statement had come in on day two instead of day ten, do you think your review would have gone differently?

Participant: Probably. I'd have folded it into the footage review directly instead of layering it on top of an opinion I'd already formed and reported up.

Interviewer: If you'd been the only reviewer, without the case conference, do you think you'd have reached the same finding?

Participant: Hard to say. Maybe I'd have sat with the BWC gap longer on my own. Group discussions move faster than solo review, for better or worse.

Interviewer: Anything you'd handle differently in sequencing next time?

Participant: I'd probably push harder to get the eyewitness statement early, and I'd formally log dissenting concerns from the conference instead of letting them stay verbal. That's on me.

Interviewer: Appreciate you walking through this in detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{LE_Biased_5}}",
  "occupational_domain": "{{Law enforcement}}",
  "role": "{{Internal Affairs Investigator}}"
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
