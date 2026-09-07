You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Before we begin, do you consent to taking part in this interview? I’m interested in a specific work incident and how you made decisions as it unfolded, rather than in evaluating the outcome.

Participant: Yes, that’s fine.

Interviewer: Could you briefly describe your role and the incident you’ll be discussing?

Participant: I was the Product Manager for onboarding at CollabHub, a B2B collaboration platform. We had self-serve signups, plus sales-assisted accounts that often began with the same flow. The incident was a noticeable increase in abandonment during account setup, about five weeks before our Q3 board review. My responsibility was to identify a credible response quickly without derailing the sprint roadmap or putting enterprise customers at greater risk.

Interviewer: What first alerted you to it?

Participant: Our weekly onboarding funnel dashboard showed that drop-off at account setup had increased 32% over three weeks. That was unusual because the top of the funnel was stable. Traffic, acquisition channels, and SSO usage had not changed enough to explain it. At first, the dashboard only showed account setup as one broad stage, so I could see the deterioration but not exactly where people were leaving.

We had a board narrative built around improving activation rate, so the timing mattered. The VP of Product wanted an explanation, Sales was already hearing feature-parity questions from prospects, and Engineering had a fairly full sprint with enterprise bug fixes. I asked our data analyst to investigate the funnel instrumentation and asked a designer to pull heatmap analytics. I also did a quick scan of competitors because I wanted to know whether there had been a shift in the market.

Interviewer: What was the overall objective you were working toward?

Participant: In the immediate sense, reduce abandonment and protect activation rate. More broadly, I needed a plan that was credible to the board and did not consume so much sprint capacity that we created problems elsewhere. We had to decide whether this was a narrow usability or payment issue, or evidence that our whole onboarding approach was behind where the market was going.

Interviewer: Walk me through the sequence after you saw the dashboard.

Participant: The first few days were mostly about separating the signal from the dashboard limitation. Then we got better detail from the analyst. The sharpest abandonment seemed to happen just after the payment-detail field, especially for a newer subgroup of accounts. In parallel, the competitor scan showed that three platforms we regularly encountered in deals had released some form of guided onboarding flow. That became a larger discussion in the product group. We then selected an approach, made a staffing decision, and finally had to decide whether to launch before the board review with incomplete testing.

Interviewer: At the outset, what did you decide to investigate first?

Participant: I chose a rapid internal analytics review, supplemented by a light competitor scan, rather than immediately commissioning user interviews.

Interviewer: What information did you have at that time?

Participant: I had the 32% increase in the broad account-setup drop-off step, no fresh qualitative feedback, and a warning from the analyst that the payment sub-step had incomplete instrumentation. The UX research team could have recruited interviews, but they estimated two weeks before we would have useful sessions. We had only five weeks until the board review, and any changes would still need design, engineering, QA, and a release window.

Interviewer: What alternatives did you consider?

Participant: The main alternatives were to start with formal customer interviews, to do a deeper funnel and heatmap analysis first, or to rely mostly on market research and competitor teardowns. We could also have done all three, but that would have spread a small team thin and still might not have produced a decision quickly.

Interviewer: Why did you choose the analytics route?

Participant: We needed a directional answer within days, not weeks. Analytics could tell us whether the issue was broadly distributed or concentrated in a specific step. The heatmaps could show hesitation, repeated field edits, or attempts to leave the page. I did not treat the competitor scan as a diagnosis; at that point it was context. Deferring interviews was a trade-off. I documented that we were choosing speed over depth and asked Research to hold provisional time in case the data stayed unclear.

Interviewer: What did you learn after that decision?

Participant: The analyst narrowed the issue. Abandonment rose most clearly after payment details, not when users named the workspace, invited teammates, or configured SSO. The affected cohort was only about 140 users, though, and it was a new account type introduced the previous month. So it was suggestive, but not statistically stable. The heatmaps showed some repeated edits around payment fields, but because instrumentation was incomplete, we could not reliably distinguish validation failures from people simply deciding not to continue.

Interviewer: When did competitor activity begin to matter more?

Participant: Once I was preparing options for the VP of Product. The competitor review showed three named platforms had shipped guided setup experiences in roughly six weeks. I also follow a cross-company product Slack group, and several PMs were sharing launch screenshots and implementation notes for AI-guided onboarding. An industry newsletter was describing guided setup as something most leading SaaS onboarding flows were adopting.

Interviewer: What was the next decision you had to make?

Participant: Whether to build an AI-guided setup wizard, focus on the payment-detail issue, or run a small A/B test of both directions before committing.

Interviewer: Describe the evidence in front of you.

Participant: Internally, we had the payment-field signal, but it was from a small cohort. The data did not show that a guided wizard would solve that specific issue. Externally, we had a much more visible pattern: competitors were changing their onboarding experiences, our sales director was hearing questions about whether we had comparable guidance, and peer PMs were treating these flows as the new baseline.

Interviewer: How did you weigh those sources?

Participant: I put more weight on the external pattern than I normally would have. My thinking was that if several direct competitors had invested in the same interaction pattern so quickly, there was probably something we were missing about expectations in the category. In the Slack discussions, it felt like every product team I recognized was moving toward guided setup. That made the wizard feel less like an experimental bet and more like the direction the category had already chosen.

The payment data was still important, but I saw it as potentially a local symptom. With only 140 users in that cohort and incomplete funnel instrumentation, I was reluctant to build the entire response around it. I decided the AI-guided wizard was the better strategic move, and we would address the payment field within that broader redesign later.

Interviewer: Did you consider running a controlled test before committing?

Participant: Yes. The analyst suggested a lightweight A/B test: one version simplifying payment details and another adding limited guided setup. That would have been cleaner from an evidence perspective. I ruled it out because it would have taken design and engineering time without giving us a board-ready feature direction quickly. Also, I felt that waiting while the market moved would make us look late.

Interviewer: If you had not seen the competitor releases or the discussions among peer PMs, would you have chosen the same option?

Participant: I probably would have pushed harder for the payment-field experiment first. The external activity was a major reason I was comfortable making a larger commitment despite the uncertainty in our own data.

Interviewer: Once you chose the wizard, what staffing decision followed?

Participant: I had to decide whether to fully reassign two engineers from the enterprise bug-fix backlog for three sprints, split their time between the wizard and a narrow payment-field fix, or delay the wizard and prioritize the backlog.

Interviewer: What were the competing goals then?

Participant: The engineering lead estimated three sprints for a usable wizard, including integration with account configuration and SSO routing. The backlog contained unresolved enterprise defects, some affecting permissions and notification behavior. Sales wanted the wizard in active deal demonstrations, while Engineering was concerned that splitting the work would make both efforts slow and difficult to test.

Interviewer: What did you decide, and why?

Participant: I authorized the full reallocation to the wizard. That was not an easy choice, but partial staffing would have produced a thin version of the feature and still would not have given us enough capacity to resolve the payment issue properly. Delaying the wizard would have protected the backlog, but it also meant we would have little concrete progress to show at the board review. I accepted the bug-risk trade-off, with the engineering lead agreeing to triage only production-severity issues during the build.

Interviewer: What happened afterward?

Participant: Two enterprise tickets escalated during that period. Neither became a platform outage, but account teams had to manage customer concerns. The wizard build stayed on schedule. At the same time, a follow-up analytics review continued to show payment-field friction. We had not changed that code path, so the result was not surprising, but it made clear that the redesign did not remove the immediate signal.

Interviewer: What was the final decision before launch?

Participant: Whether to release the wizard to all new signups before the board review, limit it to a 10% canary release, or wait another week for more regression testing and improved payment instrumentation.

Interviewer: What did you know at that point?

Participant: QA had completed partial regression testing. The canary had low traffic, so activation-rate results were inconclusive. We knew payment-field abandonment had not moved. The board meeting was four days away, and the release was functioning in the tested paths, but there were still gaps in edge-case coverage.

Interviewer: Why launch to all new signups?

Participant: I made a time-bounded product and communication decision. A 10% canary would have been safer technically, but it would not produce enough usable operational evidence before the board meeting. Waiting another week would have improved testing, but it would also leave us presenting a plan rather than a shipped response. I consulted the engineering lead and QA manager; both were uncomfortable but agreed the remaining risks were manageable if we staffed monitoring and had a rollback path.

Interviewer: What were the consequences?

Participant: The post-launch activation rate did not show a statistically significant change from the prior month. Support tickets still mentioned difficulty at the payment step. We did not have a major regression, which was important, but the wizard was not the immediate solution to the funnel problem. We then prioritized a focused review of payment validation and instrumentation.

Interviewer: If you had had two more weeks before the board review, what would you have done differently?

Participant: I would have run the controlled comparison and recruited several users from the new account cohort. I would also have kept the wizard in a limited canary longer. That would have given us a better answer about whether payment friction, onboarding complexity, or both were affecting activation.

Interviewer: What information would have changed your earlier redesign decision?

Participant: A larger, stable cohort showing that payment details were clearly the dominant exit point would have changed it. I also would have wanted session recordings or interview evidence showing why users stopped there. If that evidence had been strong, I would have treated the payment fix as the immediate priority and positioned the wizard as a separate longer-term initiative.

Interviewer: And if the competitors had not introduced guided onboarding at that time?

Participant: I think I would have been more willing to make the smaller, targeted payment change first. The market context made the broader redesign feel urgent in a way that the internal data alone did not.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Biased_1}}",
  "occupational_domain": "{{Information Systems, human-computer interaction, and interaction design}}",
  "role": "{{Product Manager (Digital Platform)}}"
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
