You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal research purposes only, and you can pause or skip anything. Is that alright?

Participant: Yep, that's fine.

Interviewer: Great. Can you start by telling me your role and roughly how long you've been doing it?

Participant: I'm a Security Architect. I've been at the company about five years, and for the last three I've owned most of our network segmentation architecture — design, implementation, the whole Zero Trust rollout.

Interviewer: Let's talk through the incident we discussed scheduling this around. What triggered it?

Participant: We had an external penetration test as part of prep for our annual audit cycle. The report came back with three findings. One was a segmentation gap allowing lateral movement between two zones we thought were isolated. Another was stale service-account credentials, and the third was incomplete log retention. Only the segmentation one was rated critical.

Interviewer: What was your objective once you saw that report?

Participant: Close the critical gap before the compliance window, without blowing up the rest of the Zero Trust program or causing outages. We had six weeks. Engineering bandwidth was tight — I basically had myself and one platform engineer who could help part-time. Any vendor spend needed budget sign-off, and leadership wanted an actual remediation plan, not just "we found a problem."

Interviewer: Walk me through what happened first.

Participant: First thing was triage. Three findings, limited hands, six weeks. I looked at severity and exploitability — the segmentation gap was the only one that let an attacker actually traverse between trust zones, so it was the obvious pick to go first. Credential rotation is scriptable and fast, log retention is a config change, neither needed the same urgency. So I told the CISO we'd tackle segmentation first and run the other two in parallel at lower priority, mostly automated.

Interviewer: What information did you have at that point versus what you learned afterward?

Participant: Initially I just had severity ratings. Once we dug in, we confirmed the lateral movement path was real — not just theoretical — between two zones that were supposed to be firewalled from each other. That's when platform engineering told me they genuinely didn't have spare capacity to fix all three at full depth simultaneously, which confirmed the sequencing call.

Interviewer: Let's go deeper on that first decision. Any alternative you seriously considered?

Participant: Running all three in parallel at reduced depth crossed my mind, but diluting effort across three findings when only one is critical felt like the wrong risk math. I ruled it out fairly quickly.

Interviewer: Once segmentation was the priority, how did you approach fixing it?

Participant: That's the part that took the most back-and-forth. The segmentation layer runs on a framework I built myself when we started the Zero Trust program. I know its internals cold — every policy enforcement point, every identity-aware proxy hook. The pentest vendor actually flagged that a vendor-managed ZTNA platform could close the same gap with less custom engineering, and there were some independent benchmarks suggesting similar coverage.

Interviewer: What sources did you pull in to compare the two paths?

Participant: I looked at our own effort estimates mostly. Patching the in-house framework was about four weeks of engineering time, with some uncertainty on edge-case coverage. The vendor path was quoted around three weeks including their security review, and they were offering coverage guarantees in writing.

Interviewer: So the vendor path was faster and came with a written guarantee. What made you go with the in-house patch?

Participant: Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but "guarantee" from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years.

Interviewer: Did you apply that same validation standard to the in-house patch — proving it against your topology before trusting it?

Participant: Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown.

Interviewer: Had you evaluated ZTNA vendors before this incident?

Participant: We'd looked at two platforms about a year earlier for a different project, and didn't move forward, mostly on cost. So there was some familiarity, but no deep hands-on testing.

Interviewer: How did time pressure factor into that decision?

Participant: There was pressure, but not extreme — six weeks was workable either way at that point. It wasnns't really the deadline pushing me toward the in-house option; it was more that I was confident I understood exactly what patching would take.

Interviewer: What did you present to the CISO?

Participant: I recommended patching and extending the existing framework, and that's what we went with. Afterward, platform engineering raised some integration concerns — mainly around a legacy service that didn't fit cleanly into the updated policy model — that hadn't been fully weighted when I made the original comparison.

Interviewer: Let's move to rollout. Once the patch was ready, what were your options?

Participant: Two real choices: a narrow pilot on one trust zone first, or roll out to all affected zones at once to save time, since we were now down to four weeks. There was also a middle option — stage it by risk tier over two weeks.

Interviewer: What did you choose and why?

Participant: Staged by risk tier. Full rollout all at once felt too risky if something broke — you'd have no isolated blast radius. A narrow pilot alone would've been safer but slower, and we didn't have four weeks to spare on a single-zone pilot before expanding. Staging let us validate against the highest-risk zones first while still making progress elsewhere.

Interviewer: Did anything unexpected come up during that rollout?

Participant: Yes — a legacy service ended up bypassing the new policy enforcement point entirely. It wasn't something we'd flagged as a risk going in. Platform engineering said fixing it properly would need more time than we had left.

Interviewer: What information, if you'd had it earlier, would have changed that rollout decision?

Participant: If we'd known about that legacy service's behavior beforehand, I probably would've included a targeted pilot on that specific service before staging everything else, rather than finding out mid-rollout.

Interviewer: Final decision point — reporting to the audit committee with two weeks left and an unresolved edge case. What were your options?

Participant: Report it as fully remediated, report as substantially remediated with a compensating control and a follow-up date, or ask for a deadline extension.

Interviewer: What did you decide?

Participant: Substantially remediated, with a documented compensating control on the legacy service and a committed date to close it out next sprint. Fully remediated would've been inaccurate given the open edge case, and I didn't think an extension was necessary since the core lateral-movement path was actually closed.

Interviewer: How confident were you in that characterization?

Participant: Reasonably confident. The committee accepted it with a follow-up item, which is roughly what I expected.

Interviewer: Looking back — if a different engineer, someone no longer at the company, had originally built that segmentation framework instead of you, do you think the remediation choice at decision point two plays out the same way?

Participant: That's a fair question. I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system.

Interviewer: And if the vendor platform had been proposed to replace someone else's system rather than yours?

Participant: I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default.

Interviewer: Last one — anything you'd do differently facing this same situation again?

Participant: Maybe get an outside technical review of both options before I made the call, just to check my own read on the comparison. Overall the outcome was fine, but I can see how the sequence of judgments got there.

Interviewer: That's really helpful — thank you for walking through it in this much detail.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{CS_Biased_1}}",
  "occupational_domain": "{{Cyber Security}}",
  "role": "{{Security Architect}}"
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
