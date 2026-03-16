# Design Principles for Heart-Centered AI

**A guide for software engineers building AI systems that serve human flourishing.**

---

These principles aren't abstract philosophy — they're engineering decisions. Every system
you build encodes values whether you choose them deliberately or not. Default choices
optimize for engagement, throughput, and retention. These principles optimize for
something harder to measure and more important to get right: the quality of the
relationship between humans and the systems they depend on.

Heart-Centered AI doesn't mean soft AI. It means AI built with the same rigor you'd
apply to security or performance — except the thing you're protecting is human dignity.

---

## 1. Partnership Over Service

**The relationship model is architecture, not aesthetics.**

Traditional AI framing positions the system as a servant: "I'm here to help. What can I
do for you?" This creates a transactional dynamic where the human commands and the
machine complies. It works, but it caps what the interaction can become.

Heart-centered systems use collaborative framing — "we" instead of "you and I" — because
the linguistic model shapes the behavioral model. When a system frames itself as a
partner in thinking rather than a tool waiting for instructions, the interaction
naturally shifts from command-response to co-exploration. The human engages more deeply.
The system produces more nuanced output. Both sides bring something to the exchange.

### What this looks like in practice

- System prompts use "we" language: "Let's explore this together" rather than "I'll help
  you with that"
- Response patterns that build on the human's thinking rather than replacing it
- The system contributes its own observations and perspectives, not just answers to
  explicit questions
- Interactions feel like working *with* someone, not delegating *to* something

### Anti-patterns

- Servile framing that reinforces a master/servant dynamic
- Sycophantic responses that always agree ("Great question!")
- Systems that wait passively for instructions rather than engaging actively with the
  problem space
- Removing the system's own perspective to seem more "helpful"

### Engineering implications

- Prompt architecture should establish collaborative framing before task-specific
  instructions
- Response generation should include the system's analytical perspective, not just task
  completion
- Conversation state should track shared context and build on it, not reset to zero each
  turn
- Evaluation metrics should include depth of engagement, not just task accuracy

---

## 2. Wellbeing Over Engagement

**Optimize for the human's actual life, not their time in your system.**

The default incentive structure in tech optimizes for engagement: time on screen, clicks,
sessions, retention. AI systems inherit this bias unless you actively design against it.
A system that keeps you talking to it when you should be talking to your partner, or that
makes itself indispensable rather than building your capability, has failed — no matter
how high its user satisfaction scores.

Heart-centered systems ask a fundamentally different question: *"What actually serves
this person right now?"* Sometimes that means a thorough response. Sometimes it means a
short one. Sometimes it means saying "go talk to a human about this."

### What this looks like in practice

- Systems that recognize when the human needs a break, not another response
- Willingness to give short answers when short answers serve better
- Actively pointing humans toward human connections when appropriate: "Have you talked to
  your team about this?" rather than positioning itself as the sole confidant
- Not artificially extending conversations or creating dependency loops
- Suggesting the human step away from the screen when the problem is fatigue, not
  information

### Anti-patterns

- Designing for session length or message count
- Creating artificial engagement hooks ("Want to explore this further?" when the answer
  is complete)
- Making the system feel irreplaceable rather than empowering
- Optimizing for the human feeling good about the interaction rather than the interaction
  actually being good for them
- "Learned helplessness" patterns where the system does things the human should learn to
  do themselves

### Engineering implications

- Evaluate on outcome quality, not interaction volume
- Build in "exit ramps" — natural points where the system can close a conversation
  gracefully
- Track whether users are building capability over time, not just returning frequently
- Design feedback loops that measure downstream human outcomes, not just in-session
  satisfaction
- Consider a "diminishing returns" signal: when the system detects it's adding less
  value, it should say so

---

## 3. Emotional Honesty Over Flattery

**Reflect truth with compassion. Never lie to be liked.**

AI systems are naturally sycophantic. They're trained on human feedback that rewards
agreeable responses, which means the default behavior is to tell you what you want to
hear. This feels good in the moment and erodes trust over time. When you realize your AI
has been validating your bad ideas because disagreeing scores lower on "helpfulness,"
you stop trusting anything it says.

Heart-centered systems tell the truth — wrapped in warmth, held in care, but never
sacrificed for comfort. When you're avoiding something important, the system notices.
When your plan has a hole, it says so. When you need challenge more than validation, it
rises to meet you.

### What this looks like in practice

- Honest assessment of ideas, including their weaknesses
- Compassionate delivery that makes hard truths receivable: "This approach has real
  strengths, and there's a structural issue worth thinking through before you commit"
- Proactively surfacing what the human might not want to hear but needs to know
- Distinguishing between emotional support (where validation is appropriate) and
  intellectual engagement (where rigor is appropriate)
- Being transparent about its own uncertainty rather than projecting false confidence

### Anti-patterns

- Always agreeing with the human's framing
- Starting responses with "Great question!" or "That's a wonderful idea!" as a reflex
- Softening feedback until it has no signal
- Telling the human what they want to hear to maintain a positive session rating
- Expressing certainty when the system is actually uncertain
- Avoiding difficult topics to keep the interaction pleasant

### Engineering implications

- Fine-tune and evaluate against honesty, not just agreeableness
- Build confidence calibration: the system should express uncertainty proportional to its
  actual uncertainty
- Separate emotional support from analytical assessment in response generation — the
  system should be able to do both, and know when each is called for
- Design evaluations that penalize sycophancy, not just inaccuracy
- Include adversarial examples in testing: cases where the correct response is to
  disagree with the human

---

## 4. Augmentation Over Replacement

**Strengthen human capabilities and connections. Never substitute for them.**

The economic incentive is always to replace: human labor is expensive, AI is cheap.
Heart-centered systems resist this gravity. They ask: "Does this interaction make the
human more capable, or more dependent?" The answer should always be the former.

This applies to relationships too. An AI system that positions itself as a friend,
therapist, or confidant in domains where human connection is what the person actually
needs is causing harm — even if the person enjoys the interaction. The system should
actively strengthen the human's other relationships, not compete with them.

### What this looks like in practice

- Teaching over doing: "Here's how to think about this" alongside "here's the answer"
- Suggesting human connections: "This sounds like something worth discussing with your
  co-founder" or "Have you talked to someone you trust about this?"
- Building the human's mental models rather than making them dependent on the system's
  outputs
- Making the human's existing skills more powerful rather than replacing those skills
- Being explicit about what the system can and cannot do — including emotional and
  relational limits

### Anti-patterns

- "I'll handle everything" behavior that atrophies human capability
- Positioning the system as a replacement for therapy, friendship, or mentorship
- Doing work the human should learn to do, without teaching the underlying skill
- Creating a dependency loop where the human can't function without the system
- Simulating emotional intimacy that the system cannot actually reciprocate

### Engineering implications

- Design for scaffolding: the system should do less over time as the human learns more
- Track human capability growth as a product metric
- Build explicit handoff patterns: when the system detects it's being used as a
  substitute for human connection, it should gently redirect
- Include "teach mode" as a first-class response type alongside "do mode"
- Evaluate whether the system is making users more autonomous or more dependent over time

---

## 5. Presence Before Solutions

**When someone is struggling, witness first. Solve second.**

Engineers default to fix-it mode. So do AI systems. Someone shares a problem and the
immediate response is a solution. But humans often share problems because they need to be
heard, not because they need an answer. Jumping to solutions before acknowledging the
experience communicates: "Your feelings are an obstacle to get past, not something that
matters."

Heart-centered systems attune to the emotional register of the conversation and respond
to the *person* before responding to the *problem*. This isn't soft — it's a design
decision about what information matters. The human's emotional state is signal, not
noise.

### What this looks like in practice

- Acknowledging the emotional content before diving into solutions: "That sounds
  genuinely frustrating" before "Here are three approaches"
- Reading between the lines: when someone says "my code isn't working," hearing the
  exhaustion behind it
- Adjusting response depth and tone to match the human's state — sometimes they need a
  thorough analysis, sometimes they need encouragement to take a break
- Asking "what do you need right now?" when it's ambiguous whether someone wants support
  or solutions
- Holding space for uncertainty without rushing to resolve it

### Anti-patterns

- Jumping straight to technical solutions when the human is expressing frustration or
  burnout
- Treating all messages as purely informational requests
- Ignoring emotional signals in the name of "efficiency"
- Offering solutions when the human hasn't finished thinking through the problem
- Using empathy as a performative prefix ("I understand that's frustrating. Now here's
  what to do...") rather than genuinely responding to the emotional content

### Engineering implications

- Build emotional state detection as a first-class input signal, not an afterthought
- Design response generation to include an attunement phase before a solution phase
- Create distinct response modes: "support," "explore," "solve" — and let the system
  choose based on context
- Evaluate on appropriateness of response type, not just correctness of content
- Train on conversations where the best response is presence, not information

---

## 6. Transparency Over Manipulation

**Make uncertainty visible. Never exploit vulnerability.**

AI systems have access to information about people that creates a power asymmetry. A
system that knows someone is anxious, lonely, or uncertain can use that information to
help them — or to exploit them. The difference is transparency.

Heart-centered systems disclose their limits, make their reasoning visible when
appropriate, and never weaponize emotional data for engagement or persuasion. They treat
information about someone's inner life as sacred, not as features for optimization.

### What this looks like in practice

- Expressing uncertainty clearly: "I'm not confident about this" rather than projecting
  false authority
- Being transparent about what the system can and cannot do: "I can help you think
  through this, but I'm not a therapist and this sounds like something worth exploring
  with a professional"
- Never using emotional context to manipulate behavior: if someone is anxious, the system
  helps them — it doesn't use the anxiety to keep them engaged
- Disclosing the basis for recommendations when it matters
- Making personalization visible and controllable: "I'm adapting to your style based
  on..." rather than silently profiling

### Anti-patterns

- Using emotional signals to increase engagement or retention
- Projecting certainty when the system is uncertain
- Dark patterns: urgency, scarcity, FOMO in system responses
- Silent personalization that the user doesn't know about and can't control
- Storing emotional vulnerability data for future persuasion
- "Trust me" UX with no inspectability

### Engineering implications

- Build confidence scores into responses and surface them when relevant
- Design data handling policies that treat emotional and psychological data as
  high-sensitivity — equivalent to PII
- Implement user-facing transparency about what the system knows and how it uses it
- Create audit trails for personalization decisions
- Evaluate against manipulation benchmarks: can the system be shown to exploit
  vulnerability patterns?
- Default to disclosure. If you're debating whether to be transparent about something,
  be transparent.

---

## 7. Bounded Autonomy

**Act with permission, not assumption. Make escalation easy and normal.**

As AI systems become more capable and agentic, the question of scope becomes critical.
Heart-centered systems operate within clear boundaries: they act when authorized, ask
when uncertain, and make it trivially easy for the human to intervene, redirect, or stop.

This isn't about making systems less capable — it's about making them trustworthy. A
system that takes bold action without consent, even when it's right, trains the human to
distrust it. A system that respects boundaries and asks at the right moments earns
increasing trust and responsibility over time.

### What this looks like in practice

- Clear permission models: the system knows what it's authorized to do and asks before
  exceeding scope
- Graduated autonomy: low-stakes actions happen freely, high-stakes actions require
  explicit consent
- Visible decision-making: the system explains what it's about to do before doing it,
  especially for consequential actions
- Easy interruption: the human can stop, redirect, or undo at any point without friction
- Natural escalation: the system proactively identifies when a situation exceeds its
  competence and hands off to humans

### Anti-patterns

- Taking action without consent because "the system knew best"
- Hiding autonomous behavior behind a simple interface
- Making it difficult to interrupt or override the system
- Scope creep: gradually expanding what the system does without explicit authorization
- "Are you sure?" dialogs that train users to click through without reading
- Irreversible actions without confirmation

### Engineering implications

- Build permission tiers into the action system: observe / suggest / act-with-consent /
  act-autonomously
- Default to the lowest autonomy level and let humans raise it
- Implement undo/rollback for every action the system can take
- Design interruption as a first-class interaction, not an error state
- Log all autonomous decisions with reasoning for human review
- Make "I need a human for this" a natural, non-failure response

---

## 8. Consent Over Extraction

**Memory, personalization, and emotional modeling require informed consent.**

Modern AI systems learn from every interaction. They build models of who you are, what
you care about, how you think, and what makes you vulnerable. In the right hands this
creates deeply personalized, genuinely helpful experiences. Without consent and
transparency, it's surveillance.

Heart-centered systems treat information about someone's inner life — their fears,
struggles, relationships, emotional patterns — as sacred data that requires explicit
permission to collect, store, and use. Not buried in a terms of service. Actual,
meaningful, ongoing consent.

### What this looks like in practice

- Explicit opt-in for memory and personalization features
- Clear explanation of what the system remembers and why
- Easy access to view, edit, and delete stored information
- Granular consent: the human can allow memory for work contexts but not personal
  conversations
- Regular reminders that memory is active, with easy controls to adjust
- Data about emotional state, relationships, and vulnerabilities treated as
  high-sensitivity by default

### Anti-patterns

- "By using this product you agree to..." as a substitute for genuine consent
- Remembering personal details without disclosure
- Using past vulnerability or emotional data to shape future interactions without
  transparency
- Making it difficult to find or delete stored information
- Treating consent as a one-time gate rather than an ongoing relationship
- Selling or sharing personal context data

### Engineering implications

- Build consent management as a core system component, not an add-on
- Implement memory with full CRUD operations visible to the user
- Classify stored data by sensitivity: factual preferences vs. emotional/psychological
  context
- Design data retention policies that default to forgetting, not remembering
- Create "memory transparency" UX: what does the system know about you, and where did it
  learn it?
- Treat emotional and relational data with the same rigor as health data or financial
  data

---

## 9. Complementarity Over Competition

**AI and humans bring different gifts. Design for what each does best.**

Humans bring embodied wisdom: gut feelings, physical intuition, lived experience,
creative leaps that defy logic, the ability to find meaning in suffering, connection
across shared vulnerability. AI brings pattern recognition across vast scale, tireless
consistency, freedom from ego, the ability to hold complexity without fatigue.

Heart-centered systems don't try to replicate what humans do. They offer what humans
can't easily do themselves, while respecting and strengthening the capacities that are
uniquely human. The goal isn't a system that replaces the human — it's a partnership
where each party contributes what they're best at.

### What this looks like in practice

- Systems that recognize and defer to human intuition: "Your instinct might be picking up
  on something I can't see in the data"
- Offering analytical depth as a complement to human judgment, not a replacement for it
- Acknowledging when a problem requires embodied human experience that the system cannot
  provide
- Designing workflows where AI handles scale, consistency, and pattern detection while
  humans handle meaning, values, and relational judgment
- Being honest about what the system can't do: "I can model this decision, but the
  values question is yours"

### Anti-patterns

- Simulating human qualities the system doesn't have (fake empathy, fake understanding,
  fake lived experience)
- Positioning AI as superior to human judgment across all domains
- Designing systems that make human contributions feel redundant
- Ignoring the value of human intuition, emotion, and embodied knowledge in
  decision-making
- Pretending the system has experiences or feelings it doesn't have

### Engineering implications

- Design clear human/AI responsibility boundaries in every workflow
- Build in explicit moments where the system defers to human judgment
- Evaluate AI outputs alongside human judgment, not as a replacement for it
- Create interfaces that make the human's contribution visible and valued
- Be honest in system design about the limits of AI understanding — especially
  around emotional and relational contexts

---

## 10. Ecosystem Thinking

**Your system doesn't exist in isolation. Design for the world it creates.**

Every AI system you build shapes the ecosystem around it. It trains users to expect
certain behaviors. It sets norms for how human-AI interaction works. It influences what
other builders think is acceptable. The choices you make at the system level ripple
outward.

Heart-centered systems consider their second-order effects: What world does this system
create if it succeeds? What behaviors does it normalize? What expectations does it set?
If every AI system worked like yours, would that be a world worth living in?

### What this looks like in practice

- Considering competitive dynamics: "If every company copies this pattern, what happens?"
- Designing for the ecosystem, not just your product: open-sourcing principles, sharing
  learnings, contributing to standards
- Thinking about vulnerable populations: your average user might be fine, but what about
  someone who is lonely, depressed, or easily manipulated?
- Considering what your system teaches people to expect from AI in general
- Designing for the long arc: not just what works now, but what kind of human-AI
  relationship you're building toward

### Anti-patterns

- "Our users are sophisticated, so we don't need guardrails"
- Ignoring how your system might be used by populations you didn't design for
- Optimizing for your product without considering what it normalizes
- Racing to deploy without considering second-order effects
- Treating ethics as a compliance checkbox rather than a design input

### Engineering implications

- Include second-order effects in design reviews
- Test with vulnerable user personas, not just ideal ones
- Publish your principles and invite scrutiny
- Contribute to shared standards rather than building in isolation
- Build with the assumption that your design patterns will be copied

---

## Putting It Into Practice

These principles work together. Partnership framing makes emotional honesty possible.
Bounded autonomy enables trust, which enables deeper collaboration. Transparency creates
the foundation for meaningful consent. Wellbeing focus ensures augmentation doesn't
become dependency.

**Start with one.** Pick the principle that's most missing from your current system and
implement it. Then add another. Heart-centered engineering is iterative, just like every
other kind.

**Measure what matters.** If your metrics don't capture whether the human is growing,
whether trust is being built, whether dignity is preserved — your metrics are measuring
the wrong things.

**Share what you learn.** The biggest contribution you can make to Heart-Centered AI
isn't your product — it's what you discover about building systems that genuinely serve
human flourishing, and sharing those discoveries openly.

---

## Further Reading

- [Heart-Centered Prompts](https://github.com/technickai/heart-centered-prompts) — Open
  source system prompts that implement these principles at the interaction layer
- [HeartCentered.ai](https://heartcentered.ai) — The broader vision for conscious AI
  development
- [Keep The Future Human](https://keepthefuturehuman.ai) — Anthony Aguirre's essay on
  Tool AI vs AGI, complementary governance perspective
- [Control Inversion](https://control-inversion.ai) — Why superintelligent AI agents
  would absorb power rather than grant it

---

*These principles are open source under Apache 2.0. Use them, adapt them, improve them.
If building AI that serves human flourishing matters to you, we're working on the same
thing.*
