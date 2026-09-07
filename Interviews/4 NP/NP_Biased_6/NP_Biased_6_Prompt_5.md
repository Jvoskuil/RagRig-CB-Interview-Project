You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm looking to understand how you actually reasoned through the feedwater heater trend during the ascension test, not to evaluate your performance. Everything stays de-identified for training and procedure review purposes. Sound okay?

Participant: Yeah, that's fine. I figured this was coming after the work order got written up.

Interviewer: Good, let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend?

Participant: Sure. We were about three hours into the ascension test, sitting around 90 percent power, working toward the dispatch commitment at end of shift. I was at the controls, doing my normal rounds on the trend recorders, and I caught that heater 1B outlet temperature had crept up about three degrees over maybe twenty minutes. Train 1A was steady, no issue there. No alarm, nothing outside our Tech Spec limit. My first thought honestly was, "here we go again" — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it.

Interviewer: What was going through your head at that point, in terms of goals and pressures?

Participant: Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered. And with the calibration history sitting right there in my head, the drift didn't feel like something new. It felt like the same story playing out again.

Interviewer: Let's reconstruct the timeline a bit before we get into the decisions themselves. After you first noticed the drift, what happened next?

Participant: I logged it as consistent with the prior calibration pattern and kept going with the ascension sequence. About fifteen minutes later the trend was still creeping, still shallow, still inside limits. Then a bit after that — maybe forty minutes in total — a maintenance tech doing an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. Shortly after that call, the trend recorder actually started flattening out as we approached the final ascension step.

Interviewer: Okay, let's go through this decision by decision. First one: when you saw that initial drift, what alternatives did you actually consider?

Participant: There were really two options. Either treat it as the same calibration issue from last cycle and just keep trending, or treat it as something new and call for an independent instrument check, maybe get I&C down there. I went with the first.

Interviewer: What made you settle on that one?

Participant: The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file.

Interviewer: Did you consider what it would take to rule that explanation out?

Participant: Not really, no. I suppose I could've asked for a quick independent check on the sensor loop, but at the time it seemed like it would've been overkill given what I was looking at. I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw "same sensor, same shape" and moved on, since I was already treating it as the same event.

Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available where you could've briefed the STA before continuing. What went into that call?

Participant: The STA was right there, actually, just hadn't said anything to him yet about it. I remember thinking it "felt manageable" — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing.

Interviewer: Was the dispatch window part of that calculation?

Participant: A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet.

Interviewer: Right after that, the technician's infrared call came in. Walk me through how you weighed that against what you were seeing on the trend recorder.

Participant: That's the one I've gone back and forth on since. His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue. I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said.

Interviewer: How did you end up weighting the two?

Participant: I leaned toward the trend data. Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures. I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation.

Interviewer: Did anything about that reasoning give you pause?

Participant: A little, yeah. He's not wrong about heat exchangers — that's literally his specialty, probably more relevant to shell heating than what I look at day to day. But in the moment, my trend line just felt like the stronger evidence, and honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words.

Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed rather than hold?

Participant: At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go.

Interviewer: Did you consider requesting a hold for independent verification before that step?

Participant: I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time.

Interviewer: How much uncertainty did you feel across all of this?

Participant: Some, especially after the tech's call. But nothing that crossed into "this violates a limit" territory, so it stayed more like background noise than something driving the decisions.

Interviewer: Let's close with a couple of hypotheticals. If that infrared call had come from another licensed operator instead of a maintenance tech, do you think you'd have weighed it differently?

Participant: Probably, yeah. I think I'd have taken it more seriously right away rather than filing it as likely noise.

Interviewer: And if the trend had kept climbing instead of flattening near the final step?

Participant: Then I think I would've held and called the STA in properly. The flattening is honestly what let me feel okay proceeding.

Interviewer: Last one — looking back, is there a point where, with the same information you had, you might've made a different call?

Participant: Maybe the second one. I could've just briefed the STA early and let him weigh in, even without hard evidence something was wrong. It wouldn't have cost us much time, and it would've gotten another set of eyes on it before things went further.

Interviewer: That's helpful, thank you. I think that covers everything I needed.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{NP_Biased_6}}",
  "occupational_domain": "{{Nuclear power and Process-control operations}}",
  "role": "{{Reactor Operator (NRC-licensed)}}"
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
