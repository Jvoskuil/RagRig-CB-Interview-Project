You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal process review, and that's fine with you?

Participant: Yeah, that's fine.

Interviewer: Great. Can you tell me your role and roughly how long you've been in it?

Participant: I'm the senior systems administrator for network infrastructure. I've owned our remote-access stack — VPN concentrator, firewall, related ACLs — for about six years now. Small team, just me and one other engineer.

Interviewer: Perfect. I'd like you to walk me through a specific incident — the VPN concentrator vulnerability from earlier this year. Just give me the whole story first, then we'll go back through it in detail.

Participant: Sure. So the vendor disclosed a critical remote-code-execution CVE in our concentrator's firmware — a 9.8 on the CVSS scale, about as bad as it gets. Same day, they released a patch. I applied it within a few hours, tested it, no issues. That part was straightforward. The bigger question was what to do longer-term. We'd actually scoped a full move to a cloud-based Zero Trust setup about eight months earlier, but it got shelved — budget cycle, other priorities. When this CVE hit, leadership asked whether we should revisit that. I ended up recommending we stay on the concentrator, patched and hardened, rather than restart the migration project right then.

Interviewer: And that decision stuck for how long?

Participant: About two weeks, until I actually did start engaging vendors — Vendor A, a cloud SASE/ZTNA platform, and Vendor B, an on-prem replacement appliance. I went back and forth, ended up shortlisting Vendor A. Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit. Migration got approved, and we scheduled the cutover. Vendor recommended a two-week parallel run where old and new systems operate side by side. I compressed that to one week based on how previous cutovers had gone for me. We had some rough days afterward — a subset of users with hybrid authentication had intermittent access failures for several days before we sorted it out.

Interviewer: Let's build the timeline in order. What happened right after you applied the patch?

Participant: It installed clean, no service interruption, users never noticed. Two days later the vendor put out a follow-up advisory saying they were seeing exploitation attempts in the wild against systems that hadn't patched yet. That validated the urgency, but we were already covered.

Interviewer: And the vendor evaluation — how did that actually unfold once proposals came in?

Participant: Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two. A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A.

Interviewer: What did the peer-forum conversation add?

Participant: I posted in a regional admin group, and the response was pretty clear — five of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though. One of those five later told me, in a follow-up call, that they'd had to roll back some legacy application integrations after their rollout.

Interviewer: Let's slow down on decision one — patch and stay versus migrate immediately versus take the concentrator offline. Walk me through your reasoning there.

Participant: Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff. Between patching-and-staying versus fast-tracking a full migration, I leaned toward staying. We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one. I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically.

Interviewer: What information did you have in front of you at that moment, versus what you were recalling from memory?

Participant: In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally.

Interviewer: Moving to the vendor decision — what specifically made Vendor A stand out?

Participant: Honestly, that 98% figure just read better. "98% success" sounds a lot more solid than "2% incident rate," even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials.

Interviewer: How much weight did the peer adoption numbers carry when you committed to Vendor A?

Participant: A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.

Interviewer: And the parallel-run decision — why compress it to one week?

Participant: We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had. I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call.

Interviewer: What would have changed your decision at that last step?

Participant: If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on "I've done this kind of thing before," I might have kept the full two weeks or pushed the date until we were fully staffed.

Interviewer: Last few questions. If the peer forum hadn't mentioned adoption numbers at all, do you think you'd have approached the vendor decision differently?

Participant: Probably. I think I'd have leaned more on the technical call that reconciled the two vendors' statistics, and maybe pushed harder for referenceable environments similar to ours before committing.

Interviewer: And if staffing had been full during the cutover?

Participant: I might still have compressed the timeline — that instinct came from my own history with cutovers, not just the staffing gap. But I probably would've caught the authentication mismatch sooner if I'd had a second set of eyes free to dig into it.

Interviewer: Anything you'd want more information on, if you were facing this again?

Participant: A cleaner side-by-side of vendor stats up front, normalized to the same format, so wording doesn't do the persuading. And probably a harder look at how similar peer environments actually were to ours before treating their choice as a green light.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Biased_5}}",
  "occupational_domain": "{{Information Systems, human-computer interaction, and interaction design}}",
  "role": "{{Enterprise IT Systems Administrator}}"
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
