You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm this is a routine debrief on your reasoning process during the Copper Creek event, not a performance review. Nothing here affects your evaluation. Are you okay proceeding on that basis?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you start by describing your role on the desk that shift?

Participant: I'm the meteorological hazard forecaster for the ESF-2/ESF-5 desk at the state EOC. My job is basically to translate NWS and SPC guidance into activation-level recommendations, warning products, and messaging calls for the counties in our basin. I coordinate with the WFO, the county EMs, and on multi-state events, with neighboring forecast desks.

Interviewer: Walk me through this particular incident from the start.

Participant: It started overnight with SPC flagging a marginal severe risk for the basin, low confidence, mostly because guidance was still sparse. By the 06Z cycle we only had four members of the convection-allowing ensemble finished — the rest were still running. Three of those four showed the cluster intensifying fast over the basin within about three hours. That got my attention because it lined up with what SPC's mesoscale discussion was hinting at. I made the call to push an early watch-to-warning upgrade based on that signal rather than wait for the fuller 09Z set. A couple hours later, radar showed a hook-shaped reflectivity signature that looked almost identical to an event I'd forecasted successfully a couple seasons back — same kind of setup, similar CAPE and shear profile. I was fairly confident about the track and timing at that point. Then flash flood guidance started trending up in two of our sub-watersheds, and I wanted to escalate the EOC activation level and get swift-water teams moving, since they need about 45 minutes lead time. But the regional director called and told the desk to hold pending review. Later, on the interstate coordination call, most of the neighboring jurisdictions said they were holding their alert levels too, so we ended up staying at the same level even though our local numbers kept climbing. Flooding started in one of our communities about fifty minutes after that call ended.

Interviewer: Let's reconstruct the sequence a bit more precisely. What did you have in front of you at each stage, and what were you still waiting on?

Participant: At the start, just the partial ensemble and the SPC discussion — no radar-observed rotation or flood-guidance exceedance yet. Then the radar signature came in, which added a qualitative cue on top of the model data. After that, the guidance numbers started climbing, which was the first hard hydrologic evidence. And finally, the coordination call added the social layer — what everyone else on the basin was doing.

Interviewer: Let's go through the four moments where you had to make a call. First: the early upgrade decision. What were the alternatives you weighed?

Participant: I could've upgraded early, held until the 09Z cycle with the bigger ensemble, or done a limited advisory just for the highest-confidence sub-area. I went with the early upgrade.

Interviewer: What tipped it?

Participant: Three of the four members agreeing was a strong signal to me. When you get that kind of consistency across model runs, it usually means something real is going on with the pattern.

Interviewer: Did the size of that ensemble — four members — factor into how much weight you gave it?

Participant: Not really, no. I mean, agreement is agreement. If three separate runs are telling you the same intensification story, that's meaningful regardless of how many total members happened to finish by that hour.

Interviewer: And the SPC discussion's confidence language?

Participant: They flagged it as low confidence given how limited the guidance still was, and that's part of why I kept an eye on the fuller ensemble coming in later at 09Z. But in the moment, the three-of-four agreement itself still read as a real signal to me.

Interviewer: Second decision — the radar signature and the track call. What made you settle on one track over maintaining both possibilities?

Participant: Honestly, the moment I saw that hook signature, it just clicked. I'd seen that exact shape develop the same way before, and it played out almost identically that time — same track, same timing window. I didn't feel like I needed to keep hedging between two tracks once I recognized the pattern.

Interviewer: Did you check that recognition against anything, like requesting the WFO's independent read before committing?

Participant: I didn't loop them in before committing, no. It felt clear enough on its own. Turned out the WFO desk was independently tracking a similar dual-track possibility, and the storm's actual path drifted a bit from what I'd called.

Interviewer: How confident were you in the moment, on a scale of how sure you'd normally be?

Participant: Pretty high, honestly — nine out of ten maybe. It looked so much like that prior case that I didn't see much reason to hedge.

Interviewer: Third decision point — the activation-level call after the director's instruction. What was your read going in?

Participant: My read was that guidance exceedance was climbing in two sub-watersheds and we should escalate and get swift-water teams moving given the lead time they need. Then the director called and said hold pending review, no new data attached to that, just a directive.

Interviewer: What did you do?

Participant: I held. He's the one with sign-off authority on activation level changes, so when he says hold, that's generally the end of the discussion on my end.

Interviewer: Could you have presented the sub-watershed exceedance numbers to him and asked him to reconsider, or logged a formal escalation recommendation for the record?

Participant: I could have — there's a process for flagging a disagreement or requesting reconsideration. I just didn't go that route. Once he'd made the call, it felt like his read of the situation was enough to settle it, so I didn't walk him through the trending numbers or push back on the hold.

Interviewer: Was there a technical case for holding at that moment, independent of the instruction?

Participant: Not that I put together myself, no. He asked afterward for a written justification for the hold, and I had to go back and construct one after the fact.

Interviewer: Fourth decision — the coordination call and public messaging.

Participant: Going into that call, my own numbers favored escalating messaging and issuing a WEA. But three of the four neighboring jurisdictions said they were holding steady, and it just felt safer to stay aligned with that rather than break from the group on my own.

Interviewer: Even though your local guidance had worsened since the director's hold?

Participant: Right, it had ticked up further. But when the majority of the desks on the call are holding, going a different direction on your own feels like it needs more justification than staying with the group does.

Interviewer: What happened afterward?

Participant: Flooding started in one of our towns about fifty minutes later. One of the neighboring jurisdictions ended up escalating on their own shortly after, citing their local data.

Interviewer: If the fuller ensemble set had been available from the very start, do you think the early upgrade call would have gone differently?

Participant: Maybe — if the signal had been muddier across more members I might have waited. But I don't think I would have weighted it much differently than I did.

Interviewer: If the director's call hadn't come in at that third decision point, what would you have done?

Participant: I probably would have pushed the escalation through myself. It was really his instruction that changed my course there.

Interviewer: Looking back, with exactly the same information you had at each point, what would you do differently?

Participant: I'd probably slow down at the radar-signature moment and get a second set of eyes before locking onto one track. And on the coordination call, I'd try to separate what our own numbers were saying from what everyone else on the call was doing before deciding.

Interviewer: That's helpful. Thanks for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Biased_4}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Meteorological Hazard Forecaster (Emergency Support Function)}}"
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
